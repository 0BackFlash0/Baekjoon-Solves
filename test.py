def clockwise(a, b, c):
    v1 = [a[0]-b[0], a[1]-b[1]]
    v2 = [c[0]-b[0], c[1]-b[1]]

    cross_product_z = v1[0]*v2[1] - v1[1]*v2[0]

    if(cross_product_z>0):
        return -1
    elif(cross_product_z==0):
        return 0
    else:
        return 1


a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

print(clockwise(a, b, c))