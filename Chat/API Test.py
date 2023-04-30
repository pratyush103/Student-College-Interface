import os
import openai
import gradio as gr
from pop import getresponsegpt

#if you have OpenAI API key as an environment variable, enable the below
#openai.api_key = os.getenv("OPENAI_API_KEY")

#if you have OpenAI API key as a string, enable the below
openai.api_key = "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"

start_sequence = "\nAI:"
restart_sequence = "\nHuman: "


prompt = "The following is a conversation with an AI assistant for the students of MPSTME. The assistant is helpful, creative, clever, and very friendly and helps the students of MPSTME.\n\nHuman: Hello, who are you?\nAI: I am Chatbot built to Assist Students of MPSTME in their subject doubts. How can I help you today?\nHuman: "

def openai_create(prompt):

    '''response = openai.Completion.create(
    model="gpt-3.5-turbo",
    prompt=prompt,
    temperature=0.9,
    max_tokens=150,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )
    breakpoint()'''
    response=getresponsegpt(prompt)


    return response



def chatgpt_clone(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = ' '.join(s)
    output = openai_create(inp)
    history.append((input, output))
    return history, history


block = gr.Blocks(theme=gr.themes.Soft(font=[gr.themes.GoogleFont("Bahnschrift")]))



with block:
    gr.Markdown("""<head> <title>MPSTME Chatbot</title>
    <img src="https://th.bing.com/th/id/R.7c0f694e69f77954e20f846a71b987ad?rik=r%2bDu860FJIOysA&riu=http%3a%2f%2fengineering.nmims.edu%2fimages%2fmpstme_main-logo-horizontal.jpg&ehk=Tp1EF7L%2bfbpBY8FxtoMuu1saiMxxd11Yedr382WlNbU%3d&risl=&pid=ImgRaw&r=0">
    <h1><center>NMIMS Mentor Bot</center></h1></head>
    <h3>Hello I am Chatbot built to Assist Students in their subject doubts</h3>
    
    """)
    chatbot = gr.Chatbot()
    
    message = gr.Textbox(placeholder="Ask a doubt")
    state = gr.State()
    submit = gr.Button("SEND",variant="primary")
    submit.click(chatgpt_clone, inputs=[message, state], outputs=[chatbot, state])
    

block.launch(debug = True)