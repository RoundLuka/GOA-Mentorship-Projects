import { useState } from "react";

export default function BookingTbilisi() {
  const [formData, setFormData] = useState({ name: "", email: "" });

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!formData.name || !formData.email) {
      return alert("Please fill in all fields.")
    }


    alert(`Booking confirmed for ${formData.name} to Tbilisi`)
    window.location.href = "/booking-success";
  };

  return (
    
    <form className="bookForm" onSubmit={handleSubmit}>
      <h2 className="bookingHeader">Book your trip to Tbilisi</h2>
      <img className="bookingImg" src="https://www.eurojet-service.com/uploads/584425240-hero-city-getaway-in-the-caucasus-tbilisi.jpg" />
      <input type="text" placeholder="Your name" value={formData.name} onChange={e => setFormData({ ...formData, name: e.target.value })} required />
      <br />
      <input type="email" placeholder="Your email" value={formData.email} onChange={e => setFormData({ ...formData, email: e.target.value })} required />
      <br />
      <button type="submit">Confirm Booking</button>
    </form>
  );
}

