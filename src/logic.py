
import random
from src.db import PromptDatabaseManager
from typing import List, Dict

class PromptBuilderManager:
    """
    Acts as a bridge between the frontend (Streamlit/FastAPI) and the database.
    """
    def __init__(self):
        self.db = PromptDatabaseManager()
        # Call this function to ensure your database has at least one prompt
        self.db.add_initial_prompt()

        self.categories = {
            "gaming": {
                "styles": ["cyberpunk", "fantasy", "sci-fi", "retro", "minimalist"],
                "elements": ["character", "landscape", "weapon", "vehicle", "creature"],
                "qualities": ["high detail", "epic", "dynamic", "atmospheric", "vibrant"]
            },
            "nature": {
                "styles": ["realistic", "painterly", "photographic", "watercolor", "digital art"],
                "elements": ["forest", "mountain", "ocean", "wildlife", "sky"],
                "qualities": ["serene", "majestic", "peaceful", "dramatic", "colorful"]
            },
            "coding": {
                "styles": ["futuristic", "abstract", "minimalist", "tech", "concept art"],
                "elements": ["code", "algorithms", "data structures", "networks", "AI"],
                "qualities": ["clean", "organized", "innovative", "complex", "elegant"]
            },
            "abstract": {
                "styles": ["geometric", "fluid", "minimalist", "surreal", "conceptual"],
                "elements": ["shapes", "colors", "patterns", "textures", "forms"],
                "qualities": ["expressive", "balanced", "harmonious", "contrasting", "rhythmic"]
            }
        }
        
        self.artistic_terms = [
            "4K resolution", "ultra detailed", "cinematic lighting", 
            "concept art", "digital painting", "trending on artstation",
            "sharp focus", "studio quality", "professional", "award winning"
        ]
    
    def detect_category(self, user_input: str) -> str:
        input_lower = user_input.lower()
        
        category_keywords = {
            "gaming": ["game", "gaming", "player", "character", "level", "quest"],
            "nature": ["nature", "forest", "mountain", "ocean", "tree", "animal"],
            "coding": ["code", "programming", "algorithm", "software", "developer", "python"],
            "abstract": ["abstract", "pattern", "shape", "color", "form", "design"]
        }
        
        for category, keywords in category_keywords.items():
            if any(keyword in input_lower for keyword in keywords):
                return category
        
        return "general"
    
    def enhance_prompt(self, user_input: str) -> str:
        category = self.detect_category(user_input)
        
        # Get category-specific enhancements or use general ones
        category_data = self.categories.get(category, {
            "styles": ["professional", "high quality", "detailed", "creative"],
            "elements": [],
            "qualities": ["excellent", "impressive", "well-composed"]
        })
        
        # Build enhanced prompt
        enhanced_parts = []
        
        # Add main input
        enhanced_parts.append(user_input.title())
        
        # Add category-specific style
        if category_data["styles"]:
            enhanced_parts.append(random.choice(category_data["styles"]))
        
        enhanced_parts.extend(random.sample(self.artistic_terms, 2))
      
        if category_data["qualities"]:
            enhanced_parts.append(random.choice(category_data["qualities"]))
        
        return ", ".join(enhanced_parts)

    def add_prompt(self, user_input: str):
        """
        Enhances and adds a new prompt to the database.
        """
        
        improved_prompt = self.enhance_prompt(user_input)

 
        new_prompt = self.db.create_prompt_record(user_input, improved_prompt)

        if new_prompt:
            return {"Success": True, "Message": "Prompt enhanced and added successfully.", "improved_prompt": improved_prompt}
        else:
            return {"Success": False, "Message": "Failed to enhance and add prompt."}

    def get_all_prompts(self) -> List[Dict]:
        """
        Retrieves all prompts from the database.
        """
        return self.db.get_all_prompts()

    def get_random_prompt(self) -> Dict:
        """
        Retrieves a single random prompt from the database.
        """
        return self.db.get_random_prompt()