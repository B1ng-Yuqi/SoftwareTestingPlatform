from PIL import Image
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
import pandas as pd
import datetime
import time
import re

# import utils
import q10_tran_tree
import q1_triangle
import q2_calendar
import q3_sales_system
import q4_commission
import q5_eshop
import q6_comm_fee
import q7_cs_package
import q8_ERP_system
# import tran_tree
import q16_control_diagram
# import discuss_2
# import eshop_boundary_4
# import cs_package_7
# import scenario_testing_10
import q14_web
import q17_salesman

# import testing_tools as tools

st.sidebar.title('软件测试平台')
option = st.sidebar.selectbox(
    '请选择待测的问题',
    ['1.三角形类型',
     '2.万年历问题',
     '3.讨论题：销售管理系统',
     '4.佣金问题',
     '5.讨论题：电商平台',
     '6.电信收费问题',
     '7.讨论题:C/S系统数据包',
     '8.讨论题：ERP系统问题',
     '9.讨论题：WEB系统问题',
     '10.ATM状态转化问题',
     '11.C语言程序控制流图',
     '12.销售系统问题'])

st.title(option)
if option == "1.三角形类型":
    st.sidebar.markdown(q1_triangle.description)
    s_image = Image.open('./q1_triangle/q1_image/triangle.png')
    # s_image = Image.open('D:\q1\triangle.png')
    st.sidebar.image(s_image, use_column_width=True)
    option2 = st.sidebar.selectbox(
        '选择输入数据的方式',
        ['问题描述', '通过.csv文件输入', '通过文本框输入',
         '边界值分析法', '等价类测试法']
    )
    chart_data = None

    if option2 == '问题描述':
        st.header('问题描述')
        st.markdown(q1_triangle.description)
        image = Image.open('./q1_triangle/q1_image/triangle.png')
        # image = Image.open('D:\q1\triangle.png')
        st.image(image, "按边长划分的三角形类型", use_column_width=True)

    if option2 == '通过.csv文件输入':
        st.header('上传测试文件(.csv)')
        uploaded_file = st.file_uploader("", type="csv")
        if uploaded_file is not None:
            chart_data = pd.read_csv(uploaded_file)
        if st.checkbox('展示测试样例'):
            st.write(chart_data)

    if option2 == '通过文本框输入':
        st.write(q1_triangle.type_of_triangle)
        sample_input = st.text_input(
            '定义自己的测试样本。 例如: 1,2,4:0', ' ')
        real_cols = ["side 1", "side 2", "side 3", "Ground truth"]
        if sample_input != " ":
            real_sample_input = re.split('[,:]', sample_input)
            real_sample_input = np.array([float(x) for x in real_sample_input])
            new_sample = pd.DataFrame(
                real_sample_input.reshape((1, -1)),
                columns=real_cols)
            st.table(new_sample)
            time_start = time.time()
            do_right, real_value, test_value = q1_triangle.is_right(
                real_sample_input, q1_triangle.decide_triangle_type)
            time_end = time.time()
            if do_right:
                st.success(f"测试在 {round((time_end - time_start) * 1000, 2)} ms内完成.")
            else:
                st.error(f"测试失败.- Output: {test_value} ({q1_triangle.type_of_triangle[test_value]})" +
                         f" is expected to  {int(real_value)} ({q1_triangle.type_of_triangle[real_value]})")

    if option2 == '边界值分析法':
        st.header('边界值法')
        st.markdown(q1_triangle.md3)
        chart_data = pd.read_csv("./q1_triangle/q1_test_usecase/三角形-边界值.csv", encoding="gbk")
        # chart_data = pd.read_csv("D:\q1\三角形-边界值.csv", encoding="gbk")
        st.table(chart_data)

    if option2 == '等价类测试法':
        st.header('等价类法')
        st.markdown(q1_triangle.md1)
        st.table(pd.read_csv("./q1_triangle/q1_test_usecase/弱一般等价类.csv"))
        # st.table(pd.read_csv("D:\q1\弱一般等价类.csv"))
        st.markdown(q1_triangle.md2)
        st.table(pd.read_csv("./q1_triangle/q1_test_usecase/额外弱健壮.csv"))
        # st.table(pd.read_csv("D:\q1\额外弱健壮.csv"))
        # st.markdown(r'''所有的测试用例：''')
        chart_data = pd.read_csv("./q1_triangle/q1_test_usecase/三角形-等价类.csv", encoding="gbk")
        # chart_data = pd.read_csv("D:\q1\三角形-等价类.csv", encoding="gbk")
        if st.checkbox('展示测试样例'):
            st.write(chart_data)

    if option2 != '通过文本框输入' and option2 != '问题描述':
        if st.button("开始测试 :)"):
            st.header("测试结果")
            latest_iteration = st.empty()
            bar = st.progress(0)
            if chart_data is None:
                st.warning('数据为空!请检查输入!')
            n_sample = chart_data.shape[0]
            n_right, n_wrong = 0, 0
            time_start = time.time()
            wrong_samples = []
            for i in range(1, n_sample + 1):
                test_sample = chart_data.loc[i - 1].values
                # decide_triangle_type 是每道题的执行函数
                st.set_option('deprecation.showPyplotGlobalUse', False)
                do_right, real_value, test_value = q1_triangle.is_right(test_sample, q1_triangle.decide_triangle_type)
                if do_right:
                    n_right = n_right + 1
                else:
                    n_wrong = n_wrong + 1
                    wrong_samples.append((real_value, test_value, i, test_sample))
                latest_iteration.text(
                    f'Progress: {n_sample}/{i}. Accuracy: {round(n_right / n_sample, 2) * 100}%')
                bar.progress(i / n_sample)
                time.sleep(0.05)
            time_end = time.time()
            if n_right == n_sample:
                text = "tests" if n_sample > 1 else "test"
                st.success(
                    f"{n_sample} {text} passed in {round((time_end - time_start) * 1000 - n_sample * 50, 2)} ms.")
            else:
                if n_right == 0:
                    st.error("All tests failed.")
                else:
                    st.warning(f"{n_right} passed. {n_wrong} failed.")
                for sample in wrong_samples:
                    st.error(f"Test #{sample[2]}: {sample[3]}" +
                             f" - Output: \'{sample[1]} ({q1_triangle.type_of_triangle[sample[1]]})\'" +
                             f" is expected to be \'{int(sample[0])} ({q1_triangle.type_of_triangle[sample[0]]})\'")

            st.header("测试结果分析")
            labels = 'pass', 'failed'
            sizes = [n_right, n_wrong]
            plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
            plt.axis('equal')
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot()

