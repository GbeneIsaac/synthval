# synthval 🔬

**Author:** Isaac Gbene  
**Affiliation:** PhD Student, South Dakota State University  
**Email:** Isaac.Gbene@jacks.sdstate.edu  
**GitHub:** [GbeneIsaac](https://github.com/GbeneIsaac)

## Overview
`synthval` is a hybrid Python framework for generating, evaluating, and validating synthetic data using Bayesian Networks, Deep Learning (CTGAN, TVAE), and fairness-aware evaluation (TSTR/TRTR, JSD, MI).

## Installation
```bash
git clone https://github.com/GbeneIsaac/synthval.git
cd synthval
pip install -e .
```

## Example
```python
from synthval.sampling import gibbs_sampler
from synthval.deepmodels import generate_ctgan
from synthval.evaluation import evaluate_tstr_trtr
from synthval.datasets import load_heart_disease

data = load_heart_disease()
gibbs_data = gibbs_sampler(data, n_samples=500)
ctgan_data = generate_ctgan(data, epochs=200)
results = evaluate_tstr_trtr(data, gibbs_data, target='target')
print(results)
```
