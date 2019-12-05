def calc(x):
    return (x//3) - 2

def part2(x):
    val = calc(x)
    if val <= 0: return 0
    return val + part2(x)