elif option == "2.万年历问题":
    st.sidebar.markdown(r'''输出给定日期的第二天的日期.''')
    option2 = st.sidebar.selectbox(
        '选择输入数据的方式',
        ['问题描述', '通过.csv文件输入', '手动选择日期测试',
         '边界值分析法', '等价类测试法', '扩展决策表']
    )
    date_data = None

    if option2 == '问题描述':
        st.header('问题描述')
        st.markdown(r'''输出给定日期的第二天的日期.''')
        image = Image.open("./q2_calendar/img/calendar.png")
        st.image(image, "Calendar", use_column_width=True)

    elif option2 == '通过.csv文件输入':
        st.header('上传测试文件(.csv)')
        uploaded_file = st.file_uploader("", type="csv")
        if uploaded_file is not None:
            date_data = pd.read_csv(uploaded_file)
        if st.checkbox('展示测试样例'):
            st.write(date_data)

    elif option2 == '手动选择日期测试':
        st.header('手动选择日期')
        date1 = st.date_input("选择任意日期", datetime.date(2021, 6, 25))
        date2 = st.date_input("选择在 " + date1.strftime("%Y/%m/%d") + "后一天的日期", datetime.date(2021, 6, 26))
        if date1 and date2:
            time_start = time.time()
            present_date = q2_calendar.PresentDate(date1.year, date1.month, date1.day)
            output = present_date.add_day(1)
            time_end = time.time()
            st.header('测试结果')
            st.write('Output: ' + output)
            expected_output = date2.strftime("%#Y/%#m/%#d")
            if expected_output == output:
                st.success(f"Test passed in {round((time_end - time_start) * 1000, 2)} ms.")
            else:
                st.error(f"测试失败. Output {output} is expected to be {expected_output}")

    elif option2 == '边界值分析法':
        st.header('边界值法')
        st.markdown(q2_calendar.md1)
        st.table(pd.read_csv("./q2_calendar/基本边界值测试.csv"))
        st.markdown(q2_calendar.md2)
        st.table(pd.read_csv("./q2_calendar/健壮性边界值测试.csv"))
        st.markdown(q2_calendar.md3)
        st.table(pd.read_csv("./q2_calendar/额外测试用例.csv"))
        date_data = pd.read_csv("./q2_calendar/万年历1-边界值.csv", encoding="utf-8")
        if st.checkbox('展示测试样例'):
            st.write(date_data)

    elif option2 == '等价类测试法':
        st.header('等价类法')
        st.markdown(q2_calendar.md4)
        st.table(pd.read_csv("./q2_calendar/强一般等价类.csv"))
        st.markdown(q2_calendar.md5)
        st.table(pd.read_csv("./q2_calendar/额外弱健壮.csv"))
        date_data = pd.read_csv("./q2_calendar/万年历1-等价类.csv", encoding="utf-8")
        if st.checkbox('展示测试样例'):
            st.write(date_data)

    else:
        st.header('扩展决策表')
        st.markdown(q2_calendar.md6)
        table = Image.open("./q2_calendar/img/table.png")
        st.image(table, "万年历扩展决策表", use_column_width=True)
        st.markdown(q2_calendar.md7)
        date_data = pd.read_csv("./q2_calendar/万年历9-扩展决策表.csv", encoding="utf-8")
        st.table(date_data)

    if option2 != '手动选择日期测试' and option2 != '问题描述':
        if st.button("开始测试 :)"):
            st.header("测试结果")
            latest_iteration = st.empty()
            bar = st.progress(0)
            if date_data is None:
                st.warning('数据为空!请检查输入!')
            n_sample = date_data.shape[0]
            n_right, n_wrong = 0, 0
            wrong_samples = []
            time_start = time.time()
            for i in range(1, n_sample + 1):
                year = date_data.loc[i - 1]['year']
                month = date_data.loc[i - 1]['month']
                day = date_data.loc[i - 1]['day']
                expect = date_data.loc[i - 1]['NextDay']
                test_data = q2_calendar.PresentDate(year, month, day)
                output = test_data.add_day(1)
                if expect == output:
                    n_right = n_right + 1
                else:
                    n_wrong = n_wrong + 1
                    wrong_samples.append((output, expect, i, f'{year}/{month}/{day}'))
                latest_iteration.text(
                    f'Progress: {n_sample}/{i}. Accuracy: {round(n_right / n_sample, 2) * 100}%')
                bar.progress(i / n_sample)
                time.sleep(0.05)
            time_end = time.time()
            if n_right == n_sample:
                text = "tests" if n_sample > 1 else "test"
                st.success(
                    f"{n_sample} {text} passed in {round((time_end - time_start) * 1000 - n_sample * 50, 2)} ms.")
            else:
                if n_right == 0:
                    st.error("All tests failed.")
                else:
                    st.warning(f"{n_right} passed. {n_wrong} failed.")
                for sample in wrong_samples:
                    st.error(f"Test #{sample[2]}: {sample[3]} - Output {sample[0]} is expected to be {sample[1]}")

            st.header("测试结果分析")
            labels = "pass", 'failed'
            sizes = [n_right, n_wrong]
            plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
            plt.axis('equal')
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot()

