import os
from flask import Flask, render_template

app = Flask(__name__)

# Structured data for temples
TEMPLES = {
    "kashi-vishwanath": {
        "name": "Kashi Vishwanath Temple",
        "desc": "One of the most famous Hindu temples dedicated to Lord Shiva, located on the western bank of the holy river Ganga.",
        "history": "The temple has been destroyed and reconstructed several times in history. The current structure was built by Ahilyabai Holkar in 1780.",
        "highlight": "The 15.5m high gold spire and the sacred Jyotirlinga.",
        "img_url": "https://images.unsplash.com/photo-1627894483216-2138af692e32?q=80&w=1000&auto=format&fit=crop"
    },
    "sankat-mochan": {
        "name": "Sankat Mochan Hanuman Temple",
        "desc": "Established by the famous Hindu preacher and saint poet Sri Goswami Tulsidas in the early 16th century.",
        "history": "It is situated by the Assi River and is one of the sacred temples of Lord Hanuman.",
        "highlight": "Famous for its 'Besan Ke Laddu' prasad and the annual music festival.",
        "img_url": "https://images.unsplash.com/photo-1582510003544-4d00b7f74220?q=80&w=1000&auto=format&fit=crop"
    },
    "kaal-bhairav": {
        "name": "Kaal Bhairav Temple",
        "desc": "The 'Kotwal of Kashi', Kaal Bhairav is believed to be the guardian deity of Varanasi.",
        "history": "It is one of the oldest Shiva temples in Varanasi, located near Visheshar Ganj.",
        "highlight": "Devotees usually visit this temple first to seek permission to stay in the city.",
        "img_url": "https://images.unsplash.com/photo-1624309325850-997274099432?q=80&w=1000&auto=format&fit=crop"
    },
    "durga-kund": {
        "name": "Durga Kund Temple",
        "desc": "Built in the 18th century, this temple is painted red with ochre and features a large rectangular tank (Kund).",
        "history": "Built by a Bengali Maharani, it is a fine example of Nagara style architecture.",
        "highlight": "The intricate stone carvings and the vibrant red color of the temple walls.",
        "img_url": "https://images.unsplash.com/photo-161912023133be-082e6d628689?q=80&w=1000&auto=format&fit=crop"
    }
}

@app.route('/')
def index():
    return render_template('index.html', temples=TEMPLES)

@app.route('/temple/<id>')
def temple_detail(id):
    temple = TEMPLES.get(id)
    if not temple:
        return "Temple not found", 404
    return render_template('detail.html', temple=temple)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)
