  
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
│   ├── Bert-Model.ipynb
│   ├── Distilbert-Model.ipynb
│   ├── XLM-Roberta-Model.ipynb
├── ner_files/                       
│   ├── data_utils.py
│   ├── preprocess.py
│   ├── metrics.py
│   ├── model_utils.py
│   ├── main.py
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
## Task 3, 4, 5: Named Entity Recognition (NER) using Transformer Models

This project aims to train and evaluate transformer-based models for Named Entity Recognition (NER) using the Hugging Face library. The task involves token classification for product-related entities such as `Product`, `Price`, and `Location`.

## Features

### 1. Data Loading and Preprocessing
The dataset follows the CoNLL format with tokens and their corresponding labels. We load the dataset using `pandas` and perform initial preprocessing such as:
- Removing empty lines and handling malformed entries.
- Mapping incorrect labels (e.g., `B-PROD`, `I-Price`) to standard labels (`B-Product`, `I-PRICE`).

Example usage:
```python
file_path = "/path/to/labeled_ner_data.txt"
conll_df = load_conll_dataset(file_path)
train_dataset, val_dataset = split_conll_dataset(conll_df)
```

### 2. Label Mapping and Tokenization
The NER tags are mapped into corresponding IDs:
```python
label_to_id = {
    "O": 0, 
    "B-Product": 1, 
    "I-Product": 2, 
    "B-PRICE": 3, 
    "I-PRICE": 4, 
    "B-LOC": 5, 
    "I-LOC": 6
}
```

Tokens are then aligned with their respective NER tags using the tokenizer for token classification models.

```python
training_dataset = train_dataset.map(lambda x: tokenize_and_align_labels(x, tokenizer), batched=True)
```

### 3. Model Training
We fine-tune the following models using Hugging Face's `Trainer` API:
- `xlm-roberta-base`
- `bert-base-multilingual-cased`
- `distilbert-base-multilingual-cased`

```python
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=training_dataset,
    eval_dataset=evaluation_dataset,
    tokenizer=tokenizer,
    data_collator=data_collator,
    compute_metrics=compute_metrics
)
trainer.train()
```

### 4. Evaluation and Metrics
The models are evaluated using `seqeval` metrics to compute accuracy and generate a detailed classification report.

```python
accuracy = accuracy_score(true_labels, true_preds)
report = classification_report(true_labels, true_preds)
```

### 5. Model Comparison
The project includes a function to compare multiple models on the same dataset.

```python
models = ["xlm-roberta-base", "bert-base-multilingual-cased", "distilbert-base-multilingual-cased"]
results = compare_models(models, dataset, label_list)
```

### 6. Label Distribution
The script includes functionality to count the occurrences of each label in the training and validation datasets.

```python
label_counts = count_labels(train_dataset)
```

### 7. Save Dataset
Preprocessed datasets can be saved for future use:
```python
save_dataset(conll_df, "preprocessed_conll_data.txt")
```

## Technical Stack

- **Telegram API**: For fetching real-time data from e-commerce channels.
- **Python**: For data scraping, preprocessing, and model development.
- **CoNLL format**: Standard format for Named Entity Recognition datasets.
- **LLMs**: Large Language Models to be fine-tuned for Amharic NER tasks.
- **Database**: For storing preprocessed and labeled data.

