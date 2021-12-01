# 동전문제
# 지불해야 하는 값이 4720원 일때 1원, 50원, 100원, 500원 동전으로 동전의 수가 가장 적게 지불하시오

coin_list = [500, 100, 50, 1]

def min_coin_count(value, coin_list):
    total_coin_count = 0
    details = list()
    coin_list.sort(reverse=True)
    for coin in coin_list:
        coin_num = value // coin
        total_coin_count += coin_num
        value -= coin_num * coin
        details.append([coin, coin_num])
    return total_coin_count, details

print(min_coin_count(4720, coin_list))