import { useNavigate } from "react-router-dom";

export default function Dashboard() {
  const nav = useNavigate();

  return (
    <div>
      <div className="title">AI Interview Evaluator</div>
      <div className="subtitle">
        Prepare smarter. Improve answers. Track performance. Ace interviews.
      </div>

      <div className="grid">
        <div className="card" onClick={() => nav("/evaluate")}>
          <h3>Technical Preparation</h3>
          <p>Practice interview questions topic-wise.</p>
        </div>

        <div className="card" onClick={() => nav("/insights")}>
          <h3>Insights</h3>
          <p>Analyze your performance and growth.</p>
        </div>

        <div className="card" onClick={() => nav("/focus")}>
          <h3>Focus Areas</h3>
          <p>Understand what concepts need improvement.</p>
        </div>

        <div className="card">
          <h3>Mock Interview (Next)</h3>
          <p>Coming soon: voice & camera evaluation.</p>
        </div>
      </div>
    </div>
  );
}