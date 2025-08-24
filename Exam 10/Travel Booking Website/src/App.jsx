import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./pages/Home";
import Paris from "./pages/Paris";
import London from "./pages/London";
import Tbilisi from "./pages/Tbilisi";
import BookingParis from "./pages/BookingParis";
import BookingLondon from "./pages/BookingLondon";
import BookingTbilisi from "./pages/BookingTbilisi";
import BookingSuccess from "./pages/BookingSuccess";
import './App.css';


function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/paris" element={<Paris />} />
        <Route path="/london" element={<London />} />
        <Route path="/tbilisi" element={<Tbilisi />} />
        <Route path="/book-paris" element={<BookingParis />} />
        <Route path="/book-london" element={<BookingLondon />} />
        <Route path="/book-tbilisi" element={<BookingTbilisi />} />
        <Route path="/booking-success" element={<BookingSuccess />} />
      </Routes>
    </Router>
  );
}

export default App;
