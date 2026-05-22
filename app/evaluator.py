from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import re

model = SentenceTransformer("all-MiniLM-L6-v2")

def extract_keywords(text):
    words = re.findall(r'\b\w+\b', text.lower())
    return list(set(words))

def evaluate_answer(user_answer, ideal_answer):
    embeddings = model.encode([user_answer, ideal_answer])

    similarity = cosine_similarity(
        [embeddings[0]], [embeddings[1]]
    )[0][0]

    score = float(similarity * 10)

    # softer keyword logic
    user_words = set(extract_keywords(user_answer))
    ideal_words = set(extract_keywords(ideal_answer))

    missing = list(ideal_words - user_words)

    # improved feedback
    if score > 8:
        feedback = "Strong answer with good conceptual understanding."
    elif score > 6:
        feedback = "Decent answer. Try adding more technical depth."
    else:
        feedback = "Answer lacks clarity. Focus on core concepts."

    return {
        "score": round(score, 2),
        "feedback": feedback,
        "missing_keywords": missing[:5]
    }