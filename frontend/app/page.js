
"use client"
import React, { useState, useRef, useEffect } from 'react';
import './ChatUI.css'; 

export default function ChatUI() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const bottomRef = useRef(null);

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages]);

  async function sendMessage() {
    if (!input.trim()) return;
    const userMsg = { role: 'user', content: input };
    setMessages(prev => [...prev, userMsg]);
    setInput('');
    setIsLoading(true);

    try {
      const res = await fetch('/chat', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ question: input }),
      });
      const { answer } = await res.json();
      const botMsg = { role: 'assistant', content: answer };
      setMessages(prev => [...prev, botMsg]);
    } catch (error) {
      console.error('Error:', error);
      const errorMsg = { role: 'assistant', content: 'Sorry, something went wrong. Please try again.' };
      setMessages(prev => [...prev, errorMsg]);
    } finally {
      setIsLoading(false);
    }
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
        {isLoading && (
          <div className="message bot">
            <div className="spinner">
              <div className="bounce1"></div>
              <div className="bounce2"></div>
              <div className="bounce3"></div>
            </div>
          </div>
        )}
        <div ref={bottomRef} />
      </div>

      <div className="input-area" style={{marginBottom: '20px', width: '100%'}}>
        <textarea
          className="chat-input"
          placeholder="Type a message..."
          value={input}
          onChange={e => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
          disabled={isLoading}
          style={{width: '100%'}}
        />
        <button 
          className="send-button" 
          onClick={sendMessage}
          disabled={isLoading}
        >
          Send
        </button>
      </div>
    </div>
  );
}
