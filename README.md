# ProductVision AI

ProductVision AI is a small web-based dashboard for collecting product-like data from public demo sources, viewing it in a structured table, and exporting it for further use. The app combines a Flask frontend with simple scraping logic and spreadsheet export support.

## What this project does

The application lets a user:

- pick a data source from a simple dropdown
- fetch product or product-like records from that source
- view the results in a table with image, name, price, rating, availability, and link
- see quick summary statistics such as item count and price range
- download the current results as CSV or Excel files

## Main features

- Flask-based web interface
- Multiple demo data sources
- Basic analytics from the fetched records
- CSV and Excel export
- Lightweight styling with a dark/light toggle

## Project structure

- app.py: Flask routes for the home page, search flow, and download endpoints
- scraper.py: logic for collecting data from the selected source
- exporter.py: functions for creating CSV and Excel files
- templates/index.html: main page layout and table rendering
- static/style.css: styling for the dashboard
- static/script.js: small client-side behavior such as theme toggle
- assests/: contains screenshots and other project assets
- output/: generated export files are stored here

## Supported data sources

The app currently supports these sample sources:

- Books to Scrape
- Quotes to Scrape
- DummyJSON products

## Installation

1. Make sure Python 3 is installed.
2. Install the required packages:

   pip install -r requirements.txt

3. Start the app:

   python app.py

4. Open the local address shown in the terminal, usually:

   http://127.0.0.1:5000/

## How it works

1. The user selects a source from the dashboard.
2. The Flask app sends the request to the scraper module.
3. The scraper gathers data and returns a list of records.
4. The records are displayed in the page and summarized in cards.
5. The export routes create files in the output folder for download.

## Dependencies

The project uses:

- Flask
- requests
- BeautifulSoup
- pandas
- openpyxl

## Screenshots

The project includes several UI screenshots in the assests folder.

Example screenshots:

- ![Dashboard Overview](assests/Screenshot%202026-06-27%20184212.png)
- ![Search and Results View](assests/Screenshot%202026-06-27%20185113.png)
- ![Product Table](assests/Screenshot%202026-06-27%20185237.png)
- ![Analytics and Export Options](assests/Screenshot%202026-06-27%20185247.png)

Additional screenshots are also available in the assests folder for reference.

## Notes

This project is intended as a practical demo for web scraping, data display, and file export. The data sources are public demo endpoints, so the app is best used for learning and experimentation.


## 👩‍💻 Author

**R. Akanksha Rani**

Software Development Intern – SkillCraft Technology