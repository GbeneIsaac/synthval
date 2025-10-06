import numpy as np
import pandas as pd
from pgmpy.sampling import BayesianModelSampling

def forward_sampling(bn_model, n_samples=1000):
    inference = BayesianModelSampling(bn_model)
    return inference.forward_sample(size=n_samples)
