import os
import random
from supabase import create_client, Client
from dotenv import load_dotenv 

# Load environment variables
load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

supabase: Client = create_client(url, key)

def create_prompt(user_input: str, improved_prompt: str):
    """Inserts a new prompt entry into the Supabase database."""
    try:
        data = supabase.table("prompts").insert({
            "user_input": user_input,
            "improved": improved_prompt
        }).execute()
        return data.data
        
    except Exception as e:
        print(f"Error creating prompt: {e}")
        return None

def get_all_prompts():
    """Fetches all prompts from the Supabase database."""
    try:
        data = supabase.table("prompts").select("*").execute()
        return data.data
    except Exception as e:
        print(f"Error fetching all prompts: {e}")
        return None
    
def get_random_prompt():
    """Fetches a single random prompt from the Supabase database."""
    try:
        all_prompts = get_all_prompts()
        if all_prompts:
            return random.choice(all_prompts)
        else:
            return None
    except Exception as e:
        print(f"Error fetching random prompt: {e}")
        return None