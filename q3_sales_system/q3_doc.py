content = r'''
    在一销售管理系统中，其中的一个模块负责对公司员工进行年终考评，考评综合考虑职工在公司工作时间长短（计年）、每年请假的次数（不能超过20天，20天以上，包括20天，则免于年终考评）、员工在公司的级别（分1，2，3，4，5个级别）及本年度的销售总额，考评的结果最高以5分计，公司成立于2000年初，该软件的设计使用周期到2025年底，请回答下列问题：
'''

question1 = r'''(1)	用基本边界值的测试方法，一共有多少测试用例；最坏情况边界值有多少测试用例。'''

question2 = r'''(2)	根据健壮的边界值测试法，写出“工作时间长短”为非正常值情况下的测试用例。'''


answer1 = r'''解答:

(1) 基本边界值的测试用例：四个变量 4n+1 = 17 

最坏情况边界值：5的n次， 5的四次 = 625'''

answer2 = r'''(2)

| 序号 | 测试用例（工作时间长短，请假次数，员工级别，年度销售总额） | 预期输出                 | 实际输出 |
| ---- | ---------------------------------------------------------- | ------------------------ | -------- |
| 1    | -1，5，3，20                                               | 工作时间长短取值超出范围 | 越界     |
| 2    | 1，5，3，20                                                | 正常计分                 | 正常计分 |
| 3    | 2，5，3，20                                                | 正常计分                 | 正常计分 |
| 4    | 10，5，3，20                                               | 正常计分                 | 正常计分 |
| 5    | 20，5，3，20                                               | 正常计分                 | 正常计分 |
| 6    | 21，5，3，20                                               | 正常计分                 | 正常计分 |
| 7    | 30，5，3，20                                               | 工作时间长短取值超出范围 | 越界     |'''
