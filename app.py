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
    /* 整体应用样式 */
    .stApp {
        max-width: 800px;
        margin: 0 auto;
        background-color: #f8f9fa;
    }
    
    /* 标题样式 */
    .main-title {
        color: #1a1a1a;
        font-size: 2.5rem;
        font-weight: 700;
        text-align: center;
        margin-bottom: 2rem;
        padding: 1rem;
        background: linear-gradient(90deg, #1DA1F2 0%, #0077e6 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    /* 输入框样式 */
    .stTextInput > div > div > input {
        background-color: white;
        border-radius: 10px;
        padding: 15px 20px;
        border: 2px solid #e6e6e6;
        font-size: 1.1rem;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #1DA1F2;
        box-shadow: 0 0 0 2px rgba(29, 161, 242, 0.2);
    }
    
    /* 按钮样式 */
    .stButton > button {
        background: linear-gradient(90deg, #1DA1F2 0%, #0077e6 100%);
        color: white;
        border-radius: 10px;
        padding: 12px 30px;
        border: none;
        width: 100%;
        font-size: 1.1rem;
        font-weight: 600;
        transition: all 0.3s ease;
        margin-top: 1rem;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(29, 161, 242, 0.3);
    }
    
    /* 结果容器样式 */
    .output-container {
        background-color: white;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-top: 2rem;
        border: 1px solid #e6e6e6;
    }
    
    /* 结果项样式 */
    .result-item {
        padding: 15px;
        border-radius: 8px;
        background-color: #f8f9fa;
        margin-bottom: 15px;
        border: 1px solid #e6e6e6;
    }
    
    .result-title {
        color: #1a1a1a;
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 8px;
    }
    
    .result-link {
        color: #1DA1F2;
        text-decoration: none;
        display: inline-flex;
        align-items: center;
        gap: 5px;
        padding: 5px 10px;
        border-radius: 5px;
        background-color: rgba(29, 161, 242, 0.1);
        transition: all 0.2s ease;
    }
    
    .result-link:hover {
        background-color: rgba(29, 161, 242, 0.2);
    }
    </style>
    """, unsafe_allow_html=True)

# 标题
st.markdown("<h1 class='main-title'>Best Comic Finder</h1>", unsafe_allow_html=True)

# 搜索区域
col1, col2, col3 = st.columns([1,2,1])
with col2:
    search_query = st.text_input("", placeholder="输入关键词搜索漫画...", label_visibility="collapsed")
    search_button = st.button("搜索")

if search_button:
    if search_query:
        with st.spinner("🔍 正在搜索中..."):
            results = search_comics(search_query)
            
            st.markdown("<div class='output-container'>", unsafe_allow_html=True)
            if results:
                st.markdown("### 🎯 搜索结果")
                for result in results:
                    st.markdown(f"""
                    <div class='result-item'>
                        <div class='result-title'>{result['title']}</div>
                        <a href='{result['link']}' target='_blank' class='result-link'>
                            🔗 点击访问
                        </a>
                    </div>
                    """, unsafe_allow_html=True)
            else:
                st.info("😢 未找到相关结果")
            st.markdown("</div>", unsafe_allow_html=True)
    else:
        st.warning("⚠️ 请输入搜索关键词")

# 添加页脚
st.markdown("""
    <div style='position: fixed; bottom: 0; left: 0; right: 0; background-color: white; 
    padding: 10px; text-align: center; font-size: 0.8rem; color: #666;
    border-top: 1px solid #eee;'>
        Made with ❤️ by Comic Finder Team
    </div>
""", unsafe_allow_html=True) 