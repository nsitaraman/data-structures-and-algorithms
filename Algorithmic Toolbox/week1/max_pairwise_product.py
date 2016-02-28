# Uses python3
def max_pairwise_product_slow(n, a):
    result = 0
    for i in range(0, n):
        for j in range(i+1, n):
            if a[i] * a[j] > result:
                result = a[i] * a[j]
    return result

def max_pairwise_product_faster(n, a):
    max_index1 = -1
    max_index2 = -1

    for i in range(0, n):
        if max_index1 == -1  or a[i] > a[max_index1]:
            max_index1 = i

    for j in range(0, n):
            if (j != max_index1) and (max_index2 == -1  or a[j] > a[max_index2]):
                max_index2 = j

    return a[max_index1] * a[max_index2]


def max_pairwise_product_fastest(n, a):
    max_index1 = -1
    max_index2 = -1

    for i in range(0, n):
        if max_index2 == -1 or a[i] > a[max_index2]:
            if max_index1 == -1 or a[i] >= a[max_index1]:
                max_index2 = max_index1
                max_index1 = i
            else:
                max_index2 = i

    return a[max_index1] * a[max_index2]

n = int(input())
a = [int(x) for x in input().split()]
assert(len(a) == n)

result = max_pairwise_product_fastest(n, a)
print(result)

'''
# stress test
import random

random.seed(0)
while True:
    n  = random.randint(2,20)
    a = [0] * n
    for i in range(n):
        a[i] = random.randint(0, 100000)

    print(n)
    #print(a)

    res1 = max_pairwise_product_slow(n, a)
    res2 = max_pairwise_product_faster(n, a)
    res3 = max_pairwise_product_fastest(n, a)

    if res1 == res2 and res1 == res3:
        print("Ok")
    else:
        print("Wrong Answer")
        break
'''
