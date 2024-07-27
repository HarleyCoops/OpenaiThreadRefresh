# OpenAI Thread Refresher

## Overview

The OpenAI Thread Refresher is a handy tool designed to help you recover and interact with OpenAI assistant threads when you encounter issues such as screen freezes or loss of context. This tool allows you to access specific threads, view messages, rerun conversations, and continue discussions right from your terminal.

## Features

- View current thread messages
- Clear a thread and create a new one
- Rerun a thread with an assistant
- Append a new message and continue the conversation

## Prerequisites

- Python 3.6 or higher
- OpenAI Python library
- python-dotenv library

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/openai-thread-refresher.git
   cd openai-thread-refresher
   ```

2. Install the required dependencies:
   ```
   pip install openai python-dotenv
   ```

3. Set up your environment variables:
   - Create a `.env` file in the project root directory
   - Add the following lines to the `.env` file:
     ```
     OPENAI_API_KEY=your_api_key_here
     OPENAI_THREAD_ID=your_thread_id_here
     OPENAI_ASSISTANT_ID=your_assistant_id_here
     ```
   - Replace `your_api_key_here`, `your_thread_id_here`, and `your_assistant_id_here` with your actual OpenAI API key, thread ID, and assistant ID respectively

## Usage

Run the script using Python:

```
python refresh_openai_thread.py
```

You will be presented with four options:

1. **View current thread messages**: This option allows you to see all the messages in the current thread, helping you recover context.

2. **Clear thread and create a new one**: Use this option if you want to start a fresh conversation.

3. **Rerun thread with assistant**: This option is useful when you've lost context due to a screen freeze. It reruns the entire thread with the assistant, potentially recovering lost information.

4. **Append message and continue conversation**: This option lets you add a new message to the thread and continue the conversation with the assistant. It's particularly useful for asking follow-up questions or providing additional information.

## How It Helps

When using OpenAI's assistant in a web interface, you might encounter situations where the screen goes white or you lose context. This tool provides an easy way to:

1. Access the specific thread you were working on
2. Recover any part of the conversation that might have been lost
3. Continue the conversation from where you left off

By running this tool in your terminal, you maintain control over your conversation threads and can easily recover from interface issues.

## Customization

You can modify the `refresh_openai_thread.py` script to add more functionality or adjust it to your specific needs. For example, you might want to add options for switching between different assistants or implementing more advanced error handling.

## Contributing

Contributions to improve the OpenAI Thread Refresher are welcome. Please feel free to submit pull requests or open issues to suggest improvements or report bugs.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This tool is not officially associated with OpenAI. Always ensure you comply with OpenAI's use policies and terms of service when using their API.