from langchain.text_splitter import RecursiveCharacterTextSplitter, SentenceTransformersTokenTextSplitter

def process_data(text):
    charater_splitter = RecursiveCharacterTextSplitter(
        separators = ["\n\n","\n","."," ",""], chunk_size = 1000, chunk_overlap = 0
    )
    
    character_split_text = charater_splitter.split_text(text)
    
    
    print(f"Total_chunk :{len(character_split_text)}")
    return character_split_text

def token_splitter(character_split_text):
    
    token_splitter = SentenceTransformersTokenTextSplitter(
        chunk_overlap=10, tokens_per_chunk=128
    )
    
    token_split_text = []
    
    for text in character_split_text:
        token_split_text += token_splitter.split_text(text)
        
    print(f"Total_chunk :{len(token_split_text)}")
    return token_split_text
    