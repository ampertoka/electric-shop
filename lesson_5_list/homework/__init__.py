nums = [1, 2, 3]
print(nums[1])
print(nums[-1])
nums[-1] = 10
print(nums)
print(len(nums))
colors = ["red", "green"]
colors.append("blue")
print(colors)
last_color = colors.pop()
print(colors)
print(last_color)
colors.remove("green")
print(colors)
print(last_color)

a = [1, 2, 3, 4]
a[2] = 99
print(a)
a.insert(1, 100)
print(a)

nums = [3, 1, 5, 2, 4]
nums.sort()
nums.sort(reverse=True)
print(nums)

words = ["aac", "aab", "ab", "az"]
words.sort()
print(words)

a = [1, 2, 3]
b = [4, 5]
for i in b:
    a.append(i)

print(a)

a = [1, 2, 3]
a.extend(b)
print(a)

vals = [1, 1, 2, 3, 3]
print(vals.count(1))

arr = [1, 2, 3, 4, 2]
print(arr.index(2))

if 10 in arr:
    print(arr.index(10))
else:
    print("не найдено")

arr = [1, 2, 3, 4, 5]
sub_arr = arr[1:3]
del arr[1:3]
print(sub_arr)
print(arr)
print()

a = [1, 2, 3, 4, 5, 6, 7, 8]
res_1 = a[0:len(a):3]
print(res_1)
res_2 = a[::3]
print(res_2)
print()

data = [3, 1, 5, 2, 4]
data_copy = data.copy()
data_copy.clear()
print(data)
data[0] = 10
data.insert(0, 0)
data.remove(5)
data.extend([8, 1.5])
data.sort(reverse=True)
print(data)
top_3 = data[0:3]
print(top_3)