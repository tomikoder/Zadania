from typing import List
from decimal import Decimal
import random

def generete_decimal() -> List[Decimal]:
    data = []
    x =  Decimal(str(random.uniform(2, 5 + 1/2)))
    data.append(x)

    new_val = x
    while True:
        new_val = new_val + Decimal("0.5")
        if not (new_val < float(5 + 1 / 2)): break
        data.append(new_val)

    new_val = x
    while True:
        new_val = new_val - Decimal("0.5")
        if not (new_val > 2): break
        data.append(new_val)
    return data

if __name__ == '__main__':
    print(generete_decimal())
