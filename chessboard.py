position = input().strip()

column = ord(position[0]) - ord('a') + 1
row = int(position[1])

if (column + row) % 2 == 0:
    print("Black")
else:
    print("White")
