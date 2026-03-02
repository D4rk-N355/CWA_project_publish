
def calculation_sum(data: list):
    total = 0
    try:
        for items in data:
            if int(items) > 0:
                total += (int(items))
    except Exception as e:
        print(f"ERROR:{e}")

    return total

price = ['130','-600','28']
print(calculation_sum(price))