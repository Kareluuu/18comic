import streamlit as st
from gemini_service import search_comics

# 设置页面配置
st.set_page_config(
    page_title="Best Comic Finder",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# 自定义CSS样式
st.markdown("""
    <style>
    .stApp {
        max-width: 800px;
        margin: 0 auto;
    }
    .stTextInput > div > div > input {
        background-color: #f0f2f5;
        border-radius: 20px;
        padding: 10px 20px;
        border: none;
    }
    .stButton > button {
        background-color: #1DA1F2;
        color: white;
        border-radius: 20px;
        padding: 10px 20px;
        border: none;
        width: 100%;
    }
    .output-container {
        background-color: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        margin-top: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# 标题
st.title("Best Comic Finder")

# 搜索输入框和按钮
search_query = st.text_input("输入关键词搜索漫画", placeholder="例如：One Piece")
if st.button("搜索"):
    if search_query:
        with st.spinner("正在搜索中..."):
            # 调用后端服务
            results = search_comics(search_query)
            
            # 显示结果
            st.markdown("<div class='output-container'>", unsafe_allow_html=True)
            if results:
                for result in results:
                    st.markdown(f"### {result['title']}")
                    st.markdown(f"下载链接: {result['link']}")
                    st.markdown("---")
            else:
                st.info("未找到相关结果")
            st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.warning("请��入搜索关键词") 