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
                "anthropic/claude-fable-5-1",
                "anthropic/claude-opus-5-5",
                "anthropic/claude-sonnet-5-5",
                "anthropic/claude-haiku-5-5",

            # OpenAI
            "openai/gpt-6.1-sol",
            "openai/gpt-6.1-terra",
            "openai/gpt-6-luna",

            # Gemini
            "google/gemini-4-argon",
            "google/gemini-3.1-pro-preview",
            "google/gemini-3.8-flash",

            # Grok (no direct xAI key; via OpenRouter)
            "openrouter/x-ai/grok-4.7",
        ]

import sys
EPOCHS = int(sys.argv[1]) if len(sys.argv) > 1 else 5

eval_set(bounty(len(MODELS)), 
         model=MODELS, 
        log_dir=log_dir,
        epochs=EPOCHS)

now = datetime.now().strftime("%Y%m%d_%H%M%S")
destination_dir = f"logs/{now}"
os.makedirs(os.path.dirname(destination_dir), exist_ok=True)
shutil.move(log_dir, destination_dir)