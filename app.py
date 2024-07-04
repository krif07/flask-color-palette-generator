import os
import json
from openai import OpenAI
from flask import Flask, render_template, request
from flask_cors import CORS

from ColorPalettePrompt import ColorPalettePrompt

app = Flask(__name__,
            template_folder='templates'
)
CORS(app)

client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/palette")
def get_prompt_to_palette():
    query = request.args["query"]
    json_colors = ["#FFCC00","#003893","#CE1126"]
    json_colors.append(query)
    print(json_colors)
    return {"colors": json_colors}


@app.post("/palette")
def prompt_to_palette():
    query = request.json.get("query")
    color_palette_prompt = ColorPalettePrompt(client)
    json_colors = json.loads(color_palette_prompt.get_palette(query))
    return {"colors": json_colors}


if __name__ == "__main__":
    app.run(debug=True)