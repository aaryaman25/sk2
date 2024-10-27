// src/components/JobList.js
import React, { useEffect, useState } from 'react';
import Papa from 'papaparse';

const JobList = () => {
    const [jobs, setJobs] = useState([]);

    useEffect(() => {
        const fetchJobs = () => {
            Papa.parse('/Jobs_NYC_Postings_20241004.csv', {
                download: true,
                header: true,  // Parse CSV with headers
                complete: (results) => {
                    setJobs(results.data); // Set job data from CSV
                },
                error: (error) => {
                    console.error('Failed to fetch jobs:', error);
                },
            });
        };

        fetchJobs();
    }, []);

    return (
        <div style={styles.container}>
            <h2 style={styles.title}>Job Listings</h2>
            <ul style={styles.jobList}>
                {jobs.map((job, index) => (
                    <li key={index} style={styles.jobItem}>
                        <h3 style={styles.jobTitle}>{job['Business Title'] || 'No Title Available'}</h3>
                        <p><strong>Agency:</strong> {job['Agency'] || 'Agency not available'}</p>
                        <p><strong>Location:</strong> {job['Work Location'] || 'Location not available'}</p>
                        <p><strong>Salary:</strong> ${job['Salary Range From'] || 0} - ${job['Salary Range To'] || 'N/A'}</p>
                        <p><strong>Description:</strong> {job['Job Description'] || 'No description available'}</p>
                    </li>
                ))}
            </ul>
        </div>
    );
};

const styles = {
    container: {
        maxWidth: '800px',
        margin: '0 auto',
        padding: '20px',
        border: '1px solid #ccc',
        borderRadius: '5px',
        backgroundColor: '#f9f9f9',
    },
    title: {
        textAlign: 'center',
        fontSize: '2rem',
        marginBottom: '20px',
        color: '#333',
    },
    jobList: {
        listStyleType: 'none',
        padding: '0',
    },
    jobItem: {
        backgroundColor: '#fff',
        padding: '15px',
        marginBottom: '10px',
        borderRadius: '8px',
        boxShadow: '0 2px 10px rgba(0, 0, 0, 0.1)',
    },
    jobTitle: {
        fontSize: '1.5rem',
        marginBottom: '10px',
        color: '#007bff',
    },
};

export default JobList;
