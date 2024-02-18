import pandas as pd
import matplotlib.pyplot as plt

#Load the dataset
file_path = 'C:\\Users\\acer\\OneDrive\\Desktop\\Python Development\\Task 2\\sales_data_sample.csv'
#Read the dataset
df = pd.read_csv(file_path , encoding='ISO-8859-1')

numeric_columns = ['ORDERNUMBER', 'QUANTITYORDERED', 'PRICEEACH', 'ORDERLINENUMBER', 'SALES']
productline_col = ["Motorcycles", "Classic Cars", "Trucks and Buses", "Vintage Cars", "Planes", "Ships", "Trains"]
yearid_col = [2003, 2004, 2005]
customer_name_col = ["Alpha Cognac", "Amica Models & Co.", "Anna's Decorations, Ltd", "Atelier graphique", "Australian Collectables, Ltd",
                    "Australian Collectors, Co.", "Australian Gift Network, Co", "Auto Assoc. & Cie.", "Auto Canal Petit", 
                    "Auto-Moto Classics Inc.", "AV Stores, Co.", "Baane Mini Imports", "Bavarian Collectables Imports, Co.", "Blauer See Auto, Co.",
                    "Boards & Toys Co.", "CAF Imports", "Cambridge Collectables Co.", "Canadian Gift Exchange Network", "Classic Gift Ideas, Inc",
                    "Classic Legends inc.", "Clover Collections, Co.", "Collectable Mini Designs Co.", "Collectables For Less inc.", "Corporate Gift Ideas Co.",
                    "Corrida Auto Replicas, Ltd", "Cruz & Sons Co.", "Daedalus Designs Imports", "Danish Wholesale Imports", "Diecast Classics Inc.", "Diecast Collectables",
                    "Double Decker Gift Stores, Ltd", "Dragon Souvenirs, Ltd.","Enaco Distributors", "Euro Shopping Channel", "FunGiftIdeas.com", "Gift Depot Inc.", "Gift Ideas Corp.",
                    "Gifts4AllAges.com", "giftsbymail.co.uk", "Handji Gifts& Co", "Heintze Collectables", "Herkku Gifts", "Iberia Gift Imports, Corp.", "La Corne D'abondance, Co", "La Rochelle Gifts", 
                    "Land of Toys Inc.", "L'ordine Souveniers", "Lyon Souveniers", "Marseille Mini Autos", "Marta's Replicas Co.", "Men R US Retailers, Ltd.", "Microsale Inc.", "Mini Auto Werke", "Mini Caravy",
                    "Mini Classics", "Mini Creations Ltd.", "Mini Gifts Distributors Ltd.", "Mini Wheels Co.", "Motor Mint Distributors Inc.", "Muscle Machine Inc", "Norway Gifts By Mail, Co."]

#Filter data based on specific criteria (productline, yearid and customername)
filtered_data = df[(df['PRODUCTLINE'] == "Vintage Cars") & (df['YEAR_ID'] == 2003) & (df['CUSTOMERNAME'] == "Euro Shopping Channel")][numeric_columns]

#Display the filtered dataframe
print(filtered_data.head)

#Calculate summary statistics for the filtered data
summary_stats = {}
for column in numeric_columns:
    column_data = filtered_data[column]
    summary_stats[column] = {
        'Sum': column_data.sum(),
        'Mean': column_data.mean(),
        'Mode': column_data.mode().iloc[0],
        'Median': column_data.median(),
        'Maximum': column_data.max(),
        'Minimum': column_data.min(),
        'Range': column_data.max() - column_data.min(),
        'Standard Deviation': column_data.std()
    }

#Print the summary statistics
for stat_type in ['Mean', 'Mode', 'Median', 'Maximum', 'Minimum', 'Range', 'Sum', 'Standard Deviation']:
    print(f"\n{stat_type} Values:")
    for column, stats in summary_stats.items():
        print(f"{column}: {stats[stat_type]}")

#Select only numeric columns for the histogram
numeric_columns = ['ORDERNUMBER', 'QUANTITYORDERED', 'PRICEEACH', 'ORDERLINENUMBER', 'SALES']
filtered_numeric_data = filtered_data[numeric_columns]

#Create histogram for filtered data
for column in numeric_columns:
    plt.figure(figsize=(8,6))
    plt.hist(filtered_data[column], bins=20, color='skyblue', edgecolor = 'black')
    plt.title(f"Histogram of {column} for Vintage Cars sold in 2003 (Euro Shopping Channel)")
    plt.xlabel(column)
    plt.ylabel("Frequency")
    plt.savefig(f"{column}_histogram_filtered_data.png")
    plt.grid(True)
    plt.show()
    plt.close()

#Bar chart for 2004 Motorcycle sales
#Filter data for motorcycle sales in the year 2004
motorcycle_sales_2004 = df[(df['PRODUCTLINE'] == 'Motorcycles') & (df['YEAR_ID'] == 2004)]
#Calculate the total sales for each customer
customer_sales = motorcycle_sales_2004.groupby('CUSTOMERNAME')['SALES'].sum().reset_index()
#Plot the bar chart for motorcycle sales in 2004 by customer name
plt.figure(figsize=(10,6))
bar_width = 0.40
index = df.index 
plt.bar(customer_sales['CUSTOMERNAME'], customer_sales['SALES'], color='purple')
plt.title("Bar Chart of Motorcycle Sales in 2004")
plt.xlabel("Customer Name")
plt.ylabel("Total Sales")
plt.xticks(rotation=90, ha='right')
plt.tight_layout()
plt.grid(True)
plt.show()
plt.savefig("motorcycle_sales_2004_bar_chart.png")

#Saving the filtered data to a new file
filtered_data.to_csv("filtered_data.csv", index=False)
#Saving the summary statistics to a new file
with open('summary_statistics.csv', 'w') as file:
    file.write("Column,Mean,Mode,Median,Maximum,Minimum,Range,Sum,Standard Deviation\n")
    for column, stats in summary_stats.items():
        file.write(f"{column},{stats['Mean']},{stats['Mode']},{stats['Median']},{stats['Maximum']},{stats['Minimum']},{stats['Range']},{stats['Sum']},{stats['Standard Deviation']}\n")