def drop(lst, interval):
    return [item2 for item1, item2 in enumerate(lst)
            if (item1 + 1) % interval]
print drop(range(15), 3)
