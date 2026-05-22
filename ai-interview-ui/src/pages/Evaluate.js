import { useState } from "react";
import axios from "axios";
import { questions } from "../data/questions";

export default function Evaluate() {
  const [topic, setTopic] = useState(null);
  const [i, setI] = useState(0);
  const [answer, setAnswer] = useState("");
  const [results, setResults] = useState([]);
  const [done, setDone] = useState(false);

  const submit = async () => {
    const res = await axios.post("http://127.0.0.1:8000/evaluate", {
      question: questions[topic][i],
      answer,
      topic
    });

    setResults([...results, res.data]);
    setAnswer("");

    if (i === 2) setDone(true);
    else setI(i + 1);
  };

  const reset = () => {
    setTopic(null);
    setI(0);
    setResults([]);
    setDone(false);
  };

  if (!topic) {
    return (
      <div className="grid">
        {Object.keys(questions).map(t => (
          <div className="card" key={t} onClick={() => setTopic(t)}>
            <h3>{t.toUpperCase()}</h3>
          </div>
        ))}
      </div>
    );
  }

  if (done) {
    const avg = results.reduce((a, b) => a + b.score, 0) / results.length;

    return (
      <div>
        <h2>Test Completed</h2>

        <div className="card">
          <h3>Average Score: {avg.toFixed(2)}</h3>
        </div>

        {results.map((r, idx) => (
          <div className="card" key={idx}>
            <p><b>Score:</b> {r.score}</p>
            <p>{r.feedback}</p>
          </div>
        ))}

        <button className="btn" onClick={reset}>Back to Topics</button>
      </div>
    );
  }

  return (
    <div>
      <h3>{questions[topic][i]}</h3>

      <textarea
        value={answer}
        onChange={(e) => setAnswer(e.target.value)}
      />

      <button className="btn" onClick={submit}>Submit</button>
    </div>
  );
}