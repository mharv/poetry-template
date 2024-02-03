from typing import List


def alter(x: int) -> int:
    return x + 1


def get_n_numbers(n: int) -> List[int]:
    return [alter(x) for x in range(n)]


def multiply_array(arr: List[int], scalar: int) -> List[int]:
    result = []
    for i in range(len(arr)):
        result.append(arr[i] * scalar)
    return result


def main() -> None:
    print(get_n_numbers(5))


if __name__ == "__main__":
    main()
