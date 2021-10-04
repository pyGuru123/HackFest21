from flask import Flask, request, jsonify, redirect
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.errorhandler(404)
def not_found(e):
  return redirect("/translate")

@app.route("/translate", methods = ["GET"])
def translate():
  text = request.args.get("text", None)
  lang = request.args.get("lang", None)

  if text is None:
    return jsonify(
      status = False,
      message = "I need a text ):"
    )
  else:
    if lang is None:
      lang = "id"
    try:
      translate = translator.translate(text, dest = lang)
      return jsonify(
        status = True,
        message = translate.text
      )
    except ValueError:
      return jsonify(
        status = False,
        message = "Target code bahasa tidak ditemukan"
      )

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=4001)