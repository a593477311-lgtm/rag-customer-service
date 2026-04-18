# RAG智能客服系统

基于检索增强生成(RAG)技术的智能客服系统，集成Streamlit Web界面，使用Ollama部署本地大模型，为电商提供专业客服问答服务。

## 功能特性

- 🤖 **智能问答**：基于RAG技术，结合知识库提供准确的客服回答
- 📚 **知识库管理**：支持动态上传和更新知识库文档
- 💬 **多轮对话**：支持上下文连贯的多轮对话
- 🔍 **向量检索**：使用向量相似度检索相关知识点
- 🌐 **Web界面**：基于Streamlit的友好交互界面
- 💾 **会话管理**：支持多用户独立会话

## 技术栈

- **框架**: LangChain
- **大模型**: Ollama (qwen3:8b)
- **向量数据库**: ChromaDB
- **嵌入模型**: qwen3-embedding:4b
- **Web框架**: Streamlit
- **编程语言**: Python 3.8+

## 安装步骤

### 1. 安装Ollama

访问 [Ollama官网](https://ollama.ai/) 下载并安装Ollama

### 2. 下载模型

```bash
# 下载对话模型
ollama pull qwen3:8b

# 下载嵌入模型
ollama pull qwen3-embedding:4b
```

### 3. 克隆项目

```bash
git clone https://github.com/a593477311-lgtm/rag-customer-service.git
cd rag-customer-service
```

### 4. 安装依赖

```bash
pip install -r requirements.txt
```

### 5. 配置文件

```bash
# 复制配置模板
cp config.example.py config.py

# 根据需要修改config.py中的配置
```

## 使用方法

### 1. 启动知识库管理服务

```bash
streamlit run app_file_uploader.py
```

访问 http://localhost:8501 上传知识库文档

### 2. 启动客服问答服务

```bash
streamlit run app_qa.py
```

访问 http://localhost:8501 开始对话

## 项目结构

```
.
├── app_qa.py              # 客服问答主程序
├── app_file_uploader.py   # 知识库上传服务
├── rag.py                 # RAG核心逻辑
├── knowledge_base.py      # 知识库管理
├── vector_stores.py       # 向量存储服务
├── file_history_store.py  # 对话历史存储
├── config.py              # 配置文件
├── config.example.py      # 配置模板
├── requirements.txt       # 依赖列表
├── 文本/                  # 示例知识库文件
│   ├── 尺码推荐.txt
│   ├── 洗涤养护.txt
│   └── 颜色选择.txt
└── README.md
```

## 核心功能说明

### 文档分块策略

采用多层次分隔符优先级机制，保证语义完整性：
- 段落级分隔符（\n\n）
- 句子级分隔符（。！？）
- 子句级分隔符（，；：）
- 字符级分隔符（最终保底）

### 知识库去重

使用MD5哈希校验机制，避免重复存储相同文档

### 向量检索

配置top-k=3参数，平衡召回率与精确度

## 配置说明

主要配置项（config.py）：

```python
# 相似度检索数量
similarity_threshold = 3

# 向量数据库配置
collection_name = "rag"
persist_directory = "./chroma_db"

# 模型配置
embedding_model = "qwen3-embedding:4b"
chat_model = "qwen3:8b"

# 文档分块配置
chunk_size = 1000
overlap = 100
```

## 注意事项

1. 确保Ollama服务已启动
2. 首次运行前需要上传知识库文档
3. 对话历史和向量数据库存储在本地，不会上传到云端


