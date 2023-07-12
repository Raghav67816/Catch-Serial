# Import dependencies
import sys
from interface.app_ui import Ui_MainWindow
from PySide6.QtCore import QCoreApplication
from utils import read_stylesheet, load_project, get_settings_val
from PySide6.QtWidgets import QMainWindow, QApplication, QFileDialog

# Import interface files
from interface.dialogs import DataCollecDialog, NewProjectWizard


class AppWindow(QMainWindow):
    def __init__(self):
        super(AppWindow, self).__init__()

        self.isProjectLoaded = False

        # Setup interface
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionExit.setShortcut("Alt+F4")

        # Window Properties
        self.setWindowTitle("Catch Serial")
        # Apply stylesheet
        self.setStyleSheet(read_stylesheet("config/themes/dark.css"))

        # Bind with actions
        self.ui.actionNew_Project.triggered.connect(self.open_new_project_wizard)
        self.ui.actionOpen_Project.triggered.connect(self.load_existing_project)
        self.ui.actionData_Collection.triggered.connect(self.open_data_collection_dialog)

    # Open new project wizard
    def open_new_project_wizard(self):
        wizard = NewProjectWizard()
        wizard.show_project_wizard()

    # Open data collection dialog
    def open_data_collection_dialog(self):
        if get_settings_val("isProjectLoaded"):
            dc_dialog = DataCollecDialog()
            dc_dialog.show_data_collect_preferences()

        else:
            # show_message("Setup Project", "Load or Create a new project", "Please load an existing project or create a new project to use the application", 0)
            print('load project first')

    # Load existing project
    def load_existing_project(self):
        try:
            file_dialog = QFileDialog.getOpenFileName(self, caption="Load existing project", filter="*.json")
            print(file_dialog[0])
            if file_dialog[0] == "":
                pass

            else:
                load_project(file_dialog[0])
                self.ui.projectName.setText(str(get_settings_val("project_name")))
                self.ui.clusterSize.setText(str(get_settings_val("cluster_size")))

        except Exception as error:
            print(error)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AppWindow()
    window.show()
    sys.exit(app.exec())
