# Enter your code here. Read input from STDIN. Print output to STDOUT
# Enter your code here. Read input from STDIN. Print output to STDOUT

q = int(input())
s = ""
history = []

for _ in range(q):
    operation = input().split()
    op_type = operation[0]

    if op_type == '1':  # append
        history.append(s)
        s += operation[1]

    elif op_type == '2':  # delete
        history.append(s)
        k = int(operation[1])
        s = s[:-k]

    elif op_type == '3':  # print
        k = int(operation[1])
        print(s[k - 1])

    elif op_type == '4':  # undo
        s = history.pop()
