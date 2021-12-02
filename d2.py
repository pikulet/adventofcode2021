with open('input2', 'r') as f:
    data = [d.split() for d in f.read().splitlines()]

cmd_fwd = "forward"
cmd_down = "down"
cmd_up = "up"

def part_a():
    x = 0
    y = 0

    for d in data:
        val = int(d[1])
        if d[0] == cmd_fwd:
            x += val
        elif d[0] == cmd_down:
            y += val
        elif d[0] == cmd_up:
            y -= val

    return x * y

def part_b():
    x = 0
    y = 0
    aim = 0

    for d in data:
        val = int(d[1])
        if d[0] == cmd_fwd:
            x += val
            y += aim * val
        elif d[0] == cmd_down:
            aim += val
        elif d[0] == cmd_up:
            aim -= val

    return x * y

print('part a:', part_a())
print('part b:', part_b())

