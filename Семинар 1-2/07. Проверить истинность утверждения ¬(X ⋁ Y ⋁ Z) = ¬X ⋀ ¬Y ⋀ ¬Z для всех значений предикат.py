# Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат

for i in range (0, 2):
    x=i
    for j in range (0, 2): 
        y=j
        for k in range (0, 2):
            z=k
            print(f'{x} {y} {z}', end = ' ')
            a = not (x or y or z)
            b = (not x) and (not y) and (not z)
            if a == b:
                print(True)
            else:
                print(False)
