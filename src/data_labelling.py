def tokenize_message(message):
    """
    Tokenize a message based on spaces.
    Args:
    - message: str, input message.

    Returns:
    - tokens: list of str, tokenized message.
    """
    if isinstance(message, str):
        return message.split()
    else:
        return []

def annotate_message(tokens):
    """
    Annotate each token in the message with labels.
    Args:
    - tokens: list of str, tokenized message.

    Returns:
    - labeled_tokens: list of tuple, each token with its label.
    """
    labeled_tokens = []
    print("\nStart labeling each token:")
    for token in tokens:
        print(f"Token: {token}")
        label = input("Enter label (B-Product, I-Product, B-LOC, I-LOC, B-PRICE, I-PRICE, O): ")
        labeled_tokens.append((token, label))
    return labeled_tokens

def save_to_conll(labeled_data, output_file):
    """
    Save labeled tokens in CoNLL format.
    Args:
    - labeled_data: list of list of tuples, token-label pairs for each message.
    - output_file: str, path to the output file.
    """
    with open(output_file, 'w', encoding='utf-8') as f:
        for message in labeled_data:
            for token, label in message:
                f.write(f"{token} {label}\n")
            f.write("\n")  # Blank line to separate messages

