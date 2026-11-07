import numpy as np
form sklearn.feature_extraction.text import TfidfVectorizer

class retriever:
    def __init__ (self,record,backend = "tfidf"):
        if not records or any (not r["text"].strip() for r in records):
            self.records =[]
            self . backend = backend
            
            
            texts =[r["text"] for r in records]
            
            
            if backend == "tfidf":
                self.vectorizer = TfidfVectorizer()
                self.vectors = self.vectorizer.fit_transform(texts)
                
                
            elif backend == "embedding":
                from sentence_transformers import SentenceTransformer
                self.model = SentenceTransformer("sentence-transformers/all-miniLM-l6-v2", device="cpu")
                self.vectors = self.model.encode(texts, normalize_embeddings=True)
            else: 
                raise ValueError("unknown backend")
            
            def search( self, query, k=3):
                
                if not query.strip():
                    return []
                
                
                if self.backend == "tfidf":
                    query_vector = self.vectorizer.transform([query])
                    scores = np.dot(self.vectors, query_vector.T).toarray().flatten()
                    
                    
                else:
                    query_vector = self.model.encode([query], normalize_embeddings=True)[0]
                    scores = np.dot(self.vectors, query_vector.T).flatten()
                    
                    indexes = np.argsort(scores)[::-1][:k]
                    
                    return [
                        (self.records[i]["text"], scores[i]) for i in indexes
                        if scores[i] > 0
                    ]
                    
                    
                    if __name__ == "__main__":
                        print("lab6 search engine is ready")
                        