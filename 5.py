def Horn(w,d,h):
    result = w*d*h/3
    print("부피 >>", result)
    return result
#=====================================================

w = 5
d = 4
h = 5

#print("가로%d,세로%d,높이%d 부피%.2f" %(w,d,h, Horn(w,d,h)))
result = Horn(5, 5, 20)


print(result)
