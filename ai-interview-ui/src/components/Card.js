function Card({ title, children }) {
  return (
    <div className="backdrop-blur-lg bg-white/60 border border-white/30 shadow-xl rounded-2xl p-6 w-72 hover:scale-105 transition duration-300">
      <h3 className="text-lg font-semibold mb-3 text-blue-900">{title}</h3>
      <div className="text-gray-700">{children}</div>
    </div>
  );
}

export default Card;