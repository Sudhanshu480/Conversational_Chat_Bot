# Conversational Bot with Chat History

Welcome to the Conversational Bot with Chat History project. This Streamlit-based application leverages the power of Google's Generative AI to provide a conversational interface, allowing users to interact with an AI model and receive responses in real-time. The bot keeps track of the conversation history, making the interaction more natural and coherent.

## Features

- **Real-time Conversation**: Engage in a back-and-forth conversation with the AI.
- **Chat History**: Keeps track of the entire conversation for context and reference until the application is closed.
- **Streamlit Interface**: Simple and intuitive UI built with Streamlit.

## How it Works

The core functionality of the Conversational Bot with Chat History revolves around the `get_response` function. In this project, we implemented two versions of the `get_response` function, with subtle differences. Here's a detailed explanation:

- **User Input:** The function takes a single input from the user: `question`, which is the user's query or message.
- **Language Model Initialization:** The function initializes a Generative AI model using the `google.generativeai` library. The model type is specified as 'gemini-1.0-pro-latest', ensuring we use the latest and most advanced model available.
- **Chat Session Initialization:** A chat session is started with an empty history using the `start_chat` method. This ensures that each session begins afresh, but the chat history is maintained within the session for context.
- **Response Processing:** In Version 1, the response is processed in chunks. While this allows for streaming responses, it results in multiple entries in the chat history, each labeled "Bot Response:". This can make the chat history look cluttered and repetitive.
- **Joining the Text Chunks into a Single String:** To overcome the issue in Version 1, Version 2 aggregates all response chunks into a single string before appending it to the chat history. This ensures that the bot's response is concise and unified, improving the readability of the chat history.
- **Response Formatting and Display:** The final, formatted response is displayed in the Streamlit interface along with the chat history. This is done by appending the user's question and the bot's response to the session state, which is then rendered on the screen.

## Maintaining Chat History

The chat history is managed using Streamlit's session state. Here’s how we do it:

### Version 1: Chunk-Based Maintenance

- **Initialization**: At the start of the session, if the `chat_history` key is not already in the session state, it is initialized as an empty list.
- **Updating History**: Each response chunk is appended individually to the chat history. This means for a single user question, multiple "Bot Response:" entries may appear.
- **Displaying History**: The chat history shows each chunk separately, which can make the conversation look disjointed and repetitive.

![Version 1 Chat History Example](version1_chat_history_example.png)

### Version 2: Aggregated Chunk Maintenance

- **Initialization**: Similar to Version 1, the `chat_history` is initialized as an empty list if not present in the session state.
- **Updating History**: All response chunks are aggregated into a single string before appending it to the chat history. This results in a single entry for each user question.
- **Displaying History**: The chat history shows the entire response as a single entry, making the conversation more readable and coherent.

![Version 2 Chat History Example](version2_chat_history_example.png)

By using a spinner labeled "Response in Progress..." during the response generation, the application also provides visual feedback to users, enhancing the user experience by informing them that the bot is processing their query.

## Prerequisites

- Python 3.8 or higher
- Streamlit
- `google-generativeai` package
- `python-dotenv` package

## Download the Model

The `gemini-1.0-pro-latest` model from Google's Generative AI library is used because it excels in generating coherent and contextually relevant text. This model is highly effective for natural language processing tasks and generates high-quality outputs. To know more visit: [Google Gemini Generative AI](https://github.com/google-gemini/generative-ai-python).

## Usage

1. **Run the Streamlit App**:
   ```sh
   streamlit run bot.py  # For Version 1
   streamlit run app.py  # For Version 2
   ```

2. **Interact with the Bot**:
   - Enter your question in the input field.
   - Click the "Get Response" button.
   - The bot's response and the chat history will be displayed on the screen.

## File Structure

```
conversational-bot/
│
├── bot.py                 # Main application script (Version 1)
├── app.py                 # Main application script (Version 2)
├── requirements.txt       # Required Python packages
├── .env.example           # Example environment variables file
├── README.md              # Project documentation
└── LICENSE                # Project license
```

## Application Code

The main difference between the code of applications lies in the `get_response` function as shown below:

### Version 1 (bot.py)

This version of the code processes the response in chunks and each chunk is appended to the chat history as a separate entry. Thus, for each chunk, "Bot Response" appears in the chat history.

```python
def get_response(question):
    response = chat.send_message(question, stream=True)
    return response
```

### Version 2 (app.py)

This version of the code collects the response chunks into a single response string before appending it to the chat history, ensuring that "Bot Response" appears only once per response.

```python
def get_response(question):
    response_chunks = chat.send_message(question, stream=True)
    response_text = ''.join(chunk.text for chunk in response_chunks)
    return response_text
```

## Contributing

Contributions are welcome! Please feel free to fork this repository and submit pull requests to propose changes or improvements.
