animals = ["Обезьяна", "Петух", "Собака", "Свинья", "Крыса", "Бык", "Тигр", "Заяц", "Дракон", "Змея", "Лошадь", "Овца"]
year = int(input())
print(animals[year % 12])


def rotate(s):
    return s[::-1]

s = input()

if len(s) == 5:
    print(int(rotate(s)))
else:
    print(int(s[0] + rotate(s[1:])))
