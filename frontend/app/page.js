// Place this in your React project under:
// frontend-react/src/components/ChatUI.jsx
"use client"
import React, { useState, useRef, useEffect } from 'react';
import './ChatUI.css'; // You can style to match ChatGPT UI

export default function ChatUI() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const bottomRef = useRef(null);

  // Scroll to bottom on new message
  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  async function sendMessage() {
    if (!input.trim()) return;
    const userMsg = { role: 'user', content: input };
    setMessages(prev => [...prev, userMsg]);
    setInput('');

    const res = await fetch('http://localhost:7860/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ question: input }),
    });
    const { answer } = await res.json();
    const botMsg = { role: 'assistant', content: answer };
    setMessages(prev => [...prev, botMsg]);
  }

  function handleKeyDown(e) {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      sendMessage();
    }
  }

  return (
    <div className="chat-container">
      <div className="messages">
        {messages.map((msg, idx) => (
          <div key={idx} className={msg.role === 'user' ? 'message user' : 'message bot'}>
            <pre>{msg.content}</pre>
          </div>
        ))}
        <div ref={bottomRef} />
      </div>

      <div className="input-area">
        <textarea
          className="chat-input"
          placeholder="Type a message..."
          value={input}
          onChange={e => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
        />
        <button className="send-button" onClick={sendMessage}>Send</button>
      </div>
    </div>
  );
}
