from llama_index.core import SimpleDirectoryReader
from llama_index.graph_stores.neo4j import Neo4jPGStore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

def dir_reader(path):
    reader = SimpleDirectoryReader(path)
    return reader

def initialize_neo4j(user, password, url):
    graph_store = Neo4jPGStore(
    username=user,
    password=password,
    url=url,
    refresh_schema=False
)
    return graph_store
    
def initialize_embed(mod):
    embed_model = HuggingFaceEmbedding(model_name=mod)
    return embed_model
