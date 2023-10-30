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

    elif choice == '0':
        break

    else:
        print("Неверный выбор. Попробуйте снова.")