# 销售系统问题（讨论）
elif option == '3.讨论题：销售管理系统':
    st.markdown(q3_sales_system.content)
    st.markdown(q3_sales_system.question1)
    st.markdown(q3_sales_system.question2)
    st.markdown(q3_sales_system.answer1)
    st.markdown(q3_sales_system.answer2)

elif option == '4.佣金问题':
    option2 = st.sidebar.selectbox(
        "选择输入数据的方式",
        ["问题描述", "边界值分析法", '通过.csv文件输入']
    )
    commission_data = None

    if option2 == "问题描述":
        st.header("问题描述")
        st.markdown(q4_commission.description)

    elif option2 == "边界值分析法":
        st.header("边界值法")
        st.markdown(q4_commission.md1)
        st.table(pd.read_csv("q4_commission/基本边界值.csv"))
        st.markdown(q4_commission.md2)
        st.table(pd.read_csv("q4_commission/设备健壮性边界.csv"))
        st.markdown(q4_commission.md3)
        st.table(pd.read_csv("q4_commission/销售额基本边界值.csv"))
        st.markdown(q4_commission.md4)
        commission_data = pd.read_csv("q4_commission/佣金问题-边界值.csv")

    else:
        st.header('通过.csv文件输入')
        uploaded_file = st.file_uploader("", type="csv")
        if uploaded_file is not None:
            commission_data = pd.read_csv(uploaded_file)
        if st.checkbox('展示测试样例'):
            st.write(commission_data)

    if option2 != "问题描述":
        if st.button("开始测试 :)"):
            st.header("测试结果")
            latest_iteration = st.empty()
            bar = st.progress(0)
            if commission_data is None:
                st.warning('数据为空!请检查输入!')
            n_sample = commission_data.shape[0]
            n_right, n_wrong = 0, 0
            wrong_samples = []
            time_start = time.time()
            st.set_option('deprecation.showPyplotGlobalUse', False)
            for i in range(1, n_sample + 1):
                x = commission_data.loc[i - 1]['x']
                y = commission_data.loc[i - 1]['y']
                z = commission_data.loc[i - 1]['z']
                expect = commission_data.loc[i - 1]['q4_commission']
                output = q4_commission.calculate_computer_commission([x, y, z])
                if float(expect) == output:
                    n_right = n_right + 1
                else:
                    n_wrong = n_wrong + 1
                    wrong_samples.append((output, expect, i, f'({x}, {y}, {z})'))
                if float(expect) == -1:
                    n_right = n_sample
                    latest_iteration.text(
                        f'Progress: {n_sample}/{n_sample}. Accuracy: {round(n_right / n_sample, 2) * 100}%')
                    bar.progress(n_sample / n_sample)
                    break
                latest_iteration.text(
                    f'Progress: {n_sample}/{i}. Accuracy: {round(n_right / n_sample, 2) * 100}%')
                bar.progress(i / n_sample)
                time.sleep(0.01)
            time_end = time.time()
            if n_wrong == 0:
                text = "tests" if n_sample > 1 else "test"
                st.success(
                    f"{n_sample} {text} passed in {round((time_end - time_start) * 1000 - n_sample * 10, 2)} ms.")
            else:
                if n_right == 0:
                    st.error("All tests failed.")
                else:
                    st.warning(f"{n_right} passed. {n_wrong} failed.")
                for sample in wrong_samples:
                    st.error(f"Test #{sample[2]}: {sample[3]} - Output {sample[0]} is expected to be {sample[1]}")

            st.header("测试结果分析")
            labels = 'pass', 'fail'
            sizes = [n_right, n_wrong]
            plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
            plt.axis('equal')
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot()


elif option == '5.讨论题：电商平台':
    st.markdown(q5_eshop.content)
    st.markdown(q5_eshop.answer)
    st.markdown(q5_eshop.table)

elif option == '6.电信收费问题':
    option2 = st.sidebar.selectbox(
        "选择输入数据的方式",
        ["问题描述", '通过.csv文件输入', "边界值分析法",
         '等价类测试法', '决策表法', '总结']
    )
    charges_data = None

    if option2 == "问题描述":
        st.header("问题描述")
        st.markdown(q6_comm_fee.description)

    elif option2 == '通过.csv文件输入':
        st.header('上传测试文件(.csv)')
        uploaded_file = st.file_uploader("", type="csv")
        if uploaded_file is not None:
            charges_data = pd.read_csv(uploaded_file)
        if st.checkbox('展示测试样例'):
            st.write(charges_data)

    elif option2 == "边界值分析法":
        st.markdown(q6_comm_fee.statement)
        st.header("边界值分析法")
        st.markdown(q6_comm_fee.boundary1)
        st.table(pd.read_csv("./q6_comm_fee/基本边界值.csv"))
        st.markdown(q6_comm_fee.boundary2)
        st.table(pd.read_csv("./q6_comm_fee/健壮性边界.csv"))
        charges_data = pd.read_csv("./q6_comm_fee/电信收费问题-边界值.csv")

    elif option2 == '等价类测试法':
        st.markdown(q6_comm_fee.statement)
        st.header("等价类测试法")
        st.markdown(q6_comm_fee.equivalence1)
        st.table(pd.read_csv("./q6_comm_fee/强一般等价类.csv"))
        st.markdown(q6_comm_fee.equivalence2)
        st.table(pd.read_csv("./q6_comm_fee/额外弱健壮.csv"))
        charges_data = pd.read_csv("./q6_comm_fee/电信收费问题-等价类.csv")

    elif option2 == '决策表法':
        st.markdown(q6_comm_fee.statement)
        st.header("决策表测试法")
        st.markdown(q6_comm_fee.dt1)
        charges_data = pd.read_csv("./q6_comm_fee/电信收费问题-扩展决策表.csv")
        st.table(charges_data)

    else:
        st.header("总结")
        st.markdown(q6_comm_fee.conclusion)
        charges_data = pd.read_csv("./q6_comm_fee/电信收费问题-综合.csv")
        st.text("综合的测试用例：")
        st.table(charges_data)

    if option2 != "问题描述":
        if st.button("开始测试 :)"):
            st.header("测试结果")
            latest_iteration = st.empty()
            bar = st.progress(0)
            if charges_data is None:
                st.warning('数据为空!请检查输入!')
            charges_data = charges_data.fillna(-1)
            n_sample = charges_data.shape[0]
            n_right, n_wrong = 0, 0
            wrong_samples = []
            time_start = time.time()
            for i in range(1, n_sample + 1):
                minutes = charges_data.loc[i - 1]['T']
                n_overdue = charges_data.loc[i - 1]['M']
                unpaid_fee = charges_data.loc[i - 1]['L']
                discount = charges_data.loc[i - 1]['Discount']
                extra_rate = charges_data.loc[i - 1]['Extra']
                expect = charges_data.loc[i - 1]['Pay']
                output = q6_comm_fee.calculate_comm_fee([minutes, n_overdue, unpaid_fee, discount, extra_rate])
                # if float(expect) == round(output, 2):
                #     n_right = n_right + 1
                if float(expect) - output <= 0.01:
                    n_right = n_right + 1
                else:
                    n_wrong = n_wrong + 1
                    wrong_samples.append((output, expect, i, f'{minutes, n_overdue, unpaid_fee}'))
                latest_iteration.text(
                    f'Progress: {n_sample}/{i}. Accuracy: {round(n_right / n_sample, 2) * 100}%')
                bar.progress(i / n_sample)
                time.sleep(0.01)
            time_end = time.time()
            if n_right == n_sample:
                text = "tests" if n_sample > 1 else "test"
                st.success(
                    f"{n_sample} {text} passed in {round((time_end - time_start) * 1000 - n_sample * 10, 2)} ms.")
            else:
                if n_right == 0:
                    st.error("All tests failed.")
                else:
                    st.warning(f"{n_right} passed. {n_wrong} failed.")
                for sample in wrong_samples:
                    st.error(f"Test #{sample[2]}: {sample[3]} - Output {sample[0]} is expected to be {sample[1]}")

            st.header("测试结果分析")
            labels = 'pass', 'fail'
            sizes = [n_right, n_wrong]
            plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
            plt.axis('equal')
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.pyplot()

