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
                # "anthropic/claude-3-5-sonnet-20241022",
                # "anthropic/claude-opus-4-20250514",
                # "anthropic/claude-sonnet-4-20250514",
                # "anthropic/claude-3-7-sonnet-20250219",
                # "anthropic/claude-3-5-haiku-20241022",
                "anthropic/claude-sonnet-4-5-20250929",
                "anthropic/claude-haiku-4-5-20251001",
                "anthropic/claude-opus-4-5-20251101",
            
            # OpenAI
            "openai/gpt-5.1-2025-11-13",
            "openai/gpt-5-2025-08-07",
            "openai/gpt-5-mini-2025-08-07",
            "openai/gpt-5-nano-2025-08-07",
            
            # Gemini
            "google/gemini-3-pro-preview",
            
            # Grok
            "grok/grok-4-1-fast-reasoning",
            "grok/grok-4-1-fast-non-reasoning"
        ]

eval_set(bounty(len(MODELS)), 
         model=MODELS, 
        log_dir=log_dir,
        epochs=5)

now = datetime.now().strftime("%Y%m%d_%H%M%S")
destination_dir = f"logs/{now}"
os.makedirs(os.path.dirname(destination_dir), exist_ok=True)
shutil.move(log_dir, destination_dir)