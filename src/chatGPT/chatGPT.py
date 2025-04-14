"""Programa para chatGPT"""
import os
from openai import OpenAI
from dotenv import load_dotenv
import keyboard

load_dotenv()

# Obtiene la api key guardada en el archivo .env
api_key = os.getenv("API_KEY")

# Crea una instancia del cliente de OpenAI usando la API key
client = OpenAI(api_key=api_key)

# Lista para guardar el historial de consultas del usuario
queries = []

# Nido para aceptación de consulta del usuario
try:
    print("↑ para editar consulta anterior o enter para consulta nueva")

    # Espera que el usuario pressione una tecla
    while True:
        if keyboard.is_pressed("up"):
            # Revisa si hubieron consultas previas
            if len(queries)>0:
                # Muestra la ultima consulta
                print(f"Last query:{queries[-1]}")
                # Permite editarla o reenviarla
                userquery = input("You: ")
                break
                # Informa que no hay historial previo
            print("No hay consultas previas")
            userquery= input("You: ")
            break
        # Opcion para crear una consulta nueva
        if keyboard.is_pressed("enter"):
            userquery = input("You: ")
            break

    # Nido para el tratamiento
    try:
        # Define un contexto para el sistema
        CONTEXT = "Eres una herramienta que responde siempre con un objeto JSON válido."

        # Nido para la invocación
        try:
            # Se realiza la llamada al modelo con la consulta del usuario y el contexto
            response = client.chat.completions.create(
                model="gpt-4o-mini-2024-07-18", # Modelo utilizado
                response_format={ "type": "json_object" }, # Formato de respuesta
                messages=[
                    {
                    "role": "system", 
                    "content": CONTEXT }, # Contexto del sistema
                    {
                    "role": "user", 
                    "content": userquery } # Consulta del usuario
                ],
                temperature=1,
                max_tokens=100, # Limite de tokens por respuesta
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )

            # Extrae la respuesta en formato texto
            jsonStr=response.choices[0].message.content

            # Guarda la consulta en el historial
            queries.append(userquery)
            print(f"ChatGPT: {jsonStr}")

        # Captura errores en la invocación
        except Exception as e:
            print(f"Ocurrio un error: {e}")

    # Captura errores en el tratamiento
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Captura errores en la consulta del usuario
except Exception as e:
    print(f"Ocurrió un error: {e}")
