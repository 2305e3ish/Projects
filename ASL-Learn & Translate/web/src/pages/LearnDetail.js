import React from 'react';
import { useParams } from 'react-router-dom';
import APIContainer from '../components/APIContainer';
import '../styles/Pages.css';

const LearnDetail = () => {
  const { level } = useParams();

  return (
    <div className="page learn-detail-page">
      <h1>{level.charAt(0).toUpperCase() + level.slice(1)} Level Lessons</h1>
      
      {/* Camera input container */}
      <div className="camera-section">
        <APIContainer label="Camera Input" />
      </div>
      
      {/* ML Model output container */}
      <div className="ml-output-section">
        <APIContainer label="ML Model Output" />
      </div>
      
      {/* Previous and Next buttons */}
      <div className="learn-detail-buttons">
        <button className="nav-button">Previous</button>
        <button className="nav-button">Next</button>
      </div>
    </div>
  );
};

export default LearnDetail;
