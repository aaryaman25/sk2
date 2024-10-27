// src/api.js
import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/api/'; // Adjust this based on your backend URL

export const fetchUserProfile = async () => {
    const response = await axios.get(`${API_URL}profile/`, { headers: { Authorization: `Bearer ${localStorage.getItem('token')}` } });
    return response.data;
};
