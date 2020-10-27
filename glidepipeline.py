from flask import Flask, request
import os
import requests
import pdfplumber
import pandas as pd
import re
import datetime
import io
import gspread
from oauth2client.service_account import ServiceAccountCredentials

#Initializing app
app = Flask(__name__)

#Reading PDF without downloading in local
def reading_pdf(url):
    response = requests.get(url)

    with io.BytesIO(response.content) as open_pdf_file:
        read_pdf = pdfplumber.open(open_pdf_file)
        first_page = read_pdf.pages[0]
        text = first_page.extract_text()

    return text

#Creating rules to extract info from PDF
def processed_info(text, URL, User):
    timestamp_raw = datetime.date.today().strftime('%d-%m-%Y')
    timestamp = re.sub('-', '/', timestamp_raw)

    for row in text.split('\n'):
        if row.startswith('Factura Nº:'):
            factura_n = row.split()[2:]
            numero_factura = re.sub('\D+', '', str(factura_n))

    for row in text.split('\n'):
        if row.startswith('Fecha de Factura:'):
            fecha = row.split()[3:]
            fecha_clean = fecha[0]
            fecha_facturacion = re.sub('\W+', '/', fecha_clean)

    for row in text.split('\n'):
        if row.startswith('Periodo Facturación:'):
            periodo = row.split()[2:]
            periodo_clean = " ".join(map(str, periodo))
            periodo_facturacion = ' '.join(periodo_clean.split(' ')[:-2])

    for row in text.split('\n'):
        if row.startswith('TOTAL FACTURA'):
            total_factura = row.split()[-1]

#Creating a new entry with the processed info
    new_record = [timestamp, numero_factura, 'Fenie Energía', fecha_facturacion, periodo_facturacion, total_factura, URL, User]

    return new_record

#Connecting to Google Sheets and sending info back
def sending_info(new_record):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
                 "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    credentials = ServiceAccountCredentials.from_json_keyfile_name("credentials.json", scope)
    client = gspread.authorize(credentials)
    sheet = client.open("DocuHub")
    worksheet = sheet.worksheet("Facturas_Processed")
    processed_data = worksheet.append_row(new_record)
    return processed_data




@app.route('/webhook', methods=['POST'])
def webhook():
    response = request.get_json()
    user = response['User']
    url = response['Imagen']
    print("User", user)
    print("Imagen", url)
    text = reading_pdf(url)
    print(text)
    new_entry = processed_info(text, url, user)
    print(new_entry)
    processed_invoice = sending_info(new_entry)
    print(processed_invoice)
    return processed_invoice





if __name__=='__main__':
    app.run(host='0.0.0.0',
            port='5000')
