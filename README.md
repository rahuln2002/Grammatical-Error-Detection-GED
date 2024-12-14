# Grammatical Error Detection (GED)

Grammatical Error Detection (GED) is a crucial task in Natural Language Processing (NLP) that focuses on identifying grammatical mistakes in text. GED is especially beneficial for Grammatical Error Correction (GEC) systems and helps second-language learners improve their writing skills. This repository contains the code, datasets, and models developed for GED experiments.

## Features
- Fine-tuned Transformer-based models (BERT, RoBERTa) for GED.
- Preprocessed and cleaned datasets for better performance.
- Experiments with various configurations and dataset sizes.

## Files in this Repository
### Code
- `lang8_cleaning.py`: Contains functions for cleaning and preprocessing the Lang-8 dataset, which are used in the `lang8.ipynb` notebook.

### Notebooks
- `lang8.ipynb`: Notebook for cleaning and analyzing the Lang-8 dataset using functions from `lang8_cleaning.py`.
- `GED.ipynb`: Handles loading the cleaned dataset, transforming it into the required format, and fine-tuning Transformer-based models (e.g., BERT, RoBERTa) in various configurations. Also saves the fine-tuned models.
- `inference.ipynb`: Used for inference/testing on LLaMA-3-70B-Instruct, GPT-4, and the fine-tuned BERT and RoBERTa models from `GED.ipynb`.

### Datasets
- Preprocessed versions of the Lang-8 dataset used for training and evaluation.
  - Dataset link: [Lang-8 Preprocessed Dataset](https://huggingface.co/datasets/rahuln2002/GED-lang8-cleaned)
- Blog by my mentor, Kushal Shah: [Cleaned Lang-8 Dataset for Grammar Error Detection](https://bekushal.medium.com/cleaned-lang8-dataset-for-grammar-error-detection-79aaa31150aa)
    - The blog provides detailed insights into the dataset preparation process, challenges faced, and its impact on GED performance.

### Models
- Fine-tuned Transformer-based models hosted on Hugging Face:
  - BERT (base): [Model on Hugging Face](https://huggingface.co/rahuln2002/bert-base-uncased-20k-GED)
  - BERT (base): [Model on Hugging Face](https://huggingface.co/rahuln2002/bert-base-uncased-180k-GED)
  - BERT (large): [Model on Hugging Face](https://huggingface.co/rahuln2002/bert-large-uncased-20k-GED)
  - RoBERTa (base): [Model on Hugging Face](https://huggingface.co/rahuln2002/roberta-base-20k-GED)
  - RoBERTa (large): [Model on Hugging Face](https://huggingface.co/rahuln2002/roberta-large-20k-GED)

### Acknowledgments
I would like to express my heartfelt gratitude to my mentor, **[Kushal Shah](https://www.linkedin.com/in/kushal-shah-95b9a3b/)**, under whom I had the privilege to intern. His invaluable guidance, encouragement, and expertise throughout this project played a significant role in its successful completion. I am deeply thankful for the opportunities and learning experiences he provided.

## How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/rahuln2002/Grammatical-Error-Detection-GED.git
