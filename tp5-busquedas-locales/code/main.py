import board as Board

# Creacion de n tableros con n reinas
tableros = []
queens = 8
for i in range(queens):
    board = Board.Board(queens)
    tableros.append(board)

tableros = sorted(tableros, key=lambda board: board.value, reverse=True)

for i in range(0,tableros.__sizeof__(),2):
    tableros[i].crossJoin(tableros[i+1])


# for i in range(queens):
#     print(tableros[i].value,end=", ")

