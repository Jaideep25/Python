for a, b in zip(x, y):
    if a <= b:
        continue
    c = calculate_c(a, b)
    if b - c >= a:
        continue
    b = min(b, c)
    if a ** 2 - b ** 2 <= 0:
        continue
    lots()
    of()
    code()
    here()
