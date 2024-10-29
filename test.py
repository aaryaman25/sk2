import pandas as pd
import re
import streamlit as st
from roadmap_generator import generate_roadmap

# Define the skills list once at the top
SKILL_PATTERNS = [
    'Python', 'Java', 'JavaScript', 'C++', 'C#',
    'PHP', 'Swift', 'Go', 'Ruby', 'SQL',
    'MySQL', 'PostgreSQL', 'MongoDB', 'AWS', 'Azure',
    'Google Cloud', 'Docker', 'Kubernetes', 'Git', 'Linux',
    'Communication', 'Leadership', 'Project Management', 'Problem Solving',
    'Teamwork', 'Analytical Skills', 'Machine Learning', 'Data Science',
    'Artificial Intelligence', 'Cloud Computing', 'Cybersecurity',
    'Web Development', 'Mobile Development', 'Software Engineering'
]

# Load the dataframe in chunks
chunksize = 1000
df_chunks = pd.read_csv("Jobs_NYC_Postings_20241004.csv", chunksize=chunksize)

def extract_skills(job_description):
    """
    Extracts common skills from a job description using regular expressions.
    """
    if isinstance(job_description, str):
        skills = []
        for skill in SKILL_PATTERNS:
            pattern = r'\b' + re.escape(skill) + r'\b'
            match = re.search(pattern, job_description, re.IGNORECASE)
            if match:
                skills.append(match.group(0))
        return skills
    else:
        return []

# Process each chunk and concatenate the results
df_list = []
for chunk in df_chunks:
    if 'Skills' not in chunk.columns:
        chunk['Skills'] = chunk['Job Description'].apply(extract_skills)
    df_list.append(chunk)

df = pd.concat(df_list)

def search_jobs_by_skills(user_skills, df):
    """
    Searches for jobs in the dataframe that require any of the user's skills.
    """
    user_skills_lower = [skill.lower() for skill in user_skills]
    return df[df['Skills'].apply(lambda skills: any(skill.lower() in user_skills_lower for skill in skills))]

def find_skills_lacking(user_skills, job_skills):
    """
    Compares user skills to job skills and returns a list of skills the user is lacking.
    """
    # Convert everything to lowercase for comparison
    user_skills_lower = {s.strip().lower() for s in user_skills}
    job_skills_lower = {s.lower() for s in job_skills}
    
    # Return only the skills from the job that the user doesn't have
    lacking_skills = list(job_skills_lower - user_skills_lower)
    return lacking_skills

# Streamlit UI
st.title('Job Skill Search')

# Multiselect for all skills
selected_skills = st.multiselect(
    "Select your skills:",
    options=SKILL_PATTERNS,
    help="Choose all the skills you possess. The search will find jobs matching any of these skills."
)

if selected_skills:
    # Search for jobs that require any of the selected skills
    jobs = search_jobs_by_skills(selected_skills, df)
    
    # Add a 'Skills Lacking' column to the jobs DataFrame
    jobs['Skills Lacking'] = jobs['Skills'].apply(
        lambda job_skills: find_skills_lacking(selected_skills, job_skills)
    )
    
    # Separate jobs with no lacking skills and jobs with lacking skills
    perfect_match_jobs = jobs[jobs['Skills Lacking'].apply(len) == 0]
    jobs_with_lacking_skills = jobs[jobs['Skills Lacking'].apply(len) > 0]
    
    # Show summary statistics first
    st.header("📊 Job Search Summary")
    total_jobs = len(jobs)
    perfect_matches = len(perfect_match_jobs)
    lacking_skills = len(jobs_with_lacking_skills)
    
    # Create three columns for statistics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Jobs Found", total_jobs)
    with col2:
        st.metric("Perfect Matches", perfect_matches)
    with col3:
        st.metric("Jobs Requiring More Skills", lacking_skills)
    
    # Display percentage of matches
    if total_jobs > 0:
        st.write(f"Perfect matches make up {(perfect_matches / total_jobs * 100):.1f}% of found jobs")
        st.progress(perfect_matches / total_jobs)
    
    # Divider
    st.divider()
    
    # Display perfect matches second
    if not perfect_match_jobs.empty:
        st.header("🌟 Perfect Skill Matches")
        st.write(f"These jobs match all your selected skills ({', '.join(selected_skills)}):")
        st.dataframe(
            perfect_match_jobs[['Job ID', 'Business Title', 'Salary Range From', 
                              'Salary Range To', 'Work Location', 'Skills']],
            use_container_width=True
        )
    else:
        st.info("No perfect matches found. Consider adding more skills to your profile!")
    
    # Divider
    st.divider()
    
  # Display jobs requiring additional skills last
    if not jobs_with_lacking_skills.empty:
        st.header("📝 Jobs Requiring Additional Skills")
        st.write("These jobs require some skills you might want to learn:")
        st.dataframe(
            jobs_with_lacking_skills[['Job ID', 'Business Title', 'Salary Range From', 
                                    'Salary Range To', 'Work Location', 'Skills', 'Skills Lacking']],
            use_container_width=True
        )
# Create a set of unique skills to learn
    skills_to_learn = set()  # To store unique skills requiring learning

    for index, row in jobs_with_lacking_skills.iterrows():
        for skill in row['Skills Lacking']:
            skills_to_learn.add(skill)  # Add to the unique set of skills

    # Create a multiselect for the user to select skills they want a roadmap for
    selected_skills = st.multiselect(
        "Select skills to generate a roadmap:",
        options=list(skills_to_learn),
        help="Choose the skills for which you want to generate a learning roadmap."
    )

    # After selecting skills, allow the user to choose experience levels and generate roadmaps
    if selected_skills:
        experience_levels = {}
        
        for skill in selected_skills:
            # Select experience level for the current skill
            experience_level = st.selectbox(
                f"Select your experience level for {skill}:",
                options=["beginner", "intermediate", "advanced"],
                key=f"exp_level_{skill}"  # Use a unique key for each selectbox
            )
            experience_levels[skill] = experience_level  # Store the selected experience level

        # Button to generate roadmap for selected skills
        if st.button("Generate Roadmap"):
            for skill, experience_level in experience_levels.items():
                roadmap_info = generate_roadmap(skill, experience_level)
                st.markdown(f"### Roadmap for {skill} (Experience Level: {experience_level})")
                st.markdown(roadmap_info)
    else:
        st.info("👆 Select skills above to generate a learning roadmap!")
else:
    st.info("👆 Select your skills above to start searching for matching jobs!")


import json
import streamlit as st

# Other existing code...

# Use this function to handle incoming requests
def search_jobs_endpoint():
    if st.button('Search Jobs'):
        skills = st.session_state.get('selected_skills', [])
        jobs = search_jobs_by_skills(skills, df)  # Call your existing function
        st.json(jobs.to_json(orient='records'))  # Return JSON response

# Call the search function in your main Streamlit app logic
search_jobs_endpoint()
