import { useNavigate } from "react-router-dom";

export default function London() {
    const navigate = useNavigate();

    return (
    <div className="desCard">
        <h2 className="desCardHeader">Explore London</h2>
        <img className="desCardImg" src="https://media.cntraveler.com/photos/66ec5d99c2fb737668ff3872/16:9/w_5616,h_3159,c_limit/GettyImages-488479062.jpg" alt="London" />
        <p className="desCardP" >London blends royal history with vibrant city life.</p>
        <button className="desCardBtn" onClick={() => navigate("/book-london")}>Book this trip</button>
    </div>
    )
};


