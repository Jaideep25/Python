test_list = [1,3,5,6,3,5,6,1]
res = []
for i in test_list:
    if i not in res:
        res.append(i)
        print(res)

L = []
for i in range(1, 99999999999999999999999):
    L.append(i*i)
    print(L)
