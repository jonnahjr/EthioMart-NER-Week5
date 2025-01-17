from seqeval.metrics import accuracy_score, classification_report

# Convert predictions and labels to the string format and compute metrics
def compute_metrics(pred, id_to_label):
    labels = pred.label_ids
    preds = pred.predictions.argmax(-1)
    
    true_labels = [[id_to_label[l] for l in label_row if l != -100] for label_row in labels]
    true_preds = [[id_to_label[p] for (p, l) in zip(pred_row, label_row) if l != -100] for pred_row, label_row in zip(preds, labels)]
    
    report = classification_report(true_labels, true_preds)
    accuracy = accuracy_score(true_labels, true_preds)
    
    return {"accuracy": accuracy, "report": report}
