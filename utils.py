"""
utils.py
Create, delete, update projects
Pre setup dialogs
"""
# Import dependencies
import csv
import serial
from PySide6.QtGui import QIcon
from serial.tools import list_ports
from PySide6.QtCore import QThread, Signal
from interface.app_ui import Ui_MainWindow
from interface.SetFieldsDialog import FieldsDialog
from PySide6.QtCore import QSettings, QCoreApplication, Qt
from PySide6.QtWidgets import QFileDialog, QDialog, QLabel

QCoreApplication.setOrganizationName("LoopTech")
QCoreApplication.setApplicationName("CatchSerial")
setting_obj = QSettings()
setting_obj.setValue("labels", [])


main_ui = Ui_MainWindow()

def get_settings_val(val: str):
    query = setting_obj.value(val)
    return query



"""
get com ports
List available com port
"""


def get_com_port():
    try:
        ports = list_ports.comports()
        return ports

    except Exception as port_error:
        print("Failed to get ports: ", str(port_error))


"""
read stylesheet
Read content in the stylesheet and return style

:arg - stylesheet_filepath
"""


def read_stylesheet(stylesheet_filepath: str):
    try:
        with open(stylesheet_filepath, "r") as stylesheet_file:
            style = stylesheet_file.read()
            stylesheet_file.close()
            return style

    except Exception as stylesheet_error:
        return stylesheet_error


"""
open dir dialog
Opens file dialog to select folder
"""


def open_dir_dialog():
    folder_dialog = QFileDialog()
    folder_path = folder_dialog.getExistingDirectory()
    folder_dialog.show()
    return folder_path


"""
read ports
Start reading port at given port number and baud rate
"""
def read_port_data(port: str, baud_rate: int):
    with serial.Serial("COM3", baudrate=baud_rate) as sr:
        #sr.open()
        while (sr.is_open):
            main_ui.terminal.append(sr.readline().decode())


"""
export data
"""
def export_data(data):
    fields = get_settings_val("labels")
    with open("data.csv", "w", newline="") as csv_file:
        file_writer = csv.writer(csv_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
        file_writer.writerow(fields)  # Write the "test" label in its own row
        file_writer.writerows([[value] for value in data])  # Write each data value in a separate row

"""
SetFieldDialog
Sets up the "SetFieldDialog"
"""


class SetFieldWindow(QDialog):
    def __init__(self):
        super(SetFieldWindow, self).__init__()

        self.fields = get_settings_val("labels")
        self.field_name = QLabel()
        # self.remove_btn.setMaximumSize(50, 30)


        self.ui = FieldsDialog()
        self.ui.setupUi(self)
        self.setStyleSheet(read_stylesheet("config/themes/dark.css"))

        self.setWindowTitle("Add Fields")
        self.setWindowIcon(QIcon("interface/icons/terminal.png"))

        # On add button clicked
        self.ui.add_btn.clicked.connect(self.add_new_field)

        for i in range(0, len(self.fields)):
            self.ui.verticalLayout_4.addWidget(QLabel(self.fields[i]))

    """
    create label
    """
    def create_label(self, text):
        self.ui.verticalLayout_4.addWidget(QLabel(text), 0, Qt.AlignmentFlag.AlignTop)

    """
    add new field
    Adds new column to be used when exporting data
    
    args:
        1. field_name (str)
    """

    def add_new_field(self):
        field_name = self.ui.field_name.text()
        if " " in field_name:
            field_name = field_name.replace(" ", "_")
        if field_name in self.fields:
            pass

        else:
            self.create_label(field_name)
            self.fields.append(field_name)
            setting_obj.setValue("labels", self.fields)

    def open(self):
        self.setModal(True)
        self.show()
        self.exec()

"""
port reader - thread
Creates new thread and read serial data
"""
class PortReader(QThread):
    data_rec = Signal(str)
    def __init__(self, port, baud_rate):
        super().__init__()
        self.port = port
        self.baud_rate = baud_rate
        self.running = True

    def run(self):
        with serial.Serial(self.port, self.baud_rate) as ser:
            while self.running:
                data = ser.readline().decode('utf-8').strip()
                self.data_rec.emit(data)

    def stop(self):
        self.running = False