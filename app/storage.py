import json
from datetime import datetime

RESULTS_FILE = "data/results.json"

def save_result(question, user_answer, result):
    record = {
        "question": question,
        "user_answer": user_answer,
        "score": result["score"],
        "concept_coverage": result["concept_coverage"],
        "matched_keywords": result["matched_keywords"],
        "missing_keywords": result["missing_keywords"],
        "feedback": result["feedback"],
        "timestamp": datetime.now().isoformat()
    }

    try:
        with open(RESULTS_FILE, "r") as f:
            data = json.load(f)
    except:
        data = []

    data.append(record)

    with open(RESULTS_FILE, "w") as f:
        json.dump(data, f, indent=2)