def fly_space(distance):
    warp_time = 0
    sum = 0
    while(sum<distance):
        sum += (warp_time-1)//2 + 1
        warp_time += 1
        # print(sum)

    return warp_time-1




n = int(input())
for i in range(n):
    w, v = map(int, input().split())
    print(fly_space(v-w))