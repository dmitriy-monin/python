from UI import *

def init(str):
    global surname, name, phone, comment

    list_date = str.split(" ")
    surname = list_date[0]
    name = list_date[1]
    phone = list_date[2]
    comment = list_date[3]
