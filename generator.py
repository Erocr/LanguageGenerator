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


def sub_frequency(sub, frequency):
    s = 0
    for elt in sub:
        s += frequency[elt]
    s = 100 / s
    res = {}
    for elt in sub:
        res[elt] = frequency[elt] * s
    return res


def rand_choose(sounds, frequency):
    i = random.random() * 100
    for sound in sounds:
        i -= frequency[sound]
        if i <= 0:
            return sound


def generate_sounds(vowels, frequency, size):
    res = []
    *sounds, = frequency.keys()
    nbCons = 1
    nbVoy = 1
    prev = None
    for i in range(size):
        s = sounds.copy()
        if prev is not None:
            s.remove(prev)
        n = rand_choose(s, frequency)
        while (nbVoy == 2 and n in vowels) or (nbCons == 2 and n not in vowels):
            n = rand_choose(s, frequency)
        if n in vowels:
            nbCons = 0
            nbVoy += 1
        else:
            nbCons += 1
            nbVoy = 0
        prev = n
        res.append(n)
    return res


vowels, frequency, rules = read("config.json")
print(generate_sounds(vowels, frequency, 8))

