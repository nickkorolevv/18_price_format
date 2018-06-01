import re
import argparse

pattern_letter = re.compile("([a-zA-Zа-яА-ЯёЁ']+)")


def format_price(price):
    if not (isinstance(price, (int, float, str))):
        raise TypeError("Данный тип не поддерживается")
    if isinstance(price, str) and pattern_letter.match(price):
        raise ValueError("Буквы не должны быть введены")
    if isinstance(price, str)and any(
        char in "!#$%&'()*+-/:;<=>?@[\]^_`{|}~" for char in price
    ):
        raise ValueError("Данные символы не поддеживаются")
    price = float(price)
    price = round(price, 2)
    if price.is_integer():
        return format(price, ",.0f").replace(",", " ")
    else:
        return format(price, ",.2f").replace(",", " ")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--price")
    parsargs = parser.parse_args()
    if parsargs.price:
        price = parsargs.price
    else:
        price = input("Введите число:\n")
    formated_price = format_price(price)
    print(formated_price)
