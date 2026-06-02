import React from 'react';
import { NavLink } from "react-router-dom";
import "./Navbar.css";

function Navbar() {
  return (
    <header className="navbar">
      <div className="navbar-container">
        <h2 className="navbar-logo">Face Recognition Demo</h2>

        <nav className="navbar-links">
          <NavLink to="/">Home</NavLink>
          <NavLink to="/register">Register</NavLink>
          <NavLink to="/live-demo">Live Demo</NavLink>
          <NavLink to="/registered-persons">Persons</NavLink>
        </nav>
      </div>
    </header>
  );
}

export default Navbar;
