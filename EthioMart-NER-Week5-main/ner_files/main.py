import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from data_utils import load_conll_dataset, split_conll_dataset, save_dataset
from preprocess import map_labels, tokenize_and_align_labels
from metrics import compute_metrics
from model_utils import compare_models

# Load and preprocess dataset
file_path = "../data/labeled_ner_data.txt"
conll_df = load_conll_dataset(file_path)
train_df, val_df = split_conll_dataset(conll_df)

# Mapping and saving
label_mapping = {
    'B-PROD': 'B-Product',
    'B-PRODUCT': 'B-Product',
    'I-PRODUCT': 'I-Product',
    'B-Price': 'B-PRICE',
    'I-Price': 'I-PRICE',
    'IO': 'O'
}
train_df = map_labels(train_df, label_mapping)
val_df = map_labels(val_df, label_mapping)
save_dataset(train_df, "train_dataset.csv")
save_dataset(val_df, "val_dataset.csv")

# Define labels and models
label_list = ['O', 'B-Product', 'I-Product', 'B-PRICE', 'I-PRICE', 'B-LOC', 'I-LOC']
models = ["xlm-roberta-base", "bert-base-multilingual-cased", "distilbert-base-multilingual-cased"]

# Compare models
results = compare_models(models, train_df, val_df, label_list, compute_metrics)
