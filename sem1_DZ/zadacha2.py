# Напишите код, который запрашивает число и сообщает является ли оно простым или составным. 
# Используйте правило для проверки: “Число является простым, если делится нацело только на единицу и на себя”. 
# Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.



def chislo():
    num = int(input("Введите число: "))

    if num < 0 or num > 100000:
        return "Введите число в допустимом диопазоне:от 0 до 100000."

    if num == 1 or num == 0:
        return "!!!Это Число не является НЕ простым, НЕ составным."

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return "Это составное число"
    return "Это простое число."

print(chislo())