import json
import random


def read(file_name):
    file = open(file_name, "r")
    res = json.load(file)
    file.close()
    rules = res["regles"]
    res.pop("regles")
    frequency = {}
    vowels = set()
    for key in res:
        if res[key][1]:
            vowels.add(key)
        frequency[key] = res[key][0]
        for e in res[key][2]:
            rules[e] = key
    return vowels, frequency, rules


def generate_sounds(vowels, frequency, size):
    res = []
    *sounds, = frequency.keys()
    *v, = vowels
    nbCons = 0
    for i in range(size):
        if nbCons == 2:
            nbCons = 0
            res.append(random.choice(v))
            continue
        n = random.choice(sounds)
        if n in vowels:
            nbCons = 0
        else:
            nbCons += 1
        res.append(n)
    return res



vowels, frequency, rules = read("config.json")
print(vowels)
print(frequency)
print(rules)
print(generate_sounds(vowels, frequency, 4))

