from setuptools import setup, find_packages

setup(
    name="eeg-compare",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "numpy>=1.21.0",
        "scipy>=1.7.0",
        "pandas>=1.3.0",
        "mne>=1.0.0",
        "braindecode>=0.7.0",
        "gradio>=3.9.0",
        "openai>=0.27.0",
        "python-dotenv>=0.19.0",
        "pyyaml>=6.0",
        "matplotlib>=3.5.0",
        "seaborn>=0.11.0",
        "tqdm>=4.62.0",
    ],
    author="Research Team",
    author_email="research@example.com",
    description="Comparative framework for EEG classification methodologies",
    keywords="eeg, classification, interpretability, machine-learning",
    url="https://github.com/la-harris/eeg-compare",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires=">=3.9",
)
