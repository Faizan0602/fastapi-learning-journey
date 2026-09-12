
import { useState, useEffect } from "react";

function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/")
      .then((response) => response.json())
      .then((result) => {
        setData(result);
      })
      .catch((error) => {
        console.log("Error:", error);
      });
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1>FastAPI + React</h1>

      {data ? (
        <p>Backend Message: {data.message}</p>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
}

export default App;

