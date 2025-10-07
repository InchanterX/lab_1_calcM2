from src.facade import Facade

'''
Users interface.
Print basic text, while user won't write an escape command
continue to ask a new expressions and return results for them
over and over again
'''


def main() -> None:
    print("Добро пожаловать в калькулятор сделанный в рамках лабораторной работы по заданию M2!")
    print("Калькулятор поддерживает операции +, -, *, /, //, %, **, скобки унарные операции + и - (до 2-х подряд).")

    while True:
        # Users expression input
        expression = input("\nВведите выражение: ").strip()

        # Programme finishing
        if expression.lower() in ("exit", "quit", "выход", "выйти"):
            print("Выход из программы.")
            break

        # Try to calculate the result for the entered expression
        # if it is not possible return an exception with a corresponding error
        try:
            result = Facade().calculate(expression)
            print(f"Результат: {result}")
        except Exception as e:
            print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
