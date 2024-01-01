import React, { useState, useEffect } from 'react';
import { Link, useLocation } from 'react-router-dom';

const OTPPage = () => {
    const [phoneNumber, setPhoneNumber] = useState('');
    const [email, setEmail] = useState('');
    const [otp, setOTP] = useState('');
    const [timer, setTimer] = useState(30);

    const location = useLocation();

    useEffect(() => {
        // Extract phone number and email from the location state
        if (location.state) {
            setPhoneNumber(location.state.phoneNumber);
            setEmail(location.state.email);
        }

        let interval;

        if (timer > 0) {
            interval = setInterval(() => {
                setTimer((prevTimer) => prevTimer - 1);
            }, 1000);
        }

        return () => clearInterval(interval);
    }, [location.state, timer]);

    const handleResendOTP = () => {
        // Implement logic to resend OTP
        setTimer(30); // Reset the timer
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        // Implement logic to verify OTP and phone number
        // If verification is successful, navigate to the next page
    };

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <label>
                    Phone Number:
                    <input
                        type="text"
                        name="phoneNumber"
                        value={phoneNumber}
                        onChange={(e) => setPhoneNumber(e.target.value)}
                        disabled // Disable editing the phone number after registration
                    />
                </label>

                <label>
                    Email:
                    <input
                        type="text"
                        name="email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        disabled // Disable editing the email after registration
                    />
                </label>

                <label>
                    OTP:
                    <input
                        type="text"
                        name="otp"
                        value={otp}
                        onChange={(e) => setOTP(e.target.value)}
                    />
                </label>

                <div className="timer-message">
                    {timer > 0 ? `Resend OTP in ${timer} seconds` : 'Click here to '}
                    <button type="button" onClick={handleResendOTP} disabled={timer > 0}>
                        Resend OTP
                    </button>
                </div>

                <button type="submit">Verify OTP</button>
            </form>

            <Link to="/" className="home-button">
                Home
            </Link>
        </div>
    );
};

export default OTPPage;
