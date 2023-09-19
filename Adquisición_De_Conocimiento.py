# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 10:30:23 2023

@author: cesar
"""

conocimiento = {
    "Hola": "Hola, ¿en qué puedo ayudarte?",
    "¿Cómo estás?": "Estoy aquí para asistirte, ¿en qué puedo ayudarte?",
    "¿De qué te gustaría hablar?": "Estoy aquí para ayudarte en cualquier tema que desees, ¿en qué estás interesado?"
}

def obtener_respuesta(pregunta):
    respuesta = conocimiento.get(pregunta, None)
    if respuesta:
        return respuesta
    else:
        print("Lo siento, no tengo una respuesta predefinida para esa pregunta.")
        agregar_nuevo_conocimiento(pregunta)

def agregar_nuevo_conocimiento(pregunta):
    respuesta = input("Por favor, proporciona una respuesta para esta pregunta: ")
    conocimiento[pregunta] = respuesta
    print("¡Gracias por agregar nueva información a mi base de datos!")

# Ejemplo de interacción
while True:
    usuario_input = input("Usuario: ")
    if usuario_input.lower() == "salir":
        print("¡Hasta luego!")
        break

    respuesta = obtener_respuesta(usuario_input)
    print("Finalizado:", respuesta)
