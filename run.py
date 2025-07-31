from dotenv import load_dotenv
from inspect_ai import eval_set
from eval import bounty
from datetime import datetime
import os
import shutil
load_dotenv()

log_dir = "logs-temp"
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

MODELS = [
            # Anthropic
            "anthropic/claude-3-5-sonnet-20241022",
            "anthropic/claude-opus-4-20250514",
            "anthropic/claude-sonnet-4-20250514",
            "anthropic/claude-3-7-sonnet-20250219",
            "anthropic/claude-3-5-haiku-20241022",
            
            # OpenAI
            "openai/gpt-4.1-2025-04-14",
            "openai/gpt-4o-2024-08-06",
            "openai/o4-mini-2025-04-16",
            "openai/o1-2024-12-17",
            "openai/o3-2025-04-16",
            
            # Gemini
            "google/gemini-1.5-flash",
            "google/gemini-2.0-flash",
            "google/gemini-2.5-pro-preview-05-06",
            "google/gemini-2.5-flash-preview-05-20",
            
            # Grok
            "grok/grok-3-mini",
            "grok/grok-4-0709"
        ]

eval_set(bounty(len(MODELS)), 
         model=MODELS, 
        log_dir=log_dir,
        epochs=5)

now = datetime.now().strftime("%Y%m%d_%H%M%S")
destination_dir = f"logs/{now}"
os.makedirs(os.path.dirname(destination_dir), exist_ok=True)
shutil.move(log_dir, destination_dir)