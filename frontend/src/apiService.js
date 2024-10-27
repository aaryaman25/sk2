// src/apiService.js
import axios from 'axios';

const API_BASE_URL = 'http://127.0.0.1:8000/api'; // Adjust the URL to your Django backend

// Set up an instance of axios
const apiClient = axios.create({
    baseURL: API_BASE_URL,
    headers: {
        'Content-Type': 'application/json',
    },
});

// Register a new user
const register = async (userData) => {
    try {
        const response = await apiClient.post('/register/', userData);
        return response.data;
    } catch (error) {
        throw error.response ? error.response.data : 'Registration failed.';
    }
};

// Log in an existing user
const login = async (credentials) => {
    try {
        const response = await apiClient.post('/login/', credentials);
        localStorage.setItem('token', response.data.token);
        return response.data;
    } catch (error) {
        throw error.response ? error.response.data : 'Login failed.';
    }
};

// Retrieve user profile
const getProfile = async () => {
    const token = localStorage.getItem('token');
    try {
        const response = await apiClient.get('/profile/', {
            headers: {
                Authorization: `Token ${token}`, // Use your token format
            },
        });
        return response.data;
    } catch (error) {
        throw error.response ? error.response.data : 'Failed to fetch profile.';
    }
};

// Fetch job listings
const getJobs = async () => {
    try {
        const response = await apiClient.get('/jobs/'); // Adjust this endpoint based on your Django setup
        return response.data; // Adjust based on your API response structure
    } catch (error) {
        throw error.response ? error.response.data : 'Failed to fetch jobs.';
    }
};

// Exporting the API methods
const apiService = {
    register,
    login,
    getProfile,
    getJobs, // Add getJobs to the exported methods
};

export default apiService;
