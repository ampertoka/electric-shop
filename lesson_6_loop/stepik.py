a = list(map(int, input().zfill(6)))
if sum(a[:-3]) == sum(a[-3:]):
    print('YES')
else:
    print('NO')