import tkinter as tk  # Dodaj ten import

def send_message(user_entry, chat_display):
    user_input = user_entry.get()
    chat_display.insert(tk.END, f"Ty: {user_input}\n")
    user_entry.delete(0, tk.END)
    # Placeholder na odpowiedź z AI
    chat_display.insert(tk.END, "AI: (tutaj pojawi się odpowiedź AI)\n")
