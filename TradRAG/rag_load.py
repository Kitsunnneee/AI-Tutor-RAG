import chromadb
from chromadb.utils.embedding_functions import SentenceTransformerEmbeddingFunction

def initiate_chormadb(name):
    chroma_client = chromadb.Client()
    chroma_collection = chroma_client.create_collection(
        name, embedding_function=SentenceTransformerEmbeddingFunction('paraphrase-MiniLM-L6-v2')
    )
    return chroma_client, chroma_collection
    
def create_add_embeddings(chroma_collection, token_split_texts):
    
    ids = [str(i) for i in range(len(token_split_texts))]
    
    chroma_collection.add(ids=ids, documents = token_split_texts)
    print(chroma_collection.count())

def delete(name):
    client = chromadb.Client()
    client.delete_collection("ai-tutor")