#Бункер

# Фобии готовы
# Профессии готовы
# Болезни готовы
# хобби готовы
# доп инфа готова
# биология готова
# качества готовы

import random
profession_arr = ["Продавец", "Учитель истории", "Актер", "Переводчик", "Ландшафтный дизайнер", "Телеведущий", "Философ", "Физик-ядерщик", "Музыкант", "Вирусолог", "Дизайнер", "Видеоинженер", "Участник реалити-шоу", "Повар", "Строитель", "Тату-мастер", "Юрист", "Психолог", "Стоматолог", "Картограф", "Экстрасенс", "Химик", "Журналист", "Агроном", "Судья", "Военный летчик", "Инструктор по выживанию", "Электрик", "Экскурсовод", "Маркетолог", "Физик", "Военный", " Автомеханик", "Эколог", "Хирург", "Модель", "Фармацевт", "Разносчик пиццы", "Биолог", "Пожарный", "Полицейский", "Сексолог", "Блогер", "Геолог", "Бизнесмен", "Фотограф", "Вор", "Зоолог", "Специалист мировой экономики", "Писатель"]
phobia_arr = ["Фазмофобия - боязнь призраков и духов", "Нет фобий", "Клаустрофобия", "Нет фобий", "Паразитофобия - боязнь насекомых-паразитов", "Киберофобия - боязнь компьютеров", "Герпетофобия - боязнь рептилий, пресмыкающихся, змей", "Топофобия - боязнь остаться одному в помещении", "Канинофобия - боязнь собак", "Фазмофобия - боязнь призраков и духов","Гоплофобия - боязнь оружия", "Коулрофобия - боязнь клоунов", "Мусофобия - боязнь мышей и крыс", "Нет фобии", "Нет фобии", "Нет фобии","Клаустрофобия", "Аквафобия - боязнь воды, утопления", "Орнитофобия - боязнь птиц и их перьев", "Турофобия - боязнь сыра", "Библиофобия - боязнь библиотек", "Зоофобия - боязнь животных", "Демонофобия - боязнь дьявола, демонов и другой нечистой силы", "Гоплофобия - боязнь оружия", "Нет фобии", "Нет фобии", "Аулофобия - боязнь флейты", "Тетрафобия - боязнь числа 4", "Акрофобия - боязнь высоты", "Арахнофобия - боязнь пауков"]
health_arr = ["Мигрень", "Ожирение", "Вич инфицирован, 1 стадия(осталось жить 5 лет)", "Носитель генетической болезни", "Глухонемой", "Идеально здоров", "Рак легких(осталось жить 3 года)", "Идеально здоров", "Носитель генетической болезни", "Алкоголизм", "Дефект речи", "Анорексия", "Идеально здоров", "Зависимость от наркотических веществ", "Диабет", "Дальтоник", "Идеально здоров", "Бесплодие", "Бесплодие", "Бесплодие", "Идеально здоров", "Псориаз", "Идеально здоров", "Дальтоник", "Бесплодие", "Идеально здоров", "Дефект речи", "Аллергическая астма", "Аллергия на солнечный свет", "Гемофилия (несворачиваемость крови)"]
other_information_arr = ["Верит в экстрасенсов", "Объездил весь мир", "Владеет языком жестов", "5 раз читал 'Гарри Поттера'", "Знает азбуку морзе", "Рос в семье фермеров", "Читал все книги про зомби", "Рос в семье геологов", "Мастер спорта по боксу", "Умеет ориентироваться по звездам", "По первому образованию химик", "Знает все стихи Пушкина наизусть", "Подрабатывает в театре", "Знал лично президента", "Учился в мед.университете 4 года", "Имеет экстрасенсорные способности", "Изучал воду и ее очищение", "Имеет звание Почетный волонтер", "По первому образованию биолог", "Знает все про компьютеры", "Знает, где склад с оружием", "Верит в инопланетян", "Занимается белой магией", "Может сделать алкоголь из чего угодно", "Состоит в клубе 'Навыки выживания' 3 года", "Умеет делать луки и копья", "Знает 5 языков", "Подрабатывал в больнице", "Остался в живых на необитаемом острове", "Архитектор по первому образованию", "Проходил курсы психолога", "Выиграл миллион, вечный везунчик"]
biology_arr = ["Мужчина, 25 лет", "Мужчина, 45 лет", "Мужчина, 50 лет", "Мужчина, 30 лет, бисексуален", "Женщина, 40 лет, гомосексуальна", "Женщина, 50 лет", "Женщина, 30 лет, бисексуальна", "Мужчина, 25 лет", "Женщина, 25 лет", "Женщина, 45 лет", "Женщина, 31 год, бисексуальна", "Мужчина, 60 лет", "Женщина, 40 лет, гомосексуальна", "Женщина, 18 лет", "Женщина, 21 год", "Женщина, 60 лет", "Женщина, 20 лет", "Мужчина, 30 лет", "Мужчина, 40 лет, гомосексуален", "Женщина, 40 лет, гомосексуальна", "Мужчина, 30 лет, бисексуален", "Мужчина, 50 лет", "Мужчина, 20 лет, гомосексуален", "Мужчина, 35 лет, гомосексуален", "Женщина, 35 лет, гомосексуальна", "Женщина, 30 лет, бисексуальна", "Женщина, 25 лет", "Мужчина, 19 лет", "Мужчина 17 лет", "Женщина, 17 лет", "Женщина, 24 года", "Женщина, 50 лет"]
characteristic_arr = ["Настырный", "Эгоистичный", "Целеустремленный", "Хитрый", "Раздражительный", "Безотказный", "Честный", "Хитрый", "Храбрый", "Буйный", "Самовлюбленный", "Требовательный", "Болтливый", "Компанейский", "Депрессивный", "Буйный", "Эгоистичный", "Общительный", "Отважный", "Веселый", "Подлый", "Конфликтный", "Замкнутый", "Креативный", "Надежный", "Безжалостный", "Добрый", "Лживый", "Конфликтный", "Истеричный"]
special_conditions_arr = ["СМЕНА КАРТ - Данная карта дает возможность перераздать у всех игроков(включая тебя) карточки 'Профессия'", "СМЕНА КАРТ - данная карта дает тебе возможность перераздать у всех игроков(включая себя) карточки 'биологическая характеристика'", "Количество мест в бункере меньше на 1", "ОКРУЖЕНИЕ - Возле вас находится бункер, в котором одни женщины (здоровые, возраст до 30 лет)", "ГОЛОСОВАНИЕ - Данная карта дает возможность аннулировать один голос против тебя", "ОКРУЖЕНИЕ - В 30 метрах от вас склад с оружием", "СМЕНА КАРТ - Ты можешь поменять свою карту 'Дополнительная информация' на новую из колоды", "СМЕНА КАРТ - Данная карта лечит тебя от бесплодия", "СМЕНА КАРТ - Ты можешь поменять свою карту 'Профессия' на новую из колоды", "ГОЛОСОВАНИЕ - Данная карта дает тебе возможность возвратить выбывшего игрока в игру", "СМЕНА КАРТ - Данная карта дает возможность вылечить тебя от любого недуга, теперь ты абсолютно здоров", "СМЕНА КАРТ - Ты можешь поменять свою карту 'Состояние здоровья' на новую из колоды", "ИММУНИТЕТ - У тебя есть защита на один игровой круг, если против твоего персонажа максимальное количество голосов.", "Количество мест в бункере меньше на 1", "СМЕНА КАРТ - Ты можешь поменять свою карту 'Биологическая характеристика' на новую из колоды", "Открытие карт - Данная карта дает тебе возможность открыть карту 'Состояние здоровья' у любого игрока на выбор", "СМЕНА КАРТ - Ты можешь поменять свою карту 'Фобия' на новую из колоды", "СМЕНА КАРТ - Данная карта дает возможность вылечить твою фобию", "ИММУНИТЕТ - У тебя есть защита на один игровой круг другого игрока, ты не можешь защитить себя.", "СМЕНА КАРТ - Данная карта дает тебе возможность поменяться картой 'Здоровье' с человеком справа.", "ОКРУЖЕНИЕ - Бункер находится на территории парка с аттракционами (разрушение парка 20%).", "ОКРУЖЕНИЕ - Рядом с вами второй бункер, где находятся два строителя.", "СМЕНА КАРТ - Данная карта дает возможность тебе поменяться картой 'Факт' с человеком справа.", "ОКРУЖЕНИЕ - В 20 метрах от вашего бункера сохранился погреб с вином.", "ГОЛОСОВАНИЕ - Данная карта дает тебе возможность самому выбрать, кто покинет игровой круг без голосования.", "СМЕНА КАРТ - Все игроки меняются картами 'Профессия' по часовой стрелке.", "ГОЛОСОВАНИЕ - Данная карта дает тебе возможность возвратить любого выбывшего игрока в игру.", "ОКРУЖЕНИЕ - Рядом с вами второй бункер, где находятся два медицинский сотрудника.", "СМЕНА КАРТ - Данная карта дает тебе возможность поменяться картой 'Здоровье' с любым игроком на выбор.", "СМЕНА КАРТ -  Ты можешь поменять свою карту 'Факт' на новую из колоды"]
disaster_arr = ["ХИМИЧЕСКАЯ ВОЙНА - В результате применения химикатов серьезно изменился экологический баланс. Был нарушен микробиологический состав почв, отравлены растения. После выхода из бункера осталась малая часть животных и растений, заражена вода и почва. Остаток здорового населения - 10%", "СУПЕРВУЛКАНЫ - Супервулканами называют вулканы, производящие чрезвычайно мощные и объемные извержения. Подобные извержения приводят к тому, что ландшафт и климат на нашей планете коренным образом изменятся. После выхода из бункера глобальная засуха. Остаток населения Земли - 5%", "ПАДЕНИЕ МЕТЕОРИТА - Крупный метеорит попал в Землю, что приводит к глобальным разрушениям и смене климата. После выхода из бункера на Земле вечна зима. Остаток населения Земли - 15%", "БИОТЕРРОРИЗМ - смертельный вирус, созданный как биологическое оружие выйдет из-под контроля и спровоцирует глобальную эпидемию. Но после выхода из бункера выявлена мутация практически всех видов животных, растений и людей. Остаток здорового населения - 7%", "ЯДЕРНАЯ КАТАСТРОФА - Начнется ядерная война, радиоактивная пыль окутает всю планету, закрыв солнечный свет, и на Земле наступит долгая ядерная зима. После выхода из бункера сложности с почвой, водой. Необходима дополнительная химическая обработка. Остаток населения Земли - 5%.", "ВСЕМИРНЫЙ ПОТОМ - Из-за глобального потепления растают все полярные и континентальные льды. Процент суши составит 15%. Вода поглотит все вокруг. Произошло нарушение климата - тропики теперь повсюду. Необходимо приспособиться к новому виду растений и крупным насекомым. Остаток населения земли - люди в бункерах."]
hobby_arr = ["Гомеопатия", "Карточные фокусы", "Рисование", "Охота", "Ремонт и создание часов", "Изучение топографических карт", "Медитация", "Шитье и вязание", "Пивоварение", "Зоология", "Выращивание растений", "Стрельба по мишеням", "Плотницкое дело", "Фотография", "Изделия из кожи (обувь)", "Любительская радиосвязь", "Шахматы", "Альпинизм", "Рыбалка", "Игра в гольф", "Стрельба из лука", "Игра на губной гармошке", "Сбор грибов", "Боевые искусства", "Создание оружия 18 века", "Парусный спорт", "Танцы", "Футбол", "Кулинария", "Пение", "Компьютерные игры", "Косплей", "Создание украшений"]

