with open('input1', 'r') as f:
    data = [int(x) for x in f.read().splitlines()]

def inc(win_size):
    return len(list(filter(lambda i: data[i + win_size] > data[i], range(len(data) - win_size))))

print('part a:', inc(1))
print('part b:', inc(3))
