from langchain_community.chat_models import ChatOpenAI 
from datetime import datetime
from langchain.output_parsers import DatetimeOutputParser
from langchain_community.document_loaders import WikipediaLoader
import os
from dotenv import load_dotenv
load_dotenv()
print(os.getenv("OPENAI_API_KEY"))
chat = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY")) 
from langchain.prompts import (
    ChatPromptTemplate,
    PromptTemplate,
    HumanMessagePromptTemplate,
    AIMessagePromptTemplate,
    SystemMessagePromptTemplate,
)





def answer_question_about(person_name,question):
    # Get Wikipedia Article
    docs = WikipediaLoader(query=person_name,load_max_docs=1)
    context_text = docs.load()[0].page_content
    
    # Connect to OpenAI Model
    
    model = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"))
    
    # Ask Model Question
    human_prompt = HumanMessagePromptTemplate.from_template('Answer this question\n{question}, here is some extra context:\n{document}')
    
    # Assemble chat prompt
    chat_prompt = ChatPromptTemplate.from_messages([human_prompt])
    
    #result
    result = model(chat_prompt.format_prompt(question=question,document=context_text).to_messages())
    
    print(result.content)
    
answer_question_about("jimi karter","Give me the summary of biography in one paragraph")