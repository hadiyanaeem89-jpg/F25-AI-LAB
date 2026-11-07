import csv, json, time
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from task2_chunks import make_chunks

def evaluate(scores, chunks, items):
    hits, reciprocal = [], []
    for row, q in zip(scores, items):
        if q["doc"] is None:
            continue
        top = np.argsort(-row, kind="stable")[:3]
        good = [rank for rank, i in enumerate(top, 1)
                if chunks[i]["doc"] == q["doc"] and q["evidence"] in chunks[i]["text"]]
        hits.append(bool(good))
        reciprocal.append(1/good[0] if good else 0)
    return (float(np.mean(hits)), float(np.mean(reciprocal))) if hits else (None, None)

def main():
    with open("corpus.json", encoding="utf-8") as f: docs = json.load(f)
    with open("queries.json", encoding="utf-8") as f: items = json.load(f)
    assert len([q for q in items if q["doc"] is not None and q["split"]=="dev"]) == 4
    assert len([q for q in items if q["doc"] is not None and q["split"]=="test"]) == 4
    assert len([q for q in items if q["doc"] is None]) == 2
    for q in items:
        if q["doc"] is not None:
            assert q["evidence"] in docs[q["doc"]]
    methods = ["tfidf", "embedding"]
    try:
        from sentence_transformers import SentenceTransformer
        t = time.perf_counter()
        model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2", device="cpu")
        print("Model load seconds:", round(time.perf_counter()-t, 4))
    except Exception as exc:
        model = None
        print("Embedding backend unavailable:", repr(exc))
        print("TF-IDF runs will continue; install sentence-transformers and download the model for full comparison.")
    logs = []
    query_texts = [q["query"] for q in items]
    for strategy in ["0", "10", "sentence"]:
        chunks = make_chunks(docs, strategy)
        texts = [c["text"] for c in chunks]
        for method in methods:
            if method == "embedding" and model is None:
                continue
            t = time.perf_counter()
            if method == "tfidf":
                vectorizer = TfidfVectorizer()
                C = vectorizer.fit_transform(texts)
                Q = vectorizer.transform(query_texts)
                encode_seconds = time.perf_counter()-t
                t = time.perf_counter()
                scores = (Q @ C.T).toarray()
            else:
                lengths = [len(model.tokenizer(x, truncation=False)["input_ids"]) for x in texts+query_texts]
                if max(lengths) > model.max_seq_length:
                    raise ValueError("Model token limit exceeded; rechunk or shorten query")
                C = model.encode(texts, normalize_embeddings=True)
                Q = model.encode(query_texts, normalize_embeddings=True)
                encode_seconds = time.perf_counter()-t
                t = time.perf_counter()
                scores = Q @ C.T
            search_seconds = time.perf_counter()-t
            print("\\n", strategy, method, "chunks", len(chunks),
                  "encode/index seconds", round(encode_seconds, 6),
                  "search seconds", round(search_seconds, 6))
            for split in ["dev", "test"]:
                idx = [i for i,q in enumerate(items) if q["split"] == split]
                print(split, "Hit@3, MRR@3:", evaluate(scores[idx], chunks, [items[i] for i in idx]))
            for row, q in zip(scores, items):
                top = np.argsort(-row, kind="stable")[:3]
                for rank, i in enumerate(top, 1):
                    c = chunks[i]
                    rec = dict(strategy=strategy, method=method, query=q["query"],
                        split=q["split"], rank=rank, score=float(row[i]),
                        chunk_id=c["id"], doc=c["doc"], start=c["start"], end=c["end"],
                        text=c["text"], answerable=q["doc"] is not None)
                    logs.append(rec)
                    print(f"  {rank}. {c['id']} score={row[i]:.3f} offsets={c['start']}:{c['end']} {c['text'][:180]}")
    if logs:
        with open("retrieval_log.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=list(logs[0]))
            writer.writeheader()
            writer.writerows(logs)
        print("\\nWrote retrieval_log.csv")
if __name__ == "__main__":
    main()