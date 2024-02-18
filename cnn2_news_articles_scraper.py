import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime

cnn_url = 'https://edition.cnn.com/world'

#Send a GET request to the specified URL
response = requests.get(cnn_url)

#Use BeautifulSoup to parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

#Find all the article headline elements
articles = soup.find_all('span', class_='container__headline-text')
#Initialize a list to store the scraped data
news_article = []

for article in articles:
    #Extract the headline text
    headline = article.text.strip()

    #Append the scraped data to the list
    news_article.append({'Headline': headline})

#Convert the list of dictionaries to a pandas DataFrame
df = pd.DataFrame(news_article)

# Create a timestamp for the CSV file
time = datetime.now().strftime('%Y%m%d_%H%M%S')

file_name = f'cnn_news_article_{time}.csv'
#Save the DtaFrame to a CSV file
df.to_csv(file_name, index = False)

print(f"News articles scraped and saved to {file_name}")

