def sum(max):
    if max <= 100 and max >= 0:
        return max +sum(max - 1)
    else:
        return 0

print(sum(100))
