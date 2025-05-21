import re

class MyString:
    def __init__(self, value=''):
        self._value = ''
        self.value = value  # use the setter for type checking

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        sentences = re.split(r'[.!?]+', self.value)
        valid_sentences = [s.strip() for s in sentences if s.strip()]
        return len(valid_sentences)
