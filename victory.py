# year of birth Лермонтова 1814
pravilny_otvet = 0
nepravilny_otvet = 0

lermontov_yob = int(input("введите год рождения М.Ю. Лермонтова в формате гггг - "))
if lermontov_yob == 1814:
    pravilny_otvet += 1
else:
    nepravilny_otvet += 1
# year of birth Северянина 1887
severyanin_yob = int(input("введите год рождения И.В.Северянина в формате гггг - "))
if severyanin_yob == 1887:
    pravilny_otvet += 1
else:
    nepravilny_otvet += 1
# year of birth Хармса 1905
harms_yob = int(input("введите год рождения Д.И. Хармса в формате гггг - "))
if harms_yob == 1905:
    pravilny_otvet += 1
else:
    nepravilny_otvet += 1
# year of birth Вангога 1853
vangog_yob = int(input("введите год рождения Винсента ван Гога в формате гггг - "))
if vangog_yob == 1853:
    pravilny_otvet += 1
else:
    nepravilny_otvet += 1
# year of birth Лотрека 1864
tuluz_yob = int(input("введите год рождения Анри де Тулуз Лотрека в формате гггг -  "))
if tuluz_yob == 1864:
    pravilny_otvet += 1
else:
    nepravilny_otvet += 1
print(pravilny_otvet, "- количество правильных ответов")
print(nepravilny_otvet, "- количество ошибок")
print(pravilny_otvet * 100 / 5, " - процент правильных ответов")
print(nepravilny_otvet * 100 / 5, " - процент неправильных ответов")
