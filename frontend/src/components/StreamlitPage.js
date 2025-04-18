import React from 'react';

const StreamlitPage = () => {
  return (
    <div>
      <h2>Streamlit App Embedded in React</h2>
      <iframe
        title="Streamlit App"
        src="http://localhost:8501"  // The URL of your locally running Streamlit app
        width="100%"                // Make the iframe take full width of the parent container
        height="800px"              // Set a reasonable height for the iframe
        frameBorder="0"             // No border for the iframe
      />
    </div>
  );
};

export default StreamlitPage;
