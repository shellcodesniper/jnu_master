# NOTE : description ["Weber's law"]
# NOTE : Author ["KuuwangE <shellcodesniper@jnu.ac.kr>"]
# NOTE : 2023.03.27

import numpy as np
import sys

# from custom_elements import SliderStyleProxy
from PyQt5 import QtCore, QtWidgets

title = f"Kuwang's law"

class KuwangWindow(QtWidgets.QMainWindow):
  def __init__(self):
    super().__init__()
    self.setWindowTitle(title)
    self.resize(800, 600)

    self.object_lumin= QtWidgets.QSlider(QtCore.Qt.Horizontal, self)
    self.surround_lumin= QtWidgets.QSlider(QtCore.Qt.Horizontal, self)
    self.set_layout()
    self.connect_handler()

  # INFO : Set Layout
  def set_layout(self):
    self.object_lumin.setRange(0, 2550)
    self.object_lumin.move(600, 10)

    self.surround_lumin.setRange(0, 2550)
    self.surround_lumin.move(600, 50)

  def connect_handler(self):
    self.object_lumin.valueChanged.connect(self.obj_lum_changed)
    self.surround_lumin.valueChanged.connect(self.sur_lum_changed)

  def obj_lum_changed(self):
    v = float(int(self.object_lumin.value()) / 10)
    print(v)

  def sur_lum_changed(self):
    v = float(int(self.surround_lumin.value()) / 10)
    print(v)



app = QtWidgets.QApplication(sys.argv)
# app.setStyle("fusion")
# app.setStyleSheet(QSS)
window = KuwangWindow()
window.show()
app.exec_()
