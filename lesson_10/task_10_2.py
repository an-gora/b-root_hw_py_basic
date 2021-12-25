def total_price(stock: dict, prices: dict) -> int:
    total_price_in_market = 0
    for key, value in stock.items(), prices.items():
        if stock.key() == prices.key():
            total_price_in_market = total_price_in_market + stock.get(key) * prices.get(key)
    return total_price_in_market


if __name__ == '__main__':
    print(total_price(stock={"banana": 6, "apple": 0, "orange": 32, "pear": 15},
                      prices={"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}))
