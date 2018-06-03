import argparse


def format_price(price):
    try:
        float_price = float(price)
    except ValueError:
        return None
    except TypeError:
        return None
    except AttributeError:
        return None
    round_price = round(float_price, 2)
    if round_price.is_integer():
        return format(round_price, ",.0f").replace(",", " ")
    else:
        return format(round_price, ",.2f").replace(",", " ")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("price")
    parsed_args = parser.parse_args()
    price = parsed_args.price
    formated_price = format_price(price)
    if formated_price is None:
        exit("Данный тип не поддерживается")
    print(formated_price)
