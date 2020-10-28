# Final Project Ironhack - DocuHub

## About the project

DocuHub is a functional MVP that allows users to automate data extraction from any kind of document using an OCR Python library. 

- Goal: Extract info from any document in seconds.
- Benefits: Reduce the time spent on data entry, reduce human error on typing.
- Scope: The app only process one type of document -> bills from a electricity provider
- Limitations: Document structure, formatting, data legibility and parsing text rules might condition the output of the algorithm

## Disclaimer

This project was tested only with one electricity provider due to time constraints (1 month worth of work) 

## How does it work?

The app is built using a no-code tool called Glide, which acts as a front-end framework and a database system. The data is processed in a Google Sheet file and the image is stored in Glide servers. 

Once a new user entry is made, Zapier will listen for that event (a new row being added) and send the data via POST method to a Heroku server built on Flask framework. 

Once the webhook receives the info it runs a Python script which:
- Retrieves the image file via HTTP request
- Process the image with an OCR library
- Returns a text object
- Applies text rules to extract desired info
- Creates a new record with the info
- Send back the processed info to the Google Sheet file


## Tecnologies used

- [Glide](https://www.glideapps.com/): No-code tool used to create the front-end of the app
- [Zapier](https://zapier.com/): Tool to create the webhook between Google Sheets file and Heroku Server
- [Flask](https://flask.palletsprojects.com/en/1.1.x/): Python framework that runs the script from a route called /webhook
- [Heroku](https://www.heroku.com/):  

## Libraries
The core of the project is Python 3.7.3 therefore you will have to install those libraries for run the script. It is advisable to create a virtual environment to import all libraries and run the script in your machine. 

### Native Python packages
- [datetime](https://docs.python.org/2/library/datetime.html)
- [io](https://docs.python.org/3/library/io.html)
- [re](https://docs.python.org/3/library/re.html)
- [requests](https://requests.readthedocs.io/en/master/)

### External libraries
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [google-auth-oauthlib](https://pypi.org/project/google-auth-oauthlib/)
- [gspread](https://gspread.readthedocs.io/en/latest/)
- [gunicorn](https://docs.gunicorn.org/en/stable/install.html)
- [json5](https://pypi.org/project/json5/)
- [oauth2client](https://github.com/googleapis/google-api-python-client)
- [oauthlib](https://oauthlib.readthedocs.io/en/latest/)
- [pdfplumber](https://pypi.org/project/pdfplumber/)
- [pytesseract](https://pypi.org/project/pytesseract/)
