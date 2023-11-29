for i in range(9):
    for j in range(i + 1, 10):
        if i < j and i != 8:
            print(f"{i}{j}", end=", ")
print(f"{8}{9}")
