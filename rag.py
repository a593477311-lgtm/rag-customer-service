from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough, RunnableWithMessageHistory, RunnableLambda
import config
from vector_stores import VectorStoreService
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_ollama import ChatOllama
from file_history_store import get_history

def p(pp):
    print("-----------")
    print(pp.to_string())
    print("-----------")
    return pp



class RagService(object):
    def __init__(self):
        self.vector_service=VectorStoreService(
            model=config.embedding_model,
        )

        self.prompt_template = ChatPromptTemplate.from_messages(
            [
                ("system", "你是一个客服，以我提供的已知参考资料为主。"
                           "简洁与专业的回答客户的问题，参考资料：{context}。"),
                ("system","并且对话历史记录如下:"),
                MessagesPlaceholder("history"),
                ("user", "请回答用户提问：{input}")
            ]
        )

        self.chat_model =ChatOllama(model=config.chat_model)

        self.chain =self.__get_chain()

    def __get_chain(self):
        retriever=self.vector_service.get_retriever()

        def format_document(docs:list[Document]):
            if not docs:
                return "无相关参考资料"

            formatted_str=""

            for doc in docs:
                formatted_str+= f"文档片段：{doc.page_content}\n文档元数据：{doc.metadata}\n\n"

            return formatted_str

        def t1(value):
            return value["input"]

        def t2(value):
            new_value ={}
            new_value["input"]=value["input"]["input"]
            new_value["context"]=value["context"]
            new_value["history"]=value["input"]["history"]
            return new_value

        chain =(
            {
                "input":RunnablePassthrough(),
                "context": RunnableLambda(t1)| retriever | format_document    #history劫持t1)  format_document拿到
            } | RunnableLambda(t2) | self.prompt_template | p | self.chat_model | StrOutputParser()  #拿到给提示词的消息t2)
        )

        #要字典
        conversation_chain=RunnableWithMessageHistory(
            chain,
            get_history,
            input_messages_key="input",
            history_messages_key="history",
        )
        return conversation_chain

if __name__ =='__main__':
    #配置session_id
    session_config={
        "configurable":{
            "session_id":"user_001",
        }
    }
    r=RagService().chain.invoke({"input":"现在是春季我175cm，125斤，给出一套穿搭"},session_config)
    print(r)