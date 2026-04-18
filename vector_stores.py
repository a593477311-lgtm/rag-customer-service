from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings
import config

class VectorStoreService(object,):
    def __init__(self,model):

        self.model =model

        self.vector_store = Chroma(
            collection_name=config.collection_name,
            embedding_function=OllamaEmbeddings(model=model),
            persist_directory=config.persist_directory,
        )

    def get_retriever(self):
        return self.vector_store.as_retriever(search_kwargs={"k":config.similarity_threshold})  #用户文本向量匹配

if __name__ == '__main__':
    r=VectorStoreService(config.embedding_model).get_retriever()
    r1=r.invoke("我的体重180斤，尺码推荐")
    print(r1)