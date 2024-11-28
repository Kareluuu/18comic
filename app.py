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
    /* 整体页面样式 */
    .stApp {
        max-width: 800px;
        margin: 0 auto;
        background-color: #000000;
        color: #ffffff;
    }
    
    /* 标题样式 */
    .main-title {
        color: #ffffff;
        font-size: 2.5rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 2rem;
        padding: 1rem;
    }
    
    /* 输入框样式 */
    .stTextInput > div > div > input {
        background-color: #16181c;
        color: #ffffff;
        border: 1px solid #333639;
        border-radius: 8px;
        padding: 12px 16px;
        font-size: 1.1rem;
    }
    
    /* 按钮样式 */
    .stButton > button {
        background-color: #1d9bf0;
        color: white;
        border-radius: 9999px;
        padding: 12px 24px;
        border: none;
        width: 100%;
        font-weight: 600;
        font-size: 1.1rem;
        transition: background-color 0.2s;
    }
    
    .stButton > button:hover {
        background-color: #1a8cd8;
    }
    
    /* 结果容器样式 */
    .output-container {
        background-color: #16181c;
        padding: 20px;
        border-radius: 16px;
        border: 1px solid #333639;
        margin-top: 20px;
    }
    
    /* 结果项样式 */
    .result-item {
        padding: 16px;
        border-bottom: 1px solid #333639;
    }
    
    .result-item:last-child {
        border-bottom: none;
    }
    
    /* 链接样式 */
    a {
        color: #1d9bf0 !important;
        text-decoration: none;
    }
    
    a:hover {
        text-decoration: underline;
    }
    
    /* 提示信息样式 */
    .stAlert {
        background-color: #16181c;
        color: #ffffff;
        border: 1px solid #333639;
    }
    
    /* 加载动画样式 */
    .stSpinner > div {
        border-color: #1d9bf0 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 标题
st.markdown('<h1 class="main-title">Best Comic Finder</h1>', unsafe_allow_html=True)

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
                    st.markdown(
                        f"""
                        <div class="result-item">
                            <div style="font-size: 1.1rem; font-weight: 600; margin-bottom: 8px;">
                                {result['title']}
                            </div>
                            <div>
                                <a href="{result['link']}" target="_blank">
                                    🔗 访问链接
                                </a>
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
            else:
                st.info("未找到相关结果")
            st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.warning("请输入搜索关键词") 