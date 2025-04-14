from openai import OpenAI
from dotenv import load_dotenv
import os
import keyboard

load_dotenv()
api_key = os.getenv("API_KEY")
client = OpenAI(api_key=api_key)

queries = []

# Nido para aceptación de consulta del usuario
try:
    print("Presiona ↑ para editar tu consulta anterior o presiona enter para escribir una consulta nueva")
    
    #Espera la tecla
    while True:
        if keyboard.is_pressed("up"):
            if len(queries)>0:
                print(f"Last query:{queries[-1]}")
                userquery = input("You: ")
                break
            else:
                print("No hay consultas previas")
                userquery= input("You: ")
                break
        elif keyboard.is_pressed("enter"):
            userquery = input("You: ")
            break
    

    # Nido para el tratamiento
    try:
        context = "Eres una herramienta que responde siempre con un objeto JSON válido."

        # Nido para la invocación
        try:
            response = client.chat.completions.create( 
                model="gpt-4o-mini-2024-07-18", 
                response_format={ "type": "json_object" }, 
                messages=[ 
                    { 
                    "role": "system", 
                    "content": context }, 
                    { 
                    "role": "user", 
                    "content": userquery } 
                ], 
                temperature=1, 
                max_tokens=100, 
                top_p=1, 
                frequency_penalty=0, 
                presence_penalty=0 
            ) 
            jsonStr=response.choices[0].message.content 
            queries.append(userquery)
            print(f"ChatGPT: {jsonStr}")

        except Exception as e:
            print(f"Ocurrio un error: {e}")

    except Exception as e:
        print(f"Ocurrió un error: {e}")

except Exception as e:
    print(f"Ocurrió un error: {e}")
