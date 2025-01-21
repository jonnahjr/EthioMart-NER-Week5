
import pandas as pd
from sklearn.model_selection import train_test_split 

# Load the dataset from a CoNLL format file
def load_conll_dataset(file_path):
    sentences, labels = [], []
    sentence, label = [], []
    
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            if line.strip():
                parts = line.strip().split()
                if len(parts) == 2:
                    token, tag = parts
                    sentence.append(token)
                    label.append(tag)
                else:
                    print(f"Skipping malformed line: {line.strip()}")
            else:
                if sentence:
                    sentences.append(sentence)
                    labels.append(label)
                sentence, label = [], []
    
    if sentence:
        sentences.append(sentence)
        labels.append(label)
    
    return pd.DataFrame({"tokens": sentences, "ner_tags": labels})

# Split the dataset into training and validation sets
def split_conll_dataset(conll_df, train_ratio=0.8):
    train_df, val_df = train_test_split(conll_df, train_size=train_ratio, random_state=42, shuffle=True)
    return train_df, val_df

# Save the dataset to a file
def save_dataset(dataset, file_path):
    dataset.to_csv(file_path, index=False)
    print(f"Dataset saved to {file_path}")
