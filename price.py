def get_summ(one, two, delimiter='&'):
    one = str(one.upper())
    two = str(two.upper())
    return (f"{one}{delimiter}{two}")


print(get_summ("Learn", "python"))


def format_price(price):
    price = int(price)
    return(f"Цена: {price} руб.")


temp = format_price(56.24)
print(temp)