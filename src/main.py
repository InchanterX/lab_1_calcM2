from src.facade import Facade

def main() -> None:
    print("Добро пожаловать в калькулятор сделанный в рамках лабораторной работы по заданию M2!")
    print("Калькулятор поддерживает операции +, -, *, /, //, %, **, скобки унарные операции + и - (до 2-х подряд).")

    while True:
        expression = input("\nВведите выражение: ").strip()
        if expression.lower() in ("exit", "quit", "выход", "выйти"):
            print("Выход из программы.")
            break

        try:
            result = Facade().calculate (expression)
            print(f"Результат: {result}")
        except Exception as e:
            print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
