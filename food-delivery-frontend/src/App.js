import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import './App.css';
import Navbar from './components/Navbar';
import Restaurant from './components/Restaurant';
import RestaurantWrapper from './components/RestaurantWrapper'

function App() {
  return (
    <BrowserRouter>
      <Navbar />
      <Routes>
        <Route path="/" element={<Restaurant />} />
        <Route path="/store/:id" element={<RestaurantWrapper/>} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
