from transformers import AutoTokenizer

# Tokenize and align labels
def tokenize_and_align_labels(examples, tokenizer, label_to_id, label_all_tokens=True):
    tokenized_inputs = tokenizer(examples['tokens'], truncation=True, is_split_into_words=True)
    
    labels = []
    for i, label in enumerate(examples['ner_tags']):
        label = ['O' if l in ['0', 'o'] else l for l in label]
        label = [label_to_id[l] for l in label]
        
        word_ids = tokenized_inputs.word_ids(batch_index=i)
        previous_word_idx = None
        label_ids = []
        for word_idx in word_ids:
            if word_idx is None:
                label_ids.append(-100)
            elif word_idx != previous_word_idx:
                label_ids.append(label[word_idx])
            else:
                label_ids.append(-100 if not label_all_tokens else label[word_idx])
            previous_word_idx = word_idx
        labels.append(label_ids)
    
    tokenized_inputs["labels"] = labels
    return tokenized_inputs

# Map incorrect labels to correct labels
def map_labels(dataset, label_mapping):
    dataset['ner_tags'] = dataset['ner_tags'].apply(
        lambda tags: [label_mapping.get(tag, tag) for tag in tags]
    )
    return dataset
