import { useEffect, useState } from 'react'
import './App.css'

import ProductCard from './components/ProductCard'
import AuthForm from './components/AuthForm';

function App() {
  const [cartItems, setCartItems] = useState([])
  const [isLoggedIn, setIsLoggedin] = useState(false);
  const [theme, setTheme] = useState("light")
  const [showCart, setShowCart] = useState(false)

  useEffect(() => {
    document.body.className = theme
  }, [theme])
  
  const toggleTheme = () => {
    if (theme === "light") {
      setTheme("dark")
    } else {
      setTheme("light")
    }
  }

  const toggleCart = () => {
    setShowCart(!showCart)
  }

  const handleLogin = (status) => {
    setIsLoggedin(status)
  }

  const onAddToCart = (product) => {
    setCartItems([...cartItems, product])
  }

  const removeFromCart = (IndexToRemove) => {
    const updatedCart = cartItems.filter((_, index) => index !== IndexToRemove)
    setCartItems(updatedCart)
  }

  const products = [
    {
      productName: "apple-macbook",
      desc: "air-13-inch-2022-mc7u4ll-a-m2-chip-16gb-256gb-ssd-space-grey-p45066",
      price: "2999",
      imgSrc: "https://zoommer.ge/_next/image?url=https%3A%2F%2Fs3.zoommer.ge%2Fzoommer-images%2Fthumbs%2F0171989_apple-macbook-air-13-inch-2022-mlxw3lla-m2-chip-8gb256gb-ssd-space-grey-apple-m25nm-apple-8-core-gpu_550.jpeg&w=256&q=50"
    },
    {
      productName: "apple-macbook-air",
      desc: "13-inch-2025-mw0w3ll-a-m4-chip-10c-cpu-8c-gpu-16gb-256gb-ssd-si-p47046",
      price: "3549",
      imgSrc: "https://zoommer.ge/_next/image?url=https%3A%2F%2Fs3.zoommer.ge%2Fsite%2Ff84005f3-485f-4a1c-a018-dc2e8f6e84d7_Thumb.jpeg&w=256&q=50"
    },
    {
      productName: "lenovo-legion",
      desc: "5-16irx9-83dg004drk-grey-p47032",
      price: "4999",
      imgSrc: "https://zoommer.ge/_next/image?url=https%3A%2F%2Fs3.zoommer.ge%2Fsite%2F13c00a70-f3df-4089-a32e-0474b2350127_Thumb.jpeg&w=256&q=50"
    },
    {
      productName: "honor-magicbook",
      desc: "x16-5301alxs-space-grey-p46955",
      price: "1499",
      imgSrc: "https://zoommer.ge/_next/image?url=https%3A%2F%2Fs3.zoommer.ge%2Fsite%2F8189f27e-0063-4323-a8c7-e108da6c5e07_Thumb.jpeg&w=256&q=50https://drive.google.com/file/d/1_wGcYdYXZpJ_WOZgHUekk62_FI9dH9uv/view?usp=drive_link"
    },
  ]



  return (
    <>
      {!isLoggedIn ? (
        <AuthForm onLogin={handleLogin} />
      ) : (
        <>
          <header>
            <h1>Highest Quality Laptops</h1>
            <div id='menu'>
            <button id='logout' onClick={() => setIsLoggedin(false)}>
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="size-6">
                <path strokeLinecap="round" strokeLinejoin="round" d="M8.25 9V5.25A2.25 2.25 0 0 1 10.5 3h6a2.25 2.25 0 0 1 2.25 2.25v13.5A2.25 2.25 0 0 1 16.5 21h-6a2.25 2.25 0 0 1-2.25-2.25V15m-3 0-3-3m0 0 3-3m-3 3H15" />
              </svg>Logout
            </button>
            <button onClick={toggleTheme}>{theme === "light" ? "Switch to 🌑" : "Switch to ☀"}</button>
            <button onClick={toggleCart}>Show Cart
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="size-6">
              <path strokeLinecap="round" strokeLinejoin="round" d="M2.25 3h1.386c.51 0 .955.343 1.087.835l.383 1.437M7.5 14.25a3 3 0 0 0-3 3h15.75m-12.75-3h11.218c1.121-2.3 2.1-4.684 2.924-7.138a60.114 60.114 0 0 0-16.536-1.84M7.5 14.25 5.106 5.272M6 20.25a.75.75 0 1 1-1.5 0 .75.75 0 0 1 1.5 0Zm12.75 0a.75.75 0 1 1-1.5 0 .75.75 0 0 1 1.5 0Z" />
            </svg>

            </button>
            </div>
          </header>
          <div id='ProductContent'>
            <div id='productContainer'>
              <h2>Shop</h2>
              {products.map((item, index) => {
                return <ProductCard key={index} productName={item.productName} desc={item.desc} price={item.price} imgSrc={item.imgSrc} onAddToCart={() => onAddToCart(item)} />
              })}
            </div>
            
            {showCart ? (
              <div id='cartContainer'>
                <h2>Cart</h2>
                {cartItems.map((item, index) => (
                <div className='product' key={index}>
                  <ProductCard key={index} productName={item.productName} desc={item.desc} price={item.price} imgSrc={item.imgSrc} removeFromCart={removeFromCart} indexRemove={index} />
                </div>
              ))}
            </div>
            ) : ''}
          </div>
        </>
      )}


      
    </>
  )
}

export default App
