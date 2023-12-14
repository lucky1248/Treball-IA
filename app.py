from flask import Flask, render_template, send_from_directory

app = Flask(__name__, static_folder='static')

# Ruta para servir archivos JSON de traducción
@app.route('/translations/<lang>.json')
def translations(lang):
    return send_from_directory('translations', f'{lang}.json')

# Ruta para servir tu página HTML
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False) #use_reloader=False pq el watchdog dona problemes
