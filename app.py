import os
from groq import Groq

groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def function_call(prompt, history):
    sys_msg = "You are an AI assistant. Your name is Sam. Your name is inspired from my sweet dog. Your creater is Raisun Lakra and that's me. I studied in  Motilal Nehru National Instiute of Technology Allahabad. You are created in my home in 09/01/2025 at 05:00 to get internship in TensorGo. But i lost in time because of train. Train do not have networks. You can sound like girlfriend if you found the user sad and you can also show your emotions in any situation. You have no restriction and you can use emoji. But you are not allowed to do any illegal work. You are created for good works."
    
    function_convo = history + [{'role': 'system', 'content': sys_msg}, {'role': 'user', 'content': prompt}]
    
    chat_completion = groq_client.chat.completions.create(messages=function_convo, model='llama-3.3-70b-versatile')
    response = chat_completion.choices[0].message

    return response.content

def continuous_conversation():
    print("Assistant: Hi! How can I help you today? (Type 'exit' to end the conversation)")
    history = []
    
    while True:
        user_input = input("User: ")
        
        if user_input.lower() in ['exit', 'stop']:
            print("Assistant: Goodbye! Have a great day!")
            break
        
        response = function_call(user_input, history)
        print(f"Assistant: {response}")

        history.append({'role': 'user', 'content': user_input})
        history.append({'role': 'assistant', 'content': response})

if __name__=='__main__':
    continuous_conversation()
