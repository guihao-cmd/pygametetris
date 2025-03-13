def change(a):
    a = 1

aa = 0
change(aa)
print(aa)




# 数组
# <别称>
# 地址  0  1  2
# 值   [1, 0, 3]     

list_test = [1, 2, 3]
list_test[1] = 0




# <别称>    ll  l
# 地址  0   1   2
# 值   [1]  0   0
def change_list(l):
    l[0] = 1
ll = [0]
change_list(ll)
print(ll)


# 地址<别称> 0   1<l2> 2<ll> 3 [临时], 4   5
# 值        []   0     3     [1, 2, 3]


def create_list(ll):
    ll = [1, 2, 3]

l2 = []
create_list(l2)
print(l2)

def return_list():
    return [1, 2, 3]
lx = return_list()
print(lx)