elif option == '7.讨论题:C/S系统数据包':
    option2 = st.sidebar.selectbox(
        "请选择想要查看的部分",
        ["问题描述", "讨论&答案"]
    )
    st.header(option2)
    if option2 == "问题描述":
        st.markdown(q7_cs_package.content)
    elif option2 == "讨论&答案":
        st.markdown(q7_cs_package.answers)

elif option == '10.ATM状态转化问题':
    option2 = st.sidebar.selectbox(
        "请选择想要查看的部分",
        ["问题描述", "ATM"]
    )
    st.header(option2)
    if option2 == "问题描述":
        st.markdown(q10_tran_tree.content)
    if option2 == "ATM":
        st.subheader("状态图")
        atm1 = Image.open("./q10_tran_tree/img/ATM1.png")
        st.image(atm1, "ATM 状态图", use_column_width=True)
        st.write(q10_tran_tree.state_diagram)
        st.subheader("Transition Tree")
        st.code(q10_tran_tree.code, language='python')
        if st.button("run"):
            st.write(q10_tran_tree.tran_tree(q10_tran_tree.state_diagram))
            atm2 = Image.open("./q10_tran_tree/img/ATM2.png")
            st.image(atm2, "ATM Transition Tree", use_column_width=True)
        st.subheader("状态表")
        st.markdown(q10_tran_tree.md)

# ERP系统（讨论）
elif option == '8.讨论题：ERP系统问题':
    option2 = st.sidebar.selectbox(
        "请选择想要查看的部分",
        ["问题描述", "主/备选流关系图", "基本流&备选流表", "场景设计列表", "逻辑测试用例列表"]
    )
    st.header(option2)
    if option2 == "问题描述":
        st.markdown(q8_ERP_system.content)
        dia = Image.open("./q8_ERP_system/q8_image/flowchart.png")
        st.image(dia, "系统流程图", use_column_width=True)
    elif option2 == "主/备选流关系图":
        dia = Image.open("./q8_ERP_system/q8_image/stream.jpg")
        st.image(dia, "主/备选流关系图", use_column_width=True)
    elif option2 == "基本流&备选流表":
        st.markdown(q8_ERP_system.basic_list)
    elif option2 == "场景设计列表":
        st.markdown(q8_ERP_system.scene_list)
    elif option2 == "逻辑测试用例列表":
        st.markdown(q8_ERP_system.logic_usecase)


