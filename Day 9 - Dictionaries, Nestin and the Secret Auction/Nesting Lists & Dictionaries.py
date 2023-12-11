capitals = {
    "Israel": ["Rehovot", "Tel Aviv", "Jerusalem"],
    "Mexico": ["Mexico city", "Taco city"]
}
# It is also possible to create a dictionary containing lists

english_dictionary = {
    "Ball": "A circular object",
    "Ladder": "A thingy you climb",
    "Stairs": "A thingy you climb",
}
hebrew_dictionary = {
    "שולחן": "משהו ששמים עליו דברים",
    "אמור": "שם של דג",
}

dictionary = {
    "Hebrew": hebrew_dictionary,
    "English": english_dictionary,
}
# It's possible to create a nested dictionary - A dictionary containing dictionaries

dictionary = {
    "English dictionary": {"Nouns": "Table", "Adjectives": "Pretty", "Misc": {"Slang": "Bussing", "Punctuation": "[]"}}
}
dict_list = [dictionary, capitals]
# It's even possible to create a list made up of dictionaries
