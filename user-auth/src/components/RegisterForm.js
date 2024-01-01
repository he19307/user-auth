// src/components/RegisterForm.js
import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import './RegisterForm.css'; // Import the CSS file

const RegisterForm = () => {
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: '',
    confirmPassword: '',
    phoneNumber: '',
    firstName: '',
    lastName: '',
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
      saveDataToJSON(formData);
      alert('Registration successful!');
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

  const saveDataToJSON = (data) => {
    // Implement saving data to JSON file or API here
    console.log('Saving data to JSON:', data);
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label>
          Username:
          <input type="text" name="username" value={formData.username} onChange={handleChange} />
          {errors.username && <div className="error">{errors.username}</div>}
        </label>

        <label>
          Email:
          <input type="email" name="email" value={formData.email} onChange={handleChange} />
          {errors.email && <div className="error">{errors.email}</div>}
        </label>

        <label>
          Password:
          <input type="text" name="password" value={formData.password} onChange={handleChange} />
          {errors.password && <div className="error">{errors.password}</div>}
        </label>

        <label>
          Confirm Password:
          <input type="text" name="confirmPassword" value={formData.confirmPassword} onChange={handleChange} />
          {errors.confirmPassword && <div className="error">{errors.confirmPassword}</div>}
        </label>

        <label>
          Phone Number:
          <input type="text" name="phoneNumber" value={formData.phoneNumber} onChange={handleChange} />
          {errors.phoneNumber && <div className="error">{errors.phoneNumber}</div>}
        </label>

        <label>
          First Name:
          <input type="text" name="firstName" value={formData.firstName} onChange={handleChange} />
          {errors.firstName && <div className="error">{errors.firstName}</div>}
        </label>

        <label>
          Last Name:
          <input type="text" name="lastName" value={formData.lastName} onChange={handleChange} />
          {errors.lastName && <div className="error">{errors.lastName}</div>}
        </label>

        <button type="submit">Register</button>
      </form>

      <Link to="/" className="home-button">
        Home
      </Link>
    </div>
  );
};

export default RegisterForm;
