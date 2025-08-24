import { useNavigate } from "react-router-dom";



export default function Paris() {
    const navigate = useNavigate();

    return (
        <div className="desCard">
            <h2 className="desCardHeader">Welcome to Paris</h2>
            <img className="desCardImg" src="https://pullman.accor.com/destinations/city/paris-1400x788-3.jpg" alt="Paris" />
            <p className="desCardP">Paris is known for its romantic ambiance and landmarks like the Eiffel Tower.</p>
            <button className="desCardBtn" onClick={() => navigate("/book-paris")}>Book this trip</button>
        </div>
    );
}
