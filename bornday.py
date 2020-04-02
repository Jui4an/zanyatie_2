pushkin_yob = int(input("введите год рождения А.С. Пушкина? в формате гггг - "))
if pushkin_yob == 1799:
    pushkin_dob = int(input("введите день рождения А.С. Пушкина? - "))
    if pushkin_dob == 6:
        print("верно")
    else:
        print("неверный день рождения.")
else:
    print("неверный год рождения.")