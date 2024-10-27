import React from 'react';

const UserProfile = ({ user }) => {
    return (
        <div>
            <h2>User Profile</h2>
            <p>Name: {user.username}</p> {/* Adjust based on your user object */}
            <p>Email: {user.email}</p> {/* Adjust based on your user object */}
            {/* Display any other user information you want */}
        </div>
    );
};

export default UserProfile;
