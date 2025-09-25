# api/main.py

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sys, os

# Get the path to the project root and append it to the system path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

# Import PromptBuilderManager from src.logic
from src.logic import PromptBuilderManager

# ------------------- App Setup -------------------
app = FastAPI(title="Prompt Builder API", version="1.0")

# ------------------- Allow frontend (Streamlit/React) to call the API -------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all origins (frontend apps)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Creating a Prompt builder instance (business logic)
prompt_builder = PromptBuilderManager()

# ------------------- Data Models -------------------
class PromptCreate(BaseModel):
    user_input: str

# ------------------- END Points -------------------
@app.get("/")
def home():
    """
    Check if the API is running
    """
    return {"message": "Prompt Builder API is running"}

@app.get("/prompts")
def get_prompts():
    """
    Get all prompts from the database.
    """
    prompts = prompt_builder.get_all_prompts()
    if prompts:
        return prompts
    raise HTTPException(status_code=404, detail="No prompts found")

@app.get("/prompts/random")
def get_random_prompt():
    """
    Get a single random prompt from the database.
    """
    random_prompt = prompt_builder.get_random_prompt()
    if random_prompt:
        return random_prompt
    raise HTTPException(status_code=404, detail="No prompts found")

@app.post("/build")
def build_prompt(prompt_data: PromptCreate):
    """
    Enhance a new prompt and add it to the database.
    """
    response = prompt_builder.add_prompt(prompt_data.user_input)
    if response["Success"]:
        return {"status": "success", "message": response["Message"], "prompt": response.get("improved_prompt")}
    raise HTTPException(status_code=500, detail=response["Message"])