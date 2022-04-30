# Реализовать алгоритм задания случайных чисел. 
# Без использования встроенного генератора псевдослучайных чисел

st = set()

for i in range(10):
    st.add(str(i))
print(st)
for i in st:
    print(int(i))
    break