profession2 = []
phobia2 = []
health2 = []
other_information2 = []
biology2 = []
characteristic2 = []
special_conditions2 = []
disaster2 = []
hobby2 = []

k_profession = -1
k_phobia = -1
k_health = -1
k_other_information = -1
k_biology = -1
k_characteristic = -1
k_special_conditions = -1
k_disaster = -1
k_hobby = -1

N = int(input('Количество игроков: '))
k_disaster = random.randint(0, (len(disaster_arr)-1))
print(len(disaster_arr), k_disaster)
print(disaster_arr[k_disaster])
f1 = open('1.txt', 'w')
f2 = open('2.txt', 'w')
f3 = open('3.txt', 'w')
f4 = open('4.txt', 'w')
f5 = open('5.txt', 'w')
f6 = open('6.txt', 'w')

if (N == 1) or (N == 2) or (N == 3) or (N == 4) or (N == 5) or (N == 6):
    k_profession = random.randint(0, (len(profession_arr)-1))
    profession2.append(profession_arr[k_profession])
    f1.write("Профессия: " + profession_arr[k_profession] + '\n')
    print("Профессия: " + profession_arr[k_profession] + '\n')
    profession_arr.pop(k_profession)
    
    k_phobia = random.randint(0, (len(phobia_arr)-1))
    phobia2.append(phobia_arr[k_phobia])
    f1.write("Фобия: " + phobia_arr[k_phobia] + "\n")
    phobia_arr.pop(k_phobia)

    k_health = random.randint(0, (len(health_arr)-1))
    health2.append(health_arr[k_health])
    f1.write("Здоровье: " + health_arr[k_health] + "\n")
    health_arr.pop(k_health)

    k_hobby = random.randint(0, (len(hobby_arr)-1))
    hobby2.append(hobby_arr[k_hobby])
    f1.write("Хобби: " + hobby_arr[k_hobby] + "\n")
    hobby_arr.pop(k_hobby)

    k_other_information = random.randint(0, (len(other_information_arr)-1))
    other_information2.append(other_information_arr[k_other_information])
    f1.write("Факт: " + other_information_arr[k_other_information] + "\n")
    other_information_arr.pop(k_other_information)

    k_biology = random.randint(0, (len(biology_arr)-1))
    biology2.append(biology_arr[k_biology])
    f1.write("Биология: " + biology_arr[k_biology] + "\n")
    biology_arr.pop(k_biology)

    k_characteristic = random.randint(0, (len(characteristic_arr)-1))
    characteristic2.append(characteristic_arr[k_characteristic])
    f1.write("Человеческие качества: " + characteristic_arr[k_characteristic] + "\n")
    characteristic_arr.pop(k_characteristic)

    k_special_conditions = random.randint(0, (len(special_conditions_arr)-1))
    special_conditions2.append(special_conditions_arr[k_special_conditions])
    f1.write("Специальные условия: " + special_conditions_arr[k_special_conditions] + "\n")
    special_conditions_arr.pop(k_special_conditions)

    f1.write("Катастрофа: " + disaster_arr[k_disaster] + "\n")
    f1.write("________________________________________________________________" + "\n")
    f1.close()

