questions = []


answers = []



res = []

#####

print("Вас вітає експертна система класифікації жанрів комп’ютерних ігор !")
print("Виконав Федоров Максим КНМС-11")
print("\nВибирайте відповіді ввівши номер варіанту\т")

#####

print(
"""
Який жанр комп'ютерних ігор вам бльше подобається?
1. Бойовики
2. Рольові
3. Стратегії
4. Пригоди
5. Симулятори
"""
)

chk = True
while chk:
    try:
        inp = int(input())
        if not inp in range(1, 7):
            print("Введіть номер варіанту")
        else:
            chk = False
    except ValueError:
        print("Введіть номер варіанту")

res.append(inp)

chk = True
while chk:
    try:
        inp = int(input())
        if not inp in range(1, 7):
            print("Введіть номер варіанту")
        else:
            chk = False
    except ValueError:
        print("Введіть номер варіанту")

