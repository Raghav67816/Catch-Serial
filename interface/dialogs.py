# Import dependencies
from json import loads, dumps
from PySide6.QtWidgets import QDialog
from PySide6.QtGui import QIntValidator
from interface.NewProjectDialog import NewProjectUi
from interface.DataCollectionDialog import DataCollecUi
from utils import (
    read_stylesheet, open_dir_dialog, create_project, get_com_port,
    get_settings_val, update_settings
)

"""
New Project Wizard
Create new project using create_new() function
"""


class NewProjectWizard(QDialog):
    def __init__(self):
        super(NewProjectWizard, self).__init__()

        # Setup ui
        self.ui = NewProjectUi()
        self.ui.setupUi(self)
        self.setWindowTitle("Create New Project")

        # Setup variables
        self.project_name = ""
        self.project_author = ""
        self.project_folder_path = ""
        self.project_desc = ""
        self.cluster_size = 0

        # Set stylesheet
        self.setStyleSheet(read_stylesheet("config/themes/dark.css"))

        # Additional settings
        self.clusterValidator = QIntValidator(50, 500, self)
        self.ui.clusterInput.setValidator(self.clusterValidator)

        # On browse button clicked
        self.ui.browseBtn.clicked.connect(self.set_project_folder)

        # On dialog accepted
        self.accepted.connect(self.finalise_project)

    # Set project folder
    def set_project_folder(self):
        project_folder = open_dir_dialog()
        self.project_folder_path = str(project_folder)
        self.ui.projectFolderInput.setText(str(self.project_folder_path))

    """
    finalise project
    once all fields are set and ok is clicked validate fields and create project
    """
    def finalise_project(self):
        if self.ui.projectFolderInput.text() == "":
            pass

        else:
            create_project(self.ui.projectNameInput.text(), self.ui.projectFolderInput.text(),
                           self.ui.projectAuthorInput.text(), self.ui.textEdit.toPlainText(),
                           self.ui.clusterInput.text())

    """
    show project wizard
    Args:-
    
    Sets up ui from NewProjectUi
    Uses create_new_project() function
    """
    def show_project_wizard(self):
        self.setModal(True)
        self.show()
        self.exec_()


"""
data collection dialog
Dialog under preferences to edit settings related to data collection
"""


class DataCollecDialog(QDialog):
    def __init__(self):
        super(DataCollecDialog, self).__init__()

        # Setup ui
        self.ui = DataCollecUi()
        self.ui.setupUi(self)
        self.setWindowTitle("Data Collection")

        self.current_port = ""
        self.mode = "monitor only"
        self.baud_rate = 9600

        # Set stylesheet
        self.setStyleSheet(read_stylesheet("config/themes/dark.css"))

        # Update ports list
        self.ports = get_com_port()
        for i in range(0, len(self.ports)):
            self.ui.portBox.addItem(str(self.ports[i]))

        self.accepted.connect(self.apply_settings)

    # Apply settings
    def apply_settings(self):
        self.baud_rate = self.ui.baudRateInput.text()
        self.current_port = self.ui.portBox.currentText()
        if self.ui.monitorOnlyRBtn.isChecked():
            self.mode = "monitor only"

        elif self.ui.storeDataRBtn.isChecked():
            self.mode = "store data"

        update_settings(get_settings_val("project_name"), get_settings_val("project_path"), self.baud_rate,
                        self.current_port, get_settings_val("cluster_size"), get_settings_val("isProjectLoaded"), self.mode)

        with open(str(get_settings_val("project_path")), "r+") as project_file:
            project_json = loads(project_file.read())
            project_file.truncate(0)
            project_file.seek(0)
            project_json["mode"] = get_settings_val("mode")
            project_json["baud rate"] = get_settings_val("baud_rate")
            project_file.write(dumps(project_json))
            project_file.close()

    def show_data_collect_preferences(self):
        self.setModal(True)
        self.show()
        self.exec_()
