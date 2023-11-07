import requests
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication
from numpy.random import randint

from ui import Ui_MainWindow


class Thread(QtCore.QThread):
    updateSignal = QtCore.pyqtSignal(str)

    def __init__(self, status, parent=None):
        super(Thread, self).__init__(parent)
        self.status = status
        self.i = 0

    def run(self):
        while True:
            self.updateSignal.emit(f'{self.status}{self.i}')
            self.i += randint(1, 10)
            self.msleep(1000)


class GUI(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.setWindowTitle("Atutum Convertil")
        # self.setWindowIcon(QIcon("LogoSmall.png"))
        self.pushButton.clicked.connect(self.showWeather)

    def start_thread(self): ...
        # self.thread = Thread(self.status)
        # self.thread.updateSignal.connect(self.statusUpgrader)
        # self.thread.start()ИМ
    def showWeather(self):
        city = self.lineEdit.text()
        api_key = "06a8d30673a0eec361072351fd181fb3"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        response = requests.get(url)
        weather_data = response.json()
        temperature = weather_data['main']['temp']
        temperature_celsius = temperature - 273.15
        weather_type = weather_data['weather'][0]['main']
        # cloudiness = weather_data["clouds"]['all']
        # precipitation = weather_data['precipitation']['value']
        wind = weather_data['wind']['speed']
        # min_temperature = weather_data['main']['temp_min']
        # max_temperature = weather_data['main']['temp_max']
        # atmospheric = weather_data['weather'][0]['description']
        weather_info = f"Temperature: {temperature_celsius:.2f}°C," \
                       f" Weather Type: {weather_type}," \
                       f" Cloudiness: {weather_type}%," \
                       f" Wind: {wind}m/s," \
                         # f" Precipitation: {precipitation}mm," \
                           # f" Atmospheric Phenomena: {atmospheric}"
                            # f" Minimum Temperature: {min_temperature - 273.15:.2f}°C," \
                            # f" Maximum Temperature: {max_temperature - 273.15:.2f}°C," \
        self.label_2.setText(weather_info)
        weather_icon = weather_data['weather'][0]['icon']
        image_url = f"http://openweathermap.org/img/w/{weather_icon}.png"
        image_data = requests.get(image_url).content
        pixmap = QtGui.QPixmap()
        pixmap.loadFromData(image_data)
        self.label_3.setPixmap(pixmap)




if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w = GUI()
    w.show()
    sys.exit(app.exec())

