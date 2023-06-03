import streamlit as st
import pandas as pd
import random


def random_selection(data, num_samples):
    # 从数据中随机选择指定数量的样本
    samples = data.sample(num_samples)
    return samples


def main():
    st.title("随机抽取人员信息")
    st.sidebar.title("选择Excel文件")

    # 选择Excel文件
    uploaded_file = st.sidebar.file_uploader("上传Excel文件", type=["xlsx", "xls"])

    if uploaded_file is not None:
        try:
            # 读取Excel数据
            data = pd.read_excel(uploaded_file)

            # 显示文件中的信息数量
            num_entries = len(data)
            st.write("文件中包含的信息数量:", num_entries)

            # 添加抽取人数输入框
            num_samples = st.number_input("请输入抽取的人数", min_value=1, max_value=num_entries, step=1, value=3)

            # 添加抽取按钮
            if st.button("随机抽取"):
                samples = random_selection(data, num_samples)

                # 显示抽取的人员信息
                st.write("随机抽取的人员信息:")
                st.dataframe(samples)
        except Exception as e:
            st.error("读取Excel文件时发生错误: {}".format(e))


if __name__ == "__main__":
    main()
