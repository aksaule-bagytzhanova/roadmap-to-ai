# import math
# fun = lambda x : 1 if x == 1 else math.ceil(math.sinh(fun (x-1)))
# print(fun(5))


# from scipy.stats import stats
#
# A = """X Y
# 4 2
# 5 1
# 2 4
# 3 3
# 1 5"""
#
# x, y = [], []
#
# [(x.append(int(a[0])), y.append(int(a[2]))) for a in A.split('\n') if a[0].isdigit()]
#
# print(stats.pearsonr(x,y)[0])

re = [0,1,2,2,3,0,4,2]
list_t = []
n = 2
for i in re:
    if i!=n:
        list_t.append(i)
print(list_t)