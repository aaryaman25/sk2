import React, { useEffect, useState } from 'react';
import apiService from '../apiService'; // Import the apiService

const Profile = () => {
    const [user, setUser] = useState(null);
    const [error, setError] = useState('');

    useEffect(() => {
        const fetchUserProfile = async () => {
            try {
                const profileData = await apiService.getProfile(); // Fetch the profile data
                setUser(profileData); // Set the user data
            } catch (err) {
                setError('Failed to fetch user profile'); // Handle error
            }
        };

        fetchUserProfile();
    }, []);

    if (error) return <p>{error}</p>; // Display error if any
    if (!user) return <div>Loading...</div>; // Display loading state

    return (
        <div>
            <h2>User Profile</h2>
            <p>Name: {user.username}</p>
            <p>Email: {user.email}</p>
            {/* Add other user details as necessary */}
        </div>
    );
};

export default Profile;
