def lis(sequence, monotone=False):
    n = len(sequence)
    dp = [1] * n
    prev = [-1] * n

    idxMax = 0
    for i in range(1, n):
        for j in range(0, i):
            if sequence[j] <= sequence[i] and dp[j] + 1 >= dp[i]:
                if not monotone and (sequence[j] == sequence[i] or dp[j] + 1 == dp[i]):
                    continue
                dp[i] = dp[j] + 1
                prev[i] = j
        if dp[i] > dp[idxMax]:
            idxMax = i

    result = []
    idx = idxMax
    while idx != -1:
        result.append(sequence[idx])
        idx = prev[idx]

    result.reverse()
    return result


if __name__ == "__main__":
    sequences = [
        [4, 1, 13, 7, 0, 2, 8, 11, 3],
        [3, 1, 5, 2, 3, 3, 2, 6, 4, 9],
        [10, 22, 9, 33, 21, 33, 50, 41, 60, 80],
    ]

    for sequence in sequences:
        print("Sequence : ", sequence)
        print("LIS      : ", lis(sequence))
        print("LMIS     : ", lis(sequence, monotone=True))
        print()