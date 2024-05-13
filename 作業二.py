import random

# 輸入三角形的三邊長
a = random.randrange(2,10,1)
b = random.randrange(2,10,1)
c = random.randrange(2,10,1)

# 檢查三邊能否形成三角形
triangle = False
if a + b > c and b + c > a and c + a > b:
    triangle = True
print('a的長:',a)
print('b的長:',b)
print('c的長:',c)
if triangle:
    print("這些邊可以形成一個三角形。")

    # 檢查是否為直角三角形
    right_triangle = False
    sides = [a, b, c]

    for side in sides:
        if side ** 2 == sides[0] ** 2 + sides[1] ** 2:
            right_triangle = True
            break  # 找到直角三角形後退出迴圈

    if right_triangle:
        print("這是一個直角三角形。")
    else:
        print("這不是一個直角三角形。")
else:
    
    print("這些邊無法形成一個三角形。")


