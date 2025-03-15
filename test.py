# Codeforces point system
n = int(input())
initial_scores = list(map(int, input().split()))
points_deducted = list(map(int, input().split()))
minimum_scores = list(map(int, input().split()))
time_submissions = []
for _ in range(n):
    time_submissions.append(list(map(int, input().split())))
score = []
for i in range(n):
    if time_submissions[i][1] < 0 or time_submissions[i][1] == 0:
        score.append(0)
    else:
        score.append(max(minimum_scores[i], initial_scores[i] - points_deducted[i] * time_submissions[i][0] - 50 * (time_submissions[i][1] - 1 )))

print(sum(score))

