from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# FAISS index
index = faiss.IndexFlatL2(384)

# Storage
id_to_text = {}
current_id = 0


# 🔹 Better chunking
def chunk_text(text, size=150):
    words = text.split()
    return [" ".join(words[i:i+size]) for i in range(0, len(words), size)]


# 🔹 Add document
def add_document(text):
    global current_id

    if not text.strip():
        return

    chunks = chunk_text(text)

    if not chunks:
        return

    embeddings = model.encode(chunks)

    index.add(np.array(embeddings))

    for chunk in chunks:
        clean_chunk = " ".join(chunk.split())  # remove extra spaces
        id_to_text[current_id] = clean_chunk
        current_id += 1


# 🔹 Search function (IMPORTANT FIX)
def search(query):
    global current_id

    # No documents case
    if current_id == 0:
        return ["No documents uploaded"]

    query_vector = model.encode([query])
    distances, indices = index.search(np.array(query_vector), k=3)

    results = []

    for i in indices[0]:
        if i in id_to_text:
            text = id_to_text[i]

            # Clean text again
            text = " ".join(text.split())

            # Filter garbage
            if len(text) > 40:
                results.append(text)

    if not results:
        return ["No relevant information found"]

    return results