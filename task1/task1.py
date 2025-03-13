import sys


def circular_path(n, m):
    """
    Возвращает путь, по которому, при движении интервалом длины m по круговому массиву,
    концом будет являться первый элемент.
    """
    if n <= 0 or m <= 0:
        raise ValueError("n и m должны быть положительными числами.")

    path = [1]  # Начинаем с первого элемента
    current = 1  # Текущий элемент

    while True:
        # Вычисляем следующий элемент с учётом зацикливания
        next_element = (current + m - 1) % n
        if next_element == 0:
            next_element = n  # Если остаток 0, это последний элемент

        # Если вернулись к первому элементу, завершаем
        if next_element == 1:
            break

        path.append(next_element)  # Добавляем элемент в путь
        current = next_element  # Обновляем текущий элемент

    return ''.join(map(str, path))  # Преобразуем путь в строку


def main():
    if len(sys.argv) != 3:
        print("Использование: python task1.py <n> <m>")
        return

    try:
        n = int(sys.argv[1])
        m = int(sys.argv[2])
    except ValueError:
        print("n и m должны быть целыми числами.")
        return

    try:
        result = circular_path(n, m)
        print(result)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
