from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
import os

app = Flask(__name__)
app.secret_key = "phoenix_secret_key_123"

# --- DATABASE CONFIG (SQLite - $0 Cost) ---
# This creates a file named 'phoenix.db' in your folder automatically.
base_dir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(base_dir, 'phoenix.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# --- DATABASE MODEL ---
class StudyLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(200), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

# Create the database file if it doesn't exist
with app.app_context():
    db.create_all()

# --- MULTI-LANGUAGE LOGIC ---
def get_t():
    lang = session.get('lang', 'en')
    with open('translations.json', 'r', encoding='utf-8') as f:
        return json.load(f)[lang]

@app.route('/set_lang/<lang_code>')
def set_lang(lang_code):
    if lang_code in ['en', 'es', 'hi']:
        session['lang'] = lang_code
    return redirect(url_for('index'))

# --- ROUTES ---
@app.route('/')
def index():
    logs = StudyLog.query.order_by(StudyLog.date_created.desc()).all()
    return render_template('index.html', t=get_t(), logs=logs)

@app.route('/add', methods=['POST'])
def add_log():
    topic = request.form.get('topic')
    if topic:
        new_log = StudyLog(topic=topic)
        db.session.add(new_log)
        db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
