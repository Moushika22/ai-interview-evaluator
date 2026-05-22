import { useEffect, useState } from "react";
import axios from "axios";

export default function Focus() {
  const [d, setD] = useState(null);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/prep")
      .then(r => setD(r.data));
  }, []);

  if (!d) return <p>Loading...</p>;

  return (
    <div>
      <h2>Focus Areas</h2>

      <div className="grid">
        {d.topics.map((t, i) => (
          <div className="card" key={i}>
            <h3>{t}</h3>
          </div>
        ))}
      </div>

      <div className="card" style={{ marginTop: "20px" }}>
        <h3>Advice</h3>
        <p>{d.advice}</p>
      </div>
    </div>
  );
}