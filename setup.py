from setuptools import setup, find_packages

setup(
    name="synthval",
    version="0.1.0",
    author="Isaac Gbene",
    author_email="Isaac.Gbene@jacks.sdstate.edu",
    description="A hybrid Python package for synthetic data generation and validation using Bayesian, deep learning, and fairness-aware frameworks.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/GbeneIsaac/synthval",
    packages=find_packages(),
    install_requires=open("requirements.txt").read().splitlines(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Information Analysis"
    ],
    python_requires=">=3.8",
)
