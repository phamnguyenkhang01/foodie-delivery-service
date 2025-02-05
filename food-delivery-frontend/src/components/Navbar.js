import React, { useState } from "react";
import './Navbar.css';

const Navbar = () => {
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);

  const toggleSidebar = () => {
    setIsSidebarOpen(!isSidebarOpen);
  };

  return (
    <>
      <nav className="navbar navbar-light bg-light">
        <button
          onClick={toggleSidebar}
          className="navbar-button"
        >
          ≡
        </button>
        <a
          href="/"
          className="navbar-brand"
        >
          Eatsy
        </a>
      </nav>

      <div
        className={`sidebar ${isSidebarOpen ? 'sidebar-open' : 'sidebar-close'}`}
      >
        <ul className="sidebar-links">
          <li>
            <button className="sidebar-button-large signup-button">
              Sign Up
            </button>
          </li>
          <li>
            <button className="sidebar-button-large login-button">
              Log In
            </button>
          </li>
        </ul>
      </div>
      {isSidebarOpen && (
        <div
          onClick={toggleSidebar}
          className="sidebar-overlay"
        ></div>
      )}
    </>
  );
};

export default Navbar;
