import axiosClient from './axiosClient';

export const signup = (payload) => axiosClient.post('/signup', payload);
export const login = (payload) => axiosClient.post('/login', payload);
