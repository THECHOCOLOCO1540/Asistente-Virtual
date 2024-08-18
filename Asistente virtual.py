import tkinter as tk
from tkinter import scrolledtext

# Función para manejar el envío de preguntas
def send_question():
    question = entry_box.get("1.0", tk.END).strip()
    if question:
        # Aquí integrarías la llamada a la API de OpenAI
        response = "Respuesta simulada de OpenAI a: " + question
        response_box.configure(state='normal')
        response_box.delete('1.0', tk.END)
        response_box.insert(tk.INSERT, response)
        response_box.configure(state='disabled')

# Configuración de la ventana principal
root = tk.Tk()
root.title("Asistente Virtual")

# Campo de entrada para preguntas
entry_box = scrolledtext.ScrolledText(root, height=3, width=50)
entry_box.pack(pady=10)

# Botón para enviar preguntas
send_button = tk.Button(root, text="Enviar Pregunta", command=send_question)
send_button.pack(pady=10)

# Área de texto para mostrar respuestas
response_box = scrolledtext.ScrolledText(root, height=10, width=50)
response_box.pack(pady=10)
response_box.configure(state='disabled')

root.mainloop()

import openai




def send_question():
    question = entry_box.get("1.0", tk.END).strip()
    if question:
        try:
            openai.api_key = 'tu_clave_api_aquí'
            response = openai.Completion.create(
                engine="text-davinci-002",
                prompt=question,
                max_tokens=150
            )
            text_response = response.choices[0].text.strip()
        except Exception as e:
            text_response = "Error: " + str(e)

        response_box.configure(state='normal')
        response_box.delete('1.0', tk.END)
        response_box.insert(tk.INSERT, text_response)
        response_box.configure(state='disabled')




