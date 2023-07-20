# Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано: a, b, c - стороны
# предполагаемого треугольника. Требуется сравнить длину каждого отрезка - стороны с суммой двух других. Если хотя бы 
# в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует.



a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
if a + b <= c or a + c <= b or b + c <= a:
    print("Треугольник не существует")
elif a != b and a != c and b != c:
    print("Разносторонний")
elif a == b == c:
    print("Равносторонний")
else:
    print("Равнобедренный")