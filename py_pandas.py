import pandas as pd
import os

# 1. Load the real Kaggle Iris dataset
file_path = "dataset.csv"

if os.path.exists(file_path):
    df = pd.read_csv(file_path)
    
    print("--- Original Dataset ---")
    print(f"Shape: {df.shape}")
    print(df.head())
    
    # 2. Check for missing values
    print("\n--- Missing Values ---")
    print(df.isnull().sum())
    
    # 3. Clean the data (Drop the 'Id' column since it's not useful for ML, and fill any blanks)
    if 'Id' in df.columns:
        df = df.drop(columns=['Id'])
        
    df = df.fillna(0) # Just in case there are any empty cells
    
    # 4. Save the cleaned data
    df.to_csv("cleaned_iris.csv", index=False)
    print("\nSuccess: Data cleaned and saved as 'cleaned_iris.csv'")
else:
    print(f"Error: Could not find {file_path}. Please make sure the file is in this folder.")