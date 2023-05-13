import questions

#####

def cin(maximal):
    chk = True
    while chk:
        try:
            inp = int(input())
            if not inp in range(1, maximal):
                print("Введіть номер варіанту")
            else:
                chk = False
        except ValueError:
            print("Введіть номер варіанту")

    res.append(inp)

#####

print("Вас вітає експертна система класифікації жанрів комп’ютерних ігор !")
print("Виконав Федоров Максим КНМС-11")
print("\nВибирайте відповіді ввівши номер варіанту\т")

#####

res = []

# Головне питання

print(
"""
Який жанр комп'ютерних ігор вам бльше подобається?

1. Бойовики
2. Рольові
3. Стратегії
4. Пригоди
5. Симулятори
6. Спорт і перегони
"""
)

cin(7)

# Перше питання

print(questions.first_questions[res[0] * 2 - 2])

cin(questions.first_questions[res[0] * 2 - 1] + 1)

# Друге питання

print("\nВиберіть варіант, який вам більше подобається")

print(questions.second_questions[res[0] - 1][res[1] * 2 - 2])

cin(questions.second_questions[res[0] - 1][res[1] * 2 - 1] + 1)

print("\nНа основі ваших відповідей найкращою грою для вас буде " 
      + questions.answers[res[0] - 1][res[1] - 1][res[2] - 1] + 
      "\n\nЯкщо вам не сподобалася запропонована гра, ось посилання на сайт з подібними іграми: "
      + questions.links[res[0] - 1][res[1] - 1])
