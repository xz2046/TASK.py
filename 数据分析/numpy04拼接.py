import numpy as np

t1 = np.arange(15).reshape(3, 5)
t2 = np.arange(15, 30).reshape(3, 5)
t3 = np.vstack((t1, t2))  # 竖直拼接
print(t3)
print("-" * 100)
t4 = np.hstack((t1, t2))  # 水平拼接
print(t4)
print("-" * 100)
t1[[1, 2], :] = t1[[2, 1], :]  # 行交换
print(t1)
print("-" * 100)
t2[:, [3, 4]] = t2[:, [4, 3]]  # 列交换
print(t2)
print("-" * 100)
t5 = np.zeros((2, 3))  # 创建一个全是零的数组
print(t5)
print("-" * 100)
t6 = np.ones((2, 4))  # 创建一个全是一的数组
print(t6)
print("-" * 100)
t7 = np.eye(5)  # 创建一个对角线为一的正方形数组
print(t7)
print("-" * 100)
a = np.argmax(t3, axis=0)  # 求行列最大值位置
b = np.argmin(t3, axis=1)
print(a, b)
t8 = t7.copy()  # 相互不影响
# 生成随机数
'''rand(d0, d1, …, dn)	产生均匀分布的随机数	dn为第n维数据的维度
randn(d0, d1, …, dn)	产生标准正态分布随机数	dn为第n维数据的维度
randint(low[, high, size, dtype])	产生随机整数	low：最小值；high：最大值；size：数据个数
random_sample([size])	在[0,1）内产生随机数	size：随机数的shape，可以为元祖或者列表，[2,3]表示2维随机数，维度为（2,3）
random([size])	同random_sample([size])	同random_sample([size])
ranf([size])	同random_sample([size])	同random_sample([size])
sample([size]))	同random_sample([size])	同random_sample([size])
choice(a[, size, replace, p])	从a中随机选择指定数据	a：1维数组 size：返回数据形状
bytes(length)	返回随机位	length：位的长度'''
'''numpy.random模块提供了产生各种分布随机数的API：

函数名称	函数功能	参数说明
beta(a, b[, size])	贝塔分布样本，在 [0, 1]内。	 
binomial(n, p[, size])	二项分布的样本。	 
chisquare(df[, size])	卡方分布样本。	 
dirichlet(alpha[, size])	狄利克雷分布样本。	 
exponential([scale, size])	指数分布	 
f(dfnum, dfden[, size])	F分布样本。	 
gamma(shape[, scale, size])	伽马分布	 
geometric(p[, size])	几何分布	 
gumbel([loc, scale, size])	耿贝尔分布。	 
hypergeometric(ngood, nbad, nsample[, size])	超几何分布样本。	 
laplace([loc, scale, size])	拉普拉斯或双指数分布样本	 
logistic([loc, scale, size])	Logistic分布样本	 
lognormal([mean, sigma, size])	对数正态分布	 
logseries(p[, size])	对数级数分布。	 
multinomial(n, pvals[, size])	多项分布	 
multivariate_normal(mean, cov[, size])	多元正态分布。	 
negative_binomial(n, p[, size])	负二项分布	 
noncentral_chisquare(df, nonc[, size])	非中心卡方分布	 
noncentral_f(dfnum, dfden, nonc[, size])	非中心F分布	 
normal([loc, scale, size])	正态(高斯)分布	 
pareto(a[, size])	帕累托（Lomax）分布	 
poisson([lam, size])	泊松分布	 
power(a[, size])	Draws samples in [0, 1] from a power distribution with positive exponent a - 1.	 
rayleigh([scale, size])	Rayleigh 分布	 
standard_cauchy([size])	标准柯西分布	 
standard_exponential([size])	标准的指数分布	 
standard_gamma(shape[, size])	标准伽马分布	 
standard_normal([size])	标准正态分布 (mean=0, stdev=1).	 
standard_t(df[, size])	Standard Student’s t distribution with df degrees of freedom.	 
triangular(left, mode, right[, size])	三角形分布	 
uniform([low, high, size])	均匀分布	 
vonmises(mu, kappa[, size])	von Mises分布	 
wald(mean, scale[, size])	瓦尔德（逆高斯）分布	 
weibull(a[, size])	Weibull 分布	 
zipf(a[, size])	齐普夫分布'''