if (N == 2) or (N == 3) or (N == 4) or (N == 5) or (N == 6):
    k_profession = random.randint(0, (len(profession_arr)-1))
    profession2.append(profession_arr[k_profession])
    f2.write("Профессия: " + profession_arr[k_profession] + '\n')
    profession_arr.pop(k_profession)
    
    k_phobia = random.randint(0, (len(phobia_arr)-1))
    phobia2.append(phobia_arr[k_phobia])
    f2.write("Фобия: " + phobia_arr[k_phobia] + "\n")
    phobia_arr.pop(k_phobia)

    k_health = random.randint(0, (len(health_arr)-1))
    health2.append(health_arr[k_health])
    f2.write("Здоровье: " + health_arr[k_health] + "\n")
    health_arr.pop(k_health)

    k_hobby = random.randint(0, (len(hobby_arr)-1))
    hobby2.append(hobby_arr[k_hobby])
    f2.write("Хобби: " + hobby_arr[k_hobby] + "\n")
    hobby_arr.pop(k_hobby)

    k_other_information = random.randint(0, (len(other_information_arr)-1))
    other_information2.append(other_information_arr[k_other_information])
    f2.write("Факт: " + other_information_arr[k_other_information] + "\n")
    other_information_arr.pop(k_other_information)

    k_biology = random.randint(0, (len(biology_arr)-1))
    biology2.append(biology_arr[k_biology])
    f2.write("Биология: " + biology_arr[k_biology] + "\n")
    biology_arr.pop(k_biology)

    k_characteristic = random.randint(0, (len(characteristic_arr)-1))
    characteristic2.append(characteristic_arr[k_characteristic])
    f2.write("Человеческие качества: " + characteristic_arr[k_characteristic] + "\n")
    characteristic_arr.pop(k_characteristic)

    k_special_conditions = random.randint(0, (len(special_conditions_arr)-1))
    special_conditions2.append(special_conditions_arr[k_special_conditions])
    f2.write("Специальные условия: " + special_conditions_arr[k_special_conditions] + "\n")
    special_conditions_arr.pop(k_special_conditions)

    f2.write("Катастрофа: " + disaster_arr[k_disaster] + "\n")
    f2.write("________________________________________________________________" + "\n")
    f2.close()


