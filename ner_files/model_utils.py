from transformers import AutoModelForTokenClassification, TrainingArguments, Trainer
from transformers import DataCollatorForTokenClassification

def train_and_evaluate_model(model_name, train_dataset, val_dataset, label_list, compute_metrics_fn, batch_size=16, epochs=15):
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForTokenClassification.from_pretrained(model_name, num_labels=len(label_list))

    training_dataset = train_dataset.map(lambda x: tokenize_and_align_labels(x, tokenizer, label_list), batched=True)
    evaluation_dataset = val_dataset.map(lambda x: tokenize_and_align_labels(x, tokenizer, label_list), batched=True)

    data_collator = DataCollatorForTokenClassification(tokenizer)
     
    training_args = TrainingArguments(
        output_dir=f"./results_{model_name}",
        evaluation_strategy="epoch",
        learning_rate=2e-5,
        per_device_train_batch_size=batch_size,
        per_device_eval_batch_size=batch_size,
        num_train_epochs=epochs,
        weight_decay=0.01,
        logging_dir=f"./logs_{model_name}",
        logging_steps=50
    )

    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=training_dataset,
        eval_dataset=evaluation_dataset,
        tokenizer=tokenizer,
        data_collator=data_collator,
        compute_metrics=compute_metrics_fn
    )

    trainer.train()
    eval_results = trainer.evaluate()
    print(f"Evaluation results for {model_name}:", eval_results)
    return eval_results

# Compare multiple models
def compare_models(models, train_dataset, val_dataset, label_list, compute_metrics_fn):
    results = {}
    for model_name in models:
        eval_result = train_and_evaluate_model(model_name, train_dataset, val_dataset, label_list, compute_metrics_fn)
        results[model_name] = eval_result
    return results
