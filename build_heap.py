# python3
import heapq

# Author: Aleksandrs Pučenkins 17.gr. 221RDB335

def build_heap(data):

    swaps = []
    heapq.heapify(data)
    for i in range(len(data)):
        while i != 0 and data[(i - 1) // 2] > data[i]:
            j = (i - 1) // 2
            swaps.append((i, j))
            data[i], data[j] = data[j], data[i]
            i = j
    return swaps


def read_input():

    input_type = input().strip()
    if input_type == 'I':
        n = int(input().strip())
        data = list(map(int, input().strip().split()))
    elif input_type == 'F':
        file_name = input().strip()
        with open(file_name, 'r') as f:
            n = int(f.readline().strip())
            data = list(map(int, f.readline().strip().split()))
    else:
        raise ValueError(f"Invalid input type: {input_type}")
    if len(data) != n:
        raise ValueError(f"Expected {n} integers, but got {len(data)}")
    return input_type, data


def main():
    input_type, data = read_input()
    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == '__main__':
    main()
