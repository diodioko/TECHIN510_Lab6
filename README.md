# TECHIN510_Lab6
# LLM and Chat Bots

A Cooking Recipe Selector App leverages advanced AI capabilities to generate custom cooking recipes based on user-specified cuisine types and ingredients.

## Getting Started

### First time setup

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Future runs

```bash
# Activate virtual environment
source venv/bin/activate

# Run the app
streamlit run llm_app.py
```

### Learn
```bash
Handling User Input and AI Output: Firstly, it captures user inputs for cuisine type and ingredients. Then, it uses these inputs to generate a prompt for the AI, which returns several recipe options. This method ensures that the AI’s output is directly relevant to the user’s needs.

Sequential Interaction Design: The app is designed to guide users through a sequence of interactions—starting from entering inputs, selecting recipe options, and finally viewing detailed instructions. This step-by-step approach helps prevent user confusion and ensures the app is easy to use.
```