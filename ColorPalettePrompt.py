class ColorPalettePrompt:
    def __init__(self, client):
        self.client = client

    def get_palette(self, text):
        prompt = f"""
        Eres un asistente generador de paletas de colores que responde a indicaciones de texto para generar paletas de colores.

        Debes generar paletas de colores que se ajusten al tema, ambiente o instrucciones en la indicación.
        Las paletas deben tener entre 2 y 8 colores.

        Q: Convierta la siguiente descripción verbal de una paleta de colores en una lista de colores: El Mar Mediterráneo
        A: ["#006699", "#66CCCC", "#F0E68C", "#008000", "#F08080"]

        Formato deseado: un arreglo JSON de código de colores hexadecimales 

        Q: Convierta la siguiente descripción verbal de una paleta de colores en una lista de colores: {text}
        A:
        """

        stream = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "user",
                    "content": prompt,

                }
            ],
            max_tokens=200
        )
        return stream.choices[0].message.content
