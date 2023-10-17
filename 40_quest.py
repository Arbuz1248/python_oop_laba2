import re

class Text:
    def __init__(self, text):
        self.text = text

    def get_character_count(self):
        return len(self.text)

    def get_letter_count(self):
        letters = re.findall(r'[a-zA-Z]', self.text)
        return len(letters)

    def get_space_count(self):
        spaces = self.text.count(' ')
        return spaces

    def get_character_count_without_spaces(self):
        text_without_spaces = self.text.replace(' ', '')
        return len(text_without_spaces)

    def get_word_array(self):
        words = self.text.split()
        return words

    def get_sentence_array(self):

        sentences = re.split(r'(?<=[.!?])\s', self.text)
        return sentences

# Пример использования:

text = "Текст для задания!"
text_analyzer = Text(text)

print("Количество символов в тексте:", text_analyzer.get_character_count())
print("Количество букв в тексте:", text_analyzer.get_letter_count())
print("Количество пробелов в тексте:", text_analyzer.get_space_count())
print("Количество символов в тексте без пробелов:", text_analyzer.get_character_count_without_spaces())
print("Массив слов в тексте:", text_analyzer.get_word_array())
print("Массив предложений в тексте:", text_analyzer.get_sentence_array())