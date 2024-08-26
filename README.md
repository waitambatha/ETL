

---

# ETL Script with Menu Interface

This Python script provides a menu-driven interface for performing various ETL (Extract, Transform, Load) operations on CSV files. The script allows you to:

- Display and view CSV files
- Transform data by removing or renaming columns
- Delete columns from a CSV file
- Merge multiple CSV files
- Load the transformed or merged data into a PostgreSQL database

## Features

### 1. Display and View CSV Files
- List all CSV files in the `Resources` folder.
- Select a file to display its contents.

### 2. Transform Data: Remove Columns
- List all CSV files in the `Resources` folder.
- Select a file and specify columns to remove.
- Display the updated DataFrame and save the changes if desired.

### 3. Transform Data: Rename Columns
- List all CSV files in the `Resources` folder.
- Select a file and specify columns to rename.
- Display the updated DataFrame and save the changes if desired.

### 4. Delete Columns
- List all CSV files in the `Resources` folder.
- Select a file and delete specific columns.
- Display the updated DataFrame and save the changes if desired.

### 5. Merge CSV Files
- List all CSV files in the `Resources` folder.
- Select two or more files to merge on common columns.
- Display the merged DataFrame and save it as `merged_output.csv` if desired.

### 6. Exit
- Exit the script.

## Prerequisites

Before running the script, ensure that you have the following installed:

- Python 3.x
- PostgreSQL database
- Required Python packages (see Installation section)

## Installation

1. Clone the repository or download the script files.
2. Install the required Python packages using the following command:

   ```bash
   pip install pandas SQLAlchemy psycopg2
   ```

3. Ensure that you have a PostgreSQL database set up.
4. Create a `config.py` file in the same directory as the script and include your database credentials:

   ```python
   # config.py

   username = "your_username"
   password = "your_password"
   ```

5. Place your CSV files in a folder named `Resources` in the same directory as the script.

## Usage

1. Run the script using the following command:

   ```bash
   python etl_script_with_menu.py
   ```

2. Follow the on-screen prompts to select the desired operation.

3. After performing operations such as transforming or merging data, you can save the changes back to the CSV files.

## Example

Here's how to use the script:

1. **Display a CSV file**:
   - Choose option `1` from the menu to display the list of CSV files.
   - Select a file to view its contents.

2. **Transform data by removing columns**:
   - Choose option `2` from the menu.
   - Select the CSV file.
   - Enter the columns you want to remove.
   - Save the changes if desired.

3. **Merge CSV files**:
   - Choose option `5` from the menu.
   - Select the CSV files to merge.
   - Specify the columns to merge on.
   - Save the merged DataFrame as `merged_output.csv`.


