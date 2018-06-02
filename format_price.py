import argparse


def format_price(price):
    if "," in str(price):
        price = price.replace(",", ".")
    try:
        float_price = float(price)
    except TypeError and ValueError:
        return None
    round_price = round(float_price, 2)
    if round_price.is_integer():
        return format(round_price, ",.0f").replace(",", " ")
    else:
        return format(round_price, ",.2f").replace(",", " ")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("price")
    parsargs = parser.parse_args()
    price = parsargs.price
    formated_price = format_price(price)
    if formated_price is None:
        exit("Данный тип не поддерживается")
    print(formated_price)
