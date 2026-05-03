# parser_tani.py
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        instructions = []
        while self.pos < len(self.tokens):
            token_type, value = self.tokens[self.pos]

            if token_type == 'TANAM':
                self.pos += 1
                instructions.append(('PRINT', self.tokens[self.pos][1]))
            
            elif token_type == 'ID':
                var_name = value
                self.pos += 1
                if self.tokens[self.pos][0] == 'PUPUK':
                    self.pos += 1
                    instructions.append(('ASSIGN', var_name, self.tokens[self.pos][1]))
            
            elif token_type == 'PANEN':
                instructions.append(('EXIT', None))
            
            self.pos += 1
        return instructions
