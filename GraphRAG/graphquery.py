from llama_index.core import PropertyGraphIndex

def query(index, q):
    query_engine = index.as_query_engine(include_text=True)

    response = query_engine.query(q)
    return response