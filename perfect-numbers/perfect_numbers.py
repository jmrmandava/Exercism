def classify(n):
    a = 0

    if n < 1:
        raise ValueError(
            f"Error occured,The number should be greater than 0(input{n})."
        )
    for i in range(1, n):
        if n % i == 0:
            a = a + i

    if a == n:
        return "perfect"
    if a < n:
        return "deficient"
    elif a > n:
        return "abundant"
