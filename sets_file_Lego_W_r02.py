import pandas as pd

# Load the CSV file into a DataFrame
file_path = r'C:\Users\Siris\Desktop\GitHub Projects 100 Days NewB\_24_0078__Day74_Aggregate_and_Merge_Data_w_Pandas__240814\NewProject\r00-r09 START\r00_env_START\data\sets.csv'
df = pd.read_csv(file_path)

# Find the lowest year in the 'year' column
lowest_year = df['year'].min()

number_of_parts = df['num_parts'].nlargest(5)

# Count the total number of products sold in the lowest year
total_products_sold = df[df['year'] == lowest_year]['set_num'].count()

print(f"The lowest year in the dataset is: {lowest_year}")
print(f"The total number of products sold in {lowest_year} is: {total_products_sold}")

print(f"The top 5 of total parts for a LEGO set is: {number_of_parts}")