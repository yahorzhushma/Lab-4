class String:
    def __init__(self, string):
        self.string = string

    def reverse(self):
        return self.string[::-1]

    def count_words(self):
        return len(self.string.split())

    def is_palindrome(self):
        temp_string = self.string.lower().replace(" ", "")
        return temp_string == temp_string[::-1]

    def count_occurrences(self, sub_string):
        return self.string.count(sub_string)

    def concatenate(self, other_string):
        return self.string + other_string.string

    def find_common_characters(self, other_string):
        common_chars = set(self.string) & set(other_string.string)
        return "".join(common_chars)

    def find_unique_characters(self, other_string):
        unique_chars = set(self.string) - set(other_string.string)
        return "".join(unique_chars)

class Country:
    def __init__(self, capital, area, population):
        self.capital = capital
        self.area = area
        self.population = population

    def __str__(self):
        return f"Столица: {self.capital}, Площадь: {self.area}, Население: {self.population}"

class ZooShop:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def most_expensive_breed(self):
        if len(self.animals) == 0:
            return None
        most_expensive_animal = max(self.animals, key=lambda animal: animal.price)
        return most_expensive_animal.breed

class Animal:
    def __init__(self, breed, price):
        self.breed = breed
        self.price = price

    def move(self):
        pass

    def __str__(self):
        return f"Порода: {self.breed}, Стоимость : {self.price}"

class Fish(Animal):
    def move(self):
        return "Плавает"

class Bird(Animal):
    def move(self):
        return "Летает"

while True:
    print("\nГлавное меню:")
    print("1. Класс String")
    print("2. Класс Country")
    print("3. Зоомагазин")
    print("4. Мой класс")
    print("0. Завершение программы")

    choice = input("Введите номер действия: ")

    if choice == '1':
        while True:
            print("\n1. Меню для работы с одной строкой")
            print("2. Меню для работы с двумя строакми")
            print("0. Назад")

            choice = input("Введите номер действия: ")

            if choice == '1':
                s = String(input("Введите строку: "))

                while True:
                    print("\nМеню для работы с одной строки")
                    print("1. Зеркало")
                    print("2. Сколько слов?")
                    print("3. Палиндром?!")
                    print("4. Сколько вхождений?")
                    print("0. Назад")

                    choice = input("Введите номер действия: ")

                    if choice == '1':
                        print(s.reverse())

                    elif choice == '2':
                        print(s.count_words())

                    elif choice == '3':
                        if s.is_palindrome():
                            print("Да, это палиндром")
                        else:
                            print("Нет, это не палиндром")

                    elif choice == '4':
                        occ = input("Что найти в строке? ")
                        print(s.count_occurrences(occ))

                    elif choice == '0':
                        break

                    else:
                        print("Неверный выбор. Попробуйте снова.")

            elif choice == '2':

                s1 = String(input("Введите первую строку: "))
                s2 = String(input("Введите вторую строку: "))

                while True:
                    print("\nМеню для работы с двумя строками")
                    print("1. Сложение строк")
                    print("2. Одинаковые буквы")
                    print("3. Уникальные буквы")
                    print("0. Назад")

                    choice = input("Введите номер действия: ")

                    if choice == '1':
                        print(s1.concatenate(s2))

                    elif choice == '2':
                        print(s1.find_common_characters(s2))

                    elif choice == '3':
                        print(s1.find_unique_characters(s2))

                    elif choice == '0':
                        break

                    else:
                        print("Неверный выбор. Попробуйте снова.")

            elif choice == '0':
                break

            else:
                print("Неверный выбор. Попробуйте снова.")

    elif choice == '2':
        print("\nСоздайте список стран")
        countries = []

        while True:
            try:
                capital = input("Введите столицу страны или '0' для завершения: ")
                if capital == '0':
                    break
                else:
                    area = float(input("Введите площадь территории страны (в кв. км): "))
                    population = int(input("Введите численность населения: "))
                    country = Country(capital, area, population)
                    countries.append(country)
            except ValueError:
                print("Ошибка: Введите корректное значение")

        while True:
            print("\n1. Вывести список стран по заданной площади")
            print("2. Вывести список стран по заданной численности населения")
            print("0. Назад")

            choice = input("Введите номер действия: ")

            if choice == '1':
                def filter_by_area(countries, min_area, max_area):
                    filtered_countries =[]
                    for country in countries:
                        if min_area <= country.area <= max_area:
                            filtered_countries.append(country)
                    return filtered_countries

                while True:
                    try:
                        min_area = float(input("Введите минимальное значение площади: "))
                        max_area = float(input("Введите максимальное значение площади: "))
                        if min_area <= 0 or max_area <= 0:
                            print("Площадь должна быть положительным числом.")
                        elif min_area > max_area:
                            print("Минимальная площадь оказалась больше максимальной. Введите значения правильно.")
                        else:
                            break
                    except ValueError:
                        print("Ошибка: Введите корректное значение")

                countries_by_area = filter_by_area(countries, min_area, max_area)
                if len(countries_by_area) == 0:
                    print("Стран с такой площадью нет")
                else:
                    print(f"Страны с площадью от {min_area} до {max_area} кв. км: ")
                    for country in countries_by_area:
                        print(country)

            elif choice == '2':
                def filter_by_population(countries, min_popul, max_popul):
                    filtered_countries =[]
                    for country in countries:
                        if min_popul <= country.population <= max_popul:
                            filtered_countries.append(country)
                    return filtered_countries

                while True:
                    try:
                        min_population = int(input("Введите минимальное значение численности населения: "))
                        max_population = int(input("Введите максимальное значение численности населения: "))
                        if min_population <= 0 or max_population <= 0:
                            print("Площадь должна быть положительным числом.")
                        elif min_population > max_population:
                            print("Минимальная численность насесления оказалась больше максимальной.")
                        else:
                            break
                    except ValueError:
                        print("Ошибка: Введите корректное значение")

                countries_by_population = filter_by_population(countries, min_population, max_population)
                if len(countries_by_population) == 0:
                    print("Стран с такой численностью нет")
                else:
                    print(f"Страны с численностью от {min_population} до {max_population} чел.: ")
                    for country in countries_by_population:
                        print(country)

            elif choice == '0':
                break

            else:
                print("Неверный выбор. Попробуйте снова.")

    elif choice == '3':


    elif choice == '0':
        break

    else:
        print("Неверный выбор. Попробуйте снова.")