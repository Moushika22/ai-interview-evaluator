TOPIC_MAP = {
    "object": "Object-Oriented Programming",
    "class": "Classes & Objects",
    "inheritance": "Inheritance",
    "polymorphism": "Polymorphism",
    "abstraction": "Abstraction",
    "encapsulation": "Encapsulation",
    "database": "DBMS",
    "sql": "SQL & Queries"
}

def map_keywords_to_topics(keywords):
    topics = set()
    for word in keywords:
        for key in TOPIC_MAP:
            if key in word:
                topics.add(TOPIC_MAP[key])
    return list(topics)