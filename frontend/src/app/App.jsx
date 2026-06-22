import { PokemonGame } from '../features/game/components/PokemonGame'
import { Leaderboard } from '../features/game/components/Leaderboard'
import './App.css'

export default function App() {
  return (
    <main className="game-shell">
      <div className="game-layout">
        <PokemonGame />
        <Leaderboard />
      </div>
    </main>
  )
}
