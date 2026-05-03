# lexer.py
import re

class Lexer:
    def __init__(self, code):
        self.code = code
        self.tokens = []

    def tokenize(self):
        # Pola untuk perintah TANI
        token_specification = [
            ('PANEN',   r'PANEN'),           # Selesai
            ('TANAM',   r'TANAM'),           # Print
            ('PUPUK',   r'PUPUK'),           # Assignment
            ('STRING',  r'"[^"]*"|\'[^\']*\''), # Teks
            ('ID',      r'[a-zA-Z_][a-zA-Z0-9_]*'), # Nama variabel
            ('NEWLINE', r'\n'),              # Baris baru
            ('SKIP',    r'[ \t]+'),          # Spasi/Tab
            ('MISMATCH',r'.'),               # Karakter ilegal
        ]
        
        tok_regex = '|'.join('(?P<%s>%s)' % pair for pair in token_specification)
        for mo in re.finditer(tok_regex, self.code):
            kind = mo.lastgroup
            value = mo.group()
            if kind == 'NEWLINE' or kind == 'SKIP':
                continue
            elif kind == 'MISMATCH':
                raise RuntimeError(f'Hama terdeteksi: {value!r}')
            self.tokens.append((kind, value))
        return self.tokens
