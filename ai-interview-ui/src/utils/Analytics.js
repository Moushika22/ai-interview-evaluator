export function processResults(history) {
  // history = [{score, missing_keywords}]

  const trend = history.map((h, i) => ({
    name: `Q${i + 1}`,
    score: h.score
  }));

  const topicMap = {
    class: "OOP",
    object: "OOP",
    encapsulation: "OOP Concepts",
    inheritance: "OOP Concepts",
    polymorphism: "OOP Concepts",
    python: "Programming Basics"
  };

  let topicCount = {};

  history.forEach(h => {
    h.missing_keywords.forEach(k => {
      const topic = topicMap[k] || "General";
      topicCount[topic] = (topicCount[topic] || 0) + 1;
    });
  });

  const weakTopics = Object.entries(topicCount)
    .map(([topic, count]) => ({ topic, count }))
    .sort((a, b) => b.count - a.count);

  const avgScore =
    history.reduce((sum, h) => sum + h.score, 0) / history.length;

  return {
    trend,
    weakTopics,
    avgScore: avgScore.toFixed(2),
    totalTests: history.length
  };
}