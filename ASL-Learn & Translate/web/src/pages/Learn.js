import React from 'react';
import { useNavigate } from 'react-router-dom';
import '../styles/Pages.css';

const Learn = () => {
  const navigate = useNavigate();

  const handleLevelClick = (level) => {
    navigate(`/learn/${level}`);
  };

  return (
    <div className="page learn-page container">
      <h1>Learn ASL</h1>
      <p>Choose your level to begin learning:</p>
      <div className="level-boxes">
        <div className="level-box" onClick={() => handleLevelClick('beginner')}>
          Beginner
        </div>
        <div className="level-box" onClick={() => handleLevelClick('intermediate')}>
          Intermediate
        </div>
        <div className="level-box" onClick={() => handleLevelClick('advanced')}>
          Advanced
        </div>
      </div>
    </div>
  );
};

export default Learn;
