def calc_stat(students, team_num, stat_sum):
    mid = team_num * stat_sum // 2

    sums = [[] for _ in range(team_num)]

    for stat in students:

        for s in range(0, team_num-1):

            for n in sums[s+1]:
                sum_stat = n + stat
                if(sum_stat not in sums[s]):
                    sums[s].append(sum_stat)

        if(stat not in sums[team_num-1]):
            sums[team_num-1].append(stat)

    min = abs(sums[0][0] - mid)
    for stat_sums in sums[0]:
        tmp = abs(stat_sums - mid)
        if(tmp<min):
            min = tmp

    return (min+mid) ** 2


n, team_num, stat_sum = map(int, input().split())

students = []
for _ in range(n):
    students.append(int(input().split()[0]))

print(calc_stat(students, team_num, stat_sum))





