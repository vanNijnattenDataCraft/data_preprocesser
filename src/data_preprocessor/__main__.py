def main() -> None:
    pass


if __name__ == "__main__":
    main()

def add_numbers(a: int, b: int) -> int:
    return a + b

result = add_numbers(5, "10")  # TypeError: expected 'int', got 'str'
