with open('/workspaces/docs/Lincoln_State_of_Union_1862.txt') as file:
    speech_text = file.read()

# Characters
len(speech_text)

len(speech_text.split())

from langchain.text_splitter import CharacterTextSplitter
text_splitter = CharacterTextSplitter(separator="\n\n",chunk_size=1000) #1000 is default value
texts = text_splitter.create_documents([speech_text])
# print(type(texts))
# print('\n')
print(texts[0])
len(texts[0].page_content)
# texts[1]
len(texts[1].page_content)
type(texts[0])
text_splitter = CharacterTextSplitter(separator="\n\n") #chunk_size is minimum length, notice at 2000 still contains a \n\n
text_splitter = CharacterTextSplitter.from_tiktoken_encoder(chunk_size = 500) #now chunk size is a hard length based on tokens
texts = text_splitter.split_text(speech_text)