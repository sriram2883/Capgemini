import React, { useState } from "react";
import "./App.css";
import Cart from "./components/Cart.jsx";
import Menu from "./components/Menu.jsx";

function App() {
  const [cart, setCart] = useState([]);

  const addToCart = (item) => {
    setCart([...cart, item]);
  };

  const removeFromCart = (index) => {
    setCart(cart.filter((_, i) => i !== index));
  };

  return (
    <div className="App">
      <div className="items">
        <Menu addToCart={addToCart} cart={cart} removeFromCart={removeFromCart} />
      </div>
    </div>
  );
}

export default App;
