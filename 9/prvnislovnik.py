# ja = {"jmeno": "Rezi", "vek": 29, "mesto": "Praha", "cisla": [3, 7, 9]}
# print(ja["mesto"])
# print(ja)
# ja["jazyk"] = "python"
# print(ja)
# del ja["vek"]
# print(ja)

barvy = {
"hruska" : "zelena",
"jablko" : "cervena",
"Pipi": "zluta",
"mrkev": "oranzova",
"lilek": "fialova",
"boruvka": "modra"
}

for klic in barvy:
    print(klic)

print()

for hodnota in barvy.values():
    print(hodnota)

print()

for klic, hodnota in barvy.items():
    print("{}: {}".format(klic, hodnota))

print()

barvy_po_tydnu = dict(barvy)
for klic in barvy_po_tydnu:
    barvy_po_tydnu[klic] = 'černo-hnědo-' + barvy_po_tydnu[klic]
print(barvy_po_tydnu)

print(barvy['jablko'])

data = [(1, "jedna"), (2, "dva"), (3, "tri")]
nazvycisel = dict(data)
print(nazvycisel)

import json

json_retezec = """
    {
      "jméno": "Anna",
      "město": "Brno",
      "jazyky": ["čeština", "angličtina", "Python"],
      "věk": 26
    }
"""

data = json.loads(json_retezec)
print(data)
print(data['město'])

print(json.dumps(data))
print(json.dumps(data, ensure_ascii=False, indent=2))
