from flask import Flask, render_template, request, session, redirect, url_for
import json
import os

app = Flask(__name__)
app.secret_key = "nebula_secret_key"

# Load Translations
with open('translations.json', 'r') as f:
    translations = json.load(f)

@app.before_request
def set_lang():
    if 'lang' not in session:
        session['lang'] = 'en'

@app.route('/change_lang/<lang>')
def change_lang(lang):
    if lang in ['en', 'es']:
        session['lang'] = lang
    return redirect(request.referrer or url_for('index'))

@app.route('/')
def index():
    t = translations[session['lang']]
    return render_template('index.html', t=t)

@app.route('/library')
def library():
    t = translations[session['lang']]
    return render_template('library.html', t=t)

@app.route('/play/<game_id>')
def play(game_id):
    t = translations[session['lang']]
    return render_template('player.html', t=t, game_id=game_id)

@app.route('/leaderboard')
def leaderboard():
    t = translations[session['lang']]
    # Simulated Data
    scores = [
        {"name": "ShadowRunner", "score": 95000, "game": "Neon Rider"},
        {"name": "CyberGhost", "score": 82400, "game": "Cyber Breach"},
        {"name": "NebulaMaster", "score": 71000, "game": "Zenith Explorer"}
    ]
    return render_template('leaderboard.html', t=t, scores=scores)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
