def knapSack(capacity, weights, values, n):
    value = [[0 for x in range(capacity + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                value[i][w] = 0
            elif weights[i - 1] <= w:
                value[i][w] = max(values[i - 1] + value[i - 1][w - weights[i - 1]], value[i - 1][w])
            else:
                value[i][w] = value[i - 1][w]

    return value[n][capacity]


values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
n = len(val)
print(knapSack(W, wt, val, n))

