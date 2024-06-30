import os
import json


def read(file_name):
    file = open(file_name, "r", encoding="utf-8")
    res = file.readlines()
    file.close()
    for i in range(len(res)):
        res[i] = res[i].split("/")[1]
    return res


def generate_infos(language_name, file_name):
    """

    :param language_name: the name of the folder that will be created
    :param file_name: the name of the file with the list of the phonemes in the chosen language. Each line has to be in
    format: words /phoneme/

    It creates a folder with few files in it:
    - A file with the list of the phonemes in the language
    - A file with a bidimensional matrix describing for each phoneme, the frequency to be after another phoneme. The
    first line is the frequency of being first
    """
    if not os.path.exists(language_name):
        os.makedirs(language_name)
    phonemes = read(file_name)
    phonemes_idx = {}
    phonemes_freq = [[]]
    max_idx = 0
    for phoneme in phonemes:
        for i in range(len(phoneme)):
            if phoneme[i] not in phonemes_idx:
                phonemes_idx[phoneme[i]] = max_idx
                max_idx += 1
                for j in range(len(phonemes_freq)):
                    phonemes_freq[j].append(0)
                phonemes_freq.append([0] * max_idx)
            if i == 0:
                phonemes_freq[0][phonemes_idx[phoneme[i]]] += 1
            else:
                phonemes_freq[phonemes_idx[phoneme[i-1]]+1][phonemes_idx[phoneme[i]]] += 1

    for line in phonemes_freq:
        s = sum(line) / 100
        if s > 0:
            for i in range(len(line)):
                line[i] /= s

    file_phoneme_list = open(language_name+"/phonemes.json", "w")
    json.dump(list(phonemes_idx.keys()), file_phoneme_list)
    file_phoneme_list.close()

    file_phonemes_freq = open(language_name + "/frequences.json", "w")
    json.dump(phonemes_freq, file_phonemes_freq)
    file_phonemes_freq.close()


if __name__ == "__main__":
    generate_infos("french", "french/phonemes_fr.txt")
    print("done")
