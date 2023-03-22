
import os
import pickle

alignment_file = open("/home/lena/git/multi-tod-german/Hilfsdateien/alignment_dict", "rb")
alignment = pickle.load(alignment_file)
alignment_file.close()

one_to_one_file = open("/home/lena/git/multi-tod-german/Hilfsdateien/one_to_one_dict", "rb")
one_to_one = pickle.load(one_to_one_file)
one_to_one_file.close()

slot_values_de_list_file = open("/home/lena/git/multi-tod-german/Hilfsdateien/slot_values_de_list", "rb")
slot_values_de_list = pickle.load(slot_values_de_list_file)
slot_values_de_list_file.close()

slot_values_en_list_file = open("/home/lena/git/multi-tod-german/Hilfsdateien/slot_values_en_list", "rb")
slot_values_en_list = pickle.load(slot_values_en_list_file)
slot_values_en_list_file.close()

#######

def search_keys_by_val(entity_to_id_dict: dict, byVal):
    keysList = []
    itemsList = entity_to_id_dict.items()
    for item in itemsList:
        if item[1] == byVal:
            keysList.append(f'key: {item[0]}, value: {byVal})')
    return keysList


def search_val_by_key(entity_to_id_dict: dict, byKey: str):
    valList = []
    itemsList = entity_to_id_dict.items()
    for item in itemsList:
        if item[0] == byKey:
            valList.append(f'key: {item[0]}, value: {byKey})')
    return valList


# search for specifc

'17. Januar 2017' in one_to_one.values()

one_to_one['17. Januar 2017']

search_keys_by_val(one_to_one, 'Garten')
search_val_by_key(one_to_one, 'Garten')
