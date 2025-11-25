import re

def tokenize(text):
    return re.findall(r"[a-zA-Z0-9]+", text.lower())

def build_inverted_index(documents):
    index = {}
    for doc_id, text in documents.items():
        for token in tokenize(text):
            index.setdefault(token, set()).add(doc_id)
    return index

def demo_index_builder():
    documents = {
        1: "Red cotton shirt for men",
        2: "Blue denim jeans for women",
        3: "Comfortable cotton jeans for kids",
    }

    print("Documents:")
    for doc_id, text in documents.items():
        print(f"{doc_id}: {text}")

    index = build_inverted_index(documents)

    print("\nInverted Index:")
    for token, doc_ids in sorted(index.items()):
        print(f"{token}: {sorted(doc_ids)}")

demo_index_builder()
