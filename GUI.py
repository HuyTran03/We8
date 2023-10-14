import tkinter as tk
from tkinter.scrolledtext import *
import datetime

def on_submit(event=None):
    user_input = input_field.get().lower()
   # User message (tag is user)
    output_field.config(state='normal')
    output_field.tag_config('user', foreground='white', background='#535353')
    output_field.insert('end', '\n' + user_input + '\n\n', 'user')
    
    # Chatbot response (tag is response)
    output_field.tag_config('response', foreground='white', background='#333333')
    output_field.insert('end', '\nBert: ', 'response')
    
    if user_input == 'hi':
        output_field.insert('end', 'Hello, how can I help you?\n\n', 'blue')
    elif user_input == 'how are you':
        output_field.insert('end', 'I am Okay. How about you?\n\n', 'blue')
    elif user_input == 'how old are you':
        output_field.insert('end', 'My creator just brought me to life in front of you. I am not much older than 10 minutes.\n\n', 'blue')
    elif user_input == 'what time is it':
        now = datetime.datetime.now()
        output_field.insert('end', "It's "+ now.strftime("%H:%M:%S %p")+'\n\n', 'blue')
    elif user_input == 'bye':
        output_field.insert('end', 'Goodbye, have a nice day!\n\n', 'blue')
    else:
        # output_field.tag_config('response', font=("Futura bold", 30))
        # output_field.insert('end', 'I LIKE PENIS\n\n', 'response')
        output_field.insert('end', 'I am sorry, I do not understand.\n\n', 'response')

    input_field.delete(0, 'end')
    output_field.yview(tk.END)
    output_field.config(state='disabled')
    
""" 
def on_submit(event=None):
    user_input = input_field.get().lower()
   # User message (tag is user)
    output_field.config(state='normal')
    output_field.tag_config('user', foreground='white', background='#535353')
    output_field.insert('end', '\n' + user_input + '\n\n', 'user')
    
    # Chatbot response (tag is response)
    output_field.tag_config('response', foreground='white', background='#333333')
    output_field.insert('end', '\nBert: ', 'response')
    
    
    # Get restaurant name recommendation 
    restaurant_recommendation = model_huy_insert_here
    output_field.tag_config('response', foreground='white', background='#333333', font=("Futura bold", 15))
    output_field.insert('end', restaurant_recommendation, 'response')
    
    # Get restaurant details 
    restaurant_background = model_sophia_insert_here
    output_field.tag_config('response', foreground='white', background='#333333', font=("Futura bold", 15))
    output_field.insert('end', restaurant_background, 'response')
    
    input_field.delete(0, 'end')
    output_field.yview(tk.END)
    output_field.config(state='disabled')

"""

root = tk.Tk()
root.title("Eating")

# Output Frame 
output_frame = tk.Frame(root, width=150, height=500)
output_frame.pack_propagate(False)
output_frame.pack(side='top', fill='both', expand=True, padx=20)
#output_label = tk.Label(output_frame, text="Chatbot:")
# output_label.pack(side='left', padx=5, pady=5)

# Make autoscrolling when text is full 
output_field = ScrolledText(output_frame)

# Output Text details 
output_field.pack(side='left', fill='both', expand=True, padx=2, pady=3)
output_field.config(state='disabled')
output_field.tag_config('user', background='#1a3a46', justify='center')  # I don't think this does anything
output_field.tag_config('response', background='lightgreen', justify='center')  # I don't think this does anything 
output_field.config(font=("Futura", 15))
output_field.yview(tk.END)

# Input frame
input_frame = tk.Frame(root, width=125, height=20)
# input_frame.pack_propogate(False)
input_frame.pack(padx=20)
input_frame.pack(side='bottom', fill='x')
#input_label = tk.Label(input_frame, text="User:")
#input_label.pack(side='left', padx=5, pady=5)

input_field = tk.Entry(input_frame, width=130, bd=2.5, justify='center')
input_field.pack(side='left', padx=5, pady=5)
input_field.bind("<Return>", on_submit)

root.mainloop() 
