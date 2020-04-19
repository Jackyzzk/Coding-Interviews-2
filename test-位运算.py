
n = t = x = u = 0b11100
# 获得最后一位1连同它的位，然后被减掉变成0
n -= n & (~n + 1)
x -= x & (-x)
# 把最后一位 1 去掉
t &= (t - 1)
print(bin(n), bin(t), bin(x))
print(bin(u), bin(u & -u), bin(u & (~u + 1)))

num = 0b11011
n = 2
# 将第n位变为1
ret = num | (1 << n)
print(bin(ret))

num = 0b11011
n = 2
# 将第n位变为0
ret = num & ~(1 << n)
print(bin(ret))





