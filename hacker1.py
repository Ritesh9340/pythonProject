if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
n = list(arr)
score = []
for i in n:
    if i < max(n):
        score.append(i)

score.sort(reverse=True)
print(score[0])

