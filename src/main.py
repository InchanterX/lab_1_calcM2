from src.facade import Facade
from src.casino import Casino

'''
Users interface.
Print basic text, while user won't write an escape command
continue to ask a new expressions and return results for them
over and over again
'''


def main() -> None:
    print("Добро пожаловать в калькулятор сделанный в рамках лабораторной работы по заданию M2!")
    print("Калькулятор поддерживает операции +, -, *, /, //, %, **, скобки унарные операции + и - (до 2-х подряд).")
    print("Волшебная команда: casino_on")

    casino = Casino()

    while True:
        # Users expression input
        expression = input("\nВведите выражение: ").strip()

        # Programme finishing
        if expression.lower() in ("exit", "quit", "выход", "выйти"):
            print("Выход из программы.")
            break

        if expression.lower() == "casino_on":
            casino.enable()
            continue
        if expression.lower() == "casino_off":
            casino.disable()
            continue

        if casino.active:
            if expression.lower().startswith("promo "):
                promo_code = expression.split(" ", 1)[1]
                casino.apply_promo(promo_code)
            elif expression.lower() == "spin":
                casino.spin()
            else:
                print("Казино активно! Доступны команды: spin, promo <код>, casino_off")
            continue

        # Try to calculate the result for the entered expression
        # if it is not possible return an exception with a corresponding error
        try:
            result = Facade().calculate(expression)
            print(f"Результат: {result}")
        except Exception as e:
            print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
