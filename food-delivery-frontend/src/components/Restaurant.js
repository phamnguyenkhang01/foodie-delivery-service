import React, { useState, useEffect } from "react";

const Restaurant = () => {
  const [restaurants, setRestaurants] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchRestaurants = async () => {
      try {
        const response = await fetch('http://127.0.0.1:8000/restaurants/get/101/');
        if (!response.ok) {
          throw new Error('Failed to fetch data');
        }
        const data = await response.json();
        setRestaurants(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchRestaurants();
  }, []);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error: {error}</p>;

  return (
    <div className="container mt-5">
      <div className="row g-4">
        {restaurants.map((restaurant, index) => (
          <div className="col-md-3 mb-4 d-flex justify-content-center" key={index}>
            <div className="card" style={{ width: "18rem" }} role="button">
              <img
                src="./images/food.jpeg"
                className="card-img-top"
                alt={restaurant.name}
                style={{ objectFit: "cover", height: "200px" }}
              />
              <div className="card-body">
                <h5
                  className="card-title text-start text-truncate"
                  style={{ maxWidth: "100%" }}
                  title={restaurant.name} // Full name appears as a tooltip on hover
                >
                  {restaurant.name}
                </h5>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Restaurant;
