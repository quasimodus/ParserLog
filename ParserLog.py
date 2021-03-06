#! /usr/bin/env python3
import re
from collections import Counter
import csv
import PySimpleGUI as sg


# парсит IP-адреса из лога и выдает список: ['192.168.0.2', '192.168.0.2', '192.168.0.2', .....
def reader(filename):
    regexp = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'  # регулярка выбирает ip адреса
    with open(filename) as f:
        log = f.read()
        ips_list = re.findall(regexp, log)
    #    print(ips_list) # для проверки
    return ips_list


# создает объект со значениями вида Counter({'192.168.0.2': 6, '192.168.0.5': 2, '192.168.4.2': 1, '0.0.0.0': 1})
def count(ips_list):
    count = Counter(ips_list)
    #    print(count) # для проверки
    return count


# создает файл 'output.csv' с колонками IP и Frequency и записывает туда IP-адреса и сколько раз они попадались с логе
def write_csv(count):
    with open('output.scv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        header = ['IP', 'Frequency']
        writer.writerow(header)

        for item in count:
            writer.writerow((item, count[item]))


sg.theme('DarkAmber')  # Add a touch of color
# All the stuff inside your window.
layout = [[sg.Text('Filename')],
          [sg.Input(), sg.FileBrowse()],
          [sg.OK(), sg.Cancel()]]

# Create the Window
window = sg.Window('Get filename example', layout)
# Event Loop to process "events" and get the "values" of the inputs


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

    elif event == 'OK':
        write_csv(count(reader(values[0])))
        break

