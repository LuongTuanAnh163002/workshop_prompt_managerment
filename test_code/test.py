import os
from dotenv import load_dotenv
from langfuse import Langfuse

# Load biến môi trường từ file .env
load_dotenv()

# Khởi tạo Langfuse client
langfuse = Langfuse(
    secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
    public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
    host=os.getenv("LANGFUSE_HOST")
)

# Ví dụ tạo text prompt
langfuse.create_prompt(
    name="movie-critic",
    type="text",
    prompt="As a {{criticlevel}} movie critic, do you like {{movie}}?",
    labels=["production"],
    config={
        "model": "gpt-4o",
        "temperature": 0.7,
        "supported_languages": ["en", "fr"],
    },
)

# Ví dụ tạo chat prompt
langfuse.create_prompt(
    name="movie-critic-chat",
    type="chat",
    prompt=[
      { "role": "system", "content": "You are an {{criticlevel}} movie critic" },
      { "role": "user", "content": "Do you like {{movie}}?" },
    ],
    labels=["production"],
    config={
        "model": "gpt-4o",
        "temperature": 0.7,
        "supported_languages": ["en", "fr"],
    },
)