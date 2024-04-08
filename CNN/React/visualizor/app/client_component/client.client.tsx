"use client"
import React, { useState } from 'react';

function Client() {
  const [message, setMessage] = useState('');

  const fetchMessage = async () => {
    const response = await fetch('http://localhost:5000/run-script',{ method: 'get', mode: 'cors' });
    const data = await response.json();
    setMessage(data.message);
  };

  return (
    <div>
        <p>{message || "Click the button to get a message from Flask!"}</p>
        <button onClick={fetchMessage}>Get Message</button>
    </div>
  );
}

export default Client;