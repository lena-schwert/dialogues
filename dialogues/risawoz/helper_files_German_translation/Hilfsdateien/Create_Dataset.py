# 1. I need to translate the Database
# 2. I need to combine the alignment

# 1. Loop through en_fewshot.json
# 2. Change user and system utterances in the obvious way
# 3. Change alignment in the obvious way
# 4. Every other slot value should be translated
# 5. I think apart from the Utterances and alignment only some Values (not keys) (In Orange should be changed)

import json
import pickle
import csv
import ast
import string
from deep_translator import GoogleTranslator
my_translator = GoogleTranslator(source='en', target='de')

one_to_one_file = open("one_to_one_dict2", "rb")
one_to_one = pickle.load(one_to_one_file)
one_to_one_file.close()
alignment_file = open("alignment_dict", "rb")
alignment = pickle.load(alignment_file)
alignment_file.close()

csv_file = open("C:/Users/jimma/annotate_translation/output/en_fewshot_output.csv", mode="r", encoding="utf-8")
csv_reader = csv.DictReader(csv_file, delimiter="\t")
fewshot_csv = []
for row in csv_reader:
    fewshot_csv += [row]

file_en = open("en_fewshot.json", "r+", encoding="utf-8")
file_de = open("de_fewshot.json", "w", encoding="utf-8")

fewshot_en = json.load(file_en)

def translate_word(en_word):
    if en_word.isnumeric():
        de_word = en_word
    else:
        de_word = my_translator.translate(en_word)
    return de_word

def get_one_to_one(entity_en):
    clean_entity_en = clean_entity(entity_en)
    if clean_entity_en in one_to_one:
        target_de = one_to_one[clean_entity_en]
    elif entity_en in one_to_one:
        target_de = one_to_one[entity_en]
    else:
        print(entity_en)
        target_de = translate_word(entity_en)
        one_to_one[entity_en] = target_de
    return target_de

def clean_entity(en_entity):
    if en_entity[-1] in string.punctuation:
        en_entity = en_entity[:-1]
    return en_entity

def index_list(word_spans, word_span1):
    for index, word_span2 in enumerate(word_spans):
        if word_span1[0] == word_span2[0] and word_span1[1] == word_span2[1]:
            return index

def string_to_list(list_represantation):
    list1 = ast.literal_eval(list_represantation)
    #list1 = [n.strip() for n in list1]
    return list1.copy()

def change_utterance(i, utterance_type):
    turn_csv = fewshot_csv[i]
    target = turn_csv["target"]
    #print(i, turn_csv["source_entity"])
    #if i == 37:
    #    print("Kock")
    #source_entity = string_to_list(turn_csv["source_entity"])
    #target_entity = string_to_list(turn_csv["target_entity"])
    #print(source_entity)
    #print(turn_csv["source_word_span"])


    source_word_span = string_to_list(turn_csv["source_word_span"])
    target_word_span = string_to_list(turn_csv["target_word_span"])
    utterance = turn[utterance_type]
    utterance[0] = target
    for type in utterance[1]:
        entities = utterance[1][type]
        entities_keys = list(entities.keys()).copy()
        for entity_en in entities_keys:
            word_span = entities[entity_en][0]
            #print(source_word_span, word_span, entities, entity_en)
            index = index_list(source_word_span, word_span)
            if index == None:
                print(i, source_word_span, word_span, entities, entity_en)
            
            # I'm cheating hear
            target_de = get_one_to_one(entity_en)
            
            entities[target_de] = [target_word_span[index]]
            entities.pop(entity_en)


def change_slot_values(dictionary):
    if type(dictionary) == dict:
        for slot in dictionary:
            slot_value_en = dictionary[slot]
            if type(slot_value_en) == list:
                for ii in range(0, len(slot_value_en)):
                    slot_value_en[ii] = get_one_to_one(slot_value_en[ii])
            else:
                slot_value_de = get_one_to_one(slot_value_en)
                dictionary[slot] = slot_value_de


def change_actions(actions):
    for action in actions:
        if action[3] in one_to_one:
            action[3] = one_to_one[action[3]]


def change_alignment(alignment_json):
    entities_en = list(alignment_json.keys())
    for entity_en in entities_en:
        #entity_de = alignment[entity_en]
        entity_de = get_one_to_one(entity_en)
        alignment_json[entity_de] = entity_en
        alignment_json.pop(entity_en)

def create_dataset():      
    i = 0
    for dialogue in fewshot_en:
        #dialogue_alignment = dict()
        for turn in dialogue["dialogue"]:
            change_utterance(i, "user_utterance")
            i += 1
            change_utterance(i, "system_utterance")
            i += 1

            belief_state = turn["belief_state"]
            inform_slot_values = belief_state["inform slot-values"]
            turn_inform = belief_state["turn_inform"]
            user_actions = turn["user_actions"]
            system_actions = turn["system_actions"]
            alignment_json = turn["alignment"]
            db_results = turn["db_results"]

            change_slot_values(inform_slot_values)
            change_slot_values(turn_inform)
            change_actions(user_actions)
            change_actions(system_actions)
            change_alignment(alignment_json)
            for thing in db_results:
                change_slot_values(thing)

    json.dump(fewshot_en, file_de, indent=4, ensure_ascii=False)
    file_de.truncate()


def change_canonical_alignment(category):
    change_slot_values(category)
    en_slots = list(category.keys())
    for en_slot in en_slots:
        de_slot = get_one_to_one(en_slot)
        category[de_slot] = category.pop(en_slot)

def create_de2canonical():
    for domain in en2canonical:
        for category in en2canonical[domain]:
            change_canonical_alignment(en2canonical[domain][category])
    json.dump(en2canonical, file_de2canonical, indent=4, ensure_ascii=False)

file_en2canonical = open("en2canonical.json", "r+", encoding="utf-8")
file_de2canonical = open("de2canonical.json", "w", encoding="utf-8")
en2canonical = json.load(file_en2canonical)

#fewshot_en = json.load(file_en)

create_de2canonical()

#It is a famous fine garden with traditional opera performances at night.
#It is a famous fine garden with traditional opera performances at night.
#It is a famous fine garden with traditional opera performances at night.