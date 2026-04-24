# import libraries
import anthropic
import json
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

#Initialize client(model)
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

# lock claude to email writing only
SYSTEM_PROMPT = """You are an email writer. ONLY write emails.
Always respond with raw JSON only, with keys 'subject' and 'body'. No markdown, no extra text."""

#memory (conversation history)
messages = []

print("AI Email Writer Ready!")
print("Type 'quit' to exit.\n")
