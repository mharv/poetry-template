from typing import List


def alter(x: int) -> int:
    return x + 1


def get_n_numbers(n: int) -> List[int]:
    return [alter(x) for x in range(n)]


def main() -> None:
    numbers = get_n_numbers(5)


if __name__ == "__main__":
    main()
