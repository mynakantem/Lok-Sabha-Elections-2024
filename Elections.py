import requests
from bs4 import BeautifulSoup
import csv
import os

# List of URLs to scrape
urls = [
    'https://results.eci.gov.in/AcResultGenJune2024/partywiseresult-S01.htm',
    'https://results.eci.gov.in/AcResultGenJune2024/partywiseresult-S18.htm',
    'https://results.eci.gov.in/AcResultGen2ndJune2024/partywiseresult-S02.htm',
    'https://results.eci.gov.in/PcResultGenJune2024/index.htm',
    'https://results.eci.gov.in/AcResultGen2ndJune2024/partywiseresult-S21.htm'
]

# Function to fetch and parse a page
def fetch_and_parse(url):
    response = requests.get(url)
    if response.status_code == 200:
        return BeautifulSoup(response.content, 'html.parser')
    else:
        print(f'Failed to fetch {url}, Status code: {response.status_code}')
        return None

# Determine the path to the Downloads directory
downloads_path = os.path.expanduser('~/Downloads')

# Function to scrape data and save to CSV
def scrape_and_save(url, filename):
    soup = fetch_and_parse(url)
    if soup:
        # Open CSV file in write mode with newline='' to prevent extra newlines
        csv_filepath = os.path.join(downloads_path, filename)
        with open(csv_filepath, 'w', newline='', encoding='utf-8') as csvfile:
            csv_writer = csv.writer(csvfile)

            # Track if headers have been written to avoid rewriting
            headers_written = False

            # Extracting data from specific tables
            tables = soup.find_all('table')
            for table in tables:
                rows = table.find_all('tr')
                for i, row in enumerate(rows):
                    cells = [cell.text.strip() for cell in row.find_all(['td', 'th'])]
                    # Skip the unwanted header row and the first row if it matches the unwanted format
                    if cells == ['Party', 'Won', 'Leading', 'Total', 'Total', '543', '0', '543'] or (i == 0 and cells == ['Party', 'Won', 'Leading', 'Total']):
                        continue
                    if cells:
                        if not headers_written:
                            csv_writer.writerow(['Party', 'Won', 'Leading', 'Total'])  # Write header row only once
                            headers_written = True
                        csv_writer.writerow(cells)  # Write data row
        print(f"Data successfully written to {csv_filepath}")
    else:
        print(f"Failed to scrape data from {url}")

# Scrape data and save to different CSV sheets
for url in urls:
    filename = url.split('/')[-1].split('.')[0] + '.csv'
    scrape_and_save(url, filename)
