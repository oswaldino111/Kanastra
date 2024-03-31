import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import { FileProvider } from './context/filecontext';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <FileProvider>
        <App />
    </FileProvider>
  </React.StrictMode>
);
