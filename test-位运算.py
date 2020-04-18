
n = t = x = 0b11100
n -= n & (~n + 1)
x -= x & (-x)
t &= (t - 1)
print(bin(n), bin(t), bin(x))

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





