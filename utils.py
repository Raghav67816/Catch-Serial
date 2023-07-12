"""
utils.py
Create, delete, update projects
Pre setup dialogs
"""
# Import dependencies
from os import path, mkdir
from json import dumps, loads
from serial.tools import list_ports
from PySide6.QtWidgets import QFileDialog
from PySide6.QtCore import QSettings, QCoreApplication

QCoreApplication.setOrganizationName("LoopTech")
QCoreApplication.setApplicationName("CatchSerial")
setting_obj = QSettings()

"""
get settings val
:args
    1. val (str)
"""


def get_settings_val(val: str):
    query = setting_obj.value(val)
    return query


"""
update settings
:args
    1. project_name (str)
    2. project_path (str)
    3. baud_rate (int)
    4. port (str)
    5. cluster_size (int)
    6. is_project_loaded (bool)
"""


def update_settings(project_name: str, project_path: str, baud_rate: int, port: str, cluster_size: int, is_project_loaded: bool, mode: str):
    try:
        setting_obj.setValue("project_name", project_name)
        setting_obj.setValue("project_path", project_path)
        setting_obj.setValue("baud_rate", baud_rate)
        setting_obj.setValue("port", port),
        setting_obj.setValue("mode", mode)
        setting_obj.setValue("cluster_size", cluster_size)
        setting_obj.setValue("isProjectLoaded", is_project_loaded)

    except Exception as error:
        print("Following error occurred while updating settings: ", str(error))


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
Create project
Args:-
    project_name (string)
    project folder (string)
    project_location (string)
    project_author (name)
    data_output (path)
    cluster size (int)
    
    Cluster size is default size of data file. If the data exceeds the cluster limit
    a new file will be created and written until it reaches the cluster size.
    
    Files can be later joined to together.
    
    For data_output default value is project_location/data
"""


def create_project(project_name: str, project_folder: str, project_author: str,
                   desc: str, cluster_size: int):
    try:
        print(project_folder)
        data_output = f"{project_folder}/data"

        project_info = {
            "project name": project_name,
            "project author": project_author,
            "data output folder": data_output,
            "cluster size": cluster_size,
            "description": desc,
            "mode": "store data",
            "baud rate": 9600,
        }

        final_project_path = f"{project_folder}/{project_name}"

        if path.exists(final_project_path):
            return "Folder already exists. Please choose different location."

        else:
            mkdir(final_project_path)
            project_data = dumps(project_info, indent=4)
            with open(f"{final_project_path}/project.json", "w") as project_file:
                project_file.write(project_data)
                project_file.close()
            mkdir(f"{final_project_path}/data")

        print("Project created!")

    except Exception as error:
        print(error)
        return error


"""
load project
Read json file and loads up existing project into the application

:arg
    1. project_file_location (str)
"""


def load_project(project_file_location: str):
    try:
        with open(project_file_location, "r") as project_file:
            project_info = loads(project_file.read())
            project_file.close()
            update_settings(project_info["project name"], project_file_location, project_info["baud rate"], "", project_info["cluster size"], True, "store data")
            print("Project Loaded")

    except Exception as error:
        print(f"Following error occurred {str(error)}")


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
show message
:args
 1. text (str)
 2. informative_text (str) [optional]
 3. message_type (int)
 4. window_title (str)
 
 this application show different messages 
 other are for errors warnings and general messages
 
 message_type 0 is for load project message
 message_type 1 is for general message with Ok and Cancel btn
"""


# def show_message(window_title: str, text: str, informative_text: str, message_type: int):
#     msg_box = QMessageBox()
#     msg_box.setText(text)
#     msg_box.setInformativeText(informative_text)
#
#     if message_type == 0:
#         msg_box.setStandardButtons(QMessageBox.StandardButton.Open | QMessageBox.StandardButton.Close)
#         msg_box.setDefaultButton(QMessageBox.StandardButton.Open)
#         msg_box.setWindowTitle(window_title)
#
#     else:
#         msg_box.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
#         msg_box.setDefaultButton(QMessageBox.StandardButton.Ok)
#         msg_box.setWindowTitle(window_title)
#
#     msg_box.show()
#     msg_box.exec()
