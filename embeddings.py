import pandas as pd
import numpy as np
from sentence_transformers  import SentenceTransformer

df = pd.read_csv('books.csv')
df['embedding_text'] = df['title'].astype(str) + " by " + df['authors'].astype(str) 
texts = df['embedding_text'].tolist()

model = SentenceTransformer("Qwen/Qwen3-Embedding-0.6B")
text_emb = model.encode(texts, show_progress_bar=True, batch_size=32).astype("float32")

np.save("book_embeddings.npy", text_emb)
df.to_csv("books_with_embeddings.csv", index=False)