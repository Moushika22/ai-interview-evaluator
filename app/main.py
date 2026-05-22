from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from collections import defaultdict

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Answer(BaseModel):
    question: str
    answer: str
    topic: str


# MEMORY
history = []

# =====================
# EVALUATION LOGIC
# =====================
def evaluate_answer(question, answer):
    vectorizer = TfidfVectorizer().fit_transform([question, answer])
    sim = cosine_similarity(vectorizer[0:1], vectorizer[1:2])[0][0]

    score = round(sim * 10, 2)

    # dynamic feedback
    if len(answer.split()) < 5:
        feedback = "Answer too short. Expand with explanation."
    elif score > 7:
        feedback = "Strong answer. Good clarity and structure."
    elif score > 4:
        feedback = "Average answer. Add examples and depth."
    else:
        feedback = "Weak answer. Revise core concepts."

    return score, feedback


# =====================
# EVALUATE API
# =====================
@app.post("/evaluate")
def evaluate(data: Answer):
    score, feedback = evaluate_answer(data.question, data.answer)

    result = {
        "question": data.question,
        "score": score,
        "feedback": feedback,
        "topic": data.topic
    }

    history.append(result)
    return result


# =====================
# INSIGHTS API
# =====================
@app.get("/insights")
def insights():
    if not history:
        return {
            "avg_score": 0,
            "total": 0,
            "topics": {},
            "weak_topics": []
        }

    topic_scores = defaultdict(list)

    for h in history:
        topic_scores[h["topic"]].append(h["score"])

    topic_avg = {
        t: round(sum(scores)/len(scores), 2)
        for t, scores in topic_scores.items()
    }

    weak = sorted(topic_avg, key=topic_avg.get)[:2]

    avg_score = round(sum([h["score"] for h in history]) / len(history), 2)

    return {
        "avg_score": avg_score,
        "total": len(history),
        "topics": topic_avg,
        "weak_topics": weak
    }


# =====================
# PREP API
# =====================
@app.get("/prep")
def prep():
    if not history:
        return {
            "topics": ["Start practicing to get recommendations"],
            "advice": "Attempt questions to generate insights"
        }

    topic_scores = defaultdict(list)

    for h in history:
        topic_scores[h["topic"]].append(h["score"])

    weak = sorted(topic_scores, key=lambda t: sum(topic_scores[t])/len(topic_scores[t]))[:2]

    return {
        "topics": weak,
        "advice": "Focus on low-scoring topics and practice structured answers."
    }