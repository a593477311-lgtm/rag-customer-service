
md5_path="./md5.text"

#session_id
session_config={
        "configurable":{
            "session_id":"user_001",
        }
    }

#相似度检索
similarity_threshold =3

#Chrome，嵌入模型
collection_name="rag"
embedding_model="qwen3-embedding:4b"
persist_directory="./chroma_db"

#聊天模型
chat_model ="qwen3:8b"

#spliter
chunk_size=1000
overlap=100
max_split_char_number = 1000
separators = [
    # 1. 段落级（最高优先级，保证语义块完整）
    "\n\n",
    "\r\n\r\n",

    # 2. 换行（列表项、代码行、诗歌等）
    "\n",
    "\r\n",

    # 3. 句子级标点（中英文通用，句末优先）
    "。",           # 中文句号
    ". ",           # 英文句号加空格（避免切分 Mr. / U.S. 等缩写在后续空格时处理）
    "！",           # 中文感叹号
    "! ",           # 英文感叹号
    "？",           # 中文问号
    "? ",           # 英文问号

    # 4. 子句级标点
    "；",           # 中文分号
    "; ",           # 英文分号
    "：",           # 中文冒号
    ": ",           # 英文冒号
    "，",           # 中文逗号
    ", ",           # 英文逗号
    "、",           # 中文顿号

    # 5. 空格（英文单词边界，英文句子内次级切分）
    " ",            # 单空格
    "\t",           # 制表符

    # 6. 字符级（最终保底策略）
    ""
]