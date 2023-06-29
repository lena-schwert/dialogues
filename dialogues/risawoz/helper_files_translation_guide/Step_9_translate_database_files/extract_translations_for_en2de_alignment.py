
import os
import json

src_db_path = "/home/lena/git/dialogues/dialogues/risawoz/database/db_en"
tgt_db_path = "/home/lena/git/dialogues/dialogues/risawoz/helper_files_translation_guide/Step_9_translate_database_files/original_version_by_Jim"

value_alignment_path = "/home/lena/git/dialogues/dialogues/risawoz/helper_files_translation_guide/Step_8_build_two_alignment_files/output_path/en2de_alignment.json"

src_lang = "en"
tgt_lang = "de"

domain = "attraction"
#     "train",
#     "pc",
#     "movie",
#     "class",
#     "car",
#     "restaurant",
#     "hotel",
#     "attraction",
#     "flight",
#     "hospital",
#     "tv",
# ]

domain_category = 'features'

# load database files

with open(f"{value_alignment_path}") as f:
    value_alignment = json.load(f)

with open(f"{src_db_path}/{domain}_{src_lang}.json", "r") as f:
    src_db = json.load(f)
    print(f"Load {len(src_db)} items in {domain} domain from {src_lang} database")

with open(f"{tgt_db_path}/{domain}_{tgt_lang}.json", "r") as f:
    tgt_db = json.load(f)
    print(f"Load {len(tgt_db)} items in {domain} domain from {tgt_lang} database")

# get all the english slot values for the English source database
slot_values_en = [entry[domain_category] for entry in src_db]
# do the same for the German version
slot_values_de = [entry[domain_category] for entry in tgt_db]

# prepare the JSON format by using a dict
slot_values_en_de_dict = {i: j for i, j in zip(slot_values_en, slot_values_de)}

# output format: print it to a json file
with open(f"/home/lena/git/dialogues/dialogues/risawoz/helper_files_translation_guide/Step_9_translate_database_files/extract_translations/{domain}_{domain_category}.json", "w",
          encoding = 'utf8') as f:
    json.dump(slot_values_en_de_dict, f, ensure_ascii = False, indent = 4)
