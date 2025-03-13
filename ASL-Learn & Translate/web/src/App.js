import React from "react";
import { Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import Learn from "./pages/Learn";
import Translate from "./pages/Translate";
import Practice from "./pages/Practice";
import Play from "./pages/Play";
import FAQ from "./pages/FAQ";
import "./styles/App.css";

function App() {
  return (
    <div className="App">
      <Navbar />
      <Routes>
        <Route path="/" element={<Learn />} />
        <Route path="/translate" element={<Translate />} />
        <Route path="/practice" element={<Practice />} />
        <Route path="/play" element={<Play />} />
        <Route path="/faq" element={<FAQ />} />
      </Routes>
    </div>
  );
}

export default App;
