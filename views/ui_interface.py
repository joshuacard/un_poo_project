# -*- coding: utf-8 -*-

################################################################################
# Form generated from reading UI file 'interfaceLkIMUC.ui'
##
# Created by: Qt User Interface Compiler version 5.15.2
##
# WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(952, 582)
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(62)
        MainWindow.setWindowFlags(Qt.FramelessWindowHint)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"*{\n"
                                 "	border: none;\n"
                                 "	background-color: transparent;\n"
                                 "	background: transparent;\n"
                                 "	margin: 0;\n"
                                 "	padding: 0;\n"
                                 "	color: #fff;\n"
                                 "	font: 'Segoe UI';\n"
                                 "	font-size: 12px;\n"
                                 "	font-weight: 500;\n"
                                 "}\n"
                                 "\n"
                                 "#centralwidget {\n"
                                 "	background-color: #1f232a;\n"
                                 "}\n"
                                 "\n"
                                 "#leftMenuSubContainer {\n"
                                 "	background-color: #16191d;\n"
                                 "}\n"
                                 "\n"
                                 "#leftMenuSubContainer QPushButton {\n"
                                 "	text-align: left;\n"
                                 "	padding: 5px 10px;\n"
                                 "	border-top-left-radius: 10px;\n"
                                 "	border-bottom-left-radius: 10px;\n"
                                 "}\n"
                                 "\n"
                                 "#centerMenuSubContainer, #rightMenuSubContainer {\n"
                                 "	background-color: #2c313c;\n"
                                 "}\n"
                                 "\n"
                                 "#frame_4, #frame_8, #frame_9 {\n"
                                 "	background-color: #16191d;\n"
                                 "	border-radius: 10px;\n"
                                 "}\n"
                                 "\n"
                                 "#headerContainer {\n"
                                 "	background-color: #2c313c;\n"
                                 "}\n"
                                 "")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuContainer = QWidget(self.centralwidget)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        self.leftMenuContainer.setStyleSheet(u"font-size: 12px;\n"
                                             "font-weight: 500;")
        self.verticalLayout = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuSubContainer = QWidget(self.leftMenuContainer)
        self.leftMenuSubContainer.setObjectName(u"leftMenuSubContainer")
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuSubContainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.frame = QFrame(self.leftMenuSubContainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.menuBtn = QPushButton(self.frame)
        self.menuBtn.setObjectName(u"menuBtn")
        self.menuBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/icons/icons/align-justify.svg",
                     QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.menuBtn)

        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.leftMenuSubContainer)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 10)
        self.studentsBtn = QPushButton(self.frame_2)
        self.studentsBtn.setObjectName(u"studentsBtn")
        font1 = QFont()
        font1.setFamily(u"MS Shell Dlg 2")
        font1.setBold(True)
        font1.setItalic(False)
        font1.setWeight(62)
        self.studentsBtn.setFont(font1)
        self.studentsBtn.setCursor(QCursor(Qt.PointingHandCursor))
        self.studentsBtn.setStyleSheet(u"background-color: #1f232a;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/users.svg",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.studentsBtn.setIcon(icon1)
        self.studentsBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.studentsBtn)

        self.subjectsBtn = QPushButton(self.frame_2)
        self.subjectsBtn.setObjectName(u"subjectsBtn")
        self.subjectsBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/book-open.svg",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.subjectsBtn.setIcon(icon2)
        self.subjectsBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.subjectsBtn)

        self.ahBtn = QPushButton(self.frame_2)
        self.ahBtn.setObjectName(u"ahBtn")
        self.ahBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/file-text.svg",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.ahBtn.setIcon(icon3)
        self.ahBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.ahBtn)

        self.classifyBtn = QPushButton(self.frame_2)
        self.classifyBtn.setObjectName(u"classifyBtn")
        self.classifyBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/info.svg",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.classifyBtn.setIcon(icon4)
        self.classifyBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_4.addWidget(self.classifyBtn)

        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(
            20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.leftMenuSubContainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 10, 0, 10)
        self.settingsBtn = QPushButton(self.frame_3)
        self.settingsBtn.setObjectName(u"settingsBtn")
        self.settingsBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/settings.svg",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.settingsBtn.setIcon(icon5)
        self.settingsBtn.setIconSize(QSize(24, 24))

        self.verticalLayout_5.addWidget(self.settingsBtn)

        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignBottom)

        self.verticalLayout.addWidget(
            self.leftMenuSubContainer, 0, Qt.AlignLeft)

        self.horizontalLayout.addWidget(
            self.leftMenuContainer, 0, Qt.AlignLeft)

        self.centerMenuContainer = QWidget(self.centralwidget)
        self.centerMenuContainer.setObjectName(u"centerMenuContainer")
        self.centerMenuContainer.setStyleSheet(u"font-size: 12px;\n"
                                               "font-weight: 500;")
        self.verticalLayout_6 = QVBoxLayout(self.centerMenuContainer)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.centerMenuSubContainer = QWidget(self.centerMenuContainer)
        self.centerMenuSubContainer.setObjectName(u"centerMenuSubContainer")
        self.centerMenuSubContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_7 = QVBoxLayout(self.centerMenuSubContainer)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.frame_4 = QFrame(self.centerMenuSubContainer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.label)

        self.pushButton = QPushButton(self.frame_4)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/x-circle.svg",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon6)
        self.pushButton.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.pushButton, 0, Qt.AlignRight)

        self.verticalLayout_7.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.stackedWidget = QStackedWidget(self.centerMenuSubContainer)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.verticalLayout_8 = QVBoxLayout(self.page)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setBold(True)
        font2.setItalic(False)
        font2.setWeight(62)
        self.label_2.setFont(font2)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_2)

        self.stackedWidget.addWidget(self.page)

        self.verticalLayout_7.addWidget(self.stackedWidget)

        self.verticalLayout_6.addWidget(
            self.centerMenuSubContainer, 0, Qt.AlignLeft)

        self.horizontalLayout.addWidget(self.centerMenuContainer)

        self.mainBodyContainer = QWidget(self.centralwidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(
            self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy1)
        self.mainBodyContainer.setFont(font2)
        self.mainBodyContainer.setStyleSheet(u"")
        self.verticalLayout_9 = QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = QWidget(self.mainBodyContainer)
        self.headerContainer.setObjectName(u"headerContainer")
        self.horizontalLayout_4 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_5 = QFrame(self.headerContainer)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(30, 30))
        self.label_3.setPixmap(QPixmap(u":/images/logo.png"))
        self.label_3.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.label_3)

        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setBold(True)
        font3.setItalic(False)
        font3.setWeight(99)
        self.label_4.setFont(font3)
        self.label_4.setStyleSheet(u"font-size: 14px;\n"
                                   "font-weight: 800;")

        self.horizontalLayout_6.addWidget(self.label_4)

        self.horizontalLayout_4.addWidget(self.frame_5, 0, Qt.AlignLeft)

        self.frame_6 = QFrame(self.headerContainer)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton_5 = QPushButton(self.frame_6)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/bell.svg",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon7)
        self.pushButton_5.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(
            self.pushButton_5, 0, Qt.AlignHCenter)

        self.horizontalLayout_4.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.headerContainer)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.minimizeBtn = QPushButton(self.frame_7)
        self.minimizeBtn.setObjectName(u"minimizeBtn")
        self.minimizeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/minus.svg",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.minimizeBtn.setIcon(icon8)
        self.minimizeBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.minimizeBtn)

        self.restoreBtn = QPushButton(self.frame_7)
        self.restoreBtn.setObjectName(u"restoreBtn")
        self.restoreBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/square.svg",
                      QSize(), QIcon.Normal, QIcon.Off)
        self.restoreBtn.setIcon(icon9)
        self.restoreBtn.setIconSize(QSize(20, 20))

        self.horizontalLayout_3.addWidget(self.restoreBtn)

        self.closeBtn = QPushButton(self.frame_7)
        self.closeBtn.setObjectName(u"closeBtn")
        self.closeBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/x.svg", QSize(),
                       QIcon.Normal, QIcon.Off)
        self.closeBtn.setIcon(icon10)
        self.closeBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_3.addWidget(self.closeBtn)

        self.horizontalLayout_4.addWidget(self.frame_7, 0, Qt.AlignRight)

        self.verticalLayout_9.addWidget(self.headerContainer, 0, Qt.AlignTop)

        self.mainBodyContent = QWidget(self.mainBodyContainer)
        self.mainBodyContent.setObjectName(u"mainBodyContent")
        sizePolicy.setHeightForWidth(
            self.mainBodyContent.sizePolicy().hasHeightForWidth())
        self.mainBodyContent.setSizePolicy(sizePolicy)
        self.horizontalLayout_7 = QHBoxLayout(self.mainBodyContent)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.mainContentContainer = QWidget(self.mainBodyContent)
        self.mainContentContainer.setObjectName(u"mainContentContainer")
        self.verticalLayout_13 = QVBoxLayout(self.mainContentContainer)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.stackedWidget_3 = QStackedWidget(self.mainContentContainer)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_14 = QVBoxLayout(self.page_3)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.widget = QWidget(self.page_3)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_19 = QVBoxLayout(self.widget)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.widget)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_9 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, -1, 0, 9)
        self.label_11 = QLabel(self.widget_2)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_9.addWidget(self.label_11, 0, Qt.AlignLeft)

        self.frame_9 = QFrame(self.widget_2)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(9, 9, 9, 9)
        self.createStudentBtn = QPushButton(self.frame_9)
        self.createStudentBtn.setObjectName(u"createStudentBtn")
        self.createStudentBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/user-plus.svg",
                       QSize(), QIcon.Normal, QIcon.Off)
        self.createStudentBtn.setIcon(icon11)
        self.createStudentBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_10.addWidget(self.createStudentBtn)

        self.searchStudentBtn = QPushButton(self.frame_9)
        self.searchStudentBtn.setObjectName(u"searchStudentBtn")
        self.searchStudentBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/search.svg",
                       QSize(), QIcon.Normal, QIcon.Off)
        self.searchStudentBtn.setIcon(icon12)
        self.searchStudentBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_10.addWidget(self.searchStudentBtn)

        self.updateStudentBtn = QPushButton(self.frame_9)
        self.updateStudentBtn.setObjectName(u"updateStudentBtn")
        self.updateStudentBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/refresh-ccw.svg",
                       QSize(), QIcon.Normal, QIcon.Off)
        self.updateStudentBtn.setIcon(icon13)
        self.updateStudentBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_10.addWidget(self.updateStudentBtn)

        self.deleteStudentBtn = QPushButton(self.frame_9)
        self.deleteStudentBtn.setObjectName(u"deleteStudentBtn")
        self.deleteStudentBtn.setCursor(QCursor(Qt.PointingHandCursor))
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/trash-2.svg",
                       QSize(), QIcon.Normal, QIcon.Off)
        self.deleteStudentBtn.setIcon(icon14)
        self.deleteStudentBtn.setIconSize(QSize(24, 24))

        self.horizontalLayout_10.addWidget(self.deleteStudentBtn)

        self.horizontalLayout_9.addWidget(self.frame_9, 0, Qt.AlignRight)

        self.verticalLayout_19.addWidget(self.widget_2, 0, Qt.AlignTop)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy.setHeightForWidth(
            self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.verticalLayout_18 = QVBoxLayout(self.widget_3)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.widget_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_7)

        self.verticalLayout_19.addWidget(self.widget_3)

        self.verticalLayout_14.addWidget(self.widget)

        self.stackedWidget_3.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_15 = QVBoxLayout(self.page_4)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_8 = QLabel(self.page_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_8)

        self.stackedWidget_3.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.verticalLayout_16 = QVBoxLayout(self.page_5)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_9 = QLabel(self.page_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_9)

        self.stackedWidget_3.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.verticalLayout_17 = QVBoxLayout(self.page_6)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_10 = QLabel(self.page_6)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_10)

        self.stackedWidget_3.addWidget(self.page_6)

        self.verticalLayout_13.addWidget(self.stackedWidget_3)

        self.horizontalLayout_7.addWidget(self.mainContentContainer)

        self.rightMenuContainer = QWidget(self.mainBodyContent)
        self.rightMenuContainer.setObjectName(u"rightMenuContainer")
        self.rightMenuContainer.setMinimumSize(QSize(200, 0))
        self.verticalLayout_10 = QVBoxLayout(self.rightMenuContainer)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.rightMenuSubContainer = QWidget(self.rightMenuContainer)
        self.rightMenuSubContainer.setObjectName(u"rightMenuSubContainer")
        self.verticalLayout_11 = QVBoxLayout(self.rightMenuSubContainer)
        self.verticalLayout_11.setSpacing(5)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(5, 5, 5, 5)
        self.frame_8 = QFrame(self.rightMenuSubContainer)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_5 = QLabel(self.frame_8)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_5)

        self.pushButton_6 = QPushButton(self.frame_8)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_6.setIcon(icon6)
        self.pushButton_6.setIconSize(QSize(24, 24))

        self.horizontalLayout_8.addWidget(self.pushButton_6, 0, Qt.AlignRight)

        self.verticalLayout_11.addWidget(self.frame_8)

        self.stackedWidget_2 = QStackedWidget(self.rightMenuSubContainer)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.verticalLayout_12 = QVBoxLayout(self.page_2)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_6 = QLabel(self.page_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout_12.addWidget(self.label_6)

        self.stackedWidget_2.addWidget(self.page_2)

        self.verticalLayout_11.addWidget(self.stackedWidget_2)

        self.verticalLayout_10.addWidget(self.rightMenuSubContainer)

        self.horizontalLayout_7.addWidget(
            self.rightMenuContainer, 0, Qt.AlignRight)

        self.verticalLayout_9.addWidget(self.mainBodyContent)

        self.horizontalLayout.addWidget(self.mainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_3.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate(
            "MainWindow", u"MainWindow", None))
# if QT_CONFIG(tooltip)
        self.menuBtn.setToolTip(
            QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuBtn.setText("")
# if QT_CONFIG(tooltip)
        self.studentsBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Go to subjects", None))
#endif // QT_CONFIG(tooltip)
        self.studentsBtn.setText(QCoreApplication.translate(
            "MainWindow", u"Students", None))
# if QT_CONFIG(tooltip)
        self.subjectsBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Go to students", None))
#endif // QT_CONFIG(tooltip)
        self.subjectsBtn.setText(QCoreApplication.translate(
            "MainWindow", u"Subjects", None))
# if QT_CONFIG(tooltip)
        self.ahBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Go to academic history", None))
#endif // QT_CONFIG(tooltip)
        self.ahBtn.setText(QCoreApplication.translate(
            "MainWindow", u"Academic History", None))
# if QT_CONFIG(tooltip)
        self.classifyBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Go to classification", None))
#endif // QT_CONFIG(tooltip)
        self.classifyBtn.setText(QCoreApplication.translate(
            "MainWindow", u"Classification", None))
# if QT_CONFIG(tooltip)
        self.settingsBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Go to settings", None))
#endif // QT_CONFIG(tooltip)
        self.settingsBtn.setText(QCoreApplication.translate(
            "MainWindow", u"Settings", None))
        self.label.setText(QCoreApplication.translate(
            "MainWindow", u"Settings Menu", None))
# if QT_CONFIG(tooltip)
        self.pushButton.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Close Settings", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText("")
        self.label_2.setText(QCoreApplication.translate(
            "MainWindow", u"Settings", None))
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate(
            "MainWindow", u"SIA Simulator 2022", None))
# if QT_CONFIG(tooltip)
        self.pushButton_5.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Notifications", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_5.setText("")
# if QT_CONFIG(tooltip)
        self.minimizeBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Minimize window", None))
#endif // QT_CONFIG(tooltip)
        self.minimizeBtn.setText("")
# if QT_CONFIG(tooltip)
        self.restoreBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Restore window", None))
#endif // QT_CONFIG(tooltip)
        self.restoreBtn.setText("")
# if QT_CONFIG(tooltip)
        self.closeBtn.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Close window", None))
#endif // QT_CONFIG(tooltip)
        self.closeBtn.setText("")
        self.label_11.setText(QCoreApplication.translate(
            "MainWindow", u"Students", None))
# if QT_CONFIG(tooltip)
        self.createStudentBtn.setToolTip(
            QCoreApplication.translate("MainWindow", u"Add student", None))
#endif // QT_CONFIG(tooltip)
        self.createStudentBtn.setText("")
# if QT_CONFIG(tooltip)
        self.searchStudentBtn.setToolTip(
            QCoreApplication.translate("MainWindow", u"Search student", None))
#endif // QT_CONFIG(tooltip)
        self.searchStudentBtn.setText("")
# if QT_CONFIG(tooltip)
        self.updateStudentBtn.setToolTip(
            QCoreApplication.translate("MainWindow", u"Update student", None))
#endif // QT_CONFIG(tooltip)
        self.updateStudentBtn.setText("")
# if QT_CONFIG(tooltip)
        self.deleteStudentBtn.setToolTip(
            QCoreApplication.translate("MainWindow", u"Delete student", None))
#endif // QT_CONFIG(tooltip)
        self.deleteStudentBtn.setText("")
        self.label_7.setText(QCoreApplication.translate(
            "MainWindow", u"Students", None))
        self.label_8.setText(QCoreApplication.translate(
            "MainWindow", u"Subjects", None))
        self.label_9.setText(QCoreApplication.translate(
            "MainWindow", u"Academic History", None))
        self.label_10.setText(QCoreApplication.translate(
            "MainWindow", u"Classification", None))
        self.label_5.setText(QCoreApplication.translate(
            "MainWindow", u"Notifications", None))
# if QT_CONFIG(tooltip)
        self.pushButton_6.setToolTip(QCoreApplication.translate(
            "MainWindow", u"Close notificatios", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_6.setText("")
        self.label_6.setText(QCoreApplication.translate(
            "MainWindow", u"Notifications", None))
    # retranslateUi
