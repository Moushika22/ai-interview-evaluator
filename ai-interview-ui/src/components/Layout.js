import React from "react";
import { Link } from "react-router-dom";

export default function Layout({ children }) {
  return (
    <div style={{ display: "flex", minHeight: "100vh", background: "#f5f7fb" }}>
      
      {/* SIDEBAR */}
      <div style={{
        width: "220px",
        background: "#0f172a",
        color: "white",
        padding: "20px"
      }}>
        <h2 style={{ marginBottom: "30px" }}>AI Interview</h2>

        <nav style={{ display: "flex", flexDirection: "column", gap: "15px" }}>
          <Link to="/" style={{ color: "white" }}>Dashboard</Link>
          <Link to="/evaluate" style={{ color: "white" }}>Evaluate</Link>
          <Link to="/insights" style={{ color: "white" }}>Insights</Link>
          <Link to="/prep" style={{ color: "white" }}>Interview Prep</Link>
        </nav>
      </div>

      {/* MAIN CONTENT */}
      <div style={{ flex: 1, padding: "30px" }}>
        
        {/* HEADER */}
        <div style={{
          background: "linear-gradient(135deg, #a5b4fc, #fbcfe8)",
          padding: "30px",
          borderRadius: "16px",
          marginBottom: "30px"
        }}>
          <h1 style={{ margin: 0 }}>AI Interview Intelligence</h1>
          <p>Prepare smarter. Perform better.</p>
        </div>

        {/* PAGE CONTENT */}
        {children}
      </div>
    </div>
  );
}