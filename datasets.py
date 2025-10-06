import pandas as pd
from sklearn.datasets import load_breast_cancer

def load_heart_disease():
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data'
    cols = ['age','sex','cp','trestbps','chol','fbs','restecg','thalach','exang','oldpeak','slope','ca','thal','target']
    df = pd.read_csv(url, header=None, names=cols, na_values='?').dropna()
    return df

def load_breast_cancer():
    data = load_breast_cancer()
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['target'] = data.target
    return df
