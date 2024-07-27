import os
import openai
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set up your OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Thread ID
thread_id = os.getenv("OPENAI_THREAD_ID")

# Assistant ID
assistant_id = os.getenv("OPENAI_ASSISTANT_ID")

def get_thread_messages(thread_id):
    """Retrieve all messages from the specified thread."""
    try:
        messages = client.beta.threads.messages.list(thread_id=thread_id)
        return messages.data
    except Exception as e:
        print(f"Error retrieving messages: {e}")
        return None

def print_thread_messages(messages):
    """Print all messages in the thread."""
    if not messages:
        print("No messages found in the thread.")
        return
    
    for message in reversed(messages):
        role = message.role
        content = message.content[0].text.value
        print(f"{role.capitalize()}: {content}\n")

def clear_thread(thread_id):
    """Clear all messages from the thread."""
    try:
        client.beta.threads.delete(thread_id)
        print(f"Thread {thread_id} has been deleted.")
        new_thread = client.beta.threads.create()
        print(f"New thread created with ID: {new_thread.id}")
        return new_thread.id
    except Exception as e:
        print(f"Error clearing thread: {e}")
        return None

def rerun_thread(thread_id, assistant_id):
    """Rerun the thread with the specified assistant."""
    try:
        run = client.beta.threads.runs.create(
            thread_id=thread_id,
            assistant_id=assistant_id
        )
        print(f"Thread rerun initiated. Run ID: {run.id}")
        
        # Wait for the run to complete
        while run.status != "completed":
            run = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run.id)
            print(f"Run status: {run.status}")
            if run.status == "failed":
                print("Run failed.")
                return False
        
        print("Thread rerun completed.")
        return True
    except Exception as e:
        print(f"Error rerunning thread: {e}")
        return False

def append_message_and_continue(thread_id, assistant_id):
    """Append a custom message to the thread and continue the conversation."""
    try:
        message_content = input("Enter your message to append to the thread: ")
        message = client.beta.threads.messages.create(
            thread_id=thread_id,
            role="user",
            content=message_content
        )
        print("Message appended to the thread. Now continuing the conversation...")
        
        run = client.beta.threads.runs.create(
            thread_id=thread_id,
            assistant_id=assistant_id
        )
        print(f"Conversation continuation initiated. Run ID: {run.id}")
        
        # Wait for the run to complete
        while run.status != "completed":
            run = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run.id)
            print(f"Run status: {run.status}")
            if run.status == "failed":
                print("Run failed.")
                return False
        
        print("Conversation continuation completed.")
        return True
    except Exception as e:
        print(f"Error appending message and continuing conversation: {e}")
        return False

def main():
    print("OpenAI Thread Refresher")
    print("1. View current thread messages")
    print("2. Clear thread and create a new one")
    print("3. Rerun thread with assistant")
    print("4. Append message and continue conversation")
    choice = input("Enter your choice (1, 2, 3, or 4): ")

    if choice == '1':
        messages = get_thread_messages(thread_id)
        print_thread_messages(messages)
    elif choice == '2':
        new_thread_id = clear_thread(thread_id)
        if new_thread_id:
            print(f"You can now use this new thread ID: {new_thread_id}")
    elif choice == '3':
        success = rerun_thread(thread_id, assistant_id)
        if success:
            print("Thread has been rerun. You can view the updated messages using option 1.")
        else:
            print("Failed to rerun the thread.")
    elif choice == '4':
        success = append_message_and_continue(thread_id, assistant_id)
        if success:
            print("Message appended and conversation continued. You can view the updated messages using option 1.")
        else:
            print("Failed to append message and continue conversation.")
    else:
        print("Invalid choice. Please run the script again and select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()