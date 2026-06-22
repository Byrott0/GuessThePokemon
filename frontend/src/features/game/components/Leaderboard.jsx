import { useCallback, useEffect, useState } from 'react'
import { getLeaderboard } from '../api/gameApi'

export function Leaderboard() {
  const [entries, setEntries] = useState([])
  const [isLoading, setIsLoading] = useState(true)
  const [error, setError] = useState('')

  const loadLeaderboard = useCallback(async () => {
    setError('')
    setIsLoading(true)

    try {
      const leaderboard = await getLeaderboard()
      setEntries(leaderboard.entries ?? [])
    } catch (requestError) {
      setError(requestError.message)
    } finally {
      setIsLoading(false)
    }
  }, [])

  useEffect(() => {
    // eslint-disable-next-line react-hooks/set-state-in-effect
    loadLeaderboard()
  }, [loadLeaderboard])

  return (
    <section className="leaderboard-panel" aria-labelledby="leaderboard-title">
      <div className="leaderboard-header">
        <div>
          <p className="eyebrow">Ranking</p>
          <h2 id="leaderboard-title">Huidige leaderboard</h2>
        </div>
        <button
          className="refresh-button"
          type="button"
          onClick={loadLeaderboard}
          disabled={isLoading}
        >
          {isLoading ? 'Laden...' : 'Ververs'}
        </button>
      </div>

      {error ? <p className="error-message">{error}</p> : null}

      {!error && isLoading ? <p className="leaderboard-state">Leaderboard wordt geladen...</p> : null}

      {!error && !isLoading && entries.length === 0 ? (
        <p className="leaderboard-state">Nog geen scores. Speel een ronde om bovenaan te komen.</p>
      ) : null}

      {!error && entries.length > 0 ? (
        <ol className="leaderboard-list" aria-label="Top scores">
          {entries.map((entry) => (
            <li className="leaderboard-row" key={entry.player_id}>
              <span className="leaderboard-rank">#{entry.rank}</span>
              <span className="leaderboard-name">{entry.player_name}</span>
              <span className="leaderboard-score">{entry.total_score} punten</span>
            </li>
          ))}
        </ol>
      ) : null}
    </section>
  )
}
