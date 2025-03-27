# EEG-Compare

A comparative framework for analyzing electroencephalogram (EEG) classification methodologies, specifically contrasting PyGol's Meta Inverse Entailment (MIE) with EEG-GPT approaches.

## Overview

EEG-Compare provides researchers and clinicians with tools to evaluate two promising approaches for transparent EEG classification:

1. **PyGol-MIE**: Uses Meta Inverse Entailment for logical rule-based classification with explicit abductive reasoning
2. **EEG-GPT**: Employs large language models with Tree-of-Thought reasoning for natural language explanations

The framework enhances both approaches through an LLM-based interpretability layer that bridges the gap between logical formalism and clinical accessibility.

![EEG-Compare Framework](docs/images/framework-diagram.png)

## Features

- Standardized feature extraction from diverse EEG formats
- PyGol-MIE implementation with transparent logical rule induction
- EEG-GPT integration with few-shot learning capabilities
- LLM interpretability enhancement for clinical relevance
- Interactive Gradio interface for comparative analysis
- Comprehensive evaluation metrics for quantitative assessment

## Installation

```bash
# Clone the repository
git clone https://github.com/la-harris/eeg-compare.git
cd eeg-compare

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install package and dependencies
pip install -e .

# Configure API keys
cp .env.example .env
# Edit .env with your OpenAI API key
```

## Requirements

- Python 3.9+
- SWI-Prolog 9.2.0+ (required for PyGol)
- OpenAI API key (for EEG-GPT and LLM enhancement)
- MNE-Python and BrainDecode for EEG processing

## Quick Start

```bash
# Launch interactive interface
python -m app.app

# Process a single EEG file
python -m scripts.analyze_eeg --input path/to/eeg.edf --output results/analysis.json --pygol --eeggpt --llm

# Batch process a directory of EEG files
python -m scripts.batch_analyze --input_dir datasets/test_set --output_dir results/batch
```

## Dataset Requirements

The framework has been tested with the following datasets:

1. **Temple University Hospital (TUH) Abnormal EEG Corpus**
   - Primary dataset used in the original EEG-GPT paper
   - Available from: [TUH EEG Corpus](https://www.isip.piconepress.com/projects/tuh_eeg/html/downloads.shtml)
   - Requires institutional credentials

2. **Sample Dataset for Quick Testing**
   - Available from: [HuggingFace](https://huggingface.co/datasets/neuroeeg/eeg-sample-dataset)
   - Install with:
     ```bash
     pip install huggingface_hub
     python -c "from huggingface_hub import snapshot_download; snapshot_download('neuroeeg/eeg-sample-dataset', repo_type='dataset', local_dir='datasets/sample')"
     ```

## Documentation

- [Setup Instructions](docs/setup.md)
- [Usage Guide](docs/usage.md)
- [API Documentation](docs/api.md)
- [Configuration Options](docs/configuration.md)
- [Advanced Topics](docs/advanced.md)

## Project Structure

```
eeg-compare/
├── app/                    # Application interface
├── config/                 # Configuration files
├── data/                   # Data storage (not tracked)
├── docs/                   # Documentation
├── examples/               # Example notebooks
├── models/                 # Model storage (not tracked)
├── scripts/                # Utility scripts
├── src/                    # Core source code
│   ├── feature_extraction/ # Feature extraction modules
│   ├── classification/     # Classification modules
│   ├── interpretability/   # Interpretability modules
│   └── utils/              # Utility modules
└── tests/                  # Unit tests
```

## Citation

If you use this framework in your research, please cite:

```
@article{author2024pygoleeg,
  title={PyGol-EEG vs EEG-GPT: A Comparative Framework for Transparent EEG Classification},
  author={Author, A. and Researcher, B.},
  journal={Journal of Neural Engineering},
  year={2024},
  volume={},
  number={},
  pages={}
}
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- The PyGol framework by Dany Varghese et al.
- The EEG-GPT paper by Jonathan W. Kim et al.
- The Temple University Hospital EEG Corpus
