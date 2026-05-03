# tani.py (Versi Modular)
import sys
from lexer import Lexer
from parser_tani import Parser

class Interpreter:
    def __init__(self):
        self.gudang = {}

    def run(self, instructions):
        for inst in instructions:
            action = inst[0]
            
            if action == 'PRINT':
                val = inst[1].strip('"\'')
                print(self.gudang.get(val, val))
                
            elif action == 'ASSIGN':
                self.gudang[inst[1]] = inst[2].strip('"\'')
                
            elif action == 'EXIT':
                print("--- Musim Tanam Berakhir ---")
                break

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Gunakan: python tani.py file.tani")
    else:
        with open(sys.argv[1], 'r') as f:
            code = f.read()
        
        # Proses 1: Lexing
        lexer = Lexer(code)
        tokens = lexer.tokenize()
        
        # Proses 2: Parsing
        parser = Parser(tokens)
        ast = parser.parse()
        
        # Proses 3: Executing
        interp = Interpreter()
        interp.run(ast)
