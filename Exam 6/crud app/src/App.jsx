import { useState, useEffect } from "react";
import "./App.css";

function App() {
  const [entries, setEntries] = useState([]);
  const [editTarget, setEditTarget] = useState(null);
  const [tempText, setTempText] = useState("");
  const [loggedIn, setLoggedIn] = useState(false);
  const [passcode, setPasscode] = useState("");
  const [isNightMode, setIsNightMode] = useState(true);
  const [apiContent, setApiContent] = useState([]);

  const toggleTheme = () => {
    const root = document.getElementById("root");
    setIsNightMode((prevMode) => !prevMode);
    root.style.backgroundColor = isNightMode ? "#FFFFFF" : "#303030";
  };

  const handleLogin = (e) => {
    e.preventDefault();
    setPasscode(e.target.password.value);
    if (e.target.password.value === "user123") {
      setLoggedIn(true);
    }
  };

  const addEntry = (e) => {
    e.preventDefault();
    const value = e.target.task?.value.trim();
    if (value) {
      setEntries([...entries, { id: Date.now(), name: value }]);
      e.target.reset();
    }
  };

  const startRenaming = (id, currentText) => {
    setEditTarget(id);
    setTempText(currentText);
  };

  const applyRename = () => {
    setEntries((old) =>
      old.map((entry) =>
        entry.id === editTarget ? { ...entry, name: tempText } : entry
      )
    );
    setEditTarget(null);
    setTempText("");
  };

  const deleteEntry = (id) => {
    setEntries(entries.filter((entry) => entry.id !== id));
  };

  useEffect(() => {
    const storedData = localStorage.getItem("tasks");
    if (storedData) setEntries(JSON.parse(storedData));
  }, []);

  useEffect(() => {
    if (entries.length > 0) {
      localStorage.setItem("tasks", JSON.stringify(entries));
    }
  }, [entries]);

  useEffect(() => {
    (async () => {
      try {
        const response = await fetch("https://jsonplaceholder.typicode.com/todos");
        const data = await response.json();
        setApiContent(data);
        console.log(data);
      } catch (error) {
        console.warn("Could not fetch data", error);
      }
    })();
  }, []);

  return (
    <div id="wrapper" className={isNightMode ? "light" : "dark"}>
      {loggedIn ? (
        <main>
          <div id="settings">
            <button id="themeBtn" className="setBtn" onClick={toggleTheme}>
              Theme {isNightMode ? "🌑" : "☀️"}
            </button>
            <button
              className="setBtn"
              id="logoutBtn"
              onClick={() => setLoggedIn(false)}
            >
              Logout 🚪
            </button>
          </div>

          <div>
            <h2>Add Entry</h2>
            <form onSubmit={addEntry}>
              <input
                id="addInput"
                name="task"
                type="text"
                placeholder="Add a task"
                required
              />
              <button id="addBtn" type="submit">
                Save
              </button>
            </form>
          </div>

          <section>
            <h2>Entries</h2>
            {entries?.length ? (
              <table id="taskTable" border={1}>
                <thead>
                  <tr>
                    <th>ID</th>
                    <th>Task</th>
                    <th>Rename</th>
                    <th>Controls</th>
                    <th>Remove</th>
                    <td>Done</td>
                  </tr>
                </thead>
                <tbody>
                  {entries.map((entry) => (
                    <tr key={entry.id}>
                      <td>{entry.id}</td>
                      <td>{entry.name}</td>
                      <td>
                        {editTarget === entry.id ? (
                          <input
                            type="text"
                            value={tempText}
                            onChange={(e) => setTempText(e.target.value)}
                          />
                        ) : (
                          entry.name
                        )}
                      </td>
                      <td>
                        {editTarget === entry.id ? (
                          <button onClick={applyRename}>Done</button>
                        ) : (
                          <button onClick={() => startRenaming(entry.id, entry.name)}>
                            Edit
                          </button>
                        )}
                      </td>
                      <td>
                        <button onClick={() => deleteEntry(entry.id)}>X</button>
                      </td>
                      <td>
                        <input type="checkbox" />
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            ) : (
              <p className="opacity-70">Nothing yet</p>
            )}
          </section>

          <section>
            <h2>Fetched Data</h2>
            {apiContent?.length ? (
              apiContent.slice(0, 10).map((item, idx) => (
                <div key={idx} className="dataSection">
                  <h4 className="dataSectionHeader">#{item.id}</h4>
                  <p className="dataP">{item.title}</p>
                </div>
              ))
            ) : (
              <p className="text-sm text-gray-500">Still loading...</p>
            )}
          </section>
        </main>
      ) : (
        <div>
          <button id="themeBtn" onClick={toggleTheme}>
            {isNightMode ? "🌙 Dark" : "☀️ Light"}
          </button>
          <h2 id="loginHeader">Log In</h2>
          <form id="loginForm" onSubmit={handleLogin}>
            <input
              id="loginInput"
              type="text"
              name="password"
              placeholder="Enter password"
              required
            />
            <button id="loginBtn" type="submit">
              Log In
            </button>
          </form>
          <p className="text-sm text-neutral-400">Password is: user123</p>
        </div>
      )}
    </div>
  );
}

export default App;
