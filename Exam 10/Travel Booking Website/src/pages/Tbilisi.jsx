import { useNavigate } from "react-router-dom";

export default function Tbilisi() {
    const navigate = useNavigate();

    return (
        <div className="desCard">
            <h2 className="desCardHeader">Welcome to Tbilisi</h2>
            <img className="desCardImg" src="https://storage.georgia.travel/images/tbilisi-capital-of-georgia-country.webp" alt="Tbilisi" />
            <p className="desCardP">Tbilisi is full of warm people, rich cuisine, and beautiful landscapes.</p>
            <button className="desCardBtn" onClick={() => navigate("/book-tbilisi")}>Book this trip</button>
        </div>
    );
}