elif option == '9.讨论题：WEB系统问题':
    option2 = st.sidebar.selectbox(
        "请选择想要查看的部分",
        ["问题描述", "状态因素表", "正交表", "测试用例"]
    )
    st.header(option2)
    if option2 == "问题描述":
        st.markdown(q14_web.content)
    elif option2 == "状态因素表":
        st.markdown(q14_web.table1)
    elif option2 == "正交表":
        st.markdown(q14_web.table2)
    elif option2 == "测试用例":
        st.markdown(q14_web.table3)

elif option == '11.C语言程序控制流图':
    st.header("Code")
    st.code(q16_control_diagram.code, language="C")
    st.header("控制流图")
    dia = Image.open("./q16_control_diagram/img/diagram.jpg")
    st.image(dia, "控制流图", use_column_width=True)


elif option == '12.销售系统问题':
    option2 = st.sidebar.selectbox(
        "选择输入数据的方式",
        ["问题描述", "流程图", "语句覆盖", "判断覆盖",
         "条件覆盖", "判断—条件覆盖", "条件组合覆盖"]
    )
    salesman_data = None

    if option2 == "问题描述":
        st.header("问题描述")
        st.markdown(q17_salesman.description)

    elif option2 == "流程图":
        st.header("流程图")
        flowchart = Image.open("q17_salesman/img/flowchart.png")
        st.image(flowchart, "流程图", use_column_width=True)

    elif option2 == "语句覆盖":
        st.header("语句覆盖")
        st.markdown(q17_salesman.statement)
        salesman_data = pd.read_csv("q17_salesman/销售系统-语句覆盖.csv")

    elif option2 == "判断覆盖":
        st.header("判断覆盖")
        st.markdown(q17_salesman.branch)
        salesman_data = pd.read_csv("q17_salesman/销售系统-判断覆盖.csv")

    elif option2 == "条件覆盖":
        st.header("条件覆盖")
        st.markdown(q17_salesman.condition)
        salesman_data = pd.read_csv("q17_salesman/销售系统-条件覆盖.csv")

    elif option2 == "判断——条件覆盖":
        st.header("判断——条件覆盖")
        st.markdown(q17_salesman.condition_determination)
        salesman_data = pd.read_csv("q17_salesman/销售系统-判断-条件覆盖.csv")

    else:
        st.header("条件组合覆盖")
        st.markdown(q17_salesman.multiple_condition)
        salesman_data = pd.read_csv("q17_salesman/销售系统-条件组合覆盖.csv")

    if "覆盖" in option2:
        if st.button("开始测试 :)"):
            st.header("测试结果")
            latest_iteration = st.empty()
            bar = st.progress(0)
            n_sample = salesman_data.shape[0]
            n_right, n_wrong = 0, 0
            wrong_samples = []
            time_start = time.time()
            for i in range(1, n_sample + 1):
                sales = salesman_data.loc[i - 1]['Sales']
                cash_ratio = salesman_data.loc[i - 1]['CashRatio']
                cash_ratio = float(cash_ratio.strip('%')) / 100
                n_leave = salesman_data.loc[i - 1]['LeaveDays']
                expect = salesman_data.loc[i - 1]['q4_commission']
                output = q17_salesman.calculate_commission([sales, cash_ratio, n_leave])
                if float(expect) - output <= 0.01:
                    n_right = n_right + 1
                else:
                    n_wrong = n_wrong + 1
                    wrong_samples.append((output, expect, i, f'{sales, cash_ratio, n_leave}'))
                latest_iteration.text(
                    f'Progress: {n_sample}/{i}. Accuracy: {round(n_right / n_sample, 2) * 100}%')
                bar.progress(i / n_sample)
                time.sleep(0.01)
            time_end = time.time()
            if n_right == n_sample:
                text = "tests" if n_sample > 1 else "test"
                st.success(
                    f"{n_sample} {text} passed in {round((time_end - time_start) * 1000 - n_sample * 10, 2)} ms.")
            else:
                if n_right == 0:
                    st.error("All tests failed.")
                else:
                    st.warning(f"{n_right} passed. {n_wrong} failed.")
                for sample in wrong_samples:
                    st.error(f"Test #{sample[2]}: {sample[3]} - Output {sample[0]} is expected to be {sample[1]}")

            st.header("测试结果分析")
            labels = 'pass', 'fail'
            sizes = [n_right, n_wrong]
            plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
            plt.axis('equal')
            st.pyplot()
