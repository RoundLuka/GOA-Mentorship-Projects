import React, {useState} from "react";


const AuthForm = ( {onLogin} ) => {
    
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [isRegistering, setIsRegistering] = useState(false)

    const handleSubmit = () => {
        const load = localStorage.getItem("users")
        const users = load ? JSON.parse(load) : [];
        

        if(isRegistering) {
            for(let i = 0; i < users.length; i++) {
                if(users[i].username === username ) {
                    alert("Account already exists")
                    return;
                }
            }
            
            if(password.length < 8) {
                alert("Password is too short, must be at least 8 characters long")
                return;
            }

            if(username.length < 5) {
                alert("Username is too short, must be at least 5 characters long")
                return;
            }

            const newUser = {username, password};
            users.push(newUser);
            localStorage.setItem('users', JSON.stringify(users));
            alert("Registration completed")
            setIsRegistering(false)

        } else {
            for(let i = 0; i < users.length; i++) {
                if(users[i].username === username && users[i].password === password) {
                    onLogin(true)
                }
            }
        }
    }

    return (
        <>
        <h1>Highest Quality Laptops</h1>
        <div id="AuthForm">
            <h2>{isRegistering ? "Register" : "Login"}</h2>
            <input type="text" placeholder="Username" value={username} onChange={(e) => setUsername(e.target.value)} />
            <input type="type" placeholder="Password" value={password} onChange={(e) => setPassword(e.target.value)} />
            <button type="submit" onClick={handleSubmit}>{isRegistering ? "Register" : "Login"}</button>

            <p>{isRegistering ? 'Already ave an account?' : 'Dont have an account?'}</p>

            <button onClick={() => setIsRegistering(!isRegistering)}>{isRegistering ? 'Switch to Login' : 'Switch to Register'}</button>
        </div>
        </>
    )
        
}

export default AuthForm;