import sounds2text as translator
import sounds_generator as generator


def generate_word(size, language):
    phonemes, frequencies = generator.read(language)
    rules = translator.read(language+"/rules.json")
    sounds = generator.generate(size, phonemes, frequencies)
    print(sounds)
    return translator.to_text(sounds, rules)


print(generate_word(7, "french"))