import random
import src.constants


class Casino:
    '''
    Give an ability to play casino in special mod of calculator.
    It contains functions for variables, turning on and turning off,
    promo codes, spins and payouts calculations.
    '''

    def __init__(self):
        self.balance = 1000
        # State of casino
        self.active = False
        # State of promo code
        self.used_promo = False

    def enable(self):
        # Enable casino
        self.active = True
        print("🎰 Казино включено! Добро пожаловать в MAI Casino!")
        print(f"Ваш баланс: {self.balance} MAI Coins")

    def disable(self):
        # Disable casino
        self.active = False
        print("🎰 Казино выключено, но всегда можно сделать додеп!")

    def apply_promo(self, promo_code: str):
        # Activate a promo if it is valid and haven't used yet
        if self.used_promo:
            print("Промокод уже был использован!")
        elif promo_code == "MAI_PO_BLATU":
            self.balance += 500
            self.used_promo = True
            print("Промокод активирован! +500 MAI Coins.")
        else:
            print("Неверный промокод!")

    def spin(self):
        # Spin the roulette for 100 coins!
        if self.balance < 100:
            print("Недостаточно средств для ставки (100 MAI Coins). Пополнить можно наличкой через автора кода, обмен монет 1 к 1.")
            return

        self.balance -= 100
        slots = [random.choice(src.constants.SYMBOLS) for _ in range(3)]
        print(f"🎰|{'|'.join(slots)}|")

        payout = self.calculate_payout(slots)
        self.balance += payout

        # Messages for payouts
        if payout == 1500:
            print(f"!!!ДЖЭЭЭЭКПОООТ - {payout} MAI Coins!!!")
        elif payout > 0:
            print(f"Юхууу, Вы выиграли {payout} монет!")
        print(f"Баланс: {self.balance} MAI Coins.")

    def calculate_payout(self, slots):
        # Count payout
        if slots[0] == slots[1] == slots[2]:
            symbol = slots[0]
            return src.constants.MULTIPLIERS[symbol]*100
        elif slots[0] == slots[1] or slots[1] == slots[2]:
            symbol = slots[1]
            return src.constants.MULTIPLIERS[symbol]*20
        elif slots[0] == slots[2]:
            symbol = slots[0]
            return src.constants.MULTIPLIERS[symbol]*20
        else:
            return 0
