import { useState, useEffect} from 'react'
import './App.css'

function App() {
  const [tasks, setTasks] = useState([]);
  const [editingId, setEditingId] = useState(null);
  const [editingValue, setEditingValue] = useState("")
  const [logged, setLogged] = useState(false)
  const [password, setPassword] = useState("")
  const [isDark, setIsDark] = useState(true)
  const [data, setData] = useState(null)

  useEffect(() => {
    const storedTasks = JSON.parse(localStorage.getItem("tasks"))
    setTasks(storedTasks)
  }, [])

  useEffect(() => {
    if (tasks.length > 0) {
      localStorage.setItem("tasks", JSON.stringify(tasks));
    } 
  }, [tasks])

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch("https://jsonplaceholder.typicode.com/todos")
        const data = await response.json()
        setData(data)
        console.log(data)
      } catch (error) {
        console.log("Error during data fetching", error)
      }
    }
    fetchData()
  }, [])


  const root = document.getElementById("root")
  const toggleTheme = () => {
    setIsDark(!isDark)
    
    if(isDark) {
      root.style.backgroundColor = "#303030"
    } else {
      root.style.backgroundColor = "#FFFFFF"
    }
  }

  const addTask = (e) => {
    e.preventDefault()

    const taskName = e.target.task.value.trim()

    setTasks([...tasks, {id: Date.now(), name: taskName}])
  }

  const beginEditing = (id, currentName) => {


    setEditingId(id)
    setEditingValue(currentName)
    
  }

  const endEditing = () => {  
    setTasks(
      tasks.map((task) =>
        task.id === editingId ? { ...task, name: editingValue } : task
      )
    );
    setEditingId(null);
    setEditingValue("");
  }
  

  const deleteTask = (id) => {
    setTasks(tasks.filter((task) => task.id !== id));  
  }
  
  const handleLogin = (e) => {
    e.preventDefault()

    setPassword(e.target.password.value)

    if (password === "user123") {
      setLogged(true)
    }
  } 



  return (
    <div id='wrapper' className={isDark ? "light" : "dark"}>
      {logged ? (
              <main>

              <div id='settings'>
              <button className='setBtn'  id='themeBtn' onClick={toggleTheme}>Switch theme {isDark ? (
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="size-6">
                <path strokeLinecap="round" strokeLinejoin="round" d="M21.752 15.002A9.72 9.72 0 0 1 18 15.75c-5.385 0-9.75-4.365-9.75-9.75 0-1.33.266-2.597.748-3.752A9.753 9.753 0 0 0 3 11.25C3 16.635 7.365 21 12.75 21a9.753 9.753 0 0 0 9.002-5.998Z" />
              </svg>
              
              
                ) : (
                  <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="size-6">
                    <path strokeLinecap="round" strokeLinejoin="round" d="M12 3v2.25m6.364.386-1.591 1.591M21 12h-2.25m-.386 6.364-1.591-1.591M12 18.75V21m-4.773-4.227-1.591 1.591M5.25 12H3m4.227-4.773L5.636 5.636M15.75 12a3.75 3.75 0 1 1-7.5 0 3.75 3.75 0 0 1 7.5 0Z" />
                  </svg>

                )}
              </button>
              <button className='setBtn' id='logoutBtn' onClick={() => setLogged(false)}>Logout
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="size-6">
                  <path strokeLinecap="round" strokeLinejoin="round" d="M8.25 9V5.25A2.25 2.25 0 0 1 10.5 3h6a2.25 2.25 0 0 1 2.25 2.25v13.5A2.25 2.25 0 0 1 16.5 21h-6a2.25 2.25 0 0 1-2.25-2.25V15M12 9l3 3m0 0-3 3m3-3H2.25" />
                </svg>
              </button>
              </div>
              <div >
                <h2>Add Task</h2>
                <form onSubmit={addTask}>
                  <input id='addInput' type='text' placeholder='Add a Task' name='task' required/>
                  <button id='addBtn' type='Submit'>Add</button>
                </form>
              </div>
      
              <section>
              <h2>Tasks</h2>
                {tasks.length ? (
                  <table id='taskTable' border={1}>
                    <thead>
                      <tr>
                        <th>Id</th>
                        <th>Task Name</th>
                        <th>Edit Task</th>
                        <th>Configure Task</th>
                        <th>Delete Task</th>
                        <td>Completed</td>
                      </tr>
                    </thead>
                    <tbody>
                      {tasks.map((task) => (
                        <tr key={task.id}>
                          <td>{task.id}</td>
                          <td>{task.name}</td>
                          <td>
                            {editingId === task.id ? (
                              <input type='text' value={editingValue} onChange={(e) => setEditingValue(e.target.value)}/>
                            ) : (
                              task.name
                            )}
                          </td>
                          <td>
                            {editingId === task.id ? (
                              <button onClick={() => endEditing(task.id)}>Save</button>
                            ) : (
                              <button onClick={() => beginEditing(task.id, task.name)}>Edit</button>
                            )}
                          </td>
                          <td>
                            <button onClick={() => deleteTask(task.id)}>Delete</button>
                          </td>
                          <td>
                            <input type='checkbox'/>
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                ) : (
                  <p>No Tasks</p>
                )}
      
              </section>
              
              <section>
                <h2>Data</h2>
                {data.map((item, index) => (
                  <div className='dataSection' key={index}>
                    <h4 className='dataSectionHeader'>Number: {item.id}</h4>
                    <p className='dataP'>{item.title}</p>
                  </div>
                ))}
              </section>
            
            </main>
      ) : (
        <div>
          <button id='themeBtn' onClick={toggleTheme}>Switch theme {isDark ? (
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="size-6">
            <path strokeLinecap="round" strokeLinejoin="round" d="M21.752 15.002A9.72 9.72 0 0 1 18 15.75c-5.385 0-9.75-4.365-9.75-9.75 0-1.33.266-2.597.748-3.752A9.753 9.753 0 0 0 3 11.25C3 16.635 7.365 21 12.75 21a9.753 9.753 0 0 0 9.002-5.998Z" />
          </svg>
          
          
            ) : (
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="size-6">
                <path strokeLinecap="round" strokeLinejoin="round" d="M12 3v2.25m6.364.386-1.591 1.591M21 12h-2.25m-.386 6.364-1.591-1.591M12 18.75V21m-4.773-4.227-1.591 1.591M5.25 12H3m4.227-4.773L5.636 5.636M15.75 12a3.75 3.75 0 1 1-7.5 0 3.75 3.75 0 0 1 7.5 0Z" />
              </svg>

            )}
          </button>
          <h2 id='loginHeader'>Login</h2>
          <form id='loginForm' onSubmit={handleLogin}>
            <input id='loginInput' type='text' placeholder='Password' name='password' required/>
            <button id='loginBtn' type='Submit'>Login</button>
          </form>
          <p>Password: user123</p>
        </div>
        

      )}
      
    </div>
  )
}

export default App
