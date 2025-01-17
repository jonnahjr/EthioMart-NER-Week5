import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from src.data_loading import load_dataset
from src.data_preprocessing import remove_emojis, remove_blank_lines, remove_unwanted_texts, save_cleaned_dataset
 
def main(input_file, column_name, unwanted_texts, output_file):
    # Step 1: Load the dataset
    df = load_dataset(input_file)
    
    # Handle Missing Values
    df = df.dropna(subset=['Message'])

    # Step 2: Preprocess the dataset
    df[column_name] = df[column_name].apply(remove_emojis)
    df = remove_blank_lines(df, column_name)
    df = remove_unwanted_texts(df, column_name, unwanted_texts)
    save_cleaned_dataset(df, output_file)
    
if __name__ == '__main__':
    input_file = "../data/modern_Data.csv"
    output_file = "../data/cleaned_dataset1.csv"
    column_name = "Message"
    
    # List of unwanted texts to remove from the messages
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
    
    main(input_file, column_name, unwanted_texts, output_file)
