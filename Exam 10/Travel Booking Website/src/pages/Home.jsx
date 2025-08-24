export default function Home() {
  return (
    <div id="home">
      <h1>Book Travels</h1>
      <div id="label">
        <p>Booking at excellent prices</p>
        <p>Select a destination:</p>
      </div>
      <div id="places">
        <a href="/paris"><div id="parisCard" className="travelCity">
            Paris
            <img className="cardImg" alt="Paris" src='https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/La_Tour_Eiffel_vue_de_la_Tour_Saint-Jacques%2C_Paris_ao%C3%BBt_2014_%282%29.jpg/330px-La_Tour_Eiffel_vue_de_la_Tour_Saint-Jacques%2C_Paris_ao%C3%BBt_2014_%282%29.jpg' />
          </div></a>
        <a href="/london"><div id="londonCard" className="travelCity">
            London
            <img className="cardImg" src="https://wikitravel.org/upload/shared//thumb/d/d0/Clock_Tower.jpg/300px-Clock_Tower.jpg" alt="London" />
          </div></a>
          
        <a href="/tbilisi"><div id="tbilisiCard" className="travelCity">
            Tbilisi
            <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Central_part_of_Tbilisi.jpg/300px-Central_part_of_Tbilisi.jpg" alt="Tbilisi" className="cardImg" />
          </div></a>
      </div>
    </div>
  );
}
