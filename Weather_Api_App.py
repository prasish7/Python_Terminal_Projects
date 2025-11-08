import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit
from PyQt5.QtCore import Qt


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()

        self.city_label = QLabel('Enter Your City:', self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton('Get Weather', self)
        self.temp_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI() 

    def initUI(self):


        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle('Weather App')
        vbox = QVBoxLayout()
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temp_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)
        self.setLayout(vbox)
        self.city_label.setAlignment(Qt.AlignCenter)
        self.temp_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)
        self.city_label.setObjectName("cityLabel")
        self.temp_label.setObjectName("tempLabel")
        self.emoji_label.setObjectName("emojiLabel")
        self.description_label.setObjectName("descriptionLabel")
        self.city_input.setObjectName("cityInput")
        self.get_weather_button.setObjectName("getWeatherButton")
        self.setStyleSheet('''
            #cityLabel, #tempLabel,  #descriptionLabel {
                font-size: 20px;
                
            }
            #emojiLabel {
                font-size: 40px;
                           font-family: "Segoe UI Emoji";
                    
                           
            }
            #descriptionLabel {
                font-size: 18px;
            }
            #cityLabel {
                font-style: italic;
                font-weight: bold;}
            #cityInput {
                font-size: 18px;
                padding: 5px;
            }
            #getWeatherButton {
                font-size: 18px;
                color: White;
                background-color: DarkBlue;
                border: none;
                padding: 10px;
                border-radius: 5px;
                font-weight: bold;
            }
            #getWeatherButton:hover {
                background-color: Blue;
            }
        ''')
        self.get_weather_button.clicked.connect(self.fetch_weather)

    def fetch_weather(self): 
        api_key = 'ec4a156bb7d9b5c2616fdc7fd50d8a80'
        city = self.city_input.text()
        base_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        print ("Fetching weather...")

        try:
            response = requests.get(base_url)
            response.raise_for_status()
            data = response.json()
            

            if data['cod'] == 200:
                main = data['main']
                temperature = main['temp'] - 273.15  
                weather_description = data['weather'][0]['description']
                weather_main = data['weather'][0]['main']
                self.display_weather({
                    "temperature": temperature,
                    "description": weather_description,
                    "main": weather_main
                })
                emoji = ""
                if weather_main == "Clear":
                    emoji = "☀️"
                elif weather_main == "Clouds":
                    emoji = "☁️"
                elif weather_main == "Rain":
                    emoji = "🌧️"
                elif weather_main == "Drizzle":
                    emoji = "🌦️"
                elif weather_main == "Thunderstorm":
                    emoji = "⛈️"
                elif weather_main == "Snow":
                    emoji = "❄️"
                else:
                    emoji = "🌫️"  
                self.temp_label.setText(f"Temperature: {temperature:.2f} °C")
                self.emoji_label.setText(emoji)
                self.description_label.setText(f"Description: {weather_description.capitalize()}")
            
        except requests.exceptions.HTTPError:
            print("HTTP error occurred")
            self.display_error("HTTP error occurred")
            match response.status_code:
                case 400:
                    self.display_error("Bad request: \n Check your input")
                case 401:
                    self.display_error("Unauthorized: \n Check your API key")
                case 403:
                    self.display_error("Forbidden: \n You don't have permission to access this resource")
                case 404:
                    self.display_error("City not found: \n Check the city name")
                case 500:
                    self.display_error("Internal Server Error: \n Try again later")
                case 502:
                    self.display_error("Bad Gateway: \n Server is down or being upgraded")
                case 503:
                    self.display_error("Service Unavailable: \n Server is overloaded or under maintenance")
                case 504:
                    self.display_error("Gateway Timeout: \n Server is not responding")
                case _:
                    self.display_error(f"HTTP Error: {response.status_code}")
                    self.display_error(f"HTTP Error: {response.status_code}")
            
        except requests.exceptions.RequestException:
            self.display_error("Network error: \n Please check your internet connection")
        except requests.exceptions.Timeout:
            self.display_error("Request timed out: \n The server is taking too long to respond")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many redirects: \n Check the URL")
        except requests.exceptions.RequestException as e:
            self.display_error(f"An error occurred: {e}")
    

    def display_error(self, message):
        self.temp_label.setText("Error")
        self.emoji_label.setText("❌")
        self.description_label.setText(message)
    def display_weather(self, weather_data):
        temperature = weather_data['temperature']
        description = weather_data['description']
        self.temp_label.setText(f"Temperature: {temperature:.2f} °C")
        self.description_label.setText(f"Description: {description.capitalize()}")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    weather_app = WeatherApp() 
    weather_app.show()
    sys.exit(app.exec_())