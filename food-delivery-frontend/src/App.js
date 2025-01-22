import React from 'react';
import {BrowserRouter, Routes, Route} from "react-router-dom";
import './App.css';
import RestaurantList from './components/RestaurantList'
import Navbar from './components/Navbar';


function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path='/' element={<Navbar/>}/>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
