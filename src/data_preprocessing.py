import re
import pandas as pd
 
# Define a function to remove emojis 
def remove_emojis(text): 
    emoji_pattern = re.compile(
        "["  # Define the emoji pattern
        "\U0001F600-\U0001F64F"  # emoticons
        "\U0001F300-\U0001F5FF"  # symbols & pictographs
        "\U0001F680-\U0001F6FF"  # transport & map symbols
        "\U0001F700-\U0001F77F"  # alchemical symbols
        "\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
        "\U0001F800-\U0001F8FF"  # Supplemental Arrows-C 
        "\U0001F900-\U0001F9FF"  # Supplemental Symbols & Pictographs
        "\U0001FA00-\U0001FAFF"  # Symbols & Pictographs Extended
        "]+", flags=re.UNICODE
    )
    return emoji_pattern.sub(r'', text)

# Function to remove blank lines 
def remove_blank_lines(df, column_name): 
    df[column_name] = df[column_name].replace(r'^\s*$', pd.NA, regex=True)  
    return df.dropna(subset=[column_name])
 
# Function to remove unwanted texts
def remove_unwanted_texts(df, column_name, unwanted_texts):
    for index, row in df.iterrows():
        message = row[column_name]
        if isinstance(message, str):
            for unwanted_text in unwanted_texts:
                message = message.replace(unwanted_text, "")
            message = message.replace('"', "") 
            df.at[index, column_name] = message.strip()
    return df

# Save the cleaned dataset to a file
def save_cleaned_dataset(df, output_file):
    df.to_csv(output_file, index=False)
    print(f"Cleaned dataset saved to {output_file}")
