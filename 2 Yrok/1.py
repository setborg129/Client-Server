# 1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных из файлов
# info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV. Для этого:
# Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и считывание данных.
# В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь значения параметров
# «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения каждого параметра поместить в
# соответствующий список. Должно получиться четыре списка — например, os_prod_list, os_name_list, os_code_list,
# os_type_list. В этой же функции создать главный список для хранения данных отчета — например, main_data — и поместить
# в него названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
# Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла);
# Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение данных
# через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл;
# Проверить работу программы через вызов функции write_to_csv().

import re
import pandas as df

file_text = ['info_1.txt', 'info_2.txt', 'info_3.txt']
list_all = []
os_prod_list = []
os_name_list = []
os_code_list = []
os_type_list = []

def get_data(text_file):
    for text in text_file:
        with open(text, 'r', encoding='cp1251') as f:
            lines = f.readlines()
            for line in lines:
                find_word = re.search(r'Название ОС:', line)
                if find_word != None:
                    os_name_list.append(line[34:].replace('\n', ''))
                    list_all.append('\nНазвание ОС: ')
                    list_all.append(line[34:].replace('\n', ''))

                find_word = re.search(r'Изготовитель системы:', line)
                if find_word != None:
                    os_prod_list.append(line[34:].replace('\n',''))
                    list_all.append('\nИзготовитель системы: ')
                    list_all.append(line[34:].replace('\n',''))

                find_word = re.search(r'Код продукта:', line)
                if find_word != None:
                    os_code_list.append(line[34:].replace('\n', ''))
                    list_all.append('\nКод продукта: ')
                    list_all.append(line[34:].replace('\n', ''))

                find_word = re.search(r'Тип системы:', line)
                if find_word != None:
                    os_type_list.append(line[34:].replace('\n', ''))
                    list_all.append('\nТип системы: ')
                    list_all.append(line[34:].replace('\n', ''))


    with open('main_data.txt','w', encoding='windows-1251' ) as file:
        for item in list_all:
            writen = file.write(item)
    f.close()
    print(list_all)
    # переводим list в excel файл !
    # write_to_csv(list_all)

def write_to_csv(list_csv):
    pass
    good_list_csv = []
    for number, line in enumerate(list_csv):
        good_list_csv.append({
            'Название ОС:': os_name_list,
            'Код продукта:': os_prod_list,
            'Изготовитель системы:': os_code_list,
            'Тип системы:': os_type_list,
        })
    df.to_excel('write_to_xlsx.xlsx', index=False)
    print(f'Файл write_to_xlsx.xlsx успешно записан !')


get_data(file_text)
