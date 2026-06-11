from fastapi import FastAPI
from langchain_core.prompts import ChatMessagePromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes
import os

api_key = os.environ["GROQ_API_KEY"]
model=ChatGroq(model="llama-3.3-70b-versatile",groq_api_key=api_key)



## prompt template
from langchain_core.prompts import ChatPromptTemplate
generic_template= "Translate the following into {language}:"

prompt=ChatPromptTemplate.from_messages(
    [
        ("system",generic_template),
        ("user","{text}")
    ]

)

parser=StrOutputParser()

##create chain
chain=prompt|model|parser

## App definition
app=FastAPI(title="Langchain Server",
            version="1.0",
            description="A simple API server using Langchain runnable interfaces ")

## adding chain routes
add_routes(
    app,
    chain,
    path="/chain"
)

if __name__=="__main__":
  import uvicorn
  uvicorn.run(app,host="127.0.0.1",port=8000)
