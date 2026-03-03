import sys

read = sys.stdin.readline

start, increase, final, decrease = map(int, read().split())

petr_offer = start
driver_ask = final

if driver_ask <= petr_offer:
    print(petr_offer)
    sys.exit(0)

while True:
    next_petr_offer = petr_offer + increase
    if next_petr_offer >= driver_ask:
        print(driver_ask)
        break
    petr_offer = next_petr_offer

    next_driver_ask = driver_ask - decrease
    if next_driver_ask <= petr_offer:
        print(petr_offer)
        break
    driver_ask = next_driver_ask