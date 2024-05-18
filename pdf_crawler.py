import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Define the URL of the webpage to scrape
url = 'http://example.com'

# Define the directory to save the downloaded files
download_directory = 'downloaded_pdfs'
os.makedirs(download_directory, exist_ok=True)

# Fetch the content of the webpage
response = requests.get(url)
if response.status_code != 200:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
    exit()

# Parse the webpage content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all link tags
link_tags = soup.find_all('a')

# Function to download a file from a URL
def download_file(url, folder_path):
    try:
        # Get the content of the file
        file_response = requests.get(url)
        if file_response.status_code == 200:
            # Extract the file name from the URL
            file_name = os.path.join(folder_path, url.split('/')[-1])
            # Write the content to a local file
            with open(file_name, 'wb') as file:
                file.write(file_response.content)
            print(f"Downloaded: {file_name}")
        else:
            print(f"Failed to download file from {url}. Status code: {file_response.status_code}")
    except Exception as e:
        print(f"An error occurred while downloading {url}. Error: {e}")

# Iterate over each link tag and download the file if it ends with .pdf
for link in link_tags:
    file_url = link.get('href')
    if file_url and file_url.endswith('.pdf'):
        # Handle relative URLs
        if not file_url.startswith('http'):
            file_url = urljoin(url, file_url)
        download_file(file_url, download_directory)

print("Download complete.")
