size = int(input())
cars_number = input()
matrix = []
car_positcion = [0, 0]
km = 0
flag = False

direction = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for i in range(size):
    line = input().split()
    matrix.append(line)


while True:
    commands = input()
    if commands == "End":
        row, col = car_positcion[0], car_positcion[1]
        matrix[row][col] = "C"
        break

    row, col = direction[commands][0] + car_positcion[0], direction[commands][1] + car_positcion[1]
    car_positcion = row, col

    if matrix[row][col] == ".":
        km += 10
    elif matrix[row][col] == "T":
        km += 30
        matrix[row][col] = "."
        for r in range(size):
            if "T" in matrix[r]:
                row, col = r, matrix[r].index("T")
                matrix[row][col] = "."
                car_positcion = row, col
                break
    elif matrix[row][col] == "F":
        flag = True
        km += 10
        matrix[row][col] = "C"
        break

if flag:
    print(f"Racing car {cars_number} finished the stage!")
else:
    print(f"Racing car {cars_number} DNF.")

print(f"Distance covered {km} km.")

for i in range(size):
    print(''.join(matrix[i]))