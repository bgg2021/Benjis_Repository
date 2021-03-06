import PyPDF2
from PyPDF2 import PdfFileReader

import requests
from pathlib import Path

from twilio.rest import Client

import datetime

from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

url = "https://fwparker.myschoolapp.com/ftpimages/1048/download/download_2215373.pdf"
response = requests.get(url)

if response.history:
    print("Request was redirected")
    for resp in response.history:
        print(resp.status_code, resp.url)
        url = resp.url

    print("Final Destination")
    print(response.status_code, response.url)
else:
    print("Request was not redirected")

filename = Path('lunch.pdf')
response = requests.get(url)
filename.write_bytes(response.content)
print(url)

# ^^^ Download the PDF from the parker website as 'lunch.pdf'

# creating a pdf file object
pdfFileObj = open('lunch.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# creating a page object
pageObj = pdfReader.getPage(0)

# extracting text from page
menu_text = str(pageObj.extractText())

menu_list = []
done = False

while not done:
    try:
        menu_text.index("\n")
    except:
        done = True
        break
    line = menu_text[0:(menu_text.index("\n"))]
    menu_text = menu_text[menu_text.index("\n") + 1:]
    menu_list.append(line.strip())

monday_list = []
tuesday_list = []
wednesday_list = []
thursday_list = []
friday_list = []

#print(menu_list)

tuesday_index = menu_list.index("Tuesday:")

try:
    wednesday_index = menu_list.index("Wednesd")
except:
    backup_wednesday_index = menu_list.index("Wednesday:")

try:
    thursday_index = menu_list.index("Thursda")
except:
    backup_thursday_index = menu_list.index("Thursday:")

friday_index = menu_list.index("Friday:")

try:
    for i in menu_list:
        if i == "Monday:":
            monday_list.append(menu_list[menu_list.index(i):tuesday_index])
except:
    try:
        print("there is no data for monday")
        tuesday_list.append(menu_list[tuesday_index:wednesday_index])
    except:
        try:
            print("there is no data for tuesday")
            wednesday_list.append(menu_list[wednesday_index:thursday_index])
        except:
            try:
                print("there is no data for wendesday")
                thursday_list.append(menu_list[thursday_index:friday_index])
            except:
                try:
                    print("there is no data for thursday")
                    friday_list.append(menu_list[friday_index:])
                except:
                    print("there is no data for friday")

try:
    tuesday_list.append(menu_list[tuesday_index:wednesday_index])
except:
    tuesday_list.append(menu_list[tuesday_index:backup_wednesday_index])
    wednesday_index = backup_wednesday_index

try:
    wednesday_list.append(menu_list[wednesday_index:thursday_index])
except:
    wednesday_list.append(menu_list[wednesday_index:backup_thursday_index])
    thursday_index = backup_thursday_index

thursday_list.append(menu_list[thursday_index:friday_index])
friday_list.append(menu_list[friday_index:])


# closing the pdf file object
pdfFileObj.close()

monday_list = monday_list[0]
tuesday_list = tuesday_list[0]
wednesday_list = wednesday_list[0]
thursday_list = thursday_list[0]
friday_list = friday_list[0]

monday = (" ".join(monday_list)) + "."
tuesday = (" ".join(tuesday_list)) + "."
wednesday = (" ".join(wednesday_list)) + "."
thursday = (" ".join(thursday_list)) + "."
friday = (" ".join(friday_list)) + "."

#weekday = datetime.date.today().strftime("%A")

f = open("menu.txt", "w")

day_list = [monday, tuesday, wednesday, thursday, friday]

f.write(str(day_list))


now = datetime.datetime.now()  # this creates a datetime object
weekday = (now.weekday())  # monday is 0. sunday is 6
hour = (now.hour)
if hour >= 14:
    weekday += 1
if weekday > 4:
    weekday = 0
