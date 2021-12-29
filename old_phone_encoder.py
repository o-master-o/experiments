class OldPhone(object):

    def __init__(self):
        self.collector = []
        self.keyboard = {'1': '.,?!', '2': 'abc', '3': 'def',
                         '4': 'ghi', '5': 'jkl', '6': 'mno',
                         '7': 'pqrs', '8': 'tuv', '9': 'wxyz',
                         '*': '\'-+=', '0': ' ', '#': '#'}
        self._previous_key = None
        self._previous_char = 'a'
        self._hold_key_char = '-'
        self._wait_char = ' '

    def send_message(self, message):
        for char in message:
            self._encode_char(char)
        return self._merge_result()

    def _encode_char(self, char):
        key, key_symbols = self._find_key(char)
        self._encode(char, key, key_symbols)
        self._previous_key = key
        if char.isalpha():
            self._previous_char = char

    def _find_key(self, char):
        for key, key_symbols in self.keyboard.items():
            if char in key or char.lower() in key_symbols:
                return key, key_symbols

    def _encode(self, char, key, key_symbols):
        self._encode_top_row_symbol(char, key)
        self._encode_bottom_row(char, key, key_symbols)

    def _encode_top_row_symbol(self, char, key):
        if char == key:
            self._same_key_repeat_checker(key)
            self.collector.append(char)
            self.collector.append(self._hold_key_char)

    def _encode_bottom_row(self, char, key, key_symbols):
        if char.lower() in key_symbols and char != '#':
            self._encode_case_toggle(char)
            self._same_key_repeat_checker(key)
            self._encode_alpha_char(char, key, key_symbols)

    def _encode_case_toggle(self, char):
        if char.isalpha() and self._char_case_is_different_than_previous_alpha_char(char):
            self.collector.append('#')

    def _char_case_is_different_than_previous_alpha_char(self, char):
        return char.isupper() != self._previous_char.isupper()

    def _same_key_repeat_checker(self, key):
        if self._previous_key == key and self.collector[-1] not in '#-':
            self.collector.append(self._wait_char)

    def _encode_alpha_char(self, char, key, key_symbols):
        index = key_symbols.find(char.lower()) + 1
        repeated_key = str(key) * index
        self.collector.append(repeated_key)

    def _merge_result(self):
        return ''.join(self.collector)


def send_message(message):
    return OldPhone().send_message(message)
