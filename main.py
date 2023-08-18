import threading
import requests
import base64
from flask import Flask, Response
from kivy.app import App
from kivy.uix.label import Label

# Define Flask app and routes
app_flask = Flask(__name__)

@app_flask.route('/scrape', methods=['GET'])
def scrape():
    image_url = "https://prowebscraping.com/wp-content/uploads/2015/09/data-scraping-service.jpg"
    response = requests.get(image_url)

    if response.status_code == 200:
        image_data = response.content

        base64_image = base64.b64encode(image_data).decode('utf-8')

        html_content = f"""
            <h1 style="text-align:center; margin-top:100px;">Web Scraping</h1>
            <img src='data:image/jpeg;base64,{base64_image}' style="width: 100%;" />
        """
        return Response(html_content, content_type="text/html")
    else:
        return "Failed to fetch image."

def run_flask():
    app_flask.run(host='0.0.0.0', port=5000)

# Define Kivy app and UI
class MyApp(App):
    def build(self):
        threading.Thread(target=run_flask).start()  # Start Flask in a separate thread

        label = Label(text="Kivy App with Flask integration")
        return label

# Run the Kivy app
if __name__ == '__main__':
    MyApp().run()
