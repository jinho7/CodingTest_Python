def solution(left, right):
    sum = 0
    for i in range(left, right+1):
        count = 0
        for k in range(1, (i+1)):
            if (i%k == 0):
                count += 1
        
        if (count%2 == 0):
            sum += i
        else:
            sum -= i
            
    return sum

# 바보.. 제곱수의 약수는 홀수개..