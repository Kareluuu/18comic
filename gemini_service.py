import google.generativeai as genai
import json
import re

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
        
        # 构建更明确的提示词
        prompt = f"""
        任务：搜索"{query}"相关的漫画资源。
        
        请按照以下格式返回结果：
        {{
            "results": [
                {{
                    "title": "漫画标题",
                    "link": "下载链接"
                }},
                // 更多结果...
            ]
        }}
        
        要求：
        1. 结果必须是有效的JSON格式
        2. 最多返回5个结果
        3. 每个结果必须包含title和link字段
        4. 链接应该是完整的URL格式
        """
        
        # 调用API
        response = model.generate_content(prompt)
        response_text = response.text
        
        # 尝试从响应文本中提取JSON部分
        json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
        if json_match:
            response_text = json_match.group()
            
            # 解析JSON
            data = json.loads(response_text)
            if isinstance(data, dict) and "results" in data:
                return data["results"]
            else:
                return [{"title": query, "link": "https://18comic.vip/search/q=" + query}]
                
        else:
            # 如果无法提取JSON，返回搜索链接
            return [{"title": query, "link": "https://18comic.vip/search/q=" + query}]
            
    except Exception as e:
        print(f"Error: {str(e)}")
        return [{"title": "搜索出错", "link": "https://18comic.vip"}] 