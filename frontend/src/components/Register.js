// src/components/Register.js
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import apiService from '../apiService'; // Adjust the import path if necessary

const Register = () => {
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState(null); // State for error messages
    const navigate = useNavigate();

    const handleRegister = async (e) => {
        e.preventDefault();
        setError(null); // Reset error before attempting to register
        try {
            await apiService.register({ username, email, password }); // Adjust the API call if necessary
            navigate('/login'); // Redirect to login after successful registration
        } catch (error) {
            console.error('Registration failed:', error);
            setError('Registration failed. Please check your input and try again.'); // Set error message
        }
    };

    return (
        <div>
            <h2>Register</h2>
            {error && <p style={{ color: 'red' }}>{error}</p>} {/* Display error message if exists */}
            <form onSubmit={handleRegister}>
                <input
                    type="text"
                    placeholder="Username"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    required
                />
                <input
                    type="email"
                    placeholder="Email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    required
                />
                <input
                    type="password"
                    placeholder="Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                />
                <button type="submit">Register</button>
            </form>
        </div>
    );
};

export default Register;
