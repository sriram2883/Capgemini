import React from "react";

function Cart({ cart, removeFromCart }) {
  const totalCost = cart.reduce((total, item) => total + item.cost, 0);

  return (
    <div>
      <h2>Cart</h2>
      {cart.length === 0 ? <p>Cart is empty</p> : (
        <>
          <ul>
            {cart.map((item, index) => (
              <li key={index}>
                {item.name} - ${item.cost}{" "}
                <button onClick={() => removeFromCart(index)}>Remove</button>
              </li>
            ))}
          </ul>
          <p><strong>Total: ${totalCost}</strong></p>
        </>
      )}
    </div>
  );
}

export default Cart;
