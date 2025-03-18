# def jumlahkan(data):
#     return sum(data)

# print(jumlahkan([1, 2, 3, 4, 5]))

# from typing import List

# def jumlahkan(data: List[int]) -> int:
#     return sum(data)

# print(jumlahkan([1, 2, 3, 4, 5]))

# def jumlahkan(data):
#     data = [int(d) for d in data]
#     return sum(data)

# print(jumlahkan([1, "2", 3.5, 4, "5"]))

from typing import List

def jumlahkan(data: List [float]) -> float:
    data = [float(d) for d in data]
    return sum(data)

print(jumlahkan([1, 2, 3.5, 4, 5]))
print(jumlahkan([1, "2", 3.5, 4, "5"]))