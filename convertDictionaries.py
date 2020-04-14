semanticClass = {
    "epistemiczny" : 1,
    "mówienia" : 2,
    "odkrycia" : 3,
    "emotywny" : 4,
    "przyczynowy" : 5,
    "percepcyjny" : 6,
    "pamięciowy" : 7,
    "wnioskowania" : 8,
    "?" : 9,
    "dowodzenia" : 10,
    "zdarzeniowy" : 11,
    "liczenia" : 12,
    "czynnościowy" : 13,
    "wolicjonalny" : 14,
    "nie-wiedzowy" : 15,
    "wolitywny" : 16,
    "performatyw" : 17
}

verbTense = {
    "past" : 1,
    "present" : 2,
    "future" : 3
}

verbVeridical = {
    "\"+\"" : 1,
    "\"-\"" : 2,
    "o" : 3,
    "?" : 4
}

def convertData(element, dictionary):
    if element in dictionary:
        return dictionary[element]
    else:
        return 0 