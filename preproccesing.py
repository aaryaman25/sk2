import pandas as pd

# Load the data
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

# Preprocess the data
def preprocess_data(df):
    # Example preprocessing steps:
    # Convert dates to the correct format
    df['Posting Date'] = pd.to_datetime(df['Posting Date'], errors='coerce').dt.strftime('%Y-%m-%d')

    # Drop unnecessary columns
    columns_to_drop = ['Column1', 'Column2']  # Replace with actual columns to drop
    df = df.drop(columns=columns_to_drop, errors='ignore')

    # Handle missing values, if necessary
    df = df.fillna({
        'Closing Date': 'Not Specified',  # Example for filling NaNs
    })

    return df

# Save the cleaned data to a new CSV file (optional)
def save_cleaned_data(df, output_file):
    df.to_csv(output_file, index=False)

# Main function
if __name__ == "__main__":
    input_file = '/Users/aaryamanshinde/Downloads/Jobs_NYC_Postings_20241004.csv'
    output_file = 'cleaned_jobs_data.csv'  # Optional

    df = load_data(input_file)
    cleaned_df = preprocess_data(df)
    #save_cleaned_data(cleaned_df, output_file)  # Optional

import pandas as pd
from datetime import datetime

# Load the CSV file
df = cleaned_df

# Select only the relevant columns
df_cleaned = df[['Job ID', 'Business Title', 'Salary Range From', 'Salary Range To', 'Work Location', 'Posting Date', 'Job Description', 'Post Until']]

# Rename the columns to match your Django model fields
df_cleaned.columns = ['job_id', 'business_title', 'salary_range_from', 'salary_range_to', 'work_location', 'posting_date', 'job_description', 'closing_date']

# Convert date columns to proper date format
df_cleaned['posting_date'] = pd.to_datetime(df_cleaned['posting_date'], errors='coerce', format='%m/%d/%Y')
df_cleaned['closing_date'] = pd.to_datetime(df_cleaned['closing_date'], errors='coerce', format='%m/%d/%Y')

# Handle any other necessary cleaning, like filling NaN or missing values
df_cleaned = df_cleaned.fillna('')

# Save the cleaned file
df_cleaned.to_csv('/Users/aaryamanshinde/Desktop/python/skillsync/cleaned_csv_file.csv', index=False)

print("Data preprocessing completed and saved.")
