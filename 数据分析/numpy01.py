import numpy as np
import random

# 创建数组的三种方法
t1 = np.array([1, 2, 3, 4])
t2 = np.array(range(10))
t3 = np.arange(10)

print(t3, t2, t1)
print(type(t3))  # 数组类型
print(t3.dtype)  # 数据类型

'''
bool_	布尔型数据类型（True 或者 False） 
int_	默认的整数类型（类似于 C 语言中的 long，int32 或 int64）
intc	与 C 的 int 类型一样，一般是 int32 或 int 64
intp	用于索引的整数类型（类似于 C 的 ssize_t，一般情况下仍然是 int32 或 int64）
int8	字节（-128 to 127）
int16	整数（-32768 to 32767）
int32	整数（-2147483648 to 2147483647）
int64	整数（-9223372036854775808 to 9223372036854775807）
uint8	无符号整数（0 to 255）
uint16	无符号整数（0 to 65535）
uint32	无符号整数（0 to 4294967295）
uint64	无符号整数（0 to 18446744073709551615）
float_	float64 类型的简写
float16	半精度浮点数，包括：1 个符号位，5 个指数位，10 个尾数位
float32	单精度浮点数，包括：1 个符号位，8 个指数位，23 个尾数位
float64	双精度浮点数，包括：1 个符号位，11 个指数位，52 个尾数位
complex_	complex128 类型的简写，即 128 位复数
complex64	复数，表示双 32 位浮点数（实数部分和虚数部分）
complex128	复数，表示双 64 位浮点数（实数部分和虚数部分）'''

t4 = np.arange(10, dtype="float")  # 指定数据类型
print(t4, t4.dtype)

t5 = t4.astype("int8")  # 更改数据类型
print(t5, t5.dtype)

t6 = np.array([random.random() for i in range(10)])
print(t6, t6.dtype)

t7 = np.round(t6, 3)  # 取小数
print(t7, t7.dtype)
t8 = round(random.random(), 2)  # python取小数
print(t8)
