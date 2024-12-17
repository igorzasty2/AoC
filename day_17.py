data = open('data/day_17.txt').read().splitlines()
val1 = int(data[0].split('A: ')[1])
val2 = int(data[1].split('B: ')[1])
val3 = int(data[2].split('C: ')[1])
prog = list(map(int, data[4][9:].split(',')))


def assembly(a, b, c, program):
    ip = 0
    out = ''
    while ip < len(program):
        c_op = -1
        l_op = program[ip + 1]
        match program[ip + 1]:
            case 0:
                c_op = 0
            case 1:
                c_op = 1
            case 2:
                c_op = 2
            case 3:
                c_op = 3
            case 4:
                c_op = a
            case 5:
                c_op = b
            case 6:
                c_op = c

        match program[ip]:
            case 0:
                a = a >> c_op
            case 1:
                b = b ^ l_op
            case 2:
                b = c_op % 8
            case 3:
                if a != 0:
                    ip = l_op - 2
            case 4:
                b = b ^ c
            case 5:
                out += f'{c_op % 8},'
            case 6:
                b = a >> c_op
            case 7:
                c = a >> c_op
        ip += 2
    return out[:-1]


print(assembly(val1, val2, val3, prog))
self_reference = data[4][9:]
sol = 0
l = len(self_reference)
for idx in range(len(prog)):
    sol <<= 3
    i = 0
    while True:
        x = assembly(sol+i, val2, val3, prog)
        instruction_slice = self_reference[-(2*(idx)+1):]
        if x == instruction_slice:
            sol += i
            break
        i+=1
print(sol)