N = int(input())
K = int(input())
time_outs = [None for x in range(K)]
for i in range(N):
    name, time_in, time_out = input().split()
    for j in range(K):
        if time_outs[j] > time_in or \
                time_outs[j] is None:
            print(name, j)
            time_outs[j] = time_out
            break
