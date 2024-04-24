## WebScraper_ImagesAndTexts ### 

### Description: ###
This project aims to extract data from the Wikipedia page listing individuals nominated for the Nobel Peace Prize using web scraping techniques. The extracted data includes images of the nominees and textual information such as their names, birth years, and other relevant details. The extracted images are stored in a separate directory, while the textual data is saved in CSV format for easy analysis and manipulation. Python programming language is utilized alongside various libraries to accomplish this web scraping task.

### Libraries Used: ###
- **BeautifulSoup:** Used for parsing HTML and navigating the website's DOM structure.
- **Requests:** Used to send HTTP requests to the website and retrieve HTML content.
- **PIL (Python Imaging Library):** Used for handling images.
- **BytesIO:** Used for handling image data as bytes.
- **os:** Used for file and directory manipulation.
- **csv:** Used for working with CSV files.

### Project Structure: ###
- **scraper.py:** This file contains the combined code for scraping both images and textual data from the website.
- **requirements.txt:** This file lists Python libraries required to be installed for running the project.
- **README.md:** This file serves as documentation, providing an overview of the project and its components.
- **images/:** This directory is where scraped images are saved.
- **Nominees_info.csv:** This CSV file contains data extracted from the website.
- **Note:** The images directory and the Nominees_info.csv file are created as a result of running the code. You may remove these two from the cloned repository if you want to run the code to see how they are generated.

### How to Run: ###
- Clone this repository to your local machine.
- Install the required libraries by running pip install -r requirements.txt.
- Run the scraper.py file to start the web scraping process.

### Note: ###
- The reason I decided to choose Wikipedia, is that it does not explicity specified that webscraping is not allowed. 
- Ensure that you are familiar with the website's terms of service and scraping policies before running the script.

### Contributing: ###
If you'd like to contribute to this project, feel free to fork the repository and submit a pull request with your changes.

### Author: ###
Zuhal