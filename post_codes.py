from typing import List

def change_num_in_code(c: int) -> str:
    c = str(c)
    return c[:2] + '-' + c[2:]

def codes_between(c1: str, c2: str) -> List[str]:
    c1 = int(c1[:2] + c1[3:])
    c2 = int(c2[:2] + c2[3:])
    data = []
    c3 = c1 + 1
    while c3 < c2:
        data.append(change_num_in_code(c3))
        c3 += 1
    return data

if __name__ == '__main__':
    print(codes_between("79-900", "80-155"))
