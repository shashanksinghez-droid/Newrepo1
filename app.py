from flask import Flask, render_template, abort

app = Flask(__name__)

# Highly detailed data for each location in Varanasi
PLACES_DATA = {
    "kashi-vishwanath": {
        "name": "Kashi Vishwanath Temple",
        "tagline": "The Golden Heart of Kashi",
        "history": "Dedicated to Lord Shiva, this is one of the twelve Jyotirlingas. The current structure was built in 1780 by Ahilyabai Holkar. The temple domes are plated with 800kg of pure gold.",
        "significance": "A visit here is believed to be a path to Moksha (salvation). It has been destroyed and rebuilt several times throughout history, standing as a symbol of resilience.",
        "highlights": ["The massive Kashi Vishwanath Corridor", "The ancient 'Gyan Vapi' well", "The 15.5m high gold spire", "The elaborate Sapta Rishi Aarti ritual"]
    },
    "dashashwamedh-ghat": {
        "name": "Dashashwamedh Ghat",
        "tagline": "Where History and Mythology Meet the Ganga",
        "history": "Known as the oldest and most spectacular ghat. According to legend, Lord Brahma performed a ten-horse sacrifice (Dash-Ashwamedh) here to welcome Lord Shiva.",
        "significance": "It serves as the religious hub of the city where the famous Ganga Aarti takes place every single evening.",
        "highlights": ["The Synchronized Evening Ganga Aarti", "The vibrant local marketplace nearby", "Spectacular boat views at sunset", "Ancient Shrines lining the steps"]
    },
    "manikarnika-ghat": {
        "name": "Manikarnika Ghat",
        "tagline": "The Gateway to the Beyond",
        "history": "One of the oldest ghats in Varanasi. Mythology says Lord Vishnu dug a pit with his discus here, and Lord Shiva's earring fell into it while he was watching Vishnu perform penance.",
        "significance": "Considered the most auspicious place for a Hindu to be cremated, ensuring the soul's immediate liberation from the cycle of birth and death.",
        "highlights": ["The Sacred Chakra-Pushkarini Kund", "The 'Eternal Fire' burning for centuries", "The Manikarnika Vinayaka Temple", "A profound atmosphere of spiritual reflection"]
    },
    "sarnath": {
        "name": "Sarnath",
        "tagline": "The Cradle of Buddhist Enlightenment",
        "history": "Located 10km from Varanasi, this is where Gautama Buddha preached his first sermon after attaining enlightenment at Bodh Gaya.",
        "significance": "One of the four holiest sites for Buddhists worldwide. It marks the birth of the 'Sangha' or the religious community.",
        "highlights": ["The massive Dhamek Stupa (128 ft high)", "The Chaukhandi Stupa", "The Ashoka Pillar and Lion Capital", "The Sarnath Archaeological Museum"]
    },
    "assi-ghat": {
        "name": "Assi Ghat",
        "tagline": "The Southern Gateway and Cultural Hub",
        "history": "Situated at the confluence of the River Assi and the Ganges. It is mentioned in the ancient Puranas as a site of great spiritual power.",
        "significance": "A place of immense peace, preferred by long-term pilgrims, scholars, and yogis for meditation and study.",
        "highlights": ["'Subah-e-Banaras' - A magical morning ritual", "The Peepal tree shrine of Assi Sangameshwar", "Nearby Tulsi Ghat, where the Ramcharitmanas was written", "Vibrant cafes and artist community"]
    },
    "ramnagar-fort": {
        "name": "Ramnagar Fort",
        "tagline": "The Royal Sandstone Legacy",
        "history": "Built in 1750 by Kashi Naresh Raja Balwant Singh. It is constructed in the 'Tulsi' style of architecture using creamy Chunar sandstone.",
        "significance": "The official residence of the Maharaja of Kashi, who is traditionally regarded as the guardian of the city.",
        "highlights": ["The Maharaja's Museum with vintage cars and ivory work", "The unique Astronomical Clock", "The famous Ramlila performance", "The massive Durga Temple inside"]
    },
    "sankat-mochan": {
        "name": "Sankat Mochan Hanuman Temple",
        "tagline": "The Destroyer of Hurdles",
        "history": "Established by the legendary saint-poet Goswami Tulsidas in the early 1500s. It is said he had a vision of Lord Hanuman at this very spot.",
        "significance": "Millions of devotees visit to seek protection from the negative influences of Shani (Saturn).",
        "highlights": ["The 'Besan Ladoo' prasad", "The beautiful temple courtyard", "The Hanuman Jayanti Music Festival", "Tulsidas' original manuscripts"]
    }
}

@app.route('/')
def home():
    return render_template('home.html', places=PLACES_DATA)

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/place/<place_id>')
def place_detail(place_id):
    if place_id not in PLACES_DATA:
        abort(404)
    return render_template('place.html', place=PLACES_DATA[place_id])

if __name__ == '__main__':
    app.run(debug=True)
