import json
import pickle
import os


def translate_database_file(filename_de, one_to_one):
    file_en = open(f"db_en/{filename_de}", "r+", encoding="utf-8")
    file_de = open(f"db_de/{filename_de[:-7] + 'de.json'}", "w", encoding="utf-8")

    database_de = json.load(file_en)
    len_database = len(database_de)
    i = 0
    print(filename_de)
    for thing_de in database_de:
        if i % 10 == 0:
            print(f"{i} / {len_database}")
        for slot_de in thing_de:
            slot_value_en = thing_de[slot_de]
            if type(slot_value_en) == list:
                for ii in range(0, len(slot_value_en)):
                    thing_de[slot_de][ii] = one_to_one[thing_de[slot_de][ii]]
            else:
                thing_de[slot_de] = one_to_one[thing_de[slot_de]]
        i = i+1
    json.dump(database_de, file_de, indent=4, ensure_ascii=False)
    file_de.truncate()


def translate_database():
    directory_in_str_de = "db_en"
    directory_de = os.fsencode(directory_in_str_de)
    one_to_one_file = open("one_to_one_dict", "rb")
    one_to_one = pickle.load(one_to_one_file)
    one_to_one_file.close()
    for file_de in os.listdir(directory_de):
        filename_de = os.fsdecode(file_de)
        translate_database_file(filename_de, one_to_one)

translate_database()

#one_to_one_file = open("one_to_one_dict", "rb")
#one_to_one = pickle.load(one_to_one_file)
#one_to_one_file.close()

#print(dict(list(one_to_one.items())[:100]))