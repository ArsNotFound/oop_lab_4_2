# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_view.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QSizePolicy, QSlider, QSpacerItem, QSpinBox,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(770, 274)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(31, 21, 711, 221))
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.a_label = QLabel(self.widget)
        self.a_label.setObjectName(u"a_label")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(40)
        self.a_label.setFont(font)
        self.a_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.a_label)

        self.a_lineEdit = QLineEdit(self.widget)
        self.a_lineEdit.setObjectName(u"a_lineEdit")

        self.verticalLayout.addWidget(self.a_lineEdit)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.a_spinBox = QSpinBox(self.widget)
        self.a_spinBox.setObjectName(u"a_spinBox")
        self.a_spinBox.setMaximum(100)

        self.verticalLayout.addWidget(self.a_spinBox)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.a_horizontalSlider = QSlider(self.widget)
        self.a_horizontalSlider.setObjectName(u"a_horizontalSlider")
        self.a_horizontalSlider.setMaximum(100)
        self.a_horizontalSlider.setOrientation(Qt.Horizontal)
        self.a_horizontalSlider.setTickPosition(QSlider.TicksBelow)
        self.a_horizontalSlider.setTickInterval(10)

        self.verticalLayout.addWidget(self.a_horizontalSlider)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(42)
        self.label.setFont(font1)

        self.horizontalLayout.addWidget(self.label)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.b_label = QLabel(self.widget)
        self.b_label.setObjectName(u"b_label")
        self.b_label.setFont(font)
        self.b_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.b_label)

        self.b_lineEdit = QLineEdit(self.widget)
        self.b_lineEdit.setObjectName(u"b_lineEdit")

        self.verticalLayout_2.addWidget(self.b_lineEdit)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_3)

        self.b_spinBox = QSpinBox(self.widget)
        self.b_spinBox.setObjectName(u"b_spinBox")
        self.b_spinBox.setMaximum(100)

        self.verticalLayout_2.addWidget(self.b_spinBox)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_4)

        self.b_horizontalSlider = QSlider(self.widget)
        self.b_horizontalSlider.setObjectName(u"b_horizontalSlider")
        self.b_horizontalSlider.setMaximum(100)
        self.b_horizontalSlider.setOrientation(Qt.Horizontal)
        self.b_horizontalSlider.setTickPosition(QSlider.TicksBelow)
        self.b_horizontalSlider.setTickInterval(10)

        self.verticalLayout_2.addWidget(self.b_horizontalSlider)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.horizontalLayout.addWidget(self.label_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.c_label = QLabel(self.widget)
        self.c_label.setObjectName(u"c_label")
        self.c_label.setFont(font)
        self.c_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.c_label)

        self.c_lineEdit = QLineEdit(self.widget)
        self.c_lineEdit.setObjectName(u"c_lineEdit")

        self.verticalLayout_3.addWidget(self.c_lineEdit)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_5)

        self.c_spinBox = QSpinBox(self.widget)
        self.c_spinBox.setObjectName(u"c_spinBox")
        self.c_spinBox.setMaximum(100)

        self.verticalLayout_3.addWidget(self.c_spinBox)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_6)

        self.c_horizontalSlider = QSlider(self.widget)
        self.c_horizontalSlider.setObjectName(u"c_horizontalSlider")
        self.c_horizontalSlider.setMaximum(100)
        self.c_horizontalSlider.setOrientation(Qt.Horizontal)
        self.c_horizontalSlider.setTickPosition(QSlider.TicksBelow)
        self.c_horizontalSlider.setTickInterval(10)

        self.verticalLayout_3.addWidget(self.c_horizontalSlider)


        self.horizontalLayout.addLayout(self.verticalLayout_3)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.a_label.setText(QCoreApplication.translate("Form", u"A", None))
        self.label.setText(QCoreApplication.translate("Form", u"<=", None))
        self.b_label.setText(QCoreApplication.translate("Form", u"B", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<=", None))
        self.c_label.setText(QCoreApplication.translate("Form", u"C", None))
    # retranslateUi

