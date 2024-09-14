import tkinter as tk
from tkinter import scrolledtext

def create_main_window(send_message_callback):
    # Utworzenie głównego okna
    window = tk.Tk()
    window.title("AI Chat App")

    # Pole wyświetlania czatu
    chat_display = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=50, height=20)
    chat_display.pack(padx=10, pady=10)

    # Pole do wpisywania tekstu przez użytkownika
    user_entry = tk.Entry(window, width=50)
    user_entry.pack(padx=10, pady=10)

    # Dodanie obsługi klawisza Enter
    user_entry.bind("<Return>", lambda event: send_message_callback())

    # Przycisk wysyłania wiadomości
    send_button = tk.Button(window, text="Wyślij", command=send_message_callback)
    send_button.pack(padx=10, pady=10)

    return window, chat_display, user_entry
