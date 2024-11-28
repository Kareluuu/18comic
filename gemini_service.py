import google.generativeai as genai
import json
import re
import urllib.parse

# 配置Gemini API
GEMINI_API_KEY = "AIzaSyAE0zCw2RgQfeMAuLWSMUZnoPakTV2uaIY"
genai.configure(api_key=GEMINI_API_KEY)

def search_comics(query):
    """
    使用Gemini API协助搜索漫画资源
    """
    try:
        # 初始化Gemini模型 (使用1.5 Flash版本)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # 构建简洁的提示词（Flash模型适合简短直接的提示）
        prompt = f"""
        在18comic.vip网站搜索"{query}"。
        搜索页面：https://18comic.vip/search/q={urllib.parse.quote(query)}
        
        返回JSON格式：
        {{
            "results": [
                {{
                    "title": "标题",
                    "link": "https://18comic.vip/xxx"
                }}
            ]
        }}
        最多返回3个结果。
        """
        
        # 设置生成参数
        generation_config = {
            "temperature": 0.3,  # 降低随机性
            "top_p": 0.8,
            "top_k": 40,
            "max_output_tokens": 1024,
        }
        
        # 调用API
        response = model.generate_content(
            prompt,
            generation_config=generation_config,
            stream=False  # Flash模型建议不使用流式传输
        )
        response_text = response.text
        
        # 尝试从响应文本中提取JSON部分
        json_match = re.search(r'\{.*\}', response_text, re.DOTALL)
        if json_match:
            response_text = json_match.group()
            
            # 解析JSON
            data = json.loads(response_text)
            if isinstance(data, dict) and "results" in data and len(data["results"]) > 0:
                return data["results"]
        
        # 如果无法获取具体结果，返回搜索页面链接
        encoded_query = urllib.parse.quote(query)
        return [{
            "title": f"搜索：{query}",
            "link": f"https://18comic.vip/search/q={encoded_query}"
        }]
            
    except Exception as e:
        print(f"Error: {str(e)}")
        # 发生错误时也返回搜索页面链接
        encoded_query = urllib.parse.quote(query)
        return [{
            "title": "点击这里搜索",
            "link": f"https://18comic.vip/search/q={encoded_query}"
        }] 