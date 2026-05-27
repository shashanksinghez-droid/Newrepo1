from flask import Flask, render_template, os

app = Flask(__name__)

# Complete list of places for separate pages
PLACES = {
    "kashi-vishwanath": {
        "title": "Kashi Vishwanath Temple",
        "description": "The spiritual heart of Varanasi, dedicated to Lord Shiva.",
        "full_text": "Kashi Vishwanath Temple is one of the most famous Hindu temples dedicated to Lord Shiva. It is located in Varanasi, Uttar Pradesh, India. The temple stands on the western bank of the holy river Ganga, and is one of the twelve Jyotirlingas, the holiest of Shiva temples.",
        "highlights": ["Golden Spire", "Ancient Gyan Vapi Well", "Kashi Vishwanath Corridor"]
    },
    "dashashwamedh-ghat": {
        "title": "Dashashwamedh Ghat",
        "description": "The main and most spectacular ghat in Varanasi.",
        "full_text": "Dashashwamedh Ghat is the main ghat in Varanasi on the Ganga River. It is located close to Vishwanath Temple and is probably the most spectacular ghat. Two Hindu legends are associated with it: according to one, Lord Brahma created it to welcome Lord Shiva.",
        "highlights": ["Evening Ganga Aarti", "Spiritual boat rides", "Proximity to markets"]
    },
    "manikarnika-ghat": {
        "title": "Manikarnika Ghat",
        "description": "The primary cremation ghat and gateway to Moksha.",
        "full_text": "One of the oldest and holiest ghats in Varanasi. It is believed that a soul cremated here attains instant liberation from the cycle of rebirth.",
        "highlights": ["Eternal Cremation Fire", "Chakra-Pushkarini Kund", "Atmosphere of reflection"]
    },
    "sarnath": {
        "title": "Sarnath",
        "description": "Where Buddha gave his first sermon.",
        "full_text": "Located 10 km from Varanasi, Sarnath is where Gautama Buddha first taught the Dharma. It is one of the four main Buddhist pilgrimage sites.",
        "highlights": ["Dhamek Stupa", "Ashoka Pillar", "Archaeological Museum"]
    },
    "assi-ghat": {
        "title": "Assi Ghat",
        "description": "The southern-most ghat, popular with students and yogis.",
        "full_text": "Situated at the confluence of the Ganga and Assi rivers, this ghat is a center for meditation, yoga, and classical music.",
        "highlights": ["Subah-e-Banaras", "Confluence of rivers", "Nearby BHU campus"]
    }
}

@app.route('/')
def home():
    return render_template('index.html', places=PLACES)

@app.route('/place/<place_id>')
def place_detail(place_id):
    place = PLACES.get(place_id)
    if not place:
        return "Place not found", 404
    return render_template('place.html', place=place)

if __name__ == '__main__':
    # Critical for Azure: listen on the PORT environment variable
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
