import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import Dashboard from "./pages/Dashboard";
import Evaluate from "./pages/Evaluate";
import Insights from "./pages/Insights";
import Focus from "./pages/Focus";

function App() {
  return (
    <Router>
      <div className="app">
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/evaluate" element={<Evaluate />} />
          <Route path="/insights" element={<Insights />} />
          <Route path="/focus" element={<Focus />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;