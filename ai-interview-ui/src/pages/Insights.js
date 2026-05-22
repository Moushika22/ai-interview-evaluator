import { useEffect, useState } from "react";
import axios from "axios";

export default function Insights() {
  const [d, setD] = useState(null);

  useEffect(() => {
    axios.get("http://127.0.0.1:8000/insights")
      .then(res => setD(res.data));
  }, []);

  if (!d) return <p>Loading...</p>;

  return (
    <div>
      <h2>Insights</h2>

      <div className="grid">
        <div className="card">
          <h3>Average Score</h3>
          <p>{d.avg_score}</p>
        </div>

        <div className="card">
          <h3>Total Attempts</h3>
          <p>{d.total}</p>
        </div>
      </div>

      <div className="card">
        <h3>Topic Performance</h3>
        {Object.entries(d.topics).map(([t, s]) => (
          <p key={t}>{t}: {s}</p>
        ))}
      </div>

      <div className="card">
        <h3>Weak Topics</h3>
        {d.weak_topics.map((w, i) => <p key={i}>{w}</p>)}
      </div>
    </div>
  );
}