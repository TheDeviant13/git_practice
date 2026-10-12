# Программа для вычисления суммы чисел от 1 до N
# ВНИМАНИЕ: в этой версии есть баг!

def sum_to_n(n):
    total = 0
    for i in range(1, n):   # Внимание!!! Баг: range не включает n
        total += i
    return total

if __name__ == "__main__":
    n = int(input("Введите число N: "))
    print(f"Сумма чисел от 1 до {n} = {sum_to_n(n)}")