if (N == 3) or (N == 4) or (N == 5) or (N == 6):
    k_profession = random.randint(0, (len(profession_arr)-1))
    profession2.append(profession_arr[k_profession])
    f3.write("Профессия: " + profession_arr[k_profession] + '\n')
    profession_arr.pop(k_profession)
    

    k_phobia = random.randint(0, (len(phobia_arr)-1))
    phobia2.append(phobia_arr[k_phobia])
    f3.write("Фобия: " + phobia_arr[k_phobia] + "\n")
    phobia_arr.pop(k_phobia)

    k_health = random.randint(0, (len(health_arr)-1))
    health2.append(health_arr[k_health])
    f3.write("Здоровье: " + health_arr[k_health] + "\n")
    health_arr.pop(k_health)

    k_hobby = random.randint(0, (len(hobby_arr)-1))
    hobby2.append(hobby_arr[k_hobby])
    f3.write("Хобби: " + hobby_arr[k_hobby] + "\n")
    hobby_arr.pop(k_hobby)

    k_other_information = random.randint(0, (len(other_information_arr)-1))
    other_information2.append(other_information_arr[k_other_information])
    f3.write("Факт: " + other_information_arr[k_other_information] + "\n")
    other_information_arr.pop(k_other_information)

    k_biology = random.randint(0, (len(biology_arr)-1))
    biology2.append(biology_arr[k_biology])
    f3.write("Биология: " + biology_arr[k_biology] + "\n")
    biology_arr.pop(k_biology)

    k_characteristic = random.randint(0, (len(characteristic_arr)-1))
    characteristic2.append(characteristic_arr[k_characteristic])
    f3.write("Человеческие качества: " + characteristic_arr[k_characteristic] + "\n")
    characteristic_arr.pop(k_characteristic)

    k_special_conditions = random.randint(0, (len(special_conditions_arr)-1))
    special_conditions2.append(special_conditions_arr[k_special_conditions])
    f3.write("Специальные условия: " + special_conditions_arr[k_special_conditions] + "\n")
    special_conditions_arr.pop(k_special_conditions)

    f3.write("Катастрофа: " + disaster_arr[k_disaster] + "\n")
    f3.write("________________________________________________________________" + "\n")
    f3.close()

if (N == 4) or (N == 5) or (N == 6):
    k_profession = random.randint(0, (len(profession_arr)-1))
    profession2.append(profession_arr[k_profession])
    f4.write("Профессия: " + profession_arr[k_profession] + '\n')
    profession_arr.pop(k_profession)
    

    k_phobia = random.randint(0, (len(phobia_arr)-1))
    phobia2.append(phobia_arr[k_phobia])
    f4.write("Фобия: " + phobia_arr[k_phobia] + "\n")
    phobia_arr.pop(k_phobia)

    k_health = random.randint(0, (len(health_arr)-1))
    health2.append(health_arr[k_health])
    f4.write("Здоровье: " + health_arr[k_health] + "\n")
    health_arr.pop(k_health)

    k_hobby = random.randint(0, (len(hobby_arr)-1))
    hobby2.append(hobby_arr[k_hobby])
    f4.write("Хобби: " + hobby_arr[k_hobby] + "\n")
    hobby_arr.pop(k_hobby)

    k_other_information = random.randint(0, (len(other_information_arr)-1))
    other_information2.append(other_information_arr[k_other_information])
    f4.write("Факт: " + other_information_arr[k_other_information] + "\n")
    other_information_arr.pop(k_other_information)

    k_biology = random.randint(0, (len(biology_arr)-1))
    biology2.append(biology_arr[k_biology])
    f4.write("Биология: " + biology_arr[k_biology] + "\n")
    biology_arr.pop(k_biology)

    k_characteristic = random.randint(0, (len(characteristic_arr)-1))
    characteristic2.append(characteristic_arr[k_characteristic])
    f4.write("Человеческие качества: " + characteristic_arr[k_characteristic] + "\n")
    characteristic_arr.pop(k_characteristic)

    k_special_conditions = random.randint(0, (len(special_conditions_arr)-1))
    special_conditions2.append(special_conditions_arr[k_special_conditions])
    f4.write("Специальные условия: " + special_conditions_arr[k_special_conditions] + "\n")
    special_conditions_arr.pop(k_special_conditions)

    f4.write("Катастрофа: " + disaster_arr[k_disaster] + "\n")
    f4.write("________________________________________________________________" + "\n")
    f4.close()

