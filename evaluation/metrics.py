# metrics.py
# Basic evaluation metrics for retrieval and classification.

from sklearn.metrics import accuracy_score, precision_recall_fscore_support
import numpy as np

def classification_metrics(y_true, y_pred):
    """Return accuracy, precision, recall, F1."""
    acc = accuracy_score(y_true, y_pred)
    p, r, f, _ = precision_recall_fscore_support(
        y_true, y_pred, average="weighted", zero_division=0
    )
    return {
        "accuracy": acc,
        "precision": p,
        "recall": r,
        "f1": f,
    }

def retrieval_mrr(true_idxs, ranked_lists):
    """Mean Reciprocal Rank across multiple retrieval queries."""
    rr = []
    for correct_idx, predicted in zip(true_idxs, ranked_lists):
        try:
            position = predicted.index(correct_idx) + 1
            rr.append(1 / position)
        except ValueError:
            rr.append(0.0)
    return float(np.mean(rr)) if rr else 0.0

def recall_at_k(true_idxs, ranked_lists, k=5):
    """Recall@k: proportion of queries where the correct answer is in top-k."""
    hits = sum(1 for t, pred in zip(true_idxs, ranked_lists) if t in pred[:k])
    return hits / len(true_idxs) if true_idxs else 0.0
