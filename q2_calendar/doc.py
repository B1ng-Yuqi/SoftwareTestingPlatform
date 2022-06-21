md1 = r'''基本边界值测试用例13个

year(1970-2070)的基本边界（最小值，略高于最小值、正常值、略低于最大值和最大值）分别为:  1970, 1971, 2020, 2069, 2070

Month的基本边界（最小值，略高于最小值、正常值、略低于最大值和最大值）: 1(31),  2(28/29), 6(30), 11(30),  12(31)

Day的基本边界（最小值，略高于最小值、正常值、略低于最大值和最大值）: 1, 2, 16, 30, 31'''


md2 = r'''健壮性边界测试用例：新增6个

Day的健壮性边界（略小于最小值，略超过最大值）: 0, 32

Month的健壮性边界（略小于最小值，略超过最大值）: 0, 13

Year的健壮性边界（略小于最小值，略超过最大值）:  1969, 2071'''


md3 = r'''考虑到一些跨年和平闰年2月天数的特殊性，增加了一些额外补充测试用例：'''


md4 = r'''有效等价类：

year：{year = 平年}，{year = 闰年}

month：{month = 31日月}，{month = 30日月}，{month = 2月}

day:{1<=day<=28}，{day = 29}，{day = 30}，{day = 31}

无效等价类：

year：{year < 1}，{year > 2100}

month：{month < 1}, {month  > 12}

day: {day < 1}, {day > 31}

强一般等价类测试用例 24个'''


md5 = r'''额外弱健壮部分的测试用例：6个'''


md6 = r'''条件：Y年份、M月份、D日期

Y1:{平年}; Y2:{被4整除但不被100整除的闰年} Y3:{被400整除的闰年} 

M1:{1,3,5,7,8,10}; M2:{4,6,9,11}; M3:{2}; M4:{12}

D1:{1-27}; D2:{28}; D3:{29}; D4:{30}; D5:{31}

行动：

A1: 输入无效

A2: 本年本月的下一天

A3: 输出本年下个月第一天

A4: 输出下一年的1月1日

扩展决策表
'''


md7 = r'''测试用例集13个测试用例：'''
