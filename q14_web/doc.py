content = r'''
某实时的Web系统，服务器端应用程序需要接受客户端发送的不同类型的数据包，为了使系统设计达到最优，使用统一接口，接口（通用包）描述为：接口包的类型：正常交易包、查询包、退货包、换货包、部分退货包、部分换货包；涉及的商品种类：1、2、3、4、5、6；支付类型：系统账户余额支付、货到付款、工行账户支付、农行账户支付、建行账户支付、交行账户支付、邮储账户支付、礼品卡支付；发票类型：日用品、电脑配件、鞋、帽、家电、服装、电脑、ipad、手机、化妆品、食品、其他；支付金额：货到付款无限制、银行支付不能超出最大限额2万、系统账户余额支付不能超出余额；订单状态：正在处理、正在送货、处理完成、订单取消。用正交实验法设计用例。
'''

table1 = r'''
由正交实验法可知：

- 因素数：6
- 状态数：12
- 行数：13

**因素状态表**

| 状态/因素 | A(接口包类型) | B(商品种类) |   C(支付类型)    | D(发票类型) |         E(支付金额)          | F(订单状态) |
| :-------: | :-----------: | :---------: | :--------------: | :---------: | :--------------------------: | :---------: |
|     0     |  正常交易包   |      1      | 系统账户余额支付 |   日用品    |        货到付款无限制        |  正在处理   |
|     1     |    查询包     |      2      |     货到付款     |  电脑配件   | 银行支付不能超出最大限额2万  |  正在送货   |
|     2     |    退货包     |      3      |   工行账户支付   |     鞋      | 系统账户余额支付不能超出余额 |  处理完成   |
|     3     |    换货包     |      4      |   农行账户支付   |     帽      |                              |  订单取消   |
|     4     |  部分退货包   |      5      |   建行账户支付   |    家电     |                              |             |
|     5     |  部分换货包   |      6      |   交行账户支付   |    服装     |                              |             |
|     6     |               |             |   邮储账户支付   |    电脑     |                              |             |
|     7     |               |             |    礼品卡支付    |    ipad     |                              |             |
|     8     |               |             |                  |    手机     |                              |             |
|     9     |               |             |                  |   化妆品    |                              |             |
|    10     |               |             |                  |    食品     |                              |             |
|    11     |               |             |                  |    其他     |                              |             |

**转换后的因素状态表**

| 状态/因素 |  A   |  B   |  C   |   D   |  E   |  F   |
| :-------: | :--: | :--: | :--: | :---: | :--: | :--: |
|     0     | $A_1$ | $B_1$ | $C_1$ | $D_1$  | $E_1$ | $F_1$ |
|     1     | $A_2$ | $B_2$ | $C_2$ | $D_2$  | $E_2$ | $F_2$ |
|     2     | $A_3$ | $B_3$ | $C_3$ | $D_3$  | $E_3$ | $F_3$ |
|     3     | $A_4$ | $B_4$ | $C_4$ | $D_4$  |      | $F_4$ |
|     4     | $A_5$ | $B_5$ | $C_5$ | $D_5$  |      |      |
|     5     | $A_6$ | $B_6$ | $C_6$ | $D_6$  |      |      |
|     6     |      |      | $C_7$ | $D_7$  |      |      |
|     7     |      |      | $C_8$ | $D_8$  |      |      |
|     8     |      |      |      | $D_9$  |      |      |
|     9     |      |      |      | $D_10$ |      |      |
|    10     |      |      |      | $D_11$ |      |      |
|    11     |      |      |      | $D_12$ |      |      |



'''

table2 = r'''
进一步分析：被测项目中一共有4个被测对象，每个被测对象的状态（水平）都不一样。

选择正交表：

- 表中的因素数大于或等于6
- 表中至少有6个因素的水平数大于或等于3
- 行数取最少的一个，即满足$（6^2 * 8^1 * 12^1 * 3^1 * 4^1）$的最少行数：
$$
 2×(6-1)+1×(8-1)+1×(12-1)+1×(3-1)+1×(4-1)+1 = 33 
$$
最后选中正交表公式：
$$
L_{36}(6^6)
$$


**$L_{36}(6^6)$正交表**

|      | 1    | 2    | 3    | 4    | 5    | 6    |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 1    | 0    | 0    | 0    | 0    | 0    | 0    |
| 2    | 0    | 1    | 1    | 1    | 1    | 1    |
| 3    | 0    | 2    | 2    | 2    | 2    | 2    |
| 4    | 0    | 3    | 3    | 3    | 3    | 3    |
| 5    | 0    | 4    | 4    | 4    | 4    | 4    |
| 6    | 0    | 5    | 5    | 5    | 5    | 5    |
| 7    | 1    | 0    | 1    | 2    | 3    | 4    |
| 8    | 1    | 1    | 0    | 4    | 2    | 3    |
| 9    | 1    | 2    | 4    | 0    | 1    | 5    |
| 10   | 1    | 3    | 2    | 1    | 0    | 2    |
| 11   | 1    | 4    | 5    | 3    | 5    | 0    |
| 12   | 1    | 5    | 3    | 5    | 4    | 1    |
| 13   | 2    | 0    | 2    | 3    | 4    | 5    |
| 14   | 2    | 1    | 0    | 2    | 5    | 3    |
| 15   | 2    | 2    | 1    | 0    | 3    | 4    |
| 16   | 2    | 3    | 4    | 5    | 0    | 2    |
| 17   | 2    | 4    | 5    | 1    | 1    | 0    |
| 18   | 2    | 5    | 3    | 4    | 2    | 1    |
| 19   | 3    | 0    | 3    | 4    | 5    | 1    |
| 20   | 3    | 1    | 0    | 3    | 4    | 2    |
| 21   | 3    | 2    | 4    | 0    | 1    | 3    |
| 22   | 3    | 3    | 1    | 2    | 0    | 5    |
| 23   | 3    | 4    | 5    | 1    | 2    | 0    |
| 24   | 3    | 5    | 2    | 5    | 3    | 4    |
| 25   | 4    | 0    | 4    | 5    | 1    | 2    |
| 26   | 4    | 1    | 0    | 1    | 2    | 5    |
| 27   | 4    | 2    | 1    | 0    | 4    | 3    |
| 28   | 4    | 3    | 5    | 2    | 0    | 1    |
| 29   | 4    | 4    | 3    | 4    | 5    | 0    |
| 30   | 4    | 5    | 2    | 3    | 3    | 4    |
| 31   | 5    | 0    | 5    | 1    | 2    | 3    |
| 32   | 5    | 1    | 0    | 5    | 4    | 2    |
| 33   | 5    | 2    | 1    | 0    | 5    | 3    |
| 34   | 5    | 3    | 2    | 4    | 0    | 5    |
| 35   | 5    | 4    | 3    | 2    | 1    | 0    |
| 36   | 5    | 5    | 4    | 3    | 3    | 1    |



**替代后的正交表**

|      | 1    | 2    | 3    | 4    | 5    | 6    |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 1    | $A_1$ | $B_1$ | $C_1$ | $D_1$ | $E_1$ | $F_1$ |
| 2    | $A_1$ | $B_2$ | $C_2$ | $D_2$ | $E_2$ | $F_2$ |
| 3    | $A_1$ | $B_3$ | $C_3$ | $D_3$ | $E_3$ | $F_3$ |
| 4    | $A_1$ | $B_4$ | $C_4$ | $D_4$ | 3    | $F_4$ |
| 5    | $A_1$ | $B_5$ | $C_5$ | $D_5$ | 4    | 4    |
| 6    | $A_1$ | $B_6$ | $C_6$ | $D_6$ | 5    | 5    |
| 7    | $A_2$ | $B_1$ | $C_2$ | $D_3$ | 3    | 4    |
| 8    | $A_2$ | $B_2$ | $C_1$ | $D_5$ | $E_3$ | $F_4$ |
| 9    | $A_2$ | $B_3$ | $C_5$ | $D_1$ | $E_2$ | 5    |
| 10   | $A_2$ | $B_4$ | $C_3$ | $D_2$ | $E_1$ | $F_3$ |
| 11   | $A_2$ | $B_5$ | $C_6$ | $D_4$ | 5    | $F_1$ |
| 12   | $A_2$ | $B_6$ | $C_6$ | $D_6$ | 4    | $F_2$ |
| 13   | $A_3$ | $B_1$ | $C_4$ | $D_4$ | 4    | 5    |
| 14   | $A_3$ | $B_2$ | $C_1$ | $D_3$ | 5    | $F_4$ |
| 15   | $A_3$ | $B_3$ | $C_2$ | $D_1$ | 3    | 4    |
| 16   | $A_3$ | $B_4$ | $C_5$ | $D_6$ | $E_1$ | $F_3$ |
| 17   | $A_3$ | $B_5$ | $C_6$ | $D_2$ | $E_2$ | $F_1$ |
| 18   | $A_3$ | $B_6$ | $C_4$ | $D_5$ | $E_3$ | $F_2$ |
| 19   | $A_4$ | $B_1$ | $C_4$ | $D_5$ | 5    | $F_2$ |
| 20   | $A_4$ | $B_2$ | $C_1$ | $D_4$ | 4    | $F_3$ |
| 21   | $A_4$ | $B_3$ | $C_5$ | $D_1$ | $E_2$ | $F_4$ |
| 22   | $A_4$ | $B_4$ | $C_2$ | $D_3$ | $E_1$ | 5    |
| 23   | $A_4$ | $B_5$ | $C_6$ | $D_2$ | $E_3$ | $F_1$ |
| 24   | $A_4$ | $B_6$ | $C_2$ | $D_6$ | 3    | 4    |
| 25   | $A_5$ | $B_1$ | $C_5$ | $D_6$ | $E_2$ | $F_3$ |
| 26   | $A_5$ | $B_2$ | $C_1$ | $D_2$ | $E_3$ | 5    |
| 27   | $A_5$ | $B_3$ | $C_2$ | $D_1$ | 4    | $F_4$ |
| 28   | $A_5$ | $B_4$ | $C_6$ | $D_3$ | $E_1$ | $F_2$ |
| 29   | $A_5$ | $B_5$ | $C_4$ | $D_5$ | 5    | $F_1$ |
| 30   | $A_5$ | $B_6$ | $C_2$ | $D_4$ | 3    | 4    |
| 31   | $A_6$ | $B_1$ | $C_6$ | $D_2$ | $E_3$ | $F_4$ |
| 32   | $A_6$ | $B_2$ | $C_1$ | $D_6$ | 4    | $F_3$ |
| 33   | $A_6$ | $B_3$ | $C_2$ | $D_1$ | 5    | $F_4$ |
| 34   | $A_6$ | $B_4$ | $C_3$ | $D_5$ | $E_1$ | 5    |
| 35   | $A_6$ | $B_5$ | $C_4$ | $D_3$ | $E_2$ | $F_1$ |
| 36   | $A_6$ | $B_6$ | $C_5$ | $D_4$ | 3    | $F_2$ |



**各自替代后的正交表**

|      | 1    | 2    | 3    | 4    | 5    | 6    |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 1    | $A_1$ | $B_1$ | $C_1$ | $D_1$ | $E_1$ | $F_1$ |
| 2    | $A_1$ | $B_2$ | $C_2$ | $D_2$ | $E_2$ | $F_2$ |
| 3    | $A_1$ | $B_3$ | $C_3$ | $D_3$ | $E_3$ | $F_3$ |
| 4    | $A_1$ | $B_4$ | $C_4$ | $D_4$ | $E_1$ | $F_4$ |
| 5    | $A_1$ | $B_5$ | $C_5$ | $D_5$ | $E_2$ | $F_1$ |
| 6    | $A_1$ | $B_6$ | $C_6$ | $D_6$ | $E_3$ | $F_2$ |
| 7    | $A_2$ | $B_1$ | $C_2$ | $D_3$ | $E_1$ | $F_1$ |
| 8    | $A_2$ | $B_2$ | $C_1$ | $D_5$ | $E_3$ | $F_4$ |
| 9    | $A_2$ | $B_3$ | $C_5$ | $D_1$ | $E_2$ | $F_2$ |
| 10   | $A_2$ | $B_4$ | $C_3$ | $D_2$ | $E_1$ | $F_3$ |
| 11   | $A_2$ | $B_5$ | $C_6$ | $D_4$ | $E_3$ | $F_1$ |
| 12   | $A_2$ | $B_6$ | $C_6$ | $D_6$ | $E_2$ | $F_2$ |
| 13   | $A_3$ | $B_1$ | $C_4$ | $D_4$ | $E_2$ | 5    |
| 14   | $A_3$ | $B_2$ | $C_1$ | $D_3$ | $E_3$ | $F_4$ |
| 15   | $A_3$ | $B_3$ | $C_2$ | $D_1$ | $E_1$ | $F_1$ |
| 16   | $A_3$ | $B_4$ | $C_5$ | $D_6$ | $E_1$ | $F_3$ |
| 17   | $A_3$ | $B_5$ | $C_6$ | $D_2$ | $E_2$ | $F_1$ |
| 18   | $A_3$ | $B_6$ | $C_4$ | $D_5$ | $E_3$ | $F_2$ |
| 19   | $A_4$ | $B_1$ | $C_4$ | $D_5$ | $E_3$ | $F_2$ |
| 20   | $A_4$ | $B_2$ | $C_1$ | $D_4$ | $E_2$ | $F_3$ |
| 21   | $A_4$ | $B_3$ | $C_5$ | $D_1$ | $E_2$ | $F_4$ |
| 22   | $A_4$ | $B_4$ | $C_2$ | $D_3$ | $E_1$ | $F_2$ |
| 23   | $A_4$ | $B_5$ | $C_6$ | $D_2$ | $E_3$ | $F_1$ |
| 24   | $A_4$ | $B_6$ | $C_2$ | $D_6$ | $E_1$ | $F_1$ |
| 25   | $A_5$ | $B_1$ | $C_5$ | $D_6$ | $E_2$ | $F_3$ |
| 26   | $A_5$ | $B_2$ | $C_1$ | $D_2$ | $E_3$ | $F_2$ |
| 27   | $A_5$ | $B_3$ | $C_2$ | $D_1$ | $E_2$ | $F_4$ |
| 28   | $A_5$ | $B_4$ | $C_6$ | $D_3$ | $E_1$ | $F_2$ |
| 29   | $A_5$ | $B_5$ | $C_4$ | $D_5$ | $E_3$ | $F_1$ |
| 30   | $A_5$ | $B_6$ | $C_2$ | $D_4$ | $E_1$ | $F_1$ |
| 31   | $A_6$ | $B_1$ | $C_6$ | $D_2$ | $E_3$ | $F_4$ |
| 32   | $A_6$ | $B_2$ | $C_1$ | $D_6$ | $E_2$ | $F_3$ |
| 33   | $A_6$ | $B_3$ | $C_2$ | $D_1$ | $E_3$ | $F_4$ |
| 34   | $A_6$ | $B_4$ | $C_3$ | $D_5$ | $E_1$ | $F_2$ |
| 35   | $A_6$ | $B_5$ | $C_4$ | $D_3$ | $E_2$ | $F_1$ |
| 36   | $A_6$ | $B_6$ | $C_5$ | $D_4$ | $E_1$ | $F_2$ |


'''


table3 = r'''
由上表可知，需要设计36个测试用例。我们以下面这一行为例，设计一个测试用例。

|      | 1     | 2     | 3     | 4     | 5     | 6     |
| ---- | ----- | ----- | ----- | ----- | ----- | ----- |
| 1    | $A_6$ | $B_5$ | $C_1$ | $D_4$ | $E_2$ | $F_3$ |


测试用例如下：


| 项目         | 内容                                          |
| ------------ | --------------------------------------------- |
| 测试用例编号 | WEB_PACKAGE_01                                |
| 测试项目     | 识别数据包内容                                |
| 重要级别     | 高                                            |
| 预置条件     | 数据包被发送                                  |
| 输入         | 接口（通报包）内容                            |
| 操作         | 1. $A_6$：部分换货包                          |
|              | 2. $B_5$：涉及的商品种类为5                   |
|              | 3. $C_1$：支付类型为系统账户余额支付          |
|              | 4. $D_4$：发票类型为鞋                        |
|              | 5. $E_2$：支付金额银行支付不能超出最大限额2万 |
|              | 6. $F_3$：订单状态为处理完成                  |


'''