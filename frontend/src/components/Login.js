import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import apiService from '../apiService'; // Import the apiService

const Login = () => {
    const [username, setUsername] = useState(''); // Change email to username
    const [password, setPassword] = useState('');
    const [error, setError] = useState('');
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            await apiService.login({ username, password }); // Call the login method with username
            navigate('/profile'); // Redirect to profile after successful login
        } catch (err) {
            setError('Invalid username or password'); // Display error message
        }
    };

    return (
        <div>
            <h2>Login</h2>
            <form onSubmit={handleSubmit}>
                <input
                    type="text" // Changed from email to text
                    placeholder="Username" // Update placeholder to "Username"
                    value={username} // Bind to username state
                    onChange={(e) => setUsername(e.target.value)} // Update state with username
                    required
                />
                <input
                    type="password"
                    placeholder="Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                />
                <button type="submit">Login</button>
                {error && <p>{error}</p>}
            </form>
        </div>
    );
};

export default Login;
