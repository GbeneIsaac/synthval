# synthval
synthval — a Python package by Isaac Gbene  A unified framework that evaluates synthetic data quality using Bayesian Network–based sampling and deep generative models with fidelity, predictive, and fairness metrics.
Package Name

synthval

Evaluating Synthetic Data Fidelity, Fairness, and Predictive Utility

🧠 Core Modules
Module	Description
sampling/	Bayesian sampling methods: Forward, Gibbs, Metropolis–Hastings, Gibbs-within-MH
models/	Deep generative models (CTGAN, TVAE) using SDV
metrics/	JSD, MI Difference, Correlation, Predictive Fidelity
evaluation/	TRTR & TSTR predictive frameworks using Random Forest, Logistic Regression, SVM
visualization/	PMF comparison plots, JSD heatmaps, ROC/AUC and fairness visualizations
datasets/	Loaders for UCI Heart Disease and Wisconsin Breast Cancer datasets
reporting/	Automatic evaluation_report.pdf with tables + plots
utils/	Preprocessing, discretization, and helper utilities
🧮 Main Features

✅ Bayesian and deep generative synthetic data creation
✅ Fidelity metrics (JSD, MI, CorrDiff)
✅ Predictive utility tests (TSTR/TRTR)
✅ Visual diagnostics and PDF export
✅ Command-line + Jupyter notebook interfaces
✅ Ready for publication (citable + open source)


synthval/
├── __init__.py
├── sampling/
│   ├── forward.py
│   ├── gibbs.py
│   ├── metropolis.py
│   ├── gibbs_within_mh.py
│   └── __init__.py
├── deepmodels/
│   ├── ctgan.py
│   ├── tvae.py
│   └── __init__.py
├── evaluation/
│   ├── jsd.py
│   ├── mutual_info.py
│   ├── tstr_trtr.py
│   ├── predictive_utils.py
│   └── __init__.py
├── datasets/
│   ├── heart.py
│   ├── breast_cancer.py
│   └── __init__.py
├── visualization/
│   ├── pmf_plot.py
│   ├── roc_plot.py
│   ├── heatmap.py
│   └── __init__.py
├── reporting/
│   ├── academic_report.py
│   ├── __init__.py
│   └── templates/
│       ├── synthval_report_template.tex
│       └── synthval_theme.css
└── utils/
    ├── preprocessing.py
    ├── metrics.py
    └── __init__.py

📘 License

MIT License
(authorship: © 2025 Isaac Gbene, South Dakota State University)

📧 Author Metadata
Author: Isaac Gbene
Email: Isaac.Gbene@jacks.sdstate.edu
Affiliation: Ph.D. student, South Dakota State University
GitHub: https://github.com/GbeneIsaac
License: MIT
