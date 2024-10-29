import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import Spline from "@splinetool/react-spline";
import Login from './components/Login';
import Profile from './components/Profile';
import Register from './components/Register';
import JobList from './components/JobList';
import { useState } from 'react'; // Import useState
import PropTypes from 'prop-types'; // Import PropTypes

export default function App() {
    return (
        <Router>
            <div style={styles.container}>
                {/* Navigation Links */}
                <nav style={styles.nav}>
                    <CustomNavLink to="/">Home</CustomNavLink>
                    <CustomNavLink to="/login">Login</CustomNavLink>
                    <CustomNavLink to="/register">Register</CustomNavLink>
                </nav>

                <Routes>
                    {/* Home page with Spline and README */}
                    <Route 
                        path="/" 
                        element={
                            <>
                                {/* Spline Section */}
                                <div style={styles.splineContainer}>
                                    <Spline scene="https://prod.spline.design/m15wGEabz5BWnnLl/scene.splinecode" />
                                </div>

                                {/* About Us Section */}
                                <div
                                    style={{
                                        padding: "20px",
                                        backgroundColor: "#020202", // Slightly lighter pitch black
                                        color: "white",
                                        minHeight: "100vh",
                                        textAlign: "center",
                                        boxShadow: "0 0 15px rgba(0, 0, 0, 0.5)", // Subtle shadow for depth
                                    }}
                                >
                                    <h1
                                        style={{
                                            marginBottom: "20px",
                                            fontSize: "2.5rem", // Increased font size for the heading
                                            transition: "text-shadow 0.3s ease, color 0.3s ease", // Smooth transition for glow effect
                                            cursor: "pointer",
                                        }}
                                        onMouseOver={(e) => {
                                            e.currentTarget.style.textShadow = "0 0 3px white, 0 0 5px white"; // Adjusted glow values for subtlety
                                            e.currentTarget.style.color = "#00000"; // Change color on hover
                                        }}
                                        onMouseOut={(e) => {
                                            e.currentTarget.style.textShadow = "none"; // Remove glow on mouse out
                                            e.currentTarget.style.color = "white"; // Revert color
                                        }}
                                    >
                                        About Us
                                    </h1>
                                    <p
                                        style={{
                                            marginBottom: "15px", // Added margin for spacing
                                            transition: "text-shadow 0.3s ease, color 0.3s ease", // Smooth transition for hover effect
                                            cursor: "pointer",
                                        }}
                                        onMouseOver={(e) => {
                                            e.currentTarget.style.textShadow = "0 0 3px white, 0 0 5px white"; // Adjusted glow values for subtlety
                                            e.currentTarget.style.color = "#00000"; // Change color on hover
                                        }}
                                        onMouseOut={(e) => {
                                            e.currentTarget.style.textShadow = "none"; // Remove glow on mouse out
                                            e.currentTarget.style.color = "white"; // Revert color
                                        }}
                                    >
                                        Welcome to SkillSync, your ultimate tool for real-time workforce management and upskilling. This is our first beta test of the platform, designed to optimize workforce matching, reduce unemployment, and empower enterprises, freelancers, and governments to stay future-ready.
                                    </p>
                                    <p
                                        style={{
                                            transition: "text-shadow 0.3s ease, color 0.3s ease", // Smooth transition for hover effect
                                            cursor: "pointer",
                                        }}
                                        onMouseOver={(e) => {
                                            e.currentTarget.style.textShadow = "0 0 3px white, 0 0 5px white"; // Adjusted glow values for subtlety
                                            e.currentTarget.style.color = "#00000"; // Change color on hover
                                        }}
                                        onMouseOut={(e) => {
                                            e.currentTarget.style.textShadow = "none"; // Remove glow on mouse out
                                            e.currentTarget.style.color = "white"; // Revert color
                                        }}
                                    >
                                        SkillSync leverages generative AI to map skills with opportunities, identify skill gaps, and recommend personalized upskilling paths. Our platform is perfect for anyone looking to manage and streamline workforce capabilities efficiently.
                                    </p>
                                </div>

                            </>
                        } 
                    />

                    {/* Login page */}
                    <Route path="/login" element={<Login />} /> 

                    {/* Register page */}
                    <Route path="/register" element={<Register />} /> 

                    {/* Profile page */}
                    <Route path="/profile" element={<Profile />} /> 

                    {/* JobList page */}
                    <Route path="/jobs" element={<JobList />} /> 
                </Routes>
            </div>
        </Router>
    );
}

// Custom NavLink component for glowing effect
const CustomNavLink = ({ to, children }) => {
    const [isHovered, setIsHovered] = useState(false);

    return (
        <Link
            to={to}
            style={{ ...styles.link, textShadow: isHovered ? '0 0 3px white, 0 0 5px white' : 'none' }}
            onMouseOver={() => setIsHovered(true)}
            onMouseOut={() => setIsHovered(false)}
        >
            {children}
        </Link>
    );
};

// Prop Types validation
CustomNavLink.propTypes = {
    to: PropTypes.string.isRequired,
    children: PropTypes.node.isRequired,
};

// Styles for layout and navigation
const styles = {
    container: {
        display: "flex",
        flexDirection: "column",
        minHeight: "100vh",
        overflow: "hidden", // Prevent overflow
    },
    nav: {
        position: "absolute",
        top: "20px",
        right: "20px",
        zIndex: 1000,
        display: "flex",
        gap: "15px",
    },
    link: {
        color: "white",
        textDecoration: "none",
        fontSize: "1rem",
        padding: "5px 10px",
        borderRadius: "5px",
        backgroundColor: "rgba(255, 255, 255, 0.1)",
        transition: "background-color 0.3s, text-shadow 0.3s",
    },
    splineContainer: {
        height: "100vh", // Full height for Spline section
        width: "100vw",
        overflow: "hidden", // Hide overflow to avoid scroll bars
    },
    aboutContainer: {
        padding: "20px",
        backgroundColor: "#020202", // Slightly lighter pitch black
        color: "white",
        flexGrow: 1, // Allow this section to take remaining space
        textAlign: "center",
        boxShadow: "0 0 15px rgba(0, 0, 0, 0.5)", // Subtle shadow for depth
        display: "flex",
        flexDirection: "column",
        justifyContent: "center", // Center content vertically
    },
    aboutTitle: {
        marginBottom: "20px",
        fontSize: "2.5rem", // Increased font size for the heading
        transition: "text-shadow 0.3s ease, color 0.3s ease", // Smooth transition for glow effect
        cursor: "pointer",
    },
    aboutText: {
        marginBottom: "15px", // Added margin for spacing
        transition: "text-shadow 0.3s ease, color 0.3s ease", // Smooth transition for hover effect
        cursor: "pointer",
    },
};
