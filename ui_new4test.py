# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new4test.ui'
##
## Created by: Qt User Interface Compiler version 6.11.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 800)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.vboxLayout = QVBoxLayout(self.centralwidget)
        self.vboxLayout.setObjectName(u"vboxLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.hboxLayout = QHBoxLayout(self.frame)
        self.hboxLayout.setObjectName(u"hboxLayout")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.hboxLayout.addWidget(self.label)

        self.spacerItem = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hboxLayout.addItem(self.spacerItem)

        self.label1 = QLabel(self.frame)
        self.label1.setObjectName(u"label1")

        self.hboxLayout.addWidget(self.label1)


        self.vboxLayout.addWidget(self.frame)

        self.frame1 = QFrame(self.centralwidget)
        self.frame1.setObjectName(u"frame1")
        self.gridLayout = QGridLayout(self.frame1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label2 = QLabel(self.frame1)
        self.label2.setObjectName(u"label2")

        self.gridLayout.addWidget(self.label2, 0, 0, 1, 1)

        self.yearCombo = QComboBox(self.frame1)
        self.yearCombo.setObjectName(u"yearCombo")

        self.gridLayout.addWidget(self.yearCombo, 0, 1, 1, 1)

        self.label3 = QLabel(self.frame1)
        self.label3.setObjectName(u"label3")

        self.gridLayout.addWidget(self.label3, 0, 2, 1, 1)

        self.roadCombo = QComboBox(self.frame1)
        self.roadCombo.setObjectName(u"roadCombo")

        self.gridLayout.addWidget(self.roadCombo, 0, 3, 1, 1)

        self.label4 = QLabel(self.frame1)
        self.label4.setObjectName(u"label4")

        self.gridLayout.addWidget(self.label4, 1, 0, 1, 1)

        self.weatherCombo = QComboBox(self.frame1)
        self.weatherCombo.setObjectName(u"weatherCombo")

        self.gridLayout.addWidget(self.weatherCombo, 1, 1, 1, 1)

        self.label5 = QLabel(self.frame1)
        self.label5.setObjectName(u"label5")

        self.gridLayout.addWidget(self.label5, 1, 2, 1, 1)

        self.severityCombo = QComboBox(self.frame1)
        self.severityCombo.setObjectName(u"severityCombo")

        self.gridLayout.addWidget(self.severityCombo, 1, 3, 1, 1)


        self.vboxLayout.addWidget(self.frame1)

        self.hboxLayout1 = QHBoxLayout()
        self.hboxLayout1.setObjectName(u"hboxLayout1")
        self.frame2 = QFrame(self.centralwidget)
        self.frame2.setObjectName(u"frame2")
        self.vboxLayout1 = QVBoxLayout(self.frame2)
        self.vboxLayout1.setObjectName(u"vboxLayout1")
        self.label6 = QLabel(self.frame2)
        self.label6.setObjectName(u"label6")

        self.vboxLayout1.addWidget(self.label6)

        self.textEdit = QTextEdit(self.frame2)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setReadOnly(True)

        self.vboxLayout1.addWidget(self.textEdit)

        self.label7 = QLabel(self.frame2)
        self.label7.setObjectName(u"label7")

        self.vboxLayout1.addWidget(self.label7)

        self.mapContainer = QWidget(self.frame2)
        self.mapContainer.setObjectName(u"mapContainer")

        self.vboxLayout1.addWidget(self.mapContainer)


        self.hboxLayout1.addWidget(self.frame2)

        self.frame3 = QFrame(self.centralwidget)
        self.frame3.setObjectName(u"frame3")
        self.vboxLayout2 = QVBoxLayout(self.frame3)
        self.vboxLayout2.setObjectName(u"vboxLayout2")
        self.label8 = QLabel(self.frame3)
        self.label8.setObjectName(u"label8")

        self.vboxLayout2.addWidget(self.label8)

        self.tableStats = QTableWidget(self.frame3)
        self.tableStats.setObjectName(u"tableStats")
        self.tableStats.setColumnCount(5)
        self.tableStats.setRowCount(5)

        self.vboxLayout2.addWidget(self.tableStats)

        self.label9 = QLabel(self.frame3)
        self.label9.setObjectName(u"label9")

        self.vboxLayout2.addWidget(self.label9)

        self.frame4 = QFrame(self.frame3)
        self.frame4.setObjectName(u"frame4")
        self.vboxLayout3 = QVBoxLayout(self.frame4)
        self.vboxLayout3.setObjectName(u"vboxLayout3")
        self.label10 = QLabel(self.frame4)
        self.label10.setObjectName(u"label10")

        self.vboxLayout3.addWidget(self.label10)


        self.vboxLayout2.addWidget(self.frame4)


        self.hboxLayout1.addWidget(self.frame3)


        self.vboxLayout.addLayout(self.hboxLayout1)

        self.frame5 = QFrame(self.centralwidget)
        self.frame5.setObjectName(u"frame5")
        self.hboxLayout2 = QHBoxLayout(self.frame5)
        self.hboxLayout2.setObjectName(u"hboxLayout2")
        self.label11 = QLabel(self.frame5)
        self.label11.setObjectName(u"label11")

        self.hboxLayout2.addWidget(self.label11)

        self.spacerItem1 = QSpacerItem(0, 0, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hboxLayout2.addItem(self.spacerItem1)

        self.refreshButton = QPushButton(self.frame5)
        self.refreshButton.setObjectName(u"refreshButton")

        self.hboxLayout2.addWidget(self.refreshButton)


        self.vboxLayout.addWidget(self.frame5)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Dashboard Seguretat Vi\u00e0ria", None))
        MainWindow.setStyleSheet(QCoreApplication.translate("MainWindow", u"\n"
"    QMainWindow {\n"
"        background-color: #0f172a;\n"
"    }\n"
"\n"
"    QLabel {\n"
"        color: #e2e8f0;\n"
"        font-size: 13px;\n"
"    }\n"
"\n"
"    QFrame {\n"
"        background-color: #1e293b;\n"
"        border-radius: 10px;\n"
"    }\n"
"\n"
"    QComboBox, QTextEdit {\n"
"        background-color: #334155;\n"
"        border: none;\n"
"        padding: 6px;\n"
"        border-radius: 6px;\n"
"        color: white;\n"
"    }\n"
"\n"
"    QTableWidget {\n"
"        background-color: #334155;\n"
"        border-radius: 8px;\n"
"        color: white;\n"
"    }\n"
"\n"
"    QPushButton {\n"
"        background-color: #3b82f6;\n"
"        border-radius: 8px;\n"
"        padding: 6px 12px;\n"
"        color: white;\n"
"        font-weight: bold;\n"
"    }\n"
"   ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\U0001f6a6 Dashboard de Seguretat Vi\U000000e0ria", None))
        self.label.setStyleSheet(QCoreApplication.translate("MainWindow", u"font-size: 20px; font-weight: bold; color:#38bdf8;", None))
        self.label1.setText(QCoreApplication.translate("MainWindow", u"\U0001f7e2 Temps real", None))
        self.label2.setText(QCoreApplication.translate("MainWindow", u"Any", None))
        self.label3.setText(QCoreApplication.translate("MainWindow", u"Tipus via", None))
        self.label4.setText(QCoreApplication.translate("MainWindow", u"Clima", None))
        self.label5.setText(QCoreApplication.translate("MainWindow", u"Gravetat", None))
        self.label6.setText(QCoreApplication.translate("MainWindow", u"\U0001f4cd Zona Cr\U000000edtica: Barcelona", None))
        self.label6.setStyleSheet(QCoreApplication.translate("MainWindow", u"font-size:16px; font-weight:bold;", None))
        self.textEdit.setText(QCoreApplication.translate("MainWindow", u"Alta densitat d'accidents entre vehicles lleugers en zones urbanes amb tr\u00e0nsit intens.", None))
        self.label7.setText(QCoreApplication.translate("MainWindow", u"\U0001f5fa\U0000fe0f Mapa de la zona cr\U000000edtica", None))
        self.label8.setText(QCoreApplication.translate("MainWindow", u"\U0001f697 Estad\U000000edstiques", None))
        self.label8.setStyleSheet(QCoreApplication.translate("MainWindow", u"font-size:16px; font-weight:bold;", None))
        self.label9.setText(QCoreApplication.translate("MainWindow", u"\U0001f4c8 Accidents per estaci\U000000f3", None))
        self.label10.setText(QCoreApplication.translate("MainWindow", u"\U0001f4ca Gr\U000000e0fic", None))
        self.label11.setText(QCoreApplication.translate("MainWindow", u"\u00a9 2026 Observatori de Tr\u00e0nsit", None))
        self.refreshButton.setText(QCoreApplication.translate("MainWindow", u"Actualitzar", None))
    # retranslateUi

# =========================
# EJECUCIÓN
# =========================
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec())