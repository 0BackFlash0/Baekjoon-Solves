import sys
input = sys.stdin.readline

class sudoku_group:
    

sudoku = []
groups = {"row" : [], "col" : [], "sq" : []}

for _ in range(9):
    sudoku.append( list(map(int, input().split())) )