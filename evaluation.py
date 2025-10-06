import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, f1_score, roc_auc_score
from philentropy import js_divergence

def jsd(p, q):
    p, q = np.array(p), np.array(q)
    return js_divergence(np.vstack([p, q]))

def evaluate_tstr_trtr(real, synth, target):
    Xr, yr = real.drop(target, axis=1), real[target]
    Xs, ys = synth.drop(target, axis=1), synth[target]

    X_train, X_test, y_train, y_test = train_test_split(Xr, yr, test_size=0.3)
    clf = RandomForestClassifier(n_estimators=200, random_state=42)
    clf.fit(X_train, y_train)

    tstr_pred = clf.predict(Xs)
    return {
        "Accuracy": accuracy_score(ys, tstr_pred),
        "F1": f1_score(ys, tstr_pred, average="weighted"),
        "AUC": roc_auc_score(ys, clf.predict_proba(Xs)[:,1])
    }
