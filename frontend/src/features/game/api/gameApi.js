import { apiRequest } from '../../../lib/apiClient'

export function startGame(playerName) {
  return apiRequest('/start_game', {
    method: 'POST',
    body: JSON.stringify({ player_name: playerName }),
  })
}

export function submitGuess(gameId, guess) {
  return apiRequest('/guess', {
    method: 'POST',
    body: JSON.stringify({ game_id: gameId, guess }),
  })
}

export function finishGame(gameId) {
  return apiRequest(`/finish_game/${gameId}`, {
    method: 'POST',
  })
}

export function getLeaderboard() {
  return apiRequest('/get_leaderboard')
}
