# year of birth
pushkin_yob = int(input("введите год рождения А.С. Пушкина? в формате гггг - "))
while pushkin_yob != 1799:
    print("Попробуйте еще раз")
    pushkin_yob = int(input("введите год рождения А.С. Пушкина? в формате гггг - "))
# day of birth
pushkin_dob = input("введите день рождения А.С. Пушкина? в формате дд - ")
while pushkin_dob != "06":
    pushkin_dob = input("попробуйте еще раз, ввести день рождения А.С. Пушкина? в формате дд - ")
print("верно")
