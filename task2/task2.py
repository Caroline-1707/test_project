import sys
from decimal import Decimal

# Чтение параметров окружности
with open(sys.argv[1], 'r') as f:
    circle_data = f.read().splitlines()
cx, cy = map(Decimal, circle_data[0].split())
radius = Decimal(circle_data[1])
radius_sq = radius ** 2  # Квадрат радиуса для сравнения

# Чтение координат точек
with open(sys.argv[2], 'r') as f:
    points = [tuple(map(Decimal, line.strip().split())) for line in f]

# Определение положения каждой точки
for x, y in points:
    dx = x - cx
    dy = y - cy
    distance_sq = dx * dx + dy * dy

    if distance_sq == radius_sq:
        print(0)
    elif distance_sq < radius_sq:
        print(1)
    else:
        print(2)
