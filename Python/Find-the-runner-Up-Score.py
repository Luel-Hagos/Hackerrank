n = int(input())
arr = list(map(int, input().split()))
my_set=set()
for i in range(n):
	my_set.add(arr[i])
k=max(my_set)
my_set.remove(k)
print(max(my_set))