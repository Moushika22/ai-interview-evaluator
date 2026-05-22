import { Link } from "react-router-dom";

function Sidebar() {
  return (
    <div className="w-64 h-screen bg-white/70 backdrop-blur-xl border-r border-gray-200 p-6">

      <h1 className="text-3xl font-extrabold mb-10 text-blue-700">
        AI Interview
      </h1>

      <nav className="flex flex-col gap-5 text-lg">
        <Link to="/" className="hover:text-blue-500">Home</Link>
        <Link to="/dashboard" className="hover:text-blue-500">Dashboard</Link>
        <Link to="/evaluate" className="hover:text-blue-500">Evaluate</Link>
        <Link to="/insights" className="hover:text-blue-500">Insights</Link>
        <Link to="/prep" className="hover:text-blue-500">Interview Prep</Link>
      </nav>

    </div>
  );
}

export default Sidebar;