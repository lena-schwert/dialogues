# README

## Welche Dateien machen was

• fewshot_output.csv enthält die Übersetzungen. Die Datei entsteht wenn man das translation tool benutzt.

• de_fewshot_original.json ist das Dataset

• de_fewshot.json ist das Dataset, in einem Format was dann für’s Preprocessing benutzt werden kann.

• en2canonical.json ist ein many-to-one mapping von verschiedenen deutschen Wörtern alle mit der selben Übersetzung zu einem deutschen Wort. Wenn man das Tool zur Erstellung des Datasets benutzt muss man die eigentliche en2canonical.json Datei durch diese Datei ersetzen.

• db_en ist die Database auf deutsch (Wurde automatisch übersetzt, wodurch manche Sachen komisch klingen)

• Hilfsdatein enthält Skripte die ich benutzt habe um die Datei zu erstellen

    ◦ annotation.py ist das Annotationstool so angepasst, dass Automatisch übersetzungen angezeigt werden
    
    ◦ one_to_one_dict ist eine pickle Datei, die in einem Dictionary fast alle Übersetzungen von Englischen slot_values, etc. enthält

## Tips

• Bei Windows muss man für deren Tool das Deufault encoding auf utf-8 stellen

• Oft wenn man in deren Tool etwas verändert um Errors zu fixen, muss man dann nochmal „pip install .“ eingeben

## Was noch fehlt

• Das Preprocessing von der de_fewshot.json Datei

• Bei Suchanfragen, von Autos mit einer Anzahl an Sitzen sollen eigentlich alle Autos die mehr (oder gleich viele) Sitze haben, gefunden werden. Das habe ich aber nicht ganz hinbekommen. Also wenn man sagt man fährt nur alleine Auto, dann werden Autos mit 5 Sitzen aber nicht mit 7 Sitzen angezeigt.
