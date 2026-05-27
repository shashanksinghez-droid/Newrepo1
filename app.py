from flask import Flask, render_template, os

app = Flask(__name__)

# Data for the website
PLACES = {
    "lotus-temple": {
        "name": "Lotus Temple",
        "info": "Known for its flowerlike shape, it is a Baháʼí House of Worship.",
        "fact": "It is open to all, regardless of religion."
    },
    "red-fort": {
        "name": "Red Fort",
        "info": "A historic fort in Delhi that served as the main residence of the Mughal Emperors.",
        "fact": "It is a UNESCO World Heritage Site."
    }
}

@app.route('/')
def index():
    return render_template('index.html', places=PLACES)

if __name__ == '__main__':
    # Azure uses the PORT environment variable to map traffic
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)
