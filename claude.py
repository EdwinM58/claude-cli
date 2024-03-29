import anthropic
import os
import time
import threading
import sys

def animate_dots(stop_event): 
    while not stop_event.is_set():
        for i in range(4):
            dot = "." * i
            print(f"\rClaude is typing{dot}", end="", flush=True)
            time.sleep(0.5)
            if stop_event.wait(0.5):
                break
        print("\r                              ", end="", flush=True)

	

def main():
    client = anthropic.Anthropic(
        # defaults to os.environ.get("ANTHROPIC_API_KEY")
        api_key="API-KEY",
    )
    print("""
          ________ 
         /        \    
	      |  o    o  |   
         \  ____  /    
          `. -- ,'    
            `--'
    """)
    print(f"===== CLAUDE 3 OPUS =====")    
    print("type 'quit' to exit")

    conversation = []
    while True: 
        user_input = input("you: ")
        if user_input.lower() == "quit": 
            break
        print()
      
        conversation.append({"role": "user", "content": user_input})

        try:
            stop_event = threading.Event()
            animation_thread = threading.Thread(target=animate_dots, args=(stop_event,))
            animation_thread.start() 
            message = client.messages.create(
                model="claude-3-opus-20240229",
                max_tokens=1024,
                messages=conversation   
            )
            stop_event.set()
            animation_thread.join()
            sys.stdout.write("\r                              \n")
            sys.stdout.flush()

            assistant_response = message.content[0].text.strip()
            conversation.append({"role": "assistant", "content": assistant_response})
            print(f"claude: {assistant_response}")
            print()
        except Exception as e: 
            print(f"An error has occured: {str(e)}")

    
if __name__ == "__main__": 
    main()
