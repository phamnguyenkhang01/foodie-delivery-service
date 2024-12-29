import React, {useEffect, useState} from 'react';
import io from 'socket.io-client';

const OrderUpdates = () =>{
    const [orderStatus, setOrderStatus] = useState('');

    useEffect(() => {
        // Replace with your backend server URL
        const socket = io('http://localhost:5000');  // Use your backend server URL here
    
        // Listen for order updates
        socket.on('orderUpdate', (status) => {
          setOrderStatus(status);
        });
    
        // Clean up the socket connection when the component unmounts
        return () => {
          socket.disconnect();
        };
      }, []);

      return (
        <div>
            <h1>Order Status</h1>
            <p>{orderStatus}</p>
        </div>
      );
    };
export default OrderUpdates;