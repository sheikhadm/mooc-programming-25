# Write your solution here
def run(program:list):
    alphabet_dict = {chr(i): 0 for i in range(ord('A'), ord('Z') + 1)}
    result = []
    i = 0
    while True:
        if i >= len(program) or program[i] == 'END' :
            break
        commands = program[i].split(' ')

        if commands[0] == 'MOV':
            alphabet_dict[commands[1]] = int(commands[2]) if commands[2] not in alphabet_dict else int(alphabet_dict[commands[2]]) 
        elif commands[0] == 'PRINT':
            result.append((int(alphabet_dict[commands[1]]) if commands[1] in alphabet_dict else int(commands[1])))
        elif commands[0] == 'ADD':
            alphabet_dict[commands[1]] = (int(alphabet_dict[commands[1]]) if commands[1] in alphabet_dict else int(commands[1])) + (int(alphabet_dict[commands[2]]) if commands[2] in alphabet_dict else int(commands[2]))
        elif commands[0] == 'SUB':
            alphabet_dict[commands[1]] = (int(alphabet_dict[commands[1]]) if commands[1] in alphabet_dict else int(commands[1])) - (int(alphabet_dict[commands[2]]) if commands[2] in alphabet_dict else int(commands[2]))
        elif commands[0] == 'MUL':
            alphabet_dict[commands[1]] = (int(alphabet_dict[commands[1]]) if commands[1] in alphabet_dict else int(commands[1])) * (int(alphabet_dict[commands[2]]) if commands[2] in alphabet_dict else int(commands[2]))
        elif commands[0] == 'IF':
            b = False
            if commands[2] == '==':
                if (int(alphabet_dict[commands[1]]) if commands[1] in alphabet_dict else int(commands[1])) == (int(alphabet_dict[commands[3]]) if commands[3] in alphabet_dict else int(commands[3])):
                    b = True
            elif commands[2] == '!=':
                if (int(alphabet_dict[commands[1]]) if commands[1] in alphabet_dict else int(commands[1])) != (int(alphabet_dict[commands[3]]) if commands[3] in alphabet_dict else int(commands[3])):
                    b = True
            elif commands[2] == '<':
                if (int(alphabet_dict[commands[1]]) if commands[1] in alphabet_dict else int(commands[1])) < (int(alphabet_dict[commands[3]]) if commands[3] in alphabet_dict else int(commands[3])):
                    b = True
            elif commands[2] == '<=':
                if (int(alphabet_dict[commands[1]]) if commands[1] in alphabet_dict else int(commands[1])) <= (int(alphabet_dict[commands[3]]) if commands[3] in alphabet_dict else int(commands[3])):
                    b = True
            elif commands[2] == '>':
                if (int(alphabet_dict[commands[1]]) if commands[1] in alphabet_dict else int(commands[1])) > (int(alphabet_dict[commands[3]]) if commands[3] in alphabet_dict else int(commands[3])):
                    b = True
            elif commands[2] == '>=':
                if (int(alphabet_dict[commands[1]]) if commands[1] in alphabet_dict else int(commands[1])) >= (int(alphabet_dict[commands[3]]) if commands[3] in alphabet_dict else int(commands[3])):
                    b = True
            
            if b and commands[4] == 'JUMP':
                if commands[5][-1] != ':':
                    commands[5] = commands[5] + ':'
                i = program.index(commands[5])
        elif commands[0] == 'JUMP':
            if commands[1][-1] != ':':
                    commands[1] = commands[1] + ':'
            i = program.index(commands[1])
        # else:
        #     if commands[0][-1] == ':':
        #         program[i] = commands[0][:-1]
        #     print(program[i])






        i +=1
    return result 


if __name__ == "__main__":
    program1 = []
    program1.append("MOV A 1")
    program1.append("MOV B 2")
    program1.append("PRINT A")
    program1.append("PRINT B")
    program1.append("ADD A B")
    program1.append("PRINT A")
    program1.append("END")
    result = run(program1)
    print(result)