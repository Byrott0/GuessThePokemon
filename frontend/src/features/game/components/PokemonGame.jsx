import { useMemo, useState } from 'react'
import { finishGame, startGame, submitGuess } from '../api/gameApi'

const initialForm = {
  playerName: '',
  guess: '',
}

export function PokemonGame() {
  const [form, setForm] = useState(initialForm)
  const [gameSession, setGameSession] = useState(null)
  const [isLoading, setIsLoading] = useState(false)
  const [error, setError] = useState('')

  const attemptsLeft = useMemo(() => {
    if (!gameSession) return 0
    return Math.max(0, gameSession.max_attempts - gameSession.attempts)
  }, [gameSession])

  const isGameActive = gameSession?.status === 'active'
  const isGameFinished = gameSession && !isGameActive

  function updateField(event) {
    const { name, value } = event.target
    setForm((currentForm) => ({ ...currentForm, [name]: value }))
  }

  async function handleStartGame(event) {
    event.preventDefault()
    setError('')
    setIsLoading(true)

    try {
      const session = await startGame(form.playerName.trim())
      setGameSession(session)
      setForm((currentForm) => ({ ...currentForm, guess: '' }))
    } catch (requestError) {
      setError(requestError.message)
    } finally {
      setIsLoading(false)
    }
  }

  async function handleGuess(event) {
    event.preventDefault()

    if (!gameSession) return

    setError('')
    setIsLoading(true)

    try {
      const session = await submitGuess(gameSession.game_id, form.guess.trim())
      setGameSession(session)
      setForm((currentForm) => ({ ...currentForm, guess: '' }))
    } catch (requestError) {
      setError(requestError.message)
    } finally {
      setIsLoading(false)
    }
  }

  async function handleFinishGame() {
    if (!gameSession) return

    setError('')
    setIsLoading(true)

    try {
      const session = await finishGame(gameSession.game_id)
      setGameSession(session)
    } catch (requestError) {
      setError(requestError.message)
    } finally {
      setIsLoading(false)
    }
  }

  function handleNewGame() {
    setGameSession(null)
    setForm(initialForm)
    setError('')
  }

  return (
      <section className="game-panel" aria-labelledby="game-title">
        <div className="game-header">
          <p className="eyebrow">Guess the Pokemon</p>
          <h1 id="game-title">Wie is deze Pokemon?</h1>
        </div>

        {!gameSession ? (
          <form className="player-form" onSubmit={handleStartGame}>
            <label htmlFor="playerName">Spelernaam</label>
            <div className="inline-controls">
              <input
                id="playerName"
                name="playerName"
                type="text"
                minLength="2"
                maxLength="25"
                value={form.playerName}
                onChange={updateField}
                placeholder="Bijv. Tim"
                required
              />
              <button type="submit" disabled={isLoading}>
                {isLoading ? 'Start...' : 'Start'}
              </button>
            </div>
          </form>
        ) : (
          <div className="play-area">
            <div className="sprite-stage">
              <img
                className={isGameActive ? 'pokemon-sprite hidden-sprite' : 'pokemon-sprite'}
                src={gameSession.sprite_url}
                alt={isGameActive ? 'Verborgen Pokemon sprite' : gameSession.pokemon_name}
              />
            </div>

            <div className="game-status">
              <span>Status: {gameSession.status}</span>
              <span>Pogingen over: {attemptsLeft}</span>
              <span>Score: {gameSession.score_gained}</span>
            </div>

            {isGameActive ? (
              <form className="guess-form" onSubmit={handleGuess}>
                <label htmlFor="guess">Jouw gok</label>
                <div className="inline-controls">
                  <input
                    id="guess"
                    name="guess"
                    type="text"
                    minLength="1"
                    maxLength="25"
                    value={form.guess}
                    onChange={updateField}
                    placeholder="Typ de naam..."
                    required
                  />
                  <button type="submit" disabled={isLoading}>
                    {isLoading ? 'Check...' : 'Guess'}
                  </button>
                </div>
              </form>
            ) : null}

            {isGameFinished ? (
              <div className="result">
                <h2>{gameSession.status === 'won' ? 'Goed geraden' : 'Game klaar'}</h2>
                <p>Het was {gameSession.pokemon_name}.</p>
                <button type="button" onClick={handleNewGame}>
                  Nieuwe game
                </button>
              </div>
            ) : (
              <button
                className="secondary-button"
                type="button"
                onClick={handleFinishGame}
                disabled={isLoading}
              >
                Stop game
              </button>
            )}
          </div>
        )}

        {error ? <p className="error-message">{error}</p> : null}
      </section>
  )
}
