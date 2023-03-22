import csv
import ast
import pickle

alignment = dict()

with open("fewshot_output2.csv", mode="r", encoding="utf-8") as csv_file:
    csv_reader = csv.DictReader(csv_file, delimiter="\t")
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            source_entities = ast.literal_eval(row["source_entity"])
            target_entities = ast.literal_eval(row["target_entity"])
            assert len(source_entities) == len(target_entities)
            for i in range(len(source_entities)):
                source_entity = source_entities[i]
                target_entity = target_entities[i]
                if source_entity not in alignment:
                    alignment[source_entity] = {target_entity}
                else:
                    alignment[source_entity].add(target_entity)
            line_count += 1
            #if line_count >= 100:
            #    break

alignment_file = open("alignment_dict", "wb")
pickle.dump(alignment, alignment_file)
alignment_file.close()

 