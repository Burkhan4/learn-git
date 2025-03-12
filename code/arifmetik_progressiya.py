n = int(input())

s = [int(n) for n in input().split()]


if n ==1:
    print("yes")
else:
    d = s[1]-s[0]
    for i in range (1,n-1):
        if s[i+1] - s[i] != d:
            print("no")
            break
    else:
            print("yes")