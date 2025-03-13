import React from 'react';
import APIContainer from '../components/APIContainer';
import '../styles/Pages.css';

const Practice = () => {
  return (
    <div className="page practice-page">
      <h1>Practice ASL</h1>
      {/* "Tests" heading */}
      <h2>Tests</h2>
      {/* API container below the "Tests" heading */}
      <div className="practice-box">
        <APIContainer label="Practice Test" />
      </div>
      <p>Test your skills with interactive exercises.</p>
    </div>
  );
};

export default Practice;
