# wca-ai-tool-alpha

## Project Overview
**wca-ai-tool-alpha** is an AI-powered Python tool designed to automate the drafting of professional emails. By utilizing the **R-T-C-C-O framework**, the tool ensures that every generated email has a clear role, task, and objective, specifically tailored for the Kenyan professional context.

## Features
* **Python-based logic**: Runs directly from the command line interface.
* **API Integration**: Connects to the **Claude-3 Haiku** model via the Anthropic API for fast and efficient generation.
* **R-T-C-C-O Prompting**: Built-in instruction design (Role, Task, Context, Constraint, Objective) ensuring high-quality and structured output.
* **JSON Handling**: Properly parses API responses into a clean and readable format for the user.

## Installation and Setup

1. Clone the Repository
git clone [https://github.com/warigialakeisha-ship-it/wca-ai-tool-alpha.git](https://github.com/warigialakeisha-ship-it/wca-ai-tool-alpha.git)
cd wca-ai-tool-alpha

Installation and setup
clone with the repo :
git clone https://github.com/warigialakeisha-ship-it/wca-ai-tool-alpha.git
cd wca-ai-tool-alpha
Setting up venv :
python -m venv venv
source venv/Scripts/activate  # On Windows: venv\Scripts\activate

Installing requirements (create a .env file in the root directory)
pip install anthropic python-dotenv
Cofiguration :
ANTHROPIC_API_KEY= claude-haiku-key-stored
Code running ( run from the command line)
python aiproject.py

Group members 
Tekila Tecash
Joseph Juma
Nicholas Murithi
Lakeisha Warigia
Nicole Hellen
