import math

def clear_snow(_snow_list):
    snow_list = _snow_list

    max_snow = max(snow_list)
    rest_snow = sum(snow_list)-max_snow
    result = 0

    if(max_snow>rest_snow):
        result = max_snow
    else:
        result = math.ceil((rest_snow - max_snow)/2) + max_snow

    if(result>1440):
        return -1
    else:
        return result


n = int(input())
snow_list = list(map(int, input().split()))

print(clear_snow(snow_list))
