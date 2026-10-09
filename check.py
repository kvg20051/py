#!/usr/bin/env python3
"""Автопроверка задач.

    python3 check.py 1        # проверить все задачи дня 1
    python3 check.py 1 13     # проверить одну задачу
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent

FIZZ = "\n".join(
    "FizzBuzz" if i % 15 == 0 else "Fizz" if i % 3 == 0 else "Buzz" if i % 5 == 0 else str(i)
    for i in range(1, 101)
)

# задача: [(stdin, ожидаемый stdout), ...]
TESTS = {
    1: {
        1: [("Виктор\n", "Привет, Виктор!")],
        2: [("5 7\n", "12\n-2\n35\n0\n5"), ("17 5\n", "22\n12\n85\n3\n2")],
        3: [("4\n", "чётное"), ("7\n", "нечётное"), ("0\n", "чётное")],
        4: [("2024\n", "YES"), ("1900\n", "NO"), ("2000\n", "YES"), ("2026\n", "NO")],
        6: [("", FIZZ)],
        7: [("12345\n", "15"), ("99999999999999999999\n", "180")],
        8: [("", "2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97")],
        9: [("", "30414093201713378043612608166064768844377641568960512000000000000")],
        10: [("0\n", "0"), ("10\n", "55"), ("90\n", "2880067194370816120")],
        11: [("48 18\n", "6"), ("17 5\n", "1")],
        12: [("a b\nc\n", "2 3 6")],
        13: [("alice 30\nbob 45\ncarol 12\n", "sum: 87\navg: 29.00\nmax: 45 (bob)")],
        14: [((ROOT / "day1/data/test.log").read_text(),
              "total: 6\nINFO: 2\nWARN: 1\nERROR: 3\nfirst error: 10:01:05\nlast error: 10:05:13")],
    },
}


def run(day, num):
    script = ROOT / f"day{day}" / f"d{day}_{num:02d}.py"
    tests = TESTS.get(day, {}).get(num)
    if tests is None:
        print(f"  d{day}_{num:02d}: автотеста нет — пришлите решение на проверку")
        return True
    for stdin, expected in tests:
        try:
            p = subprocess.run([sys.executable, script], input=stdin, capture_output=True,
                               text=True, timeout=5)
        except subprocess.TimeoutExpired:
            print(f"  d{day}_{num:02d}: ТАЙМАУТ (бесконечный цикл?)")
            return False
        got = p.stdout.strip()
        if p.returncode != 0 or got != expected.strip():
            print(f"  d{day}_{num:02d}: ОШИБКА")
            print(f"    ввод:     {stdin[:60]!r}")
            print(f"    ожидалось:{expected.strip()[:200]!r}")
            print(f"    получено: {got[:200]!r}")
            if p.stderr:
                print("    stderr:", p.stderr.strip().splitlines()[-1])
            return False
    print(f"  d{day}_{num:02d}: OK")
    return True


def main():
    day = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    nums = [int(sys.argv[2])] if len(sys.argv) > 2 else sorted(
        int(p.stem.split("_")[1]) for p in (ROOT / f"day{day}").glob(f"d{day}_*.py"))
    ok = sum(run(day, n) for n in nums)
    print(f"\nПройдено: {ok}/{len(nums)}")


if __name__ == "__main__":
    main()
