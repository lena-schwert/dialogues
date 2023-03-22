import json
#import tkinter as tk
from deep_translator import GoogleTranslator
import pickle
import os

my_translator = GoogleTranslator(source='en', target='de')

#file= open("db_en/attraction_en.json", "r")
#database = json.load(file)

def test_result():
    one_to_one_file = open("one_to_one_dict", "rb")
    one_to_one = pickle.load(one_to_one_file)
    one_to_one_file.close()
    slot_values_en_file = open("slot_values_en_list", "rb")
    slot_values_en = pickle.load(slot_values_en_file)
    slot_values_en_file.close()
    slot_values_de_file = open("slot_values_de_list", "rb")
    slot_values_de = pickle.load(slot_values_de_file)
    slot_values_de_file.close()
    print(dict(list(one_to_one.items())[:20]))
    print(slot_values_en[:20])
    print(slot_values_de[:20])


def translate_slot_value(slot_value_en, slot_value_zh, one_to_one, slot_values_en, slot_values_de):
    if slot_value_en.isnumeric() or slot_value_en == slot_value_zh:
        slot_value_de = slot_value_en
    else:
        slot_value_de = my_translator.translate(slot_value_en)
    slot_values_en += [slot_value_en]
    slot_values_de += [slot_value_de]
    one_to_one[slot_value_en] = slot_value_de


def translate_database_file(filename_en, filename_zh, one_to_one, slot_values_en, slot_values_de):
    file_en = open(f"db_en/{filename_en}", "r", encoding="utf-8")
    file_zh = open(f"db_zh/{filename_zh}", "r", encoding="utf-8")

    database_en = json.load(file_en)
    database_zh = json.load(file_zh)
    len_database = len(database_en)
    i = 0
    print(filename_en)
    for thing_en, thing_zh in zip(database_en, database_zh):
        if i % 10 == 0:
            print(f"{i} / {len_database}")
        for slot_en, slot_zh in zip(thing_en, thing_zh):
            slot_value_en = thing_en[slot_en]
            slot_value_zh = thing_zh[slot_zh]
            if type(slot_value_en) == list:
                for element in slot_value_en:
                    if element not in one_to_one:
                        translate_slot_value(element, slot_value_zh, one_to_one, slot_values_en, slot_values_de)
            else:
                if slot_value_en not in one_to_one:
                    translate_slot_value(slot_value_en, slot_value_zh, one_to_one, slot_values_en, slot_values_de)
        i = i+1


def translate_database():
    directory_in_str_en = "db_en"
    directory_en = os.fsencode(directory_in_str_en)
    directory_in_str_zh = "db_zh"
    directory_zh = os.fsencode(directory_in_str_zh)
    one_to_one = dict()
    slot_values_en = []
    slot_values_de = []
    for file_en, file_zh in zip(os.listdir(directory_en), os.listdir(directory_zh)):
        filename_en = os.fsdecode(file_en)
        filename_zh = os.fsdecode(file_zh)
        translate_database_file(filename_en, filename_zh, one_to_one, slot_values_en, slot_values_de)
    return one_to_one, slot_values_en, slot_values_de

one_to_one, slot_values_en, slot_values_de = translate_database()

one_to_one_file = open("one_to_one_dict", "wb")
pickle.dump(one_to_one, one_to_one_file)
one_to_one_file.close()
slot_values_en_file = open("slot_values_en_list", "wb")
pickle.dump(slot_values_en, slot_values_en_file)
slot_values_en_file.close()
slot_values_de_file = open("slot_values_de_list", "wb")
pickle.dump(slot_values_de, slot_values_de_file)
slot_values_de_file.close()

test_result()

# One_to_One scheint Leer zu sein (wird nicht geprinted und slot_values kommen doppelt vor)