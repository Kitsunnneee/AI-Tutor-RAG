from langchain_community.chat_models import ChatOllama
from langchain.prompts import ChatPromptTemplate

def retreiver(topic, collection):
    results = collection.query(query_texts=[topic], n_results = 5)
    documents = results["documents"]
    return documents

def query(model_name, topic,documents):
    model_local = ChatOllama(model=model_name)

    template = """
    You are an expert English Teacher with 10 years of experience. You specialize in teaching kids from class 5-10.
    You have done a lot of research on how to teach kids effectively. You have a lot of experience in teaching both kids and adults 
    who want to learn English later in life.
    Based on the topic and context provided teach the topic elaborately and also give excercises.
    Context: {documents}
    Topic: {topic}
    """
    
    prompt = ChatPromptTemplate.from_template(template)
    
    final_prompt = prompt.format(topic=topic, documents=documents)
    
    response = model_local.predict(final_prompt)
    
    return response
    
    