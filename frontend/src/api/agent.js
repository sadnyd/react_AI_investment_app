import axiosClient from './axiosClient';

export const getRecommendation = () => axiosClient.get('/recommendation');
