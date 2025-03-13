import sys


def min_moves_to_single_number(file_path):
    """
    Вычисляет минимальное количество ходов для приведения всех чисел к одному значению.

    Args:
        file_path (str): Путь к файлу с числами

    Returns:
        int: Минимальное количество ходов
    """

    # Чтение данных из файла
    with open(file_path, 'r') as file:
        nums = [int(line.strip()) for line in file if line.strip()]

    # Вычисление медианы и суммы ходов
    nums_sorted = sorted(nums)
    n = len(nums_sorted)
    median = nums_sorted[n // 2]

    return sum(abs(num - median) for num in nums_sorted)


if __name__ == "__main__":
    try:
        # Проверка аргументов командной строки
        if len(sys.argv) != 2:
            raise RuntimeError("Использование: python task4.py <numbers.txt>")

        input_file = sys.argv[1]
        result = min_moves_to_single_number(input_file)
        print(result)

    except Exception as e:
        print(f"Ошибка: {e}")
        sys.exit(1)
