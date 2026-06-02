import { apiClient } from './apiClient';
export const faceService = {
  register: async (data) => apiClient.post('/register', data),
  list: async () => apiClient.get('/persons'),
};
