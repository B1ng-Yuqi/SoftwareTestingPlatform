def is_right(test_sample, tfunc):
    real_value = test_sample[-1]
    test_value = tfunc(test_sample[:-1])
    if real_value == test_value:
        return True, real_value, test_value
    else:
        return False, real_value, test_value


type_of_triangle = {
    0: '超出范围',
    1: '非三角形',
    2: '普通三角形',
    3: '等腰三角形',
    4: '等边三角形'
}

description = r'''输入三角形的三条边并确定它们是否可以形成三角形。
                如果是的话，根据三角形边的长度来判断三角形的类型。'''


# 每道题的input都是一个 np.array,其中最后一个值是输出值
#  0 不在范围
#  1 非三角形
#  2 啥都不等
#  3 等腰
#  4 等边
def decide_triangle_type(test_sample):
    line1, line2, line3 = test_sample
    if not (1 <= line1 <= 200 and 1 <= line2 <= 200 and 1 <= line3 <= 200):
        return 0
    # elif max(test_sample) >= sum(test_sample) - max(test_sample):
    #     return 1

    # 人工注入bug
    elif max(test_sample) > sum(test_sample) - max(test_sample):
        return 1
    else:
        lines = list(set([line1, line2, line3]))
        n_line = len(lines)
        if n_line == 1:
            return 4
        elif n_line == 2:
            return 3
        elif n_line == 3:
            return 2