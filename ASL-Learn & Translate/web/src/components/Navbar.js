import React from "react";
import { Link } from "react-router-dom";
import "./../styles/Navbar.css";

const Navbar = () => {
  return (
    <nav className="navbar">
      <h2>ASL Learn & Translate</h2>
      <ul>
        <li><Link to="/">Learn</Link></li>
        <li><Link to="/translate">Translate</Link></li>
        <li><Link to="/practice">Practice</Link></li>
        <li><Link to="/play">Play</Link></li>
        <li><Link to="/faq">FAQ</Link></li>
      </ul>
    </nav>
  );
};

export default Navbar;
