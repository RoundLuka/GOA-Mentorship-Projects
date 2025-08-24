import { useState } from "react";

export default function BookingParis() {
  const [formData, setFormData] = useState({ name: "", email: "" });

  const handleSubmit = (e) => {
    e.preventDefault();


    
    if (!formData.name || !formData.email) {
      return alert("Please fill in all fields.")
    }


    alert(`Booking confirmed for ${formData.name} to Paris`)
    window.location.href = "/booking-success";
  };

  return (
    <form className="bookForm" onSubmit={handleSubmit}>
      <h2 className="bookingHeader">Book your trip to Paris</h2>
      <img className="bookingImg" src="https://www.travelandleisure.com/thmb/SPUPzO88ZXq6P4Sm4mC5Xuinoik=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/eiffel-tower-paris-france-EIFFEL0217-6ccc3553e98946f18c893018d5b42bde.jpg" />
      <input type="text" placeholder="Your name" value={formData.name} onChange={e => setFormData({ ...formData, name: e.target.value })} required />
      <br />
      <input type="email" placeholder="Your email" value={formData.email} onChange={e => setFormData({ ...formData, email: e.target.value })} required />
      <br />
      <button type="submit">Confirm Booking</button>
    </form>
  );
}


