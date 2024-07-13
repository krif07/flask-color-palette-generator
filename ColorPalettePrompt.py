class ColorPalettePrompt:
    def __init__(self, client):
        self.client = client

    def get_palette(self, text):
        messages = [
            {"role": "system", "content": "Eres un asistente generador de paletas de colores que responde a indicaciones de texto para generar paletas de colores. Debes generar paletas de colores que se ajusten al tema, ambiente o instrucciones en la indicación. Las paletas deben tener entre 2 y 8 colores."},
            {"role": "user", "content": "Convierta la siguiente descripción verbal de una paleta de colores en una lista de colores: El Mar Mediterráneo"},
            {"role": "assistant", "content": '["#006699", "#66CCCC", "#F0E68C", "#008000", "#F08080"]'},
            {"role": "user", "content": f"Convierta la siguiente descripción verbal de una paleta de colores en una lista de colores: {text}"}
        ]

        stream = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=200
        )
        return stream.choices[0].message.content
