
md5_path="./md5.text"

session_config={
    "configurable":{
        "session_id":"user_001",
    }
}

similarity_threshold = 3

collection_name = "rag"
embedding_model = "qwen3-embedding:4b"
persist_directory = "./chroma_db"

chat_model = "qwen3:8b"

chunk_size = 1000
overlap = 100
max_split_char_number = 1000
separators = [
    "\n\n",
    "\r\n\r\n",
    "\n",
    "\r\n",
    "。",
    ". ",
    "！",
    "! ",
    "？",
    "? ",
    "；",
    "; ",
    "：",
    ": ",
    "，",
    ", ",
    "、",
    " ",
    "\t",
    ""
]
