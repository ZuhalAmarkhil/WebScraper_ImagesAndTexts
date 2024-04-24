# Import required libraires 
import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import os
import csv

# This is the url to the website/page I want to scrape
url = "https://en.wikipedia.org/wiki/List_of_individuals_nominated_for_the_Nobel_Peace_Prize"
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    print('Success')
else:
    print('Failed to retrieve content. Status code:', response.status_code)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the table containing the list of individuals nominated for the Nobel Peace Prize
table = soup.find('table', class_='wikitable')

# Check if the table is found
if table:
    # Find all rows in the table
    rows = table.find_all('tr')

    # Create a directory to save the images
    image_dir = 'images'
    os.makedirs(image_dir, exist_ok=True)

    # Counter to generate numbered filenames for images
    image_counter = 1

    # Initialize a list to store row data for the CSV file
    all_rows = []

    # Process each body row in the table 
    for row in rows:
        # Extract cells from the body row
        cells = row.find_all(['th', 'td'])

        # Process the cells
        row_data = []
        for cell in cells:
            # Check if the cell contains an image
            image = cell.find('img')
            if image:
                # Extract the URL of the image
                image_url = 'https:' + image['src']

                try:
                    # Make a GET request to fetch the image
                    image_response = requests.get(image_url)

                    # Save the image to the directory with a numbered filename
                    image_filename = f'{image_dir}/{image_counter}.jpg'
                    with open(image_filename, 'wb') as f:
                        f.write(image_response.content)

                    print(f"Downloaded image {image_counter}")
                    row_data.append(image_filename)
                    image_counter += 1

                except Exception as e:
                    print(f"Error downloading image {image_counter}: {e}")

            # Extract and append text content to row_data
            text_content = cell.get_text(strip=True)
            row_data.append(text_content)

        # Append row_data to all_rows
        all_rows.append(row_data)

    # Write data to a CSV file
    csv_filename = "Nominees_info.csv"
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(all_rows)

    print("CSV file successfully created.")

else:
    print('Table not found on the webpage')
