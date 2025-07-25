import axiosClient from './axiosClient';

export const saveProfile = (payload) => axiosClient.post('/profile', payload);
export const getProfile = () => axiosClient.get('/profile');
