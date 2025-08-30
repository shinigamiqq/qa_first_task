import subprocess
from main import draw_tree


def run_tree_script(levels, output_file):
    """Запускает скрипт main.py через subprocess, чтобы проверить работу в консоли."""
    subprocess.run(["python", "main.py", str(levels), output_file], check=True)
    with open(output_file, encoding="utf-8") as f:
        return f.read()

def normalize(s: str) -> str:
    """Убирает лишние пробелы справа для корректного сравнения."""
    return "\n".join(line.rstrip() for line in s.strip().split("\n"))

def test_draw_tree_function():
    """Проверка функции напрямую."""
    tree = draw_tree(2)
    expected = "\n".join([
        "        W        ",
        "        *        ",
        "    @* * * * *   ",
        "* * * * * * * * *@",
        "      TTTTT",
        "      TTTTT"
    ])
    assert normalize(tree) == normalize(expected)

def test_cli_output(tmp_path):
    """Проверка запуска через командную строку."""
    output_file = tmp_path / "tree.txt"
    result = run_tree_script(1, str(output_file))
    expected = "\n".join([
        "    W     ",
        "    *     ",
        "@* * * * *",
        "  TTTTT   ",
        "  TTTTT   "
    ])
    assert normalize(result) == normalize(expected)

def test_negative_levels(tmp_path):
    """Проверка реакции на отрицательный ввод."""
    output_file = tmp_path / "tree.txt"
    proc = subprocess.run(
        ["python", "main.py", "-2", str(output_file)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    assert "Ошибка" in proc.stdout or "Ошибка" in proc.stderr
    assert proc.returncode != 0

