import random

print("Добро пожаловать в игру камень, ножницы, бумага!")


print("Чтобы выбрать камень напишите К")
print("Чтобы выбрать ножницы напишите Н")
print("Чтобы выбрать бумагу напишите Б")



wins = 0
defeat = 0

def total_score():
    print("Побед", wins)
    print("Поражений", defeat)



while True:


    your_choice = input("Ваш ход: ").upper()

    enemy_choice = random.choice(["К", "Н", "Б"])




    if your_choice == enemy_choice:
        print("Противник выбрал тоже что и вы, ничья!")
        total_score()



    elif your_choice == "К":
        if enemy_choice == "Н":
            print("Противник выбрал ножницы, камень бьёт ножницы, победа!")
            wins += 1
            total_score()



        elif enemy_choice == "Б":
            print("Противник выбрал бумагу, бумага побеждает камень, поражение!")
            defeat += 1
            total_score()



    elif your_choice == "Н":
        if enemy_choice == "К":
            print("Противник выбрал камень, камень бьёт ножницы, поражение!")
            defeat += 1
            total_score()



        elif enemy_choice == "Б":
            print("Противник выбрал бумагу, ножницы режут бумагу, победа!")
            wins += 1
            total_score()



    elif your_choice == "Б":
        if enemy_choice == "Н":
            print("Противник выбрал ножницы, ножницы режут бумагу, поражение!")
            defeat += 1
            total_score()



        elif enemy_choice == "К":
            print("Противник выбрал камень, бумага побеждает камень, победа!")
            wins += 1
            total_score()


    else:
        print("Введите букву соответствующую предмету")