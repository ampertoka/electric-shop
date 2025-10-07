lst_lst = [[1, 2, 3], [56, 6, 5], [8, 9, 3]]

for a, b, c in lst_lst:
    print(f'a = {a}, b = {b}, c = {c}')

for i, v in enumerate(lst_lst):
    if i % 2 == 0:
        print(v)
