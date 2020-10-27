# Final Project Ironhack - DocuHub

## About the project

DocuHub is a functional MVP that allows users to automate data extraction from any kind of document using an OCR Python library. 

- Goal: Extract info from any document in seconds.
- Benefits: Reduce the time spent on data entry, reduce human error on typing.
- Scope: The app only process one type of document -> bills from a electricity provider
- Limitations: Document structure, formatting, data legibility and parsing text rules might condition the output of the algorithm

## Disclaimer

This project was tested only with one electricity provider due to time constraints 

## How does it work?

The app is built using a no-code tool called [Glide](https://www.glideapps.com/), which acts as a front-end framework and a database system. The data is processed in a Google Sheet file and the image is stored in Glide servers. 

Once a new user entry is made, [Zapier](https://zapier.com/) will listen for that event (a new row being added) and send the data via POST method to a [Heroku](https://www.heroku.com/) server built on [Flask](https://flask.palletsprojects.com/en/1.1.x/) framework. 

Once the webhook receives the info it runs a Python script which:
- Retrieves the image file via HTTP request
- Process the image with an OCR library
- Returns a text object
- Applies text rules to extract desired info
- Creates a new record with the info
- Send back the processed info to the Google Sheet file


## Tecnologies used

- Glide: No-code tool used to create the front-end of the app
- Zapier: Tool to create the webhook between Google Sheets file and Heroku Server
- Flask: Python framework that runs the script from a route called /webhook

## Libraries 

### Native Python packages

### External libraries
