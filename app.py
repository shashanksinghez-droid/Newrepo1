from flask import Flask, render_template, session, redirect, url_for, request
import json
import os

app = Flask(__name__)
app.secret_key = "ultra_secret_nebula"

# Load Translations
def load_translations():
    with open('translations.json', 'r', encoding='utf-8') as f:
        return json.load(f)

@app.before_request
def setup():
    if 'lang' not in session:
        session['lang'] = 'en'

@app.route('/lang/<lang_code>')
def set_language(lang_code):
    if lang_code in ['en', 'es', 'hi']:
        session['lang'] = lang_code
    return redirect(request.referrer or url_for('index'))

@app.route('/')
def index():
    t_all = load_translations()
    return render_template('index.html', t=t_all[session['lang']])

@app.route('/library')
def library():
    t_all = load_translations()
    return render_template('library.html', t=t_all[session['lang']])

@app.route('/rankings')
def rankings():
    t_all = load_translations()
    # Mock data
    players = [
        {"name": "Shadow_X", "score": "98,400", "rank": 1},
        {"name": "Cyber_Ghost", "score": "92,100", "rank": 2},
        {"name": "Neon_Bolt", "score": "85,600", "rank": 3}
    ]
    return render_template('rankings.html', t=t_all[session['lang']], players=players)

@app.route('/play/<game_id>')
def play(game_id):
    t_all = load_translations()
    return render_template('player.html', t=t_all[session['lang']], game_id=game_id)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
