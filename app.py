from PIL import Image
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
import pandas as pd
import datetime
import time
import re

# import utils
import q1_triangle
#import myCalendar
#import commission
#import comm_fee
import q3_sales_system
#import tran_tree
#import q9
#import discuss_2
#import eshop_boundary_4
#import cs_package_7
#import scenario_testing_10
#import cs_web_11
#import testing_tools as tools

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
    #s_image = Image.open('./q1_triangle/q1_image/triangle.png')
    #s_image = Image.open('D:\q1\triangle.png')
    #st.sidebar.image(s_image, use_column_width=True)
    option2 = st.sidebar.selectbox(
        '选择输入数据的方式',
        ['问题描述', '通过.csv文件输入', '通过文本框输入',
         '边界值分析法', '等价类测试法']
    )
    chart_data = None

    if option2 == '问题描述':
        st.header('问题描述')
        st.markdown(q1_triangle.description)
        #image = Image.open('./q1_triangle/q1_image/triangle.png')
        #image = Image.open('D:\q1\triangle.png')
        #st.image(image, "按边长划分的三角形类型", use_column_width=True)

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
        #chart_data = pd.read_csv("./q1_triangle/q1_test_usecase/三角形-边界值.csv", encoding="gbk")
        chart_data = pd.read_csv("D:\q1\三角形-边界值.csv", encoding="gbk")
        st.table(chart_data)

    if option2 == '等价类测试法':
        st.header('等价类法')
        st.markdown(q1_triangle.md1)
        #st.table(pd.read_csv("./q1_triangle/q1_test_usecase/弱一般等价类.csv"))
        st.table(pd.read_csv("D:\q1\弱一般等价类.csv"))
        st.markdown(q1_triangle.md2)
        #st.table(pd.read_csv("./q1_triangle/q1_test_usecase/额外弱健壮.csv"))
        st.table(pd.read_csv("D:\q1\额外弱健壮.csv"))
        # st.markdown(r'''所有的测试用例：''')
        #chart_data = pd.read_csv("./q1_triangle/q1_test_usecase/三角形-等价类.csv", encoding="gbk")
        chart_data = pd.read_csv("D:\q1\三角形-等价类.csv", encoding="gbk")
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
            st.pyplot()

#销售系统问题（讨论）
elif option == '3.讨论题：销售管理系统':
    st.markdown(q3_sales_system.content)
    st.markdown(q3_sales_system.question1)
    st.markdown(q3_sales_system.question2)
    st.markdown(q3_sales_system.answer1)
    st.markdown(q3_sales_system.answer2)

