// src/components/LoginForm.js
import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import './LoginForm.css'; // Import the CSS file

const LoginForm = () => {
    const [formData, setFormData] = useState({
        username: '',
        password: '',
    });

    const [errors, setErrors] = useState({});

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData({
            ...formData,
            [name]: value,
        });
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        const validationErrors = validateForm(formData);
        if (Object.keys(validationErrors).length === 0) {
            // You can add further logic for submitting the form (e.g., sending data to a server)
            alert('Login successful!');
        } else {
            setErrors(validationErrors);
        }
    };

    const validateForm = (data) => {
        // Implement your validation logic here
        const errors = {};
        // Example validation: Check if fields are not empty
        Object.keys(data).forEach((key) => {
            if (!data[key]) {
                errors[key] = `${key} is required`;
            }
        });
        return errors;
    };

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <label>
                    Username:
                    <input
                        type="text"
                        name="username"
                        value={formData.username}
                        onChange={handleChange}
                    />
                    {errors.username && <div className="error">{errors.username}</div>}
                </label>

                <label>
                    Password:
                    <input
                        type="password"
                        name="password"
                        value={formData.password}
                        onChange={handleChange}
                    />
                    {errors.password && <div className="error">{errors.password}</div>}
                </label>

                <button type="submit">Login</button>
            </form>

            <Link to="/" className="home-button">
                Home
            </Link>
        </div>
    );
};

export default LoginForm;
