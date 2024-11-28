import google.generativeai as genai
import json

# 配置Gemini API
GEMINI_API_KEY = "AIzaSyAE0zCw2RgQfeMAuLWSMUZnoPakTV2uaIY"
genai.configure(api_key=GEMINI_API_KEY)

def search_comics(query):
    """
    使用Gemini API搜索漫画资源
    """
    try:
        # 初始化Gemini模型
        model = genai.GenerativeModel('gemini-pro')
        
        # 构建提示词
        prompt = f"""
        请在18comic.vip网站上搜索关于"{query}"的漫画资源。
        请返回JSON格式的结果，包含以下字段：
        - title: 漫画标题
        - link: 下载链接
        最多返回5个结果。
        """
        
        # 调用API
        response = model.generate_content(prompt)
        
        # 解析响应
        try:
            # 尝试解析JSON响应
            results = json.loads(response.text)
            return results
        except json.JSONDecodeError:
            # 如果无法解析JSON，返回格式化后的结果
            return [{"title": "解析结果失败", "link": "请稍后重试"}]
            
    except Exception as e:
        print(f"Error: {str(e)}")
        return [] 