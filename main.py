from ui import create_main_window
from chat import send_message

# Funkcja pomocnicza do obsługi wysyłania wiadomości (przekazywana do UI)
def handle_send_message():
    send_message(user_entry, chat_display)

# Tworzenie głównego okna
window, chat_display, user_entry = create_main_window(handle_send_message)

# Uruchomienie aplikacji
window.mainloop()
