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

while True:
    # Collect R-T-C-C-O inputs from the user
    role        = input("Your Role: ")
    if role.lower() == "quit": break  # Exit the loop if user types quit
    task        = input("Task: ")
    context     = input("Context: ")
    constraints = input("Constraints: ")

    # Format all inputs into one structured prompt for Claude
    user_input = f"Role: {role}. Task: {task}. Context: {context}. Constraints: {constraints}."
   
    #Add user in    put to messages to conversation history
    messages.append({"role": "user", "content": user_input})
    
    #Generate response from the model
    response = client.messages.create(
        model="claude-haiku-4-5-20251001",
        system=SYSTEM_PROMPT,
        messages=messages,
        max_tokens=200,
    )
    
    #claude response
    reply = response.content[0].text.strip().replace("json", "").replace("", "").strip()
    
    #Add assistant reply to memory
    messages.append({"role": "assistant", "content": reply})