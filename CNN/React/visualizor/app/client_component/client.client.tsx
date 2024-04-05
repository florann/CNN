"use client"
import React, { useState } from 'react';

function Client() {
  const [message, setMessage] = useState('');

  const fetchMessage = async () => {
    const response = await fetch('https://studious-yodel-g74wx6wx9qqhvw5v-5000.app.github.dev/',{ method: 'get', mode: 'cors' });
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