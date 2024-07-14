# Claude Interactive Chatbot

This Python script interacts with the Claude API from Anthropic to create a conversational assistant. The script reads user inputs, sends them to the API, and returns the assistant's responses in a terminal-based chat interface.

## Features

- Interactive text-based conversation with Claude.
- Typing animation to simulate the assistant's response time.
- Exit the conversation by typing `quit`.

## Requirements

- Python 3.x
- `anthropic` Python package

## Installation

1. **Clone the repository** (or download the script directly):
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Install required packages**:
    ```bash
    pip install anthropic
    ```

3. **Set your API key**:
    - You can set your API key directly in the script by replacing `"API-KEY"` with your actual API key.
    - Alternatively, set the `ANTHROPIC_API_KEY` environment variable:
        ```bash
        export ANTHROPIC_API_KEY="your-api-key"
        ```

## Usage

1. **Run the script**:
    ```bash
    python script_name.py
    ```

2. **Interact with the assistant**:
    - Type your message and press Enter.
    - Type `quit` to exit the conversation.

### Specifying the Model

The script uses the Claude model, which needs to be specified. You can change the model in the `client.messages.create` function. Example models include `claude-1`, `claude-2`, `claude-3-opus-20240229`, etc.

## Example

      ________ 
     /        \    
    |  o    o  |   
     \  ____  /    
      `. -- ,'    
        `--'

===== CLAUDE INTERACTIVE CHATBOT =====
type 'quit' to exit
you: Hello, Claude!
Claude is typing...
claude: Hello! How can I assist you today?

you: Tell me a joke.
Claude is typing...
claude: Why did the scarecrow win an award? Because he was outstanding in his field!

you: quit



