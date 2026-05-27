from flask import Flask, render_template, os

app = Flask(__name__)

# Detailed data for Delhi locations
PLACES = {
    "red-fort": {
        "title": "The Red Fort",
        "description": "A symbol of Mughal architectural brilliance.",
        "full_text": "The Red Fort is a historic fort in the city of Delhi in India that served as the main residence of the Mughal Emperors. Built by Shah Jahan in 1639, it is made of massive red sandstone walls. Every year on India's Independence Day, the Prime Minister hoists the national flag here.",
        "highlights": ["Lohori Gate", "Diwan-i-Aam", "Sound and Light Show"]
    },
    "qutub-minar": {
        "title": "Qutub Minar",
        "description": "The tallest brick minaret in the world.",
        "full_text": "The Qutub Minar is a UNESCO World Heritage Site in the Mehrauli area of Delhi. It is a 73-meter tall tapering tower of five storeys, built by Qutb-ud-din Aibak in 1192. It is surrounded by several other ancient and medieval structures.",
        "highlights": ["Iron Pillar of Delhi", "Quwwat-ul-Islam Mosque", "Indo-Islamic Architecture"]
    },
    "india-gate": {
        "title": "India Gate",
        "description": "A war memorial dedicated to Indian soldiers.",
        "full_text": "The India Gate is a memorial to 70,000 soldiers of the British Indian Army who died in the period 1914–21 in the First World War. It is located on the Rajpath and is especially beautiful when lit up at night.",
        "highlights": ["Amar Jawan Jyoti", "Boating at the lake", "Evening walks on Kartavya Path"]
    },
    "lotus-temple": {
        "title": "Lotus Temple",
        "description": "A Baháʼí House of Worship known for its flowerlike shape.",
        "full_text": "Notable for its flowerlike shape, it has become a prominent attraction in the city. Like all Baháʼí Houses of Worship, the Lotus Temple is open to all, regardless of religion or any other qualification.",
        "highlights": ["Petal architecture", "Silent meditation hall", "Beautiful gardens"]
    },
    "humayun-tomb": {
        "title": "Humayun's Tomb",
        "description": "The inspiration for the Taj Mahal.",
        "full_text": "This tomb, built in 1570, is of particular cultural significance as it was the first garden-tomb on the Indian subcontinent. It inspired several major architectural innovations, culminating in the construction of the Taj Mahal.",
        "highlights": ["Charbagh Garden", "Mughal Architecture", "Peaceful surroundings"]
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
    # Required for Azure: Use PORT from environment or 8000 for gunicorn default
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)