if (N == 5) or (N == 6):
    k_profession = random.randint(0, (len(profession_arr)-1))
    profession2.append(profession_arr[k_profession])
    f5.write("Профессия: " + profession_arr[k_profession] + '\n')
    profession_arr.pop(k_profession)
    

    k_phobia = random.randint(0, (len(phobia_arr)-1))
    phobia2.append(phobia_arr[k_phobia])
    f5.write("Фобия: " + phobia_arr[k_phobia] + "\n")
    phobia_arr.pop(k_phobia)

    k_health = random.randint(0, (len(health_arr)-1))
    health2.append(health_arr[k_health])
    f5.write("Здоровье: " + health_arr[k_health] + "\n")
    health_arr.pop(k_health)

    k_hobby = random.randint(0, (len(hobby_arr)-1))
    hobby2.append(hobby_arr[k_hobby])
    f5.write("Хобби: " + hobby_arr[k_hobby] + "\n")
    hobby_arr.pop(k_hobby)

    k_other_information = random.randint(0, (len(other_information_arr)-1))
    other_information2.append(other_information_arr[k_other_information])
    f5.write("Факт: " + other_information_arr[k_other_information] + "\n")
    other_information_arr.pop(k_other_information)

    k_biology = random.randint(0, (len(biology_arr)-1))
    biology2.append(biology_arr[k_biology])
    f5.write("Биология: " + biology_arr[k_biology] + "\n")
    biology_arr.pop(k_biology)

    k_characteristic = random.randint(0, (len(characteristic_arr)-1))
    characteristic2.append(characteristic_arr[k_characteristic])
    f5.write("Человеческие качества: " + characteristic_arr[k_characteristic] + "\n")
    characteristic_arr.pop(k_characteristic)

    k_special_conditions = random.randint(0, (len(special_conditions_arr)-1))
    special_conditions2.append(special_conditions_arr[k_special_conditions])
    f5.write("Специальные условия: " + special_conditions_arr[k_special_conditions] + "\n")
    special_conditions_arr.pop(k_special_conditions)

    f5.write("Катастрофа: " + disaster_arr[k_disaster] + "\n")
    f5.write("________________________________________________________________" + "\n")
    f5.close()

if (N == 6):
    k_profession = random.randint(0, (len(profession_arr)-1))
    profession2.append(profession_arr[k_profession])
    f6.write("Профессия: " + profession_arr[k_profession] + '\n')
    profession_arr.pop(k_profession)
    

    k_phobia = random.randint(0, (len(phobia_arr)-1))
    phobia2.append(phobia_arr[k_phobia])
    f6.write("Фобия: " + phobia_arr[k_phobia] + "\n")
    phobia_arr.pop(k_phobia)

    k_health = random.randint(0, (len(health_arr)-1))
    health2.append(health_arr[k_health])
    f6.write("Здоровье: " + health_arr[k_health] + "\n")
    health_arr.pop(k_health)

    k_hobby = random.randint(0, (len(hobby_arr)-1))
    hobby2.append(hobby_arr[k_hobby])
    f6.write("Хобби: " + hobby_arr[k_hobby] + "\n")
    hobby_arr.pop(k_hobby)

    k_other_information = random.randint(0, (len(other_information_arr)-1))
    other_information2.append(other_information_arr[k_other_information])
    f6.write("Факт: " + other_information_arr[k_other_information] + "\n")
    other_information_arr.pop(k_other_information)

    k_biology = random.randint(0, (len(biology_arr)-1))
    biology2.append(biology_arr[k_biology])
    f6.write("Биология: " + biology_arr[k_biology] + "\n")
    biology_arr.pop(k_biology)

    k_characteristic = random.randint(0, (len(characteristic_arr)-1))
    characteristic2.append(characteristic_arr[k_characteristic])
    f6.write("Человеческие качества: " + characteristic_arr[k_characteristic] + "\n")
    characteristic_arr.pop(k_characteristic)

    k_special_conditions = random.randint(0, (len(special_conditions_arr)-1))
    special_conditions2.append(special_conditions_arr[k_special_conditions])
    f6.write("Специальные условия: " + special_conditions_arr[k_special_conditions] + "\n")
    special_conditions_arr.pop(k_special_conditions)

    f6.write("Катастрофа: " + disaster_arr[k_disaster] + "\n")
    f6.write("________________________________________________________________" + "\n")
    f6.close()
