import { useState } from "react";

export default function BookingLondon() {
  const [formData, setFormData] = useState({ name: "",   email: "" });

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!formData.name || !formData.email) {
      return alert("Please fill in all fields.")
    }

    alert(`Booking confirmed for ${formData.name} to London`)
    window.location.href = "/booking-success";
  };

  return (
    
    <form className="bookForm" onSubmit={handleSubmit}>
      <h2 className="bookingHeader">Book your trip to London</h2>
      <img className="bookingImg" src="https://media.cntraveler.com/photos/66ec5d99c2fb737668ff3872/16:9/w_5616,h_3159,c_limit/GettyImages-488479062.jpg" />
      <input type="text" placeholder="Your name" value={formData.name} onChange={e => setFormData({ ...formData, name: e.target.value })} required />
      <br />
      <input type="email" placeholder="Your email" value={formData.email} onChange={e => setFormData({ ...formData, email: e.target.value })} required />
      <br />
      <button type="submit">Confirm Booking</button>
    </form>
  );
}
