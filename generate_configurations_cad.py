import sys
import os

from PySide6.QtWidgets import QApplication, QMessageBox


# Create the application instance
app = QApplication(sys.argv)

FREECAD_ABS_PATH = 'C:/Users/Work/Downloads/FreeCAD_1.0.1-conda-Windows-x86_64-py311/bin'
sys.path.append(FREECAD_ABS_PATH)

freecad_file_name = "generic_parametric_printable_box.FCStd"
PROJECT_DIR = os.path.dirname(__file__)
freecad_file_dir = os.path.join(PROJECT_DIR, freecad_file_name)

# import the FreeCAD Python interface
try:
    import FreeCAD
    print('The FreeCAD Python interface has been loaded')
except:
    print('FreeCAD API not found. Please check the FREECAD_ABS_PATH variable.')

doc = FreeCAD.openDocument(freecad_file_dir)

params_sheet = doc.Spreadsheet
configurations_sheet = doc.Spreadsheet001


for i in range(2, 6):
	if configurations_sheet.get("A"+str(i)):
		partname = configurations_sheet.get("A" + str(i))
		inside_length = configurations_sheet.get("B" + str(i))
		inside_width = configurations_sheet.get("C" + str(i))
		box_inside_height = configurations_sheet.get("D" + str(i))
		print(inside_length, inside_width, box_inside_height)
		params_sheet.set('inside_length', str(inside_length))
		params_sheet.set('inside_width', str(inside_width))
		params_sheet.set('box_inside_height', str(box_inside_height))
		doc.recompute()
		
		### Begin command Std_Export
		__objs__ = []
		__objs__.append(doc.getObject("Body010"))
		__objs__.append(doc.getObject("Body011"))

		if __objs__:
			export_filepath = os.path.join(os.path.dirname(__file__), "dist", f'{str(partname)}_{str(inside_length)}_{str(inside_width)}_{str(box_inside_height)}_regular.step')
			Part.export(__objs__, export_filepath)
		else:
			pass
		del __objs__
		### End command Std_Export
	else:
		break

# Show a message box
msg_box = QMessageBox()
msg_box.setWindowTitle("Configuration Assist")
msg_box.setText("Generating all configurations has finished.")
msg_box.setIcon(QMessageBox.Information)
msg_box.exec_()

# Exit the application
sys.exit(0)