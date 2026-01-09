# Digital Factory Academy - AI Stream Workshop

A hands-on workshop for building AI-powered chatbots using Streamlit and OpenAI.

## Project Structure

```
├── openai_integration/
│   └── app.py          # Template with blank function for attendees to implement
├── response_streaming/
│   └── app.py          # Complete chatbot with streaming responses
├── static_response/
│   └── app.py          # Complete chatbot without streaming
├── .env                # Environment variables (API keys)
├── .gitignore          # Python gitignore template
├── requirements.txt    # Python dependencies
└── README.md
```

## Prerequisites

- Python 3.8 or higher
- VSCode with Python extension installed
- OpenAI API key

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository-url>
cd <repository-name>
```

### 2. Create a Virtual Environment

Open the terminal in VSCode (`Ctrl+`` ` or `Cmd+`` ` on Mac) and run:

```bash
python -m venv venv
```

Activate the virtual environment:

- Windows:
  ```bash
  venv\Scripts\activate
  ```
- Mac/Linux:
  ```bash
  source venv/bin/activate
  ```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Open the `.env` file and add your OpenAI API key:

```
OPENAI_API_KEY=your-api-key-here
```

## Running the Applications

Each folder contains a different version of the chatbot. Use the following commands to run them:

### Static Response (No Streaming)

```bash
streamlit run static_response/app.py
```

This version waits for the complete response before displaying it.

### Response Streaming

```bash
streamlit run response_streaming/app.py
```

This version displays the response in real-time as it's generated.

### OpenAI Integration (Workshop Exercise)

```bash
streamlit run openai_integration/app.py
```

This is a template for workshop attendees to implement the OpenAI API integration themselves.

## Testing Locally

1. Run any of the applications using the commands above
2. Your browser will automatically open to `http://localhost:8501`
3. Type a message in the chat input and press Enter
4. Use the sidebar to adjust settings (where available)

## Workshop Exercise

For the `openai_integration` version, implement the `get_ai_response()` function:

```python
def get_ai_response(messages: list) -> str:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages
    )
    return response.choices[0].message.content
```

## Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError` | Ensure virtual environment is activated and dependencies are installed |
| `AuthenticationError` | Check that your OpenAI API key is correctly set in `.env` |
| Port already in use | Run with a different port: `streamlit run app.py --server.port 8502` |
