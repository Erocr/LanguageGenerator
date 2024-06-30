import json
import random


def read(rules_name):
    file = open(rules_name, "r", encoding="utf-8")
    rules = json.load(file)
    file.close()
    return rules


def retro_problems(word, rules, nb_letters_added):
    for l2 in rules:
        if len(l2) > nb_letters_added:
            for i in range(nb_letters_added):
                if word[max(len(word) - len(l2) - i, 0):len(word)] == l2:
                    return True
    return False


def to_text(sounds, rules, word=" "):
    if len(sounds) == 0:
        if not retro_problems(word+" ", rules, 1):
            return word[1:]
        return None
    possibilities = []
    for letters in rules:
        if rules[letters] == sounds[:len(rules[letters])] and not retro_problems(word+letters, rules, len(letters)):
            possibilities.append(letters)
    possibilities.sort(key=lambda p:len(p)-len(rules[p]))
    for possibility in possibilities:
        res = to_text(sounds[len(rules[possibility]):], rules, word+possibility)
        if res is not None:
            return res


if __name__ == "__main__":
    rules = read("french/rules.json")
    print(to_text("saly", rules), "salu")
    print(to_text("twa", rules), "None")
    print(to_text("kat", rules), "cat/kat")
