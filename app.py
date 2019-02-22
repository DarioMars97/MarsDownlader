from PyQt5.QtCore import *
import urllib.request
from PyQt5.QtWidgets import *
import sys

import MarsDownloader2


class MarsDownloader(QDialog,MarsDownloader2.Ui_Dialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        self.close_button.clicked.connect(self.close)
        self.download_button.clicked.connect(self.download_file)
        self.save_location_button.clicked.connect(self.browse_save_location)

    def browse_save_location(self):
        save_file, _ = QFileDialog.getSaveFileName(caption="Save File As", directory=".",
                                                   filter="All Files (*.*)")
        self.save_location.setText(QDir.toNativeSeparators(save_file))

    def download_file(self):
        url = self.lineEdit.text()
        save_location = self.save_location.text()
        try:
            urllib.request.urlretrieve(url, save_location, self.report_for_download)

        except:
            QMessageBox.Warning(self, "Warning", "The download failed. ")
            return
        #
        self.lineEdit.setText("")
        self.progressBar.setValue(0)
        self.save_location.setText("")
        QMessageBox.information(self, "Information", "The Download is complete")

    def report_for_download(self, block_num, block_size, total_size):
        read_so_far = block_num * block_size
        if total_size > 0:
            percentage = read_so_far * 100 / total_size
            self.progressBar.setValue(int(percentage))


app = QApplication(sys.argv)
mars_downloader = MarsDownloader()
mars_downloader.show()
app.exec_()
