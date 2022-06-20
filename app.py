from PIL import Image
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np
import pandas as pd
import datetime
import time
import re

# import utils
# import triangle
#import myCalendar
#import commission
#import comm_fee
#import salesman
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


