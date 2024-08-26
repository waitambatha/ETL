import pandas as pd
import os
from sqlalchemy import create_engine
from config import username, password  # Importing credentials from config.py

# Function to display the menu and get the user's choice
def display_menu():
    print("\nSelect an option:")
    print("1. Display list of CSV files and view a file")
    print("2. Transform Data: Remove columns")
    print("3. Transform Data: Rename columns")
    print("4. Delete columns from a CSV file")
    print("5. Merge CSV files")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ")
    return choice

# Function to list CSV files in the Resources folder
def list_csv_files():
    files = [f for f in os.listdir("./Resources") if f.endswith('.csv')]
    for i, file in enumerate(files, start=1):
        print(f"{i}. {file}")
    return files

# Function to read and display a CSV file
def read_and_display_csv(file_path):
    df = pd.read_csv(file_path)
    print(df.head())
    return df

# Function to remove columns from a DataFrame
def remove_columns(df):
    print(f"Current columns: {df.columns.tolist()}")
    cols_to_remove = input("Enter the columns to remove (comma-separated): ").split(',')
    df.drop(columns=cols_to_remove, inplace=True)
    print("Updated DataFrame:")
    print(df.head())
    return df

# Function to rename columns in a DataFrame
def rename_columns(df):
    print(f"Current columns: {df.columns.tolist()}")
    rename_cols = input(f"Enter columns to rename in 'old:new' format (comma-separated): ")
    if rename_cols:
        rename_dict = dict(pair.split(':') for pair in rename_cols.split(','))
        df.rename(columns=rename_dict, inplace=True)
    print("Updated DataFrame:")
    print(df.head())
    return df

# Function to delete columns from a DataFrame
def delete_columns(df):
    return remove_columns(df)

# Function to merge two or more DataFrames
def merge_dataframes(dfs):
    print("Columns to merge on (common in all selected DataFrames):")
    merge_cols = input("Enter the columns to merge on (comma-separated): ").split(',')
    merged_df = dfs[0]
    for df in dfs[1:]:
        merged_df = pd.merge(merged_df, df, on=merge_cols, how='left')
    print("Merged DataFrame:")
    print(merged_df.head())
    return merged_df

# Main script logic
def main():
    while True:
        choice = display_menu()

        if choice == '1':
            print("\nDisplaying list of CSV files:")
            files = list_csv_files()
            file_index = int(input("Enter the number of the file to view: ")) - 1
            if 0 <= file_index < len(files):
                file_path = os.path.join("./Resources", files[file_index])
                read_and_display_csv(file_path)
            else:
                print("Invalid file selection.")

        elif choice == '2':
            print("\nTransform Data: Remove columns")
            files = list_csv_files()
            file_index = int(input("Enter the number of the file to transform: ")) - 1
            if 0 <= file_index < len(files):
                file_path = os.path.join("./Resources", files[file_index])
                df = read_and_display_csv(file_path)
                df = remove_columns(df)
                save_choice = input("Do you want to save the changes? (yes/no): ")
                if save_choice.lower() == 'yes':
                    df.to_csv(file_path, index=False)
                    print("Changes saved.")
            else:
                print("Invalid file selection.")

        elif choice == '3':
            print("\nTransform Data: Rename columns")
            files = list_csv_files()
            file_index = int(input("Enter the number of the file to transform: ")) - 1
            if 0 <= file_index < len(files):
                file_path = os.path.join("./Resources", files[file_index])
                df = read_and_display_csv(file_path)
                df = rename_columns(df)
                save_choice = input("Do you want to save the changes? (yes/no): ")
                if save_choice.lower() == 'yes':
                    df.to_csv(file_path, index=False)
                    print("Changes saved.")
            else:
                print("Invalid file selection.")

        elif choice == '4':
            print("\nDelete columns from a CSV file")
            files = list_csv_files()
            file_index = int(input("Enter the number of the file to delete columns: ")) - 1
            if 0 <= file_index < len(files):
                file_path = os.path.join("./Resources", files[file_index])
                df = read_and_display_csv(file_path)
                df = delete_columns(df)
                save_choice = input("Do you want to save the changes? (yes/no): ")
                if save_choice.lower() == 'yes':
                    df.to_csv(file_path, index=False)
                    print("Changes saved.")
            else:
                print("Invalid file selection.")

        elif choice == '5':
            print("\nMerge CSV files")
            files = list_csv_files()
            selected_files_indices = input("Enter the numbers of the files to merge (comma-separated): ").split(',')
            selected_files = [os.path.join("./Resources", files[int(index) - 1]) for index in selected_files_indices]
            dfs = [pd.read_csv(file) for file in selected_files]
            merged_df = merge_dataframes(dfs)
            save_choice = input("Do you want to save the merged DataFrame? (yes/no): ")
            if save_choice.lower() == 'yes':
                merged_df.to_csv("./Resources/merged_output.csv", index=False)
                print("Merged DataFrame saved as 'merged_output.csv'.")

        elif choice == '6':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
