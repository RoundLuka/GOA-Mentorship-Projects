import { useState } from 'react'
import './App.css'

function App() {
  const apiKey = 'b267c0add690d4d5d51b2e499de2039c'
  const [data, setData] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
  
  


    const city = e.target.city.value
    try {
      const response = await fetch(`https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKey}
        `)
        const weatherInfo = await response.json();
        setData(weatherInfo)
        e.target.reset()
    } catch (error) {
      console.log("Error", error)
    }


  }

  

  return (
    <>
      <h1>Search weather</h1>
      <form onSubmit={handleSubmit}>
        <input type='text' name='city' placeholder='Search city' required/>
        <button type='submit'>Search</button>
      </form>

      
      {data && (
        <div>
          <h2>City Name: {data.name}</h2>
          <p>Temperature {Math.floor(data.main.temp - 273.15)}°C</p>
          <p>Weather condition:  {data.weather[0].description}</p>
        </div>
      )}
    </>
  )
}

export default App
