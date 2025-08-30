import sys


def draw_tree(levels: int) -> str:
    """
    Рисует центрированную ёлку с правильным форматом:
    - W сверху
    - 0-й уровень: *
    - 1-й уровень: @* * * * *@
    - 2-й уровень: * * * * * * * * *@
    - ...
    - ствол: две строки TTTTT
    """
    if levels < 0:
        return ""

    level_lines = []

    for level in range(levels + 1):
        stars_count = 1 + 4 * level
        stars = " ".join("*" for _ in range(stars_count))

        if level == 0:
            line = stars
        elif level % 2 == 1:
            line = "@" + stars
        else:
            line = stars + "@"

        level_lines.append(line)

    max_width = max(len(line) for line in level_lines)

    lines = ["W".center(max_width)]

    for line in level_lines:
        lines.append(line.center(max_width))

    trunk = "TTTTT"
    lines.append(trunk.center(max_width))
    lines.append(trunk.center(max_width))

    return "\n".join(lines)


def main():
    if len(sys.argv) != 3:
        print("Использование: python main.py <количество_этажей> <путь_к_файлу>")
        sys.exit(1)

    try:
        levels = int(sys.argv[1])
    except ValueError:
        print("Ошибка: количество этажей должно быть целым положительным числом.")
        sys.exit(1)

    if levels < 0:
        print("Ошибка: количество этажей не может быть отрицательным.")
        sys.exit(1)

    output_path = sys.argv[2]
    tree = draw_tree(levels)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(tree)

    print(f"Ёлка с {levels} этаж(ами) сохранена в {output_path}")


if __name__ == "__main__":
    main()

#test
