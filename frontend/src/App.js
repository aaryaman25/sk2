import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Spline from "@splinetool/react-spline";
import Login from './components/Login';
import Profile from './components/Profile';
import Register from './components/Register';
import JobList from './components/JobList';

export default function App() {
    return (
        <Router>
            <div style={{ minHeight: "200vh", overflowY: "scroll" }}>
                <Routes>
                    {/* Home page with Spline and README */}
                    <Route 
                        path="/" 
                        element={
                            <>
                                {/* Spline Section */}
                                <div style={{ height: "100vh", width: "100vw" }}>
                                    <Spline scene="https://prod.spline.design/m15wGEabz5BWnnLl/scene.splinecode" />
                                </div>

                                {/* README Section */}
                                <div
                                    style={{
                                        padding: "20px",
                                        backgroundColor: "#0a0a0a", // Slightly lighter pitch black
                                        color: "white",
                                        minHeight: "100vh",
                                        textAlign: "center",
                                    }}
                                >
                                    <h1 style={{ textShadow: "0px 0px 8px rgba(255, 255, 255, 0.8)" }}>
                                        README Section
                                    </h1>
                                    <p>
                                        Welcome to SkillSync, your ultimate tool for real-time workforce management and upskilling. SkillSync is a generative AI-powered platform designed to optimize workforce matching, reduce unemployment, and empower enterprises, freelancers, and governments to stay future-ready. SkillSync leverages AI to map skills with opportunities, identify skill gaps, and recommend personalized upskilling paths. Our platform is perfect for anyone looking to manage and streamline workforce capabilities efficiently.
                                    </p>
                                    <p>
                                        You can provide instructions, features, or any other details you&apos;d like to include.
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
