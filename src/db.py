import os
import random
from supabase import create_client, Client
from dotenv import load_dotenv 

# Load environment variables
load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

class PromptDatabaseManager:
    def __init__(self):
        self.supabase: Client = create_client(url, key)

    def create_prompt_record(self, user_input: str, improved_prompt: str):
        """Inserts a new prompt record into the Supabase database and returns the data."""
        try:
            data = self.supabase.table("prompts").insert({
                "user_input": user_input,
                "improved": improved_prompt
            }).execute()
            return data.data
        except Exception as e:
            print(f"Error creating prompt record: {e}")
            return None

    def get_all_prompts(self):
        """Fetches all prompts from the Supabase database."""
        try:
            data = self.supabase.table("prompts").select("*").execute()
            return data.data
        except Exception as e:
            print(f"Error fetching all prompts: {e}")
            return None
        
    def get_random_prompt(self):
        """Fetches a single random prompt from the Supabase database."""
        try:
            all_prompts = self.get_all_prompts()
            if all_prompts:
                return random.choice(all_prompts)
            else:
                return None
        except Exception as e:
            print(f"Error fetching random prompt: {e}")
            return None

    def add_initial_prompt(self):
        """
        Adds a single predefined prompt to the database if it's empty.
        This is for initial setup and testing.
        """
        try:
           
            count_data = self.supabase.table("prompts").select("*", count='exact').execute()
            count = count_data.count
            
            if count == 0:
                print("Database is empty. Adding initial prompt...")
                self.create_prompt_record(
                    "coding wallpaper",
                    "A futuristic coding wallpaper with neon glowing screens, abstract circuits, highly detailed, 8K resolution."
                )
                print("Initial prompt added successfully.")
            
        except Exception as e:
            print(f"Error adding initial prompt: {e}")
            return None