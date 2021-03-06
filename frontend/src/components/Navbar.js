import React from 'react';
import { Link } from 'react-router-dom';

export const Navbar = () => {
    return (
        <nav className="navbar navbar-expand-lg navbar-light bg-light">
        <div className="container-fluid">
          <Link className="navbar-brand" to="/">Flask And React</Link>
          
          <div className="collapse navbar-collapse" id="navbarNavAltMarkup">
            <div className="navbar-nav">
             
              <Link className="nav-link" to="/about">About</Link>
              
            </div>
          </div>
        </div>
      </nav>
    )
}
