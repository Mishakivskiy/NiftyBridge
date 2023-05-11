import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Depends
from langchain import OpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Chroma
from pydantic import BaseModel

app = FastAPI()

load_dotenv()
API_KEY = os.getenv("API_KEY")


class Message(BaseModel):
    message: str


async def authenticate(api_key_token: str):
    if api_key_token != API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API key")
    return api_key_token


async def generate_response(message):
    loader = PyPDFLoader("Untitled5.pdf")
    documents = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    texts = text_splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()

    db = Chroma.from_documents(texts, embeddings)

    retriver = db.as_retriever(search_type="similarity", search_kwargs={"k": 2})

    qa = ConversationalRetrievalChain.from_llm(OpenAI(), retriver)

    result = qa({"question": message})
    return result["answer"] or None


@app.post("/api/send")
async def send_message(message: Message, api_key_token: str = Depends(authenticate)):
    if "hello" in message.message.lower():
        return {"message": "Hello I am NiftyBridge AI assistant. How could I help you?"}
    if "nifty bridge" not in message.message.lower():
        raise HTTPException(status_code=400, detail="Invalid message")

    response = await generate_response(message.message)

    if not response:
        response = "NiftyBridge AI assistant: I don't know. Please contact support at support@nifty-bridge.com"

    return {"message": response}
