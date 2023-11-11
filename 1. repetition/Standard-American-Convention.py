# 1
n = '{:,}'.format(int(input()))
print(n)

# 2
seq = list(input())
new_s = ""

while len(seq) >= 3:
    # отрываем 3 последние цифры и ставим после них запятую
    new_s += seq.pop(-1) + seq.pop(-1) + seq.pop(-1) + ","

# обрабатываем цифры, которые могли остаться (их 1 или 2)
new_s += "".join(seq[::-1])

new_s = new_s[::-1]  # переворачивааем результат в первоначальный вид
new_s = new_s.lstrip(",")  # убираем лишнюю запятую

print(new_s)
