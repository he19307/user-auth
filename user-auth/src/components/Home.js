// src/components/Home.js
import React from 'react';
import { Link } from 'react-router-dom';
import './Home.css'; //import the css file

const Home = () => {
    return (
        <div>
            <h1>Welcome to the Home Page</h1>

            <Link to="/login">
                <button>Login</button>
            </Link>

            <Link to="/register">
                <button>Register</button>
            </Link>
        </div>
    );
};

export default Home;

