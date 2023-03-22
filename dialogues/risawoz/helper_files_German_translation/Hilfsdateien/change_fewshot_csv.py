import csv
import ast
import string

"""
with open("fewshot_output3.csv", mode="r", encoding="utf-8") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter="\t")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            source_entities = row["source_entity"]
            target_entities = row["target_entity"]
            source_entities_puncs = []
            target_entities_puncs = []
            for i in range(len(source_entities) - 2):
                if ((source_entities[i] in string.punctuation) and source_entities[i] != "[") and (source_entities[i+1] == "'") and (source_entities[i+2] == "," or source_entities[i+2] == "]"):
                    source_entities_puncs += [i]
            for i in range(len(target_entities) - 2):
                if ((target_entities[i] in string.punctuation) and target_entities[i] != "[") and (target_entities[i+1] == "'") and (target_entities[i+2] == "," or target_entities[i+2] == "]"):
                    target_entities_puncs += [i]

            for r, i in enumerate(source_entities_puncs):
                i -= r
                source_entities = source_entities[:i] + source_entities[i+1:]

            for r, i in enumerate(target_entities_puncs):
                i -= r
                target_entities = target_entities[:i] + target_entities[i+1:]

            line_count += 1
            if line_count >= 50:
                break
"""
"""
source_entities = ast.literal_eval(row["source_entity"])
target_entities = ast.literal_eval(row["target_entity"])
assert len(source_entities) == len(target_entities)
for i in range(len(source_entities)):
    source_entity = source_entities[i]
    target_entity = target_entities[i]
    if source_entity[-1] in string.punctuation:
        source_entity = source_entity[:-1]
    if target_entity[-1] in string.punctuation:
        target_entity = source_entity[:-1]
    source_entities[i] = source_entity
    target_entities[i] = target_entity
"""

with open("fewshot_output3.csv", mode="r", encoding="utf-8") as csv_file:
    text = csv_file.read()
    text_puncs = []
    for i in range(len(text) - 2):
        if ((text[i] in string.punctuation) and text[i] != "[" and text[i] != "%") and (text[i+1] == "'") and (text[i+2] == "," or text[i+2] == "]"):
            text_puncs += [i]

    for r, i in enumerate(text_puncs):
        i -= r
        text = text[:i] + text[i+1:]
    with open("fewshot_output4.csv", mode="w", encoding="utf-8") as csv_file2:
        csv_file2.write(text)

"""
import pickle
import json

one_to_one_file = open("one_to_one_dict2", "rb")
one_to_one = pickle.load(one_to_one_file)
one_to_one_file.close()
alignment_file = open("alignment_dict", "rb")
alignment = pickle.load(alignment_file)
alignment_file.close()

csv_file = open("fewshot_output2.csv", mode="r", encoding="utf-8")
csv_reader = csv.DictReader(csv_file, delimiter="\t")
fewshot_csv = []
for row in csv_reader:
    fewshot_csv += [row]

file_en = open("en_fewshot.json", "r+", encoding="utf-8")

fewshot_en = json.load(file_en)

def string_to_list(list_represantation):
    list1 = ast.literal_eval(list_represantation)
    #list1 = [n.strip() for n in list1]
    return list1.copy()

def change_utterance(i, utterance_type):
    #if i + 2 == 4:
    #    print("kock")
    turn_csv = fewshot_csv[i]
    target = turn_csv["target"]
    source_word_span = string_to_list(turn_csv["source_word_span"])
    target_word_span = string_to_list(turn_csv["target_word_span"])
    num_entities_in_csv = len(source_word_span)
    num_entities_in_json = 0
    utterance = turn[utterance_type]
    utterance[0] = target
    for type in utterance[1]:
        entities = utterance[1][type]
        entities_keys = list(entities.keys()).copy()
        num_entities_in_json += len(entities_keys)
    if num_entities_in_csv != num_entities_in_json:
        print(i + 2, num_entities_in_json, num_entities_in_csv)
        return True
    return False

    

i = 0
count = 0
for dialogue in fewshot_en:
    #dialogue_alignment = dict()
    for turn in dialogue["dialogue"]:
        if change_utterance(i, "user_utterance"):
            count += 1
        i += 1
        if change_utterance(i, "system_utterance"):
            count += 1
        i += 1

print(count)
"""