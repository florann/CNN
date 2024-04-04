// use client
import React, { useState } from 'react';
import './App.css';

function App() {
  const [message, setMessage] = useState('');

  const fetchMessage = async () => {
    const response = await fetch('http://localhost:5000/run-script');
    const data = await response.json();
    setMessage(data.message);
  };

  return (
    <div className="App">
      <header className="App-header">
        <p>{message || "Click the button to get a message from Flask!"}</p>
        <button onClick={fetchMessage}>Get Message</button>
      </header>
    </div>
  );
}

export default App;