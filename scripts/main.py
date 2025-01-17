import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from src.data_loading import load_dataset
from src.data_labelling import tokenize_message, annotate_message, save_to_conll

def main(output_file, column_name, label_output_file, start_row, num_rows):
    # Load the dataset
    df = load_dataset(output_file) 

    # Annotate a subset of the cleaned data
    labeled_data = []
    df_subset = df.iloc[start_row : start_row + num_rows]

    for index, row in df_subset.iterrows():
        message = row['Message']

        # Tokenize the message (handle non-string cases)
        tokens = tokenize_message(message)

        if tokens:  # Skip messages that couldn't be tokenized (empty or non-string)
            print(f"\nMessage {index + 1}: {message}")

            # Annotate tokens
            labeled_tokens = annotate_message(tokens)

            # Append labeled tokens
            labeled_data.append(labeled_tokens)
            
    # Save the annotated data in CoNLL format
    save_to_conll(labeled_data, output_file)
    print(f"\nAnnotated data saved to {output_file}")

if __name__ == "__main__":
    output_file = "../data/cleaned_dataset.csv"
    label_output_file = "../data/labeled_data_CoNLL.txt"
    column_name = 'Message'
    
    # Specify the starting row and number of rows to process
    start_row = int(input("Enter the starting row: "))
    num_rows = int(input("Enter the number of rows to label: "))

    main(output_file, column_name, label_output_file, start_row, num_rows)
