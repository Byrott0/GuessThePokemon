import { API_BASE_URL } from '../config/env'

export async function apiRequest(path, options = {}) {
  const response = await fetch(`${API_BASE_URL}${path}`, {
    headers: {
      'Content-Type': 'application/json',
      ...options.headers,
    },
    ...options,
  })

  if (!response.ok) {
    let message = 'Er ging iets mis met de API.'

    try {
      const errorBody = await response.json()
      message = errorBody.detail ?? message
    } catch {
      message = response.statusText || message
    }

    throw new Error(message)
  }

  return response.json()
}
