import re

STOPWORDS = {"for", "the", "and", "is", "a", "an", "of", "to"}

def tokenize(text):
    tokens = re.findall(r"[a-zA-Z0-9]+", text.lower())
    return [t for t in tokens if t not in STOPWORDS]

def build_inverted_index(documents):
    index = {}
    for doc_id, text in documents.items():
        for token in tokenize(text):
            index.setdefault(token, set()).add(doc_id)
    return index

def search(index, query):
    tokens = tokenize(query)
    if not tokens:
        return set()
    result = index.get(tokens[0], set()).copy()
    for token in tokens[1:]:
        result &= index.get(token, set())
    return result

def demo_search():
    documents = {
        1: "Red cotton shirt for men",
        2: "Blue denim jeans for women",
        3: "Comfortable cotton jeans for kids",
    }

    index = build_inverted_index(documents)

    print("Inverted Index:")
    for token, doc_ids in sorted(index.items()):
        print(f"{token}: {sorted(doc_ids)}")

    print("\nSearch Results:")
    queries = ["cotton jeans", "shirt", "kids cotton", "for"]
    for q in queries:
        print(f"{q} -> {sorted(search(index, q))}")

# Execution
demo_search()
