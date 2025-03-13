import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import Learn from './pages/Learn';
import LearnDetail from './pages/LearnDetail';
import Play from './pages/Play';
import Translate from './pages/Translate';
import Practice from './pages/Practice';
import './styles/App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <Routes>
          <Route path="/" element={<Home />} />           {/* Home Page (Page 5) */}
          <Route path="/learn" element={<Learn />} />       {/* Learn Landing (Page 2) */}
          <Route path="/learn/:level" element={<LearnDetail />} /> {/* Learn Detail (Page 4) */}
          <Route path="/play" element={<Play />} />         {/* Play (Page 1) */}
          <Route path="/translate" element={<Translate />} />{/* Translate (Page 3) */}
          <Route path="/practice" element={<Practice />} />  {/* Practice (Page 6) */}
        </Routes>
      </div>
    </Router>
  );
}

export default App;
