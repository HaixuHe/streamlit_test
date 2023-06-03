import streamlit as st
import pandas as pd


def main():
    st.title("修改Excel表格")

    # 选择Excel文件
    uploaded_file = st.file_uploader("上传Excel文件", type=["xlsx", "xls"])

    if uploaded_file is not None:
        try:
            # 读取Excel数据
            data = pd.read_excel(uploaded_file)

            # 显示Excel数据
            st.write("Excel数据:")
            st.dataframe(data)

            # 添加修改表格的功能
            st.write("修改表格:")

            # 创建"修改专家信息"按钮
            modify_experts_btn = st.button("修改专家信息")

            # 展开修改专家信息的部分
            with st.expander("修改专家信息", expanded=modify_experts_btn):
                # 选择要修改的行和列
                row_labels = data.index.tolist()
                selected_row = st.selectbox("选择行", row_labels)

                col_labels = data.columns.tolist()
                selected_col = st.selectbox("选择列", col_labels)

                # 显示选定单元格的当前值
                current_value = data.loc[selected_row, selected_col]
                st.write("当前值:", current_value)

                # 添加输入框进行修改
                new_value = st.text_input("输入新的值", current_value)

                # 修改选定的单元格
                data.loc[selected_row, selected_col] = new_value

                if st.button("保存修改"):
                    # 保存修改后的数据到Excel文件
                    modified_file = uploaded_file.name.replace('.xlsx', '_modified.xlsx')
                    data.to_excel(modified_file, index=False)
                    st.success("修改已保存到文件: {}".format(modified_file))

            # 创建"添加专家信息"按钮
            add_expert_btn = st.button("添加专家信息")

            # 展开添加专家信息的部分
            with st.expander("添加专家信息", expanded=add_expert_btn):
                new_row = []
                for col in col_labels:
                    value = st.text_input("输入{}的值".format(col), "")
                    new_row.append(value)

                if st.button("添加人员"):
                    new_data = pd.DataFrame([new_row], columns=col_labels)
                    data = pd.concat([data, new_data], ignore_index=True)
                    st.write("添加成功！")

                    # 保存添加后的数据到Excel文件
                    modified_file = uploaded_file.name.replace('.xlsx', '_modified.xlsx')
                    data.to_excel(modified_file, index=False)
                    st.success("修改已保存到文件: {}".format(modified_file))

        except Exception as e:
            st.error("读取Excel文件时发生错误: {}".format(e))


if __name__ == "__main__":
    main()
