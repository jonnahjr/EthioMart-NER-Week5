
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
=======
# EthioMart - Named Entity Recognition for Amharic E-commerce Data

## Overview

EthioMart, a growing hub for Telegram-based e-commerce in Ethiopia, aims to consolidate multiple independent e-commerce channels into a single centralized platform. With the increasing use of Telegram for business transactions, customers and vendors are currently spread across various channels, leading to challenges in product discovery, communication, and order management. 

This project focuses on building an **Amharic Named Entity Recognition (NER) system** to extract important business entities—such as product names, prices, and locations—from the messages shared in these Telegram channels. The extracted data will be used to populate EthioMart's centralized database, providing a seamless and organized shopping experience for customers and a unified platform for vendors.

## Key Objectives

1. **Real-time Data Extraction**: Fetch data from various Ethiopian Telegram e-commerce channels.
2. **Fine-tuning Large Language Models (LLMs)**: Adapt existing LLMs to accurately extract business entities like product names, prices, and locations from Amharic text.

## Project Structure

The project is organized as follows:

```bash
├── .github/                       
│   ├── workflows/                    
│       ├── ci-cd.yml
├── data/                       
│   ├── modern_Data.csv                    
│   ├── labeled_data.txt             
├── notebooks/                  # Jupyter notebooks for analysis, experiments, and exploration
│   ├── KAIM-Week-5-task-2.ipynb
├── scripts/                       
│   ├── main.py
│   ├── preprocess.py
│   ├── scraper.py
├── src/                        # Source code for different project modules
│   ├── data_loading.py       
│   ├── data_preprocessing.py
│   ├── data_labelling.py
├── tests/                      # Unit tests for code modules
│   └── test_data_loading.py
├── requirements.txt            # Python dependencies for the project
├── README.md                   # Project overview and detailed documentation
└── .gitignore                  # Files and directories to ignore in Git version control
```

## Tasks Breakdown

### Task 1: Data Ingestion and Data Preprocessing
This task involves building a system that collects messages from multiple Ethiopian Telegram e-commerce channels, processes them, and prepares the data for entity extraction.

#### Steps:
1. **Identify and Connect to Relevant Telegram Channels**:
   - Develop a custom scraper to fetch real-time data from selected Telegram e-commerce channels.
   - List of relevant channels will be identified for data collection.

2. **Ingest Messages**:
   - Collect text messages, images, and documents from these channels.
   - Ensure real-time collection of data as they are posted.

3. **Preprocess Text Data**:
   - Tokenize and normalize Amharic text.
   - Handle Amharic-specific linguistic features such as script and morphology.
   - Structure the data into a unified format, including metadata (sender, timestamp) and message content.

4. **Data Storage**:
   - Store preprocessed data in a structured database for further analysis and model training.

### Task 2: Label a Subset of the Dataset in CoNLL Format

For fine-tuning the Named Entity Recognition (NER) model, a subset of the dataset will be manually labeled in the CoNLL format. The goal is to identify entities such as **Product**, **Price**, and **Location** from the Amharic text messages.

#### Steps:
1. **Label Entities**:
   - Each word (token) in a message is labeled with the appropriate entity tag: 
     - `B-Product`: Beginning of a product entity (e.g., "Baby bottle").
     - `I-Product`: Inside a product entity (e.g., "bottle" in "Baby bottle").
     - `B-LOC`: Beginning of a location entity (e.g., "Addis Abeba").
     - `I-LOC`: Inside a location entity (e.g., "Abeba" in "Addis Abeba").
     - `B-PRICE`: Beginning of a price entity (e.g., "ዋጋ 1000 ብር").
     - `I-PRICE`: Inside a price entity (e.g., "1000" in "ዋጋ 1000 ብር").
     - `O`: Outside of any entity.
     
2. **Format Data in CoNLL Format**:
   - Each token is labeled on its own line, followed by its entity tag.
   - Blank lines separate individual messages.
   - The labeled dataset will be saved in plain text files, ensuring compatibility with machine learning frameworks.

3. **Label 30-50 Messages**:
   - A minimum of 30-50 messages will be manually labeled in CoNLL format to create a labeled dataset for training the NER model.

#### CoNLL Format Example:

```bash
እንኳን O
ወደ O
ኢትዮ O
ማርት B-Product
እንኳን O
በደኅና O
ትደርሳለህ O
ዋጋ B-PRICE
1000 I-PRICE
ብር I-PRICE
አዲስ B-LOC
አበባ I-LOC
```

## Technical Stack

- **Telegram API**: For fetching real-time data from e-commerce channels.
- **Python**: For data scraping, preprocessing, and model development.
- **CoNLL format**: Standard format for Named Entity Recognition datasets.
- **LLMs**: Large Language Models to be fine-tuned for Amharic NER tasks.
- **Database**: For storing preprocessed and labeled data.

## Future Work

- **LLM Fine-Tuning**: After collecting and labeling the data, the next step will involve fine-tuning large language models for Named Entity Recognition.
- **Model Evaluation and Testing**: Testing the accuracy of the model in extracting entities from Amharic text.
- **Integration**: Incorporating the model into EthioMart’s real-time system for data extraction and database population.

