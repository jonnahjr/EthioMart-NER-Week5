# Import necessary libraries
import sys
import os

# Add the parent directory to the system path so we can import the modules from src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

# Import the required functions from the src modules
from src.data_loading import load_dataset
from src.data_preprocessing import remove_emojis, remove_blank_lines, remove_unwanted_texts, save_cleaned_dataset

# Main function to handle the processing of the dataset
def main(input_file, column_name, unwanted_texts, output_file):
    # Step 1: Load the dataset from the provided file path
    df = load_dataset(input_file)
    
    # Handle Missing Values: Drop rows where the 'Message' column has missing values
    df = df.dropna(subset=['Message'])

    # Step 2: Preprocess the dataset

    # Remove emojis from the text in the specified column
    df[column_name] = df[column_name].apply(remove_emojis)
    
    # Remove blank lines from the column
    df = remove_blank_lines(df, column_name)
    
    # Remove any unwanted texts from the specified column based on the list provided
    df = remove_unwanted_texts(df, column_name, unwanted_texts)
    
    # Save the cleaned dataset to the specified output file
    save_cleaned_dataset(df, output_file)
    
# Main script execution block
if __name__ == '__main__':
    # Define the file paths and column name to be used in the main function
    input_file = "../data/modern_Data.csv"  # Path to the input dataset
    output_file = "../data/cleaned_dataset1.csv"  # Path to save the cleaned dataset
    column_name = "Message"  # Column containing the text to be cleaned
    
    # List of unwanted texts that need to be removed from the 'Message' column
    unwanted_texts = [
        "ቴሌግራምt.me/modernshoppingcenter",
        '"በአዲስ ነገረ ሁሌም ቀዳሚዏች ነን"',
        "t.me/modernshopping1",
        "t.me/modernshopping2",
        "በስራችን ላይ ቅሬታ ካለዎት ብቻ በዚህ ስልክ ደዉለዉ ያሳዉቁን።",
        "0956415152",
        "0924743736",
        "0974978584",
        '"በሞደርን እቃወዏች ሂወትዎን ሞደርናይዝ ያድርጉ"',
        'የመረጡትን እቃ ለማዘዝ ከታች ባለዉ የቴሌግራም አድራሻ ይላኩልን',
        'ተጀመረ ተጀመረ ተጀመረ',
        'ልዩ እዉነተኛ የበዓል ቅናሽ',
        'ከነሐሴ 29 እስከ መስከረም 7 ድረስ የሚቆይ እዉነተኛ ቅናሽ አድርገናል።',
        'ለክፍለሀገር ደንበኞቻችን ባሉበት ሐገር በመናሐሪያ እንልካለን።',
    ]
    
    # Call the main function with the specified inputs
    main(input_file, column_name, unwanted_texts, output_file)
