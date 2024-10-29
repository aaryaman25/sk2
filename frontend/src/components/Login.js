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
        <div style={styles.container}>
            <h2 style={styles.title}>Login</h2>
            <form onSubmit={handleSubmit} style={styles.form}>
                <input
                    type="text" // Changed from email to text
                    placeholder="Username" // Update placeholder to "Username"
                    value={username} // Bind to username state
                    onChange={(e) => setUsername(e.target.value)} // Update state with username
                    required
                    style={styles.input} // Apply styles to input
                />
                <input
                    type="password"
                    placeholder="Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                    style={styles.input} // Apply styles to input
                />
                <button type="submit" style={styles.button}>Login</button>
                {error && <p style={styles.error}>{error}</p>}
            </form>
        </div>
    );
};

const styles = {
    container: {
        backgroundColor: '#000000', // Black background
        minHeight: '100vh', // Full viewport height
        color: 'white', // Text color for contrast
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        justifyContent: 'center',
        padding: '20px',
    },
    title: {
        fontSize: '2rem',
        marginBottom: '20px',
    },
    form: {
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
    },
    input: {
        padding: '10px',
        marginBottom: '10px',
        width: '300px',
        border: 'none',
        borderRadius: '4px',
        outline: 'none',
        backgroundColor: '#333', // Darker input background
        color: 'white',
    },
    button: {
        padding: '10px 20px',
        backgroundColor: '#ccc', // Softer grey color for the button
        color: 'black', // Change text color to black for contrast
        border: 'none',
        borderRadius: '4px',
        cursor: 'pointer',
        transition: 'background-color 0.3s', // Smooth transition for hover effect
    },
    error: {
        color: 'red',
        marginTop: '10px',
    },
};

// Add hover effect for button
styles.buttonHover = {
    backgroundColor: '#bbb', // Darker grey on hover
};

export default Login;
