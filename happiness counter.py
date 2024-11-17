#You gain  unit of happiness for elements  and  in set . You lose  unit for  in set . The element  in set  does not exist in the array so it is not included in the calculation.Hence, the total happiness is .
n, m = map(int, input().split())
array = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int, input().split()))
happiness = 0

for i in array:
    if i in a:  # Check if the current number is in set `a`
        happiness += 1
    elif i in b:  # Check if the current number is in set `b`
        happiness -= 1

print(happiness)  # Print happiness after the loop
