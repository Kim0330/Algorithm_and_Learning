import sys

# order
N = int(sys.stdin.readline())
stack = []
for _ in range(N):
    n = list(map(int, sys.stdin.readline().split()))
    if n[0] == 1:
        stack.append(n[1])

    elif n[0] == 2:
        if stack:
            a = stack.pop()
            print(a)

        else:
            print(-1)

    elif n[0] == 3:
        print(len(stack))

    elif n[0] == 4:
        if stack:
            print(0)
        else:
            print(1)

    elif n[0] == 5:
        if stack:
            print(stack[-1])
        else:
            print(-1)