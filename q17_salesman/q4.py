description = r'''一销售系统，如果销售员的年销售额大于200万RMB且请假天数不超过10天的情况下，现金到帐大于等于60%，则佣金（提成）系数为7，即佣金值为销售额除以佣金系数；现金到帐小于60
%，佣金不予计算。所有其他情况且现金到帐小于等于85%，则按佣金系数均为6计算佣金，现金到账大于85%，佣金系数按5处理。 根据题意设计流程图并设计测试用例实现白盒测试（White Box Test）

1. 语句覆盖

2. 判断覆盖

3. 条件覆盖 

4. 判断—条件覆盖

5. 条件组合覆盖

(测试用例及覆盖表示要清晰） 
'''


def calculate_commission(test_sample):
    sales, cash_ratio, n_leave = test_sample
    if sales > 200 and n_leave <= 10:
        if cash_ratio >= 0.6:
            commission = round(sales/7, 2)
        else:
            commission = 0

    else:
        if cash_ratio <= 0.85:
            commission = round(sales/6, 2)
        else:
            commission = round(sales/5, 2)

    return commission


if __name__ == "__main__":
    print(calculate_commission([300, 0.6, 9]))
