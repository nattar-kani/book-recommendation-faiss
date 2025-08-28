from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import numpy as np
import faiss
from sentence_transformers  import SentenceTransformer

df = pd.read_csv('books_with_embeddings.csv')

text_emb = np.load("book_embeddings.npy")

faiss.normalize_L2(text_emb)
d = text_emb.shape[1]
index = faiss.IndexFlatIP(d)
index.add(text_emb)

class Query(BaseModel):
    text: str
    topk: int = 3

app = FastAPI()

@app.post("/query")
def query_books(query: Query):
    query_emb = model.encode([query.text]).astype("float32")
    faiss.normalize_L2(query_emb)
    D, I = index.search(query_emb, query.topk)
    results = []
    for idx in I[0]:
        book = df.iloc[idx]
        results.append({
            "Title": book['title'],
            "Author": book['authors'],
            "Rating": book['average_rating']}
        )


    return {"query": query.text, "recommendations": results}