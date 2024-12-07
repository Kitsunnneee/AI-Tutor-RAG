from llama_index.core import PropertyGraphIndex

def load_graph(doc, mod, embed, graph_store):
    index = PropertyGraphIndex.from_documents(
    doc,
    llm=mod,
    embed_model=embed,
    property_graph_store=graph_store,
    show_progress=True)
    return index