# 从python3.8镜像基础上创建
FROM python:3.8

# 设置镜像源，提高pip install 速度
COPY requirements.txt ./
RUN pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

COPY . .

# streamlit hello创建一个演示页面，映射80端口以便网页访问
CMD ["streamlit","run","app.py", "--server.port","8501"]
