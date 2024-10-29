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
        <div style={styles.container}>
            <h2 style={styles.title}>Register</h2>
            {error && <p style={styles.error}>{error}</p>} {/* Display error message if exists */}
            <form onSubmit={handleRegister} style={styles.form}>
                <input
                    type="text"
                    placeholder="Username"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    required
                    style={styles.input} // Apply styles to input
                />
                <input
                    type="email"
                    placeholder="Email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
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
                <button type="submit" style={styles.button}>Register</button>
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

export default Register;
