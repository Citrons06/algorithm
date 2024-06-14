def hanjo(idx, peak):

    cnt = 0
    for i in range(idx + 1, len(peaks)):
        if peak > peaks[i]:
            cnt += 1
        else:
            break

    return cnt

n = int(input())
peaks = list(map(int, input().split()))

idx = 0
kill = []
for peak in peaks:

    kill.append(hanjo(idx, peak))
    idx += 1

print(max(kill))