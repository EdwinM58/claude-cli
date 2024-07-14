# Claude 3 Opus Interactive Chatbot

This Python script interacts with the Claude 3 Opus API from Anthropic to create a conversational assistant. The script reads user inputs, sends them to the API, and returns the assistant's responses in a terminal-based chat interface.

## Features

- Interactive text-based conversation with Claude 3 Opus.
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

## Example

