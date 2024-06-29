import json
from random import random


def read(language_name):
    f1 = open(language_name+"/phonemes.json", "r")
    f2 = open(language_name+"/frequences.json", "r")
    phonemes_list, frequencies = json.load(f1), json.load(f2)
    f1.close()
    f2.close()
    phonemes = {}
    for i in range(len(phonemes_list)):
        phonemes[phonemes_list[i]] = i
    return phonemes, frequencies


def rand_choice(frequence):
    """ Renvoie l'index de la lettre choisie """
    a = random()*100
    for i in range(len(frequence)):
        a -= frequence[i]
        if a < 0:
            return i


def generate(size, phonemes, frequencies):
    res = ''
    phonemes_list = list(phonemes.keys())
    for i in range(size):
        if i == 0:
            frequence = frequencies[0]
        else:
            frequence = frequencies[phonemes[res[-1]]+1]
        choice = rand_choice(frequence)
        if choice is None:
            return res
        res += phonemes_list[choice]
    return res


phonemes, frequencies = read("french")
print(generate(10, phonemes, frequencies))
