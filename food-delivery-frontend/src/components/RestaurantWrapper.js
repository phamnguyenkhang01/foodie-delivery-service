import React, { useState, useEffect } from 'react'
import { useParams } from 'react-router-dom'
import { FaHeart } from "react-icons/fa";
// import axios from 'axios';

const RestaurantWrapper = () => {
    const { id } = useParams();
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [restaurant, setRestaurant] = useState(null)
    const [menuItems, setMenuItems] = useState(null)

    useEffect(() => {
        const fetchRestaurants = async () => {
            try {
              const response = await fetch(`http://localhost:8000/restaurants/get/${id}/`);
              if (!response.ok) {
                throw new Error('Failed to fetch data');
              }
              const data = await response.json();
              console.log("Line 16: ", data.menu_items)
              setRestaurant(data.restaurant)
              setMenuItems(data.menu_items)
            } catch (err) {
              setError(err.message);
            } finally {
              setLoading(false);
            }
          };
      
          fetchRestaurants();
    },[id])

    if (loading) return <p>Loading...</p>;
    if (error) return <p>Error: {error}</p>;


    return(
        <div className="container my-4">
            <div className="position-relative">
                <img 
                    src="/images/food.jpeg"
                    alt="Restaurant Cover"
                    className="img-fluid w-100"
                    style={{ maxHeight: "300px", objectFit: "cover" }}
                />
            </div>

        
            <div className="mt-3">
                <h1 className="fw-bold text-uppercase">
                    {restaurant.name}<br/>
                    <span className="d-block mt-2">{restaurant.address}</span>
                </h1>

            <p
                className="fst-italic text-muted"
                style={{ opacity: 0.7 }}
            >
                {restaurant.address}
            </p>
            <p className="text-body">
                This is a description of the restaurant. It serves delicious dishes
                and has a cozy atmosphere. Come visit us for a great experience.
            </p>
            </div>

            <div className="row row-cols-1 row-cols-md-2 g-4 mt-4">
                {menuItems?.map((item, index) => (
                    <div key={index} className="col">
                        <div
                            className="card shadow-sm p-3 hover-effect"
                            style={{
                                cursor: "pointer",
                                transition: "transform 0.2s ease-in-out"
                            }}
                            onMouseEnter={(e) =>
                            (e.currentTarget.style.transform= "scale(1.02)")
                            }
                            onMouseLeave={(e) =>
                            (e.currentTarget.style.transform = "scale(1)")
                            }
                        >
                            <div className="d-flex align-items-center">
                                <div className="flex-grow-1">
                                    <h6 className="fw-bold mb-1">{item.name}</h6>
                                    <p className="mb-1">
                                        ${item.price}
                                        <FaHeart className="text-danger ms-2" />
                                        <span className="ms-1 text-muted small">85%</span>
                                    </p>
                                    <p className="text-muted small mb-0">{item.description}</p>
                                </div>
                                <img 
                                    // src={item.image_url}
                                    src="/images/food.jpeg"
                                    alt={item.name}
                                    className="ms-3"
                                    style={{
                                        width: "80px",
                                        height: "80px",
                                        objectFit: "cover",
                                        borderRadius: "8px"
                                    }}
                                />
                            </div>
                        </div>
                    </div>
                ))}
            </div>
        </div>
    )
}
export default RestaurantWrapper