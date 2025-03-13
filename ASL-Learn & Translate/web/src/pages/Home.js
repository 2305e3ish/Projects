import React from 'react';
import { useNavigate } from 'react-router-dom';
import APIContainer from '../components/APIContainer';
import '../styles/Pages.css';

const Home = () => {
  const navigate = useNavigate();

  const handleGetStarted = () => {
    navigate("/learn");
  };

  return (
    <div className="page home-page">
      <h1>Welcome to Smart ASL</h1>
      {/* Example content container for the home page */}
      <div className="home-box">
        <APIContainer label="Home Content" />
      </div>
      {/* Get Started button */}
      <button className="cta-button" onClick={handleGetStarted}>Get Started</button>
    </div>
  );
};

export default Home;
