# EthioMart Named Entity Recognition (NER)

## Overview

EthioMart aims to create a centralized platform for e-commerce activities in Ethiopia by consolidating data from multiple Telegram channels. This project focuses on fine-tuning a Named Entity Recognition (NER) system for Amharic text, allowing for the extraction of key business entities such as product names, prices, and locations from messages, images, and documents shared across these channels.

## Objective

The primary objectives of this project are to:

- Extract real-time data from Telegram channels related to e-commerce.
- Fine-tune large language models (LLMs) for Amharic NER to accurately identify entities such as product names, prices, and locations.
- Provide a comprehensive dataset for EthioMart's centralized database, enhancing the e-commerce experience for users.

## Methodology

The project follows a structured approach:

1. **Data Ingestion**: Set up a system to fetch messages from various Ethiopian-based Telegram e-commerce channels.
2. **Data Preprocessing**: Normalize and tokenize the Amharic text, handling specific linguistic features.
3. **Labeling**: Label a subset of the dataset in CoNLL format, identifying product names, prices, and locations.
4. **Model Fine-tuning**: Fine-tune pre-trained models (e.g., XLM-Roberta) for NER tasks using the labeled dataset.
5. **Model Comparison**: Evaluate multiple models based on performance metrics such as accuracy, precision, and recall.
6. **Interpretability**: Implement SHAP and LIME to explain the model's predictions and enhance transparency.

## Technology Used

- **Programming Languages**: Python
- **Libraries**: 
  - Transformers (Hugging Face)
  - Pandas
  - NumPy
  - Matplotlib
  - Scikit-learn
  - SHAP
  - LIME
- **Platforms**: Google Colab (for training and evaluation)

## Collaboration

Feel free to contribute to this project! If you would like to collaborate, please fork the repository and submit a pull request. For any issues or suggestions, create an issue in the GitHub repository.

## License

This project is licensed under the Apache License 2.0. See the LICENSE file for more details.
