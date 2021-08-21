                                  #SuperInsta by Syed Hamza
                                  #     Version v1.8
#Follow Me on Instagram @Mostuselessboy
#Follow Me on Twitter @Mostuselessboy
# My gmail = mostuselessboy@gmail.com
#Do not copy the code. To make changes in the code first ask me on any of the above platform

#Imports
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QStackedWidget,QFileDialog
from instagram_private_api import Client, ClientCompatPatch
from PyQt5.QtCore import Qt
import cookie
import threading
import pyperclip as pc
import time
import requests
from numconv import * #( this module is created by Syed Hamza )
#from ratioconv11 import reshape  #(this module is also created by me )
from circularimg import circularimg  #(this module is also created by me )
import os.path
from datetime import datetime
import pytz
from os import path


from PIL import Image
def reshape(filename):
   def reshape_image(image):
       old_size = image.size
       max_dimension, min_dimension = max(old_size), min(old_size)
       desired_size = (max_dimension, max_dimension)
       position = int(max_dimension/2) - int(min_dimension/2) 
       blank_image = Image.new("RGB", desired_size, color='#1d1d1d')
       if image.height<image.width:
           blank_image.paste(image, (0, position))
       else:
           blank_image.paste(image, (position, 0))
       return blank_image
   test_image = Image.open(filename)
   new_image = reshape_image(test_image)
   new_image.save(filename)




#Main Window (Class)
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):


        #main-window
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(810, 545)
        MainWindow.setMinimumSize(QtCore.QSize(810, 545))
        MainWindow.setMaximumSize(QtCore.QSize(810, 545))
        MainWindow.setWindowFlag(Qt.WindowSystemMenuHint)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(21)
        MainWindow.setFont(font)
        MainWindow.setWindowIcon(QtGui.QIcon("icon.ico"))
        MainWindow.setStyleSheet("background:rgb(22, 22, 22);color:white;")

        #Blur Effect
        self.blur_effect = QtWidgets.QGraphicsBlurEffect()
        #MainWindow.setGraphicsEffect(self.blur_effect)

        #All Windows
        MainWindow.central_widget = QtWidgets.QStackedWidget()
        MainWindow.setCentralWidget(MainWindow.central_widget)




        #homescreen
        self.homescreen = QtWidgets.QWidget(MainWindow)
        self.homescreen.setObjectName("homescreen")
	


        #insta-logo
        self.insta_logo = QtWidgets.QLabel(self.homescreen)
        self.insta_logo.setGeometry(QtCore.QRect(10, 10, 41, 41))
        self.insta_logo.setText("")
        self.insta_logo.setPixmap(QtGui.QPixmap(":/elem/logo.png"))
        self.insta_logo.setScaledContents(True)
        self.insta_logo.setObjectName("insta_logo")



        #instagrade-logo
        self.instagrade_logo = QtWidgets.QLabel(self.homescreen)
        self.instagrade_logo.setGeometry(QtCore.QRect(50, 10, 191, 51))
        font = QtGui.QFont()
        font.setFamily("billabong")
        font.setPointSize(41)
        self.instagrade_logo.setFont(font)
        self.instagrade_logo.setStyleSheet("background:transparent;\n")
        self.instagrade_logo.setScaledContents(True)
        self.instagrade_logo.setObjectName("instagrade_logo")



        #search box
        self.search_box = QtWidgets.QLineEdit(self.homescreen)
        self.search_box.setGeometry(QtCore.QRect(40, 90, 731, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.search_box.setFont(font)
        self.search_box.setStyleSheet("background-color:rgb(29, 29, 29);border-radius:12px;padding-left:10px;color:white;padding-right:34px;padding-top:3px;padding-bottom:3px")
        self.search_box.setObjectName("search_box")
        self.search_box.returnPressed.connect(lambda: searchfromhomescreen()) 



        #image (DP)
        self.image = QtWidgets.QLabel(self.homescreen)
        self.image.setGeometry(QtCore.QRect(40, 180, 200, 200))
        self.image.setStyleSheet("border:3px solid rgb(29, 29, 29)")
        self.image.setText("")
        #self.image.setPixmap(QtGui.QPixmap(":/elem/liam.jpg"))
        self.image.setScaledContents(True)
        self.image.setObjectName("image")



        #Follow button
        self.follow = QtWidgets.QPushButton(self.homescreen)
        self.follow.setGeometry(QtCore.QRect(650, 160, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.follow.setFont(font)
        self.follow.setStyleSheet("QPushButton{background-color:rgb(0, 157, 236);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.follow.setObjectName("follow")
        self.follow.clicked.connect(lambda: follow_user())



        #Block Button
        self.block = QtWidgets.QPushButton(self.homescreen)
        self.block.setGeometry(QtCore.QRect(650, 210, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.block.setFont(font)
        self.block.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.block.setObjectName("block")
        self.block.clicked.connect(lambda: block_user())



        #Hide/Show Story Button
        self.hidestory = QtWidgets.QPushButton(self.homescreen)
        self.hidestory.setGeometry(QtCore.QRect(650, 260, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.hidestory.setFont(font)
        self.hidestory.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.hidestory.setObjectName("hidestory")
        self.hidestory.clicked.connect(lambda: hide_story())



        #Save/Download DP Button
        self.viewposts = QtWidgets.QPushButton(self.homescreen)
        self.viewposts.setGeometry(QtCore.QRect(650, 310, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.viewposts.setFont(font)
        self.viewposts.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.viewposts.setObjectName("viewposts")
        self.viewposts.clicked.connect(lambda: setscreen_posts_screen())

        #Save/Download DP Button
        self.viewposts2 = QtWidgets.QPushButton(self.homescreen)
        self.viewposts2.setGeometry(QtCore.QRect(650, 360, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.viewposts2.setFont(font)
        self.viewposts2.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.viewposts2.setObjectName("s")
        self.viewposts2.clicked.connect(lambda: setscreen_likedposts_screen())



        #SignOut Button
        self.signout = QtWidgets.QPushButton(self.homescreen)
        self.signout.setGeometry(QtCore.QRect(680, 10, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.signout.setFont(font)
        self.signout.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-radius:15px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));color:rgb(255, 142, 231);}")
        self.signout.setObjectName("signout")
        self.signout.clicked.connect(lambda:logout_instagram())


        #Search Icon/Button
        self.search_icon = QtWidgets.QPushButton(self.homescreen)
        self.search_icon.setGeometry(QtCore.QRect(740, 100, 21, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.search_icon.setFont(font)
        self.search_icon.setStyleSheet("background:transparent;")
        self.search_icon.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/elem/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_icon.setIcon(icon)
        self.search_icon.setIconSize(QtCore.QSize(40, 20))
        self.search_icon.setObjectName("search_icon")
        self.search_logo_btn = QtWidgets.QPushButton(self.homescreen)
        self.search_logo_btn.setGeometry(QtCore.QRect(740, 100, 21, 31))
        self.search_logo_btn.setStyleSheet("background:transparent;")
        self.search_logo_btn.setObjectName("search_logo_btn")
        self.search_logo_btn.clicked.connect(lambda:searchfromhomescreen()) 


        #Username
        self.username = QtWidgets.QLabel(self.homescreen)
        self.username.setGeometry(QtCore.QRect(260, 180, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.username.setFont(font)
        self.username.setStyleSheet("background:transparent;")
        self.username.setScaledContents(True)
        self.username.setObjectName("username")



        #Vertical Layout 
        self.verticalLayoutWidget = QtWidgets.QWidget(self.homescreen)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(260, 220, 381, 161))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")



        #Bio-Layout: Layout
        self.bio_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.bio_layout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.bio_layout.setContentsMargins(0, 0, 0, 0)
        self.bio_layout.setObjectName("bio_layout")



        #Bio-Layout: account
        self.account = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.account.sizePolicy().hasHeightForWidth())
        self.account.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.account.setFont(font)
        self.account.setStyleSheet("background:transparent;")
        self.account.setScaledContents(True)
        self.account.setWordWrap(True)
        self.account.setOpenExternalLinks(True)
        self.account.setObjectName("account")
        self.bio_layout.addWidget(self.account)



        #Bio-Layout: Bio
        self.bio = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bio.sizePolicy().hasHeightForWidth())
        self.bio.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.bio.setFont(font)
        self.bio.setStyleSheet("background:transparent;")
        self.bio.setScaledContents(True)
        self.bio.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.bio.setWordWrap(True)
        self.bio.setObjectName("bio")
        self.bio_layout.addWidget(self.bio)



        #Bio-Layout: Website
        self.website = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.website.sizePolicy().hasHeightForWidth())
        self.website.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.website.setFont(font)
        self.website.setStyleSheet("background:transparent;")
        self.website.setScaledContents(True)
        self.website.setWordWrap(True)
        self.website.setOpenExternalLinks(True)
        self.website.setObjectName("website")
        self.bio_layout.addWidget(self.website)



        #Bio-Layout: Mutual
        self.mutual = QtWidgets.QLabel(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mutual.sizePolicy().hasHeightForWidth())
        self.mutual.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.mutual.setFont(font)
        self.mutual.setStyleSheet("background:transparent;")
        self.mutual.setScaledContents(True)
        self.mutual.setWordWrap(True)
        self.mutual.setOpenExternalLinks(True)
        self.mutual.setObjectName("mutual")
        self.bio_layout.addWidget(self.mutual)



        #Bio-Layout: Spacer
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.bio_layout.addItem(spacerItem)



        #Following-Display
        self.following = QtWidgets.QLabel(self.homescreen)
        self.following.setGeometry(QtCore.QRect(30, 420, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.following.setFont(font)
        self.following.setStyleSheet("QLabel{background-color:rgb(26, 26, 26);border-radius:9px;color:white;}")
        self.following.setScaledContents(True)
        self.following.setObjectName("following")



        #Follower-Display
        self.follower = QtWidgets.QLabel(self.homescreen)
        self.follower.setGeometry(QtCore.QRect(220, 420, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.follower.setFont(font)
        self.follower.setStyleSheet("QLabel{background-color:rgb(26, 26, 26);border-radius:9px;color:white;}")
        self.follower.setScaledContents(True)
        self.follower.setObjectName("follower")




        #Total Post Count
        self.post = QtWidgets.QLabel(self.homescreen)
        self.post.setGeometry(QtCore.QRect(410, 420, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.post.setFont(font)
        self.post.setStyleSheet("QLabel{background-color:rgb(26, 26, 26);border-radius:9px;color:white;}")
        self.post.setScaledContents(True)
        self.post.setObjectName("post")



        #Follow/Not follow you
        self.followsyou = QtWidgets.QLabel(self.homescreen)
        self.followsyou.setGeometry(QtCore.QRect(600, 420, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.followsyou.setFont(font)
        self.followsyou.setStyleSheet("QLabel{background-color:rgb(26, 26, 26);border-radius:9px;color:white;}")
        self.followsyou.setScaledContents(True)
        self.followsyou.setObjectName("followsyou")

        #TaskBar
        
        self.TB = QtWidgets.QLabel(self.homescreen)
        self.TB.setGeometry(QtCore.QRect(-40, 480, 861, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.TB.setFont(font)
        self.TB.setStyleSheet("background:rgb(36, 36, 36);")
        self.TB.setScaledContents(True)
        self.TB.setObjectName("TB")



        
        self.TB_Home = QtWidgets.QPushButton(self.homescreen)
        self.TB_Home.setGeometry(QtCore.QRect(10, 490, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.TB_Home.setFont(font)
        self.TB_Home.setStyleSheet("QPushButton{background-color:rgb(50, 50, 50);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.TB_Home.setObjectName("TB_Home")
        self.TB_Home.clicked.connect(lambda: setscreen_feed())

        
        self.TB_Search = QtWidgets.QPushButton(self.homescreen)
        self.TB_Search.setGeometry(QtCore.QRect(170, 490, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.TB_Search.setFont(font)
        self.TB_Search.setStyleSheet("QPushButton{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.TB_Search.setObjectName("TB_Search")
        self.TB_Search.clicked.connect(lambda: setscreen_searchmain())


        
        self.TB_Profile = QtWidgets.QPushButton(self.homescreen)
        self.TB_Profile.setGeometry(QtCore.QRect(490, 490, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.TB_Profile.setFont(font)
        self.TB_Profile.setStyleSheet("QPushButton{background-color:rgb(50, 50, 50);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.TB_Profile.setObjectName("TB_Profile")
        self.TB_Profile.clicked.connect(lambda: setscreen_profile())

        
        self.TB_Timeline = QtWidgets.QPushButton(self.homescreen)
        self.TB_Timeline.setGeometry(QtCore.QRect(330, 490, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.TB_Timeline.setFont(font)
        self.TB_Timeline.setStyleSheet("QPushButton{background-color:rgb(50, 50, 50);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.TB_Timeline.setObjectName("TB_Timeline")
        #self.TB_Timeline.clicked.connect(lambda: setscreen_onepost())


        
        self.TB_Settings = QtWidgets.QPushButton(self.homescreen)
        self.TB_Settings.setGeometry(QtCore.QRect(650, 490, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.TB_Settings.setFont(font)
        self.TB_Settings.setStyleSheet("QPushButton{background-color:rgb(50, 50, 50);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.TB_Settings.setObjectName("TB_Settings")
        #self.TB_Timeline.clicked.connect(lambda: settingscreen())

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        _translate = QtCore.QCoreApplication.translate       
        self.TB.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.TB_Home.setText(_translate("MainWindow", "Home"))
        self.TB_Search.setText(_translate("MainWindow", "Search"))
        self.TB_Profile.setText(_translate("MainWindow", "Your Profile"))
        self.TB_Timeline.setText(_translate("MainWindow", "Timeline"))
        self.TB_Settings.setText(_translate("MainWindow", "SuperInsta"))

















        #Translatable Texts

        MainWindow.setWindowTitle(_translate("MainWindow", "SuperInsta 1.8 - BETA"))
        self.instagrade_logo.setText(_translate("MainWindow", " SuperInsta"))
        self.search_box.setPlaceholderText(_translate("MainWindow", "Search User"))
        self.follow.setText(_translate("MainWindow", "Follow"))
        self.block.setText(_translate("MainWindow", "Block"))
        self.hidestory.setText(_translate("MainWindow", "Hide Story"))
        self.viewposts.setText(_translate("MainWindow", "View Posts"))
        self.viewposts2.setText(_translate("MainWindow", "Liked Posts"))

        self.signout.setText(_translate("MainWindow", "Sign Out"))
        self.username.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">@username</span></p></body></html>"))
        self.account.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#757575;\">Account Type</span></p></body></html>"))
        self.bio.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#4d4d4d;\">Bio</span></p></body></html>"))
        self.website.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#00aaff;\">External URL</span></p></body></html>"))
        self.mutual.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#b3b1b1;\">Followerd by @username</span></p></body></html>"))
        self.following.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Following: </span></p></body></html>"))
        self.follower.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Follower: </span></p></body></html>"))
        self.post.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Total Post:</span></p></body></html>"))
        self.followsyou.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Follow Status</span></p></body></html>"))



###########################################LOGIN SCREEN#################################################

        #LoginScreen
        self.loginscreen = QtWidgets.QWidget(MainWindow)        
        self.loginscreen.setObjectName("loginscreen")
        



        #LoginScreen - Logo
        self.login_insta_logo = QtWidgets.QLabel(self.loginscreen)
        self.login_insta_logo.setGeometry(QtCore.QRect(290, 90, 41, 41))
        self.login_insta_logo.setText("")
        self.login_insta_logo.setPixmap(QtGui.QPixmap(":/elem/logo.png"))
        self.login_insta_logo.setScaledContents(True)
        self.login_insta_logo.setObjectName("login_insta_logo")



        #LoginScreen - Text Logo
        self.login_instagrade_logo = QtWidgets.QLabel(self.loginscreen)
        self.login_instagrade_logo.setGeometry(QtCore.QRect(330, 90, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Billabong")
        font.setPointSize(41)
        self.login_instagrade_logo.setFont(font)
        self.login_instagrade_logo.setStyleSheet("background:transparent;")
        self.login_instagrade_logo.setScaledContents(True)
        self.login_instagrade_logo.setObjectName("login_instagrade_logo")



        #LoginScreen - UsernameBox
        self.login_usernamebox = QtWidgets.QLineEdit(self.loginscreen)
        self.login_usernamebox.setGeometry(QtCore.QRect(180, 160, 451, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.login_usernamebox.setFont(font)
        self.login_usernamebox.setStyleSheet("background-color:rgb(29, 29, 29); border-radius:12px; padding-left:10px;color:white; padding-right:34px; padding-top:3px; padding-bottom:3px;")
        self.login_usernamebox.setText("")
        self.login_usernamebox.setDragEnabled(False)
        self.login_usernamebox.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.login_usernamebox.setClearButtonEnabled(False)
        self.login_usernamebox.setObjectName("login_usernamebox")



        #LoginScreen - Sign IN Button
        self.login_signbutton = QtWidgets.QPushButton(self.loginscreen)
        self.login_signbutton.setGeometry(QtCore.QRect(330, 340, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.login_signbutton.setFont(font)
        self.login_signbutton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.login_signbutton.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.login_signbutton.setObjectName("login_signbutton")



        #LoginScreen - Version
        self.login_version = QtWidgets.QLabel(self.loginscreen)
        self.login_version.setGeometry(QtCore.QRect(680, 480, 121, 21))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_version.sizePolicy().hasHeightForWidth())
        self.login_version.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.login_version.setFont(font)
        self.login_version.setStyleSheet("background:transparent;")
        self.login_version.setScaledContents(True)
        self.login_version.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.login_version.setWordWrap(True)
        self.login_version.setObjectName("login_version")



        #LoginScreen - Terms & Condition.
        self.login_terms = QtWidgets.QLabel(self.loginscreen)
        self.login_terms.setGeometry(QtCore.QRect(270, 310, 281, 19))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_terms.sizePolicy().hasHeightForWidth())
        self.login_terms.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.login_terms.setFont(font)
        self.login_terms.setStyleSheet("background:transparent;")
        self.login_terms.setScaledContents(True)
        self.login_terms.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.login_terms.setWordWrap(True)
        self.login_terms.setObjectName("login_terms")



        #LoginScreen - Password Box
        self.login_passwordbox = QtWidgets.QLineEdit(self.loginscreen)
        self.login_passwordbox.setGeometry(QtCore.QRect(180, 230, 451, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.login_passwordbox.setFont(font)
        self.login_passwordbox.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.login_passwordbox.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.login_passwordbox.setStyleSheet("background-color:rgb(29, 29, 29);border-radius:12px;padding-left:10px;color:white;padding-right:34px;padding-top:3px;padding-bottom:3px;")
        self.login_passwordbox.setText("")
        self.login_passwordbox.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login_passwordbox.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.login_passwordbox.setObjectName("login_passwordbox")



        #LoginScreen - error message
        self.login_errormsg = QtWidgets.QLabel(self.loginscreen)
        self.login_errormsg.setGeometry(QtCore.QRect(260, 470, 301, 19))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.login_errormsg.sizePolicy().hasHeightForWidth())
        self.login_errormsg.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.login_errormsg.setFont(font)
        self.login_errormsg.setFocusPolicy(QtCore.Qt.NoFocus)
        self.login_errormsg.setStyleSheet("background:transparent;")
        self.login_errormsg.setScaledContents(True)
        self.login_errormsg.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.login_errormsg.setWordWrap(True)
        self.login_errormsg.setObjectName("login_errormsg")


        self.login_instagrade_logo.setText(_translate("MainWindow", " SuperInsta"))
        self.login_usernamebox.setPlaceholderText(_translate("MainWindow", "Username"))
        self.login_signbutton.setText(_translate("MainWindow", "Sign In"))
        self.login_signbutton.clicked.connect(lambda:login_instagram())
        self.login_version.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#4d4d4d;\">SuperInsta 2021</span></p></body></html>"))
        self.login_terms.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#4d4d4d;\">SuperInsta won\'t save your password.</span></p></body></html>"))
        self.login_passwordbox.setPlaceholderText(_translate("MainWindow", "Password"))

###########################################SEARCH SCREEN#################################################
        #Searchscreen
        self.searchscreen = QtWidgets.QWidget(MainWindow)
        self.searchscreen.setObjectName("searchscreen")



        #search - logo
        self.search_logo = QtWidgets.QLabel(self.searchscreen)
        self.search_logo.setGeometry(QtCore.QRect(10, 10, 41, 41))
        self.search_logo.setText("")
        self.search_logo.setPixmap(QtGui.QPixmap(":/elem/logo.png"))
        self.search_logo.setScaledContents(True)
        self.search_logo.setObjectName("search_logo")



        #search - textlogo
        self.search_textlogo = QtWidgets.QLabel(self.searchscreen)
        self.search_textlogo.setGeometry(QtCore.QRect(50, 10, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Billabong")
        font.setPointSize(41)
        self.search_textlogo.setFont(font)
        self.search_textlogo.setStyleSheet("background:transparent;")
        self.search_textlogo.setScaledContents(True)
        self.search_textlogo.setObjectName("search_textlogo")



        #Search - Search_box
        self.search_search_box = QtWidgets.QLineEdit(self.searchscreen)
        self.search_search_box.setGeometry(QtCore.QRect(40, 90, 731, 51))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.search_search_box.setFont(font)
        self.search_search_box.setStyleSheet("background-color:rgb(29, 29, 29);border-radius:12px;padding-left:10px;color:white;padding-right:34px;padding-top:3px;padding-bottom:3px;")
        self.search_search_box.setObjectName("search_search_box")
        self.search_search_box.returnPressed.connect(lambda:searchfromsearchscreen()) 


        #search - signout button
        self.search_signout = QtWidgets.QPushButton(self.searchscreen)
        self.search_signout.setGeometry(QtCore.QRect(680, 10, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.search_signout.setFont(font)
        self.search_signout.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-radius:15px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));color:rgb(255, 142, 231);}")
        self.search_signout.setObjectName("search_signout")
        self.search_signout.clicked.connect(lambda:logout_instagram())


        #Search - search icon
        self.search_search_icon = QtWidgets.QPushButton(self.searchscreen)
        self.search_search_icon.setGeometry(QtCore.QRect(740, 100, 21, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.search_search_icon.setFont(font)
        self.search_search_icon.setStyleSheet("background:transparent;")
        self.search_search_icon.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/elem/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_search_icon.setIcon(icon)
        self.search_search_icon.setIconSize(QtCore.QSize(40, 20))
        self.search_search_icon.setObjectName("search_search_icon")
        self.search_logo_btn = QtWidgets.QPushButton(self.searchscreen)
        self.search_logo_btn.setGeometry(QtCore.QRect(740, 100, 21, 31))
        self.search_logo_btn.setStyleSheet("background:transparent;")
        self.search_logo_btn.setObjectName("search_logo_btn")
        self.search_logo_btn.clicked.connect(lambda:searchfromsearchscreen()) 








        #Search UserList
        self.search_userlist = QtWidgets.QScrollArea(self.searchscreen)
        self.search_userlist.setGeometry(QtCore.QRect(40, 150, 731, 311))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_userlist.sizePolicy().hasHeightForWidth())
        self.search_userlist.setSizePolicy(sizePolicy)
        self.scrolllbar = QtWidgets.QScrollBar(self.searchscreen)
        self.scrolllbar.setStyleSheet("QScrollBar:vertical{border: none;background: rgb(45,45,45);width: 10px;margin: 0px 0 0px 0;}QScrollBar::handle:vertical{background: dark grey;min-height: 26px;border-radius: 5px;}QScrollBar::add-line:vertical{background: none;height: 26px;subcontrol-position: bottom;subcontrol-origin: margin;}QScrollBar::sub-line:vertical{background: none;height: 0px;subcontrol-position: top left;subcontrol-origin: margin;position: absolute;}QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical{background: rgb(45,45,45);}")
        self.search_userlist.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.search_userlist.setFrameShadow(QtWidgets.QFrame.Plain)
        self.search_userlist.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.search_userlist.setWidgetResizable(True)
        self.search_userlist.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.search_userlist.setVerticalScrollBar(self.scrolllbar)
        self.search_userlist.setObjectName("search_userlist")



        #Search - Scroll Area Content
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 731, 311))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName("verticalLayout")



        #Search UserList-Data
        self.userlist_user1 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.userlist_user1.setMinimumSize(QtCore.QSize(0, 50))
        self.userlist_user1.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.userlist_user1.setFont(font)
        self.userlist_user1.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.userlist_user1.setObjectName("userlist_user1")
        self.verticalLayout.addWidget(self.userlist_user1)

        self.userlist_user2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.userlist_user2.setMinimumSize(QtCore.QSize(0, 50))
        self.userlist_user2.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.userlist_user2.setFont(font)
        self.userlist_user2.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.userlist_user2.setObjectName("userlist_user2")
        self.verticalLayout.addWidget(self.userlist_user2)

        self.userlist_user3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.userlist_user3.setMinimumSize(QtCore.QSize(0, 50))
        self.userlist_user3.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.userlist_user3.setFont(font)
        self.userlist_user3.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.userlist_user3.setObjectName("userlist_user3")
        self.verticalLayout.addWidget(self.userlist_user3)

        self.userlist_user4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.userlist_user4.setMinimumSize(QtCore.QSize(0, 50))
        self.userlist_user4.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.userlist_user4.setFont(font)
        self.userlist_user4.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.userlist_user4.setObjectName("userlist_user4")
        self.verticalLayout.addWidget(self.userlist_user4)

        self.userlist_user5 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.userlist_user5.setMinimumSize(QtCore.QSize(0, 50))
        self.userlist_user5.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.userlist_user5.setFont(font)
        self.userlist_user5.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.userlist_user5.setObjectName("userlist_user5")
        self.verticalLayout.addWidget(self.userlist_user5)


        self.userlist_user6 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.userlist_user6.setMinimumSize(QtCore.QSize(0, 50))
        self.userlist_user6.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.userlist_user6.setFont(font)
        self.userlist_user6.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.userlist_user6.setObjectName("userlist_user6")
        self.verticalLayout.addWidget(self.userlist_user6)



        self.userlist_user7 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.userlist_user7.setMinimumSize(QtCore.QSize(0, 50))
        self.userlist_user7.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.userlist_user7.setFont(font)
        self.userlist_user7.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.userlist_user7.setObjectName("userlist_user7")
        self.verticalLayout.addWidget(self.userlist_user7)



        self.userlist_user8 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.userlist_user8.setMinimumSize(QtCore.QSize(0, 50))
        self.userlist_user8.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.userlist_user8.setFont(font)
        self.userlist_user8.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.userlist_user8.setObjectName("userlist_user8")
        self.verticalLayout.addWidget(self.userlist_user8)


        self.userlist_user9 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.userlist_user9.setMinimumSize(QtCore.QSize(0, 50))
        self.userlist_user9.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.userlist_user9.setFont(font)
        self.userlist_user9.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.userlist_user9.setObjectName("userlist_user9")
        self.verticalLayout.addWidget(self.userlist_user9)



        self.userlist_user10 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.userlist_user10.setMinimumSize(QtCore.QSize(0, 50))
        self.userlist_user10.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.userlist_user10.setFont(font)
        self.userlist_user10.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.userlist_user10.setObjectName("userlist_user10")
        self.verticalLayout.addWidget(self.userlist_user10)


        self.userlist_user11 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.userlist_user11.setMinimumSize(QtCore.QSize(0, 50))
        self.userlist_user11.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.userlist_user11.setFont(font)
        self.userlist_user11.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.userlist_user11.setObjectName("userlist_user11")
        self.verticalLayout.addWidget(self.userlist_user11)



        self.userlist_user12 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.userlist_user12.setMinimumSize(QtCore.QSize(0, 50))
        self.userlist_user12.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.userlist_user12.setFont(font)
        self.userlist_user12.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.userlist_user12.setObjectName("userlist_user12")
        self.verticalLayout.addWidget(self.userlist_user12)


        self.userlist_user13 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.userlist_user13.setMinimumSize(QtCore.QSize(0, 50))
        self.userlist_user13.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.userlist_user13.setFont(font)
        self.userlist_user13.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.userlist_user13.setObjectName("userlist_user13")
        self.verticalLayout.addWidget(self.userlist_user13)


        self.userlist_user14 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.userlist_user14.setMinimumSize(QtCore.QSize(0, 50))
        self.userlist_user14.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.userlist_user14.setFont(font)
        self.userlist_user14.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.userlist_user14.setObjectName("userlist_user14")
        self.verticalLayout.addWidget(self.userlist_user14)
        self.userlist_user14.setHidden(True)
        self.userlist_user13.setHidden(True)
        self.userlist_user12.setHidden(True)
        self.userlist_user11.setHidden(True)
        self.userlist_user10.setHidden(True)
        self.userlist_user9.setHidden(True)
        self.userlist_user8.setHidden(True)
        self.userlist_user7.setHidden(True)
        self.userlist_user6.setHidden(True)
        self.userlist_user5.setHidden(True)
        self.userlist_user4.setHidden(True)
        self.userlist_user3.setHidden(True)
        self.userlist_user2.setHidden(True)
        self.userlist_user1.setHidden(True)

        


        
        #Search Userlist-Spacer
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.search_userlist.setWidget(self.scrollAreaWidgetContents)



        #TaskBar
        
        self.TB = QtWidgets.QLabel(self.searchscreen)
        self.TB.setGeometry(QtCore.QRect(-40, 480, 861, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.TB.setFont(font)
        self.TB.setStyleSheet("background:rgb(36, 36, 36);")
        self.TB.setScaledContents(True)
        self.TB.setObjectName("TB")



        
        self.TB_Home = QtWidgets.QPushButton(self.searchscreen)
        self.TB_Home.setGeometry(QtCore.QRect(10, 490, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.TB_Home.setFont(font)
        self.TB_Home.setStyleSheet("QPushButton{background-color:rgb(50, 50, 50);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.TB_Home.setObjectName("TB_Home")
        self.TB_Home.clicked.connect(lambda: setscreen_feed())

        
        self.TB_Search = QtWidgets.QPushButton(self.searchscreen)
        self.TB_Search.setGeometry(QtCore.QRect(170, 490, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.TB_Search.setFont(font)
        self.TB_Search.setStyleSheet("QPushButton{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.TB_Search.setObjectName("TB_Search")
        #self.TB_Search.clicked.connect(lambda: searchscreen())


        
        self.TB_Profile = QtWidgets.QPushButton(self.searchscreen)
        self.TB_Profile.setGeometry(QtCore.QRect(490, 490, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.TB_Profile.setFont(font)
        self.TB_Profile.setStyleSheet("QPushButton{background-color:rgb(50, 50, 50);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.TB_Profile.setObjectName("TB_Profile")
        self.TB_Profile.clicked.connect(lambda: setscreen_profile())

        
        self.TB_Timeline = QtWidgets.QPushButton(self.searchscreen)
        self.TB_Timeline.setGeometry(QtCore.QRect(330, 490, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.TB_Timeline.setFont(font)
        self.TB_Timeline.setStyleSheet("QPushButton{background-color:rgb(50, 50, 50);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.TB_Timeline.setObjectName("TB_Timeline")
        #self.TB_Timeline.clicked.connect(lambda: timelinescreen())


        
        self.TB_Settings = QtWidgets.QPushButton(self.searchscreen)
        self.TB_Settings.setGeometry(QtCore.QRect(650, 490, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.TB_Settings.setFont(font)
        self.TB_Settings.setStyleSheet("QPushButton{background-color:rgb(50, 50, 50);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.TB_Settings.setObjectName("TB_Settings")
        #self.TB_Timeline.clicked.connect(lambda: settingscreen())

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        _translate = QtCore.QCoreApplication.translate       
        self.TB.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.TB_Home.setText(_translate("MainWindow", "Home"))
        self.TB_Search.setText(_translate("MainWindow", "Search"))
        self.TB_Profile.setText(_translate("MainWindow", "Your Profile"))
        self.TB_Timeline.setText(_translate("MainWindow", "Timeline"))
        self.TB_Settings.setText(_translate("MainWindow", "SuperInsta"))


        self.search_textlogo.setText(_translate("MainWindow", " SuperInsta"))
        self.search_search_box.setPlaceholderText(_translate("MainWindow", "Search User"))
        self.search_signout.setText(_translate("MainWindow", "Sign Out"))


########################################### PROFILE SCREEN ################################################
        #homescreen
        self.profilescreen = QtWidgets.QWidget(MainWindow)
        self.profilescreen.setObjectName("profilescreen")
	


        #insta-logo
        self.profile_insta_logo = QtWidgets.QLabel(self.profilescreen)
        self.profile_insta_logo.setGeometry(QtCore.QRect(10, 10, 41, 41))
        self.profile_insta_logo.setText("")
        self.profile_insta_logo.setPixmap(QtGui.QPixmap(":/elem/logo.png"))
        self.profile_insta_logo.setScaledContents(True)
        self.profile_insta_logo.setObjectName("insta_logo")



        #instagrade-logo
        self.profile_instagrade_logo = QtWidgets.QLabel(self.profilescreen)
        self.profile_instagrade_logo.setGeometry(QtCore.QRect(50, 10, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Billabong")
        font.setPointSize(41)
        self.profile_instagrade_logo.setFont(font)
        self.profile_instagrade_logo.setStyleSheet("background:transparent;\n")
        self.profile_instagrade_logo.setScaledContents(True)
        self.profile_instagrade_logo.setObjectName("instagrade_logo")



        #image (DP)
        self.profile_image = QtWidgets.QLabel(self.profilescreen)
        self.profile_image.setGeometry(QtCore.QRect(40, 180, 200, 200))
        self.profile_image.setStyleSheet("border:3px solid rgb(29, 29, 29)")
        self.profile_image.setText("")
        #self.image.setPixmap(QtGui.QPixmap(":/elem/liam.jpg"))
        self.profile_image.setScaledContents(True)
        self.profile_image.setObjectName("image")



        #Edit Profile button
        self.profile_follow = QtWidgets.QPushButton(self.profilescreen)
        self.profile_follow.setGeometry(QtCore.QRect(600, 100, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.profile_follow.setFont(font)
        self.profile_follow.setStyleSheet("QPushButton{background-color:rgb(0, 157, 236);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.profile_follow.setObjectName("Edit Profile")



        #Change Password Button
        self.profile_block = QtWidgets.QPushButton(self.profilescreen)
        self.profile_block.setGeometry(QtCore.QRect(410, 100, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.profile_block.setFont(font)
        self.profile_block.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.profile_block.setObjectName("Change Password")



        #Liked Post Button
        self.profile_hidestory = QtWidgets.QPushButton(self.profilescreen)
        self.profile_hidestory.setGeometry(QtCore.QRect(220, 100, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.profile_hidestory.setFont(font)
        self.profile_hidestory.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.profile_hidestory.setObjectName("Liked Post")



        #Saved Post  Button
        self.profile_savedp = QtWidgets.QPushButton(self.profilescreen)
        self.profile_savedp.setGeometry(QtCore.QRect(30, 100, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.profile_savedp.setFont(font)
        self.profile_savedp.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.profile_savedp.setObjectName("savedp")



        #SignOut Button
        self.profile_signout = QtWidgets.QPushButton(self.profilescreen)
        self.profile_signout.setGeometry(QtCore.QRect(680, 10, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.profile_signout.setFont(font)
        self.profile_signout.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-radius:15px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));color:rgb(255, 142, 231);}")
        self.profile_signout.setObjectName("signout")
        self.profile_signout.clicked.connect(lambda:logout_instagram())

        #Refresh Button
        self.profile_refresh = QtWidgets.QPushButton(self.profilescreen)
        self.profile_refresh.setGeometry(QtCore.QRect(550, 10, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.profile_refresh.setFont(font)
        self.profile_refresh.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-radius:15px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));color:rgb(255, 142, 231);}")
        self.profile_refresh.setObjectName("signout")
        self.profile_refresh.clicked.connect(lambda:update_myprofile())
        self.profile_refresh.setToolTip("To Not get Banned, You can refresh every 25 seconds only")

        #Username
        self.profile_username = QtWidgets.QLabel(self.profilescreen)
        self.profile_username.setGeometry(QtCore.QRect(260, 180, 331, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.profile_username.setFont(font)
        self.profile_username.setStyleSheet("background:transparent;")
        self.profile_username.setScaledContents(True)



        #Vertical Layout 
        self.profile_verticalLayoutWidget = QtWidgets.QWidget(self.profilescreen)                              
        self.profile_verticalLayoutWidget.setGeometry(QtCore.QRect(260, 220, 381, 161))



        #Bio-Layout: Layout
        self.profile_bio_layout = QtWidgets.QVBoxLayout(self.profile_verticalLayoutWidget)
        self.profile_bio_layout.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.profile_bio_layout.setContentsMargins(0, 0, 0, 0)



        #Bio-Layout: account
        self.profile_account = QtWidgets.QLabel(self.profile_verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.profile_account.sizePolicy().hasHeightForWidth())
        self.profile_account.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.profile_account.setFont(font)
        self.profile_account.setStyleSheet("background:transparent;")
        self.profile_account.setScaledContents(True)
        self.profile_account.setWordWrap(True)
        self.profile_account.setOpenExternalLinks(True)
        self.profile_bio_layout.addWidget(self.profile_account)



        #Bio-Layout: Bio
        self.profile_bio = QtWidgets.QLabel(self.profile_verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.profile_bio.sizePolicy().hasHeightForWidth())
        self.profile_bio.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.profile_bio.setFont(font)
        self.profile_bio.setStyleSheet("background:transparent;")
        self.profile_bio.setScaledContents(True)
        self.profile_bio.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.bio.setWordWrap(True)
        self.profile_bio_layout.addWidget(self.profile_bio)



        #Bio-Layout: Website
        self.profile_website = QtWidgets.QLabel(self.profile_verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.profile_website.sizePolicy().hasHeightForWidth())
        self.website.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.profile_website.setFont(font)
        self.profile_website.setStyleSheet("background:transparent;")
        self.profile_website.setScaledContents(True)
        self.profile_website.setWordWrap(True)
        self.profile_website.setOpenExternalLinks(True)
        self.profile_bio_layout.addWidget(self.profile_website)



        #Bio-Layout: Mutual
        self.profile_mutual = QtWidgets.QLabel(self.profile_verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.profile_mutual.sizePolicy().hasHeightForWidth())
        self.profile_mutual.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.profile_mutual.setFont(font)
        self.profile_mutual.setStyleSheet("background:transparent;")
        self.profile_mutual.setScaledContents(True)
        self.profile_mutual.setWordWrap(True)
        self.profile_mutual.setOpenExternalLinks(True)
        self.profile_bio_layout.addWidget(self.profile_mutual)



        #Bio-Layout: Spacer
        profile_spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.profile_bio_layout.addItem(profile_spacerItem)



        #Following-Display
        self.profile_following = QtWidgets.QLabel(self.profilescreen)
        self.profile_following.setGeometry(QtCore.QRect(30, 420, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.profile_following.setFont(font)
        self.profile_following.setStyleSheet("QLabel{background-color:rgb(26, 26, 26);border-radius:9px;color:white;}")
        self.profile_following.setScaledContents(True)



        #Follower-Display
        self.profile_follower = QtWidgets.QLabel(self.profilescreen)
        self.profile_follower.setGeometry(QtCore.QRect(220, 420, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.profile_follower.setFont(font)
        self.profile_follower.setStyleSheet("QLabel{background-color:rgb(26, 26, 26);border-radius:9px;color:white;}")
        self.profile_follower.setScaledContents(True)




        #Total Post Count
        self.profile_post = QtWidgets.QLabel(self.profilescreen)
        self.profile_post.setGeometry(QtCore.QRect(410, 420, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.profile_post.setFont(font)
        self.profile_post.setStyleSheet("QLabel{background-color:rgb(26, 26, 26);border-radius:9px;color:white;}")
        self.profile_post.setScaledContents(True)



        #Follow/Not follow you
        self.profile_followsyou = QtWidgets.QLabel(self.profilescreen)
        self.profile_followsyou.setGeometry(QtCore.QRect(600, 420, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.profile_followsyou.setFont(font)
        self.profile_followsyou.setStyleSheet("QLabel{background-color:rgb(26, 26, 26);border-radius:9px;color:white;}")
        self.profile_followsyou.setScaledContents(True)

        self.myposts = QtWidgets.QPushButton(self.profilescreen)
        self.myposts.setGeometry(QtCore.QRect(600, 150, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.myposts.setFont(font)
        self.myposts.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.myposts.setObjectName("myposts")
        self.myposts.clicked.connect(lambda: setscreen_myposts_screen())




        #TaskBar  
        self.TB = QtWidgets.QLabel(self.profilescreen)
        self.TB.setGeometry(QtCore.QRect(-40, 480, 861, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.TB.setFont(font)
        self.TB.setStyleSheet("background:rgb(36, 36, 36);")
        self.TB.setScaledContents(True)
        self.TB.setObjectName("TB")



        
        self.TB_Home = QtWidgets.QPushButton(self.profilescreen)
        self.TB_Home.setGeometry(QtCore.QRect(10, 490, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.TB_Home.setFont(font)
        self.TB_Home.setStyleSheet("QPushButton{background-color:rgb(50, 50, 50);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.TB_Home.setObjectName("TB_Home")
        self.TB_Home.clicked.connect(lambda: setscreen_feed())

        
        self.TB_Search = QtWidgets.QPushButton(self.profilescreen)
        self.TB_Search.setGeometry(QtCore.QRect(170, 490, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.TB_Search.setFont(font)
        self.TB_Search.setStyleSheet("QPushButton{background-color:rgb(50, 50, 50);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.TB_Search.setObjectName("TB_Search")
        self.TB_Search.clicked.connect(lambda: setscreen_search())


        
        self.TB_Profile = QtWidgets.QPushButton(self.profilescreen)
        self.TB_Profile.setGeometry(QtCore.QRect(490, 490, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.TB_Profile.setFont(font)
        self.TB_Profile.setStyleSheet("QPushButton{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.TB_Profile.setObjectName("TB_Profile")
        self.TB_Profile.clicked.connect(lambda: setscreen_profilemain())

        
        self.TB_Timeline = QtWidgets.QPushButton(self.profilescreen)
        self.TB_Timeline.setGeometry(QtCore.QRect(330, 490, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.TB_Timeline.setFont(font)
        self.TB_Timeline.setStyleSheet("QPushButton{background-color:rgb(50, 50, 50);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.TB_Timeline.setObjectName("TB_Timeline")
        #self.TB_Timeline.clicked.connect(lambda: timelinescreen())


        
        self.TB_Settings = QtWidgets.QPushButton(self.profilescreen)
        self.TB_Settings.setGeometry(QtCore.QRect(650, 490, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.TB_Settings.setFont(font)
        self.TB_Settings.setStyleSheet("QPushButton{background-color:rgb(50, 50, 50);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.TB_Settings.setObjectName("TB_Settings")
        #self.TB_Timeline.clicked.connect(lambda: settingscreen())

        self.TB.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.TB_Home.setText(_translate("MainWindow", "Home"))
        self.TB_Search.setText(_translate("MainWindow", "Search"))
        self.TB_Profile.setText(_translate("MainWindow", "Your Profile"))
        self.TB_Timeline.setText(_translate("MainWindow", "Timeline"))
        self.TB_Settings.setText(_translate("MainWindow", "SuperInsta"))
        #Translatable Texts

        self.profile_instagrade_logo.setText(_translate("MainWindow", " SuperInsta"))
        self.profile_follow.setText(_translate("MainWindow", "Edit Profile"))
        self.profile_block.setText(_translate("MainWindow", "Change Password"))
        self.profile_hidestory.setText(_translate("MainWindow", "Liked Posts"))
        self.profile_savedp.setText(_translate("MainWindow", "Saved Posts"))
        self.profile_signout.setText(_translate("MainWindow", "Sign Out"))
        self.profile_refresh.setText(_translate("MainWindow", "Refresh"))
        self.myposts.setText(_translate("MainWindow", "My Posts"))
        self.profile_username.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">@username</span></p></body></html>"))
        self.profile_account.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#757575;\">Account Type</span></p></body></html>"))
        self.profile_bio.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#4d4d4d;\"> Bio</span></p></body></html>"))
        self.profile_website.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#00aaff;\">External URL</span></p></body></html>"))
        self.profile_following.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Following: </span></p></body></html>"))
        self.profile_follower.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Follower: </span></p></body></html>"))
        self.profile_post.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Total Post:</span></p></body></html>"))
        self.profile_followsyou.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Blocked:</span></p></body></html>"))
########################################### Post screen################################################
        #Post Screen
        self.postscreen = QtWidgets.QWidget(MainWindow)
        self.postscreen.setObjectName("postscreen")



        #Post Logo
        self.post_logo = QtWidgets.QLabel(self.postscreen)
        self.post_logo.setGeometry(QtCore.QRect(10, 10, 41, 41))
        self.post_logo.setText("")
        self.post_logo.setPixmap(QtGui.QPixmap(":/elem/logo.png"))
        self.post_logo.setScaledContents(True)
        self.post_logo.setObjectName("post_logo")



        #Post Text Logo
        self.post_textlogo = QtWidgets.QLabel(self.postscreen)
        self.post_textlogo.setGeometry(QtCore.QRect(50, 10, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Billabong")
        font.setPointSize(41)
        self.post_textlogo.setFont(font)
        self.post_textlogo.setStyleSheet("background:transparent;")
        self.post_textlogo.setScaledContents(True)
        self.post_textlogo.setObjectName("post_textlogo")



        #POst Signout
        self.post_signout = QtWidgets.QPushButton(self.postscreen)
        self.post_signout.setGeometry(QtCore.QRect(680, 10, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.post_signout.setFont(font)
        self.post_signout.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-radius:15px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));color:rgb(255, 142, 231);}")
        self.post_signout.setObjectName("post_signout")
        self.post_signout.clicked.connect(lambda:logout_instagram())



        #Post Username
        self.post_username = QtWidgets.QLabel(self.postscreen)
        self.post_username.setGeometry(QtCore.QRect(60, 70, 741, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.post_username.setFont(font)
        self.post_username.setStyleSheet("QLabel{background-color:rgb(26, 26, 26);border-radius:9px;color:white;}")
        self.post_username.setScaledContents(True)
        self.post_username.setObjectName("post_username")



        #Post Close Button
        self.post_close = QtWidgets.QPushButton(self.postscreen)
        self.post_close.setGeometry(QtCore.QRect(10, 70, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.post_close.setFont(font)
        self.post_close.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.post_close.setObjectName("post_close")
        self.post_close.clicked.connect(lambda: posts_close())



        #Post-Post1
        self.post_post1 = QtWidgets.QLabel(self.postscreen)
        self.post_post1.setGeometry(QtCore.QRect(5, 120, 162, 162))
        self.post_post1.setStyleSheet("border:3px solid rgb(29, 29, 29);")
        self.post_post1.setText("")
        self.post_post1.setScaledContents(True)
        self.post_post1.setObjectName("post_post1")

        #Post-Post2
        self.post_post2 = QtWidgets.QLabel(self.postscreen)
        self.post_post2.setGeometry(QtCore.QRect(164, 120, 162, 162))
        self.post_post2.setStyleSheet("border:3px solid rgb(29, 29, 29);")
        self.post_post2.setText("")
        self.post_post2.setScaledContents(True)
        self.post_post2.setObjectName("post_post2")

        #Post-Post3
        self.post_post3 = QtWidgets.QLabel(self.postscreen)
        self.post_post3.setGeometry(QtCore.QRect(323, 120, 162, 162))
        self.post_post3.setStyleSheet("border:3px solid rgb(29, 29, 29);")
        self.post_post3.setText("")
        self.post_post3.setScaledContents(True)
        self.post_post3.setObjectName("post_post3")

        #Post-Post4
        self.post_post4 = QtWidgets.QLabel(self.postscreen)
        self.post_post4.setGeometry(QtCore.QRect(482, 120, 162, 162))
        self.post_post4.setStyleSheet("border:3px solid rgb(29, 29, 29);")
        self.post_post4.setText("")
        self.post_post4.setScaledContents(True)
        self.post_post4.setObjectName("post_post4")

        #Post-Post5
        self.post_post5 = QtWidgets.QLabel(self.postscreen)
        self.post_post5.setGeometry(QtCore.QRect(641, 120, 162, 162))
        self.post_post5.setStyleSheet("border:3px solid rgb(29, 29, 29);")
        self.post_post5.setText("")
        self.post_post5.setScaledContents(True)
        self.post_post5.setObjectName("post_post5")
        
        #Post-Post6
        self.post_post6 = QtWidgets.QLabel(self.postscreen)
        self.post_post6.setGeometry(QtCore.QRect(5, 280, 162, 162))
        self.post_post6.setStyleSheet("border:3px solid rgb(29, 29, 29);")
        self.post_post6.setText("")
        self.post_post6.setScaledContents(True)
        self.post_post6.setObjectName("post_post6")
        
        #Post-Post7
        self.post_post7 = QtWidgets.QLabel(self.postscreen)
        self.post_post7.setGeometry(QtCore.QRect(164, 280, 162, 162))
        self.post_post7.setStyleSheet("border:3px solid rgb(29, 29, 29);")
        self.post_post7.setText("")
        self.post_post7.setScaledContents(True)
        self.post_post7.setObjectName("post_post7")

        #Post-Post8
        self.post_post8 = QtWidgets.QLabel(self.postscreen)
        self.post_post8.setGeometry(QtCore.QRect(323, 280, 162, 162))
        self.post_post8.setStyleSheet("border:3px solid rgb(29, 29, 29);")
        self.post_post8.setText("")
        self.post_post8.setScaledContents(True)
        self.post_post8.setObjectName("post_post8")

        #Post-Post9
        self.post_post9 = QtWidgets.QLabel(self.postscreen)
        self.post_post9.setGeometry(QtCore.QRect(482, 280, 162, 162))
        self.post_post9.setStyleSheet("border:3px solid rgb(29, 29, 29);")
        self.post_post9.setText("")
        self.post_post9.setScaledContents(True)
        self.post_post9.setObjectName("post_post9")

        #Post-Post10
        self.post_post10 = QtWidgets.QLabel(self.postscreen)
        self.post_post10.setGeometry(QtCore.QRect(641, 280, 162, 162))
        self.post_post10.setStyleSheet("border:3px solid rgb(29, 29, 29);")
        self.post_post10.setText("")
        self.post_post10.setScaledContents(True)
        self.post_post10.setObjectName("post_post10")






        self.post_type1 = QtWidgets.QLabel(self.postscreen)
        self.post_type1.setGeometry(QtCore.QRect(127, 131, 31, 31))
        self.post_type1.setStyleSheet("background:transparent")
        self.post_type1.setText("")
        self.post_type1.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
        self.post_type1.setScaledContents(True)
        self.post_type1.setObjectName("post_type1")
        self.post_type2 = QtWidgets.QLabel(self.postscreen)
        self.post_type2.setGeometry(QtCore.QRect(288, 131, 31, 31))
        self.post_type2.setStyleSheet("background:transparent")
        self.post_type2.setText("")
        self.post_type2.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
        self.post_type2.setScaledContents(True)
        self.post_type2.setObjectName("post_type2")
        self.post_type4 = QtWidgets.QLabel(self.postscreen)
        self.post_type4.setGeometry(QtCore.QRect(607, 131, 31, 31))
        self.post_type4.setStyleSheet("background:transparent")
        self.post_type4.setText("")
        self.post_type4.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
        self.post_type4.setScaledContents(True)
        self.post_type4.setObjectName("post_type4")
        self.post_type3 = QtWidgets.QLabel(self.postscreen)
        self.post_type3.setGeometry(QtCore.QRect(449, 131, 31, 31))
        self.post_type3.setStyleSheet("background:transparent")
        self.post_type3.setText("")
        self.post_type3.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
        self.post_type3.setScaledContents(True)
        self.post_type3.setObjectName("post_type3")
        self.post_type5 = QtWidgets.QLabel(self.postscreen)
        self.post_type5.setGeometry(QtCore.QRect(766, 131, 31, 31))
        self.post_type5.setStyleSheet("background:transparent")
        self.post_type5.setText("")
        self.post_type5.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
        self.post_type5.setScaledContents(True)
        self.post_type5.setObjectName("post_type5")
        self.post_type9 = QtWidgets.QLabel(self.postscreen)
        self.post_type9.setGeometry(QtCore.QRect(607, 290, 31, 31))
        self.post_type9.setStyleSheet("background:transparent")
        self.post_type9.setText("")
        self.post_type9.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
        self.post_type9.setScaledContents(True)
        self.post_type9.setObjectName("post_type9")
        self.post_type8 = QtWidgets.QLabel(self.postscreen)
        self.post_type8.setGeometry(QtCore.QRect(449, 290, 31, 31))
        self.post_type8.setStyleSheet("background:transparent")
        self.post_type8.setText("")
        self.post_type8.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
        self.post_type8.setScaledContents(True)
        self.post_type8.setObjectName("post_type8")
        self.post_type7 = QtWidgets.QLabel(self.postscreen)
        self.post_type7.setGeometry(QtCore.QRect(288, 290, 31, 31))
        self.post_type7.setStyleSheet("background:transparent")
        self.post_type7.setText("")
        self.post_type7.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
        self.post_type7.setScaledContents(True)
        self.post_type7.setObjectName("post_type7")
        self.post_type6 = QtWidgets.QLabel(self.postscreen)
        self.post_type6.setGeometry(QtCore.QRect(131, 290, 31, 31))
        self.post_type6.setStyleSheet("background:transparent")
        self.post_type6.setText("")
        self.post_type6.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
        self.post_type6.setScaledContents(True)
        self.post_type6.setObjectName("post_type6")
        self.post_type10 = QtWidgets.QLabel(self.postscreen)
        self.post_type10.setGeometry(QtCore.QRect(766, 290, 31, 31))
        self.post_type10.setStyleSheet("background:transparent")
        self.post_type10.setText("")
        self.post_type10.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
        self.post_type10.setScaledContents(True)
        self.post_type10.setObjectName("post_type10")




        #Post-Post1btn
        self.post_post1btn = QtWidgets.QPushButton(self.postscreen)
        self.post_post1btn.setGeometry(QtCore.QRect(5, 120, 162, 162))
        self.post_post1btn.setStyleSheet("background:transparent")
        self.post_post1btn.setText("")
        self.post_post1btn.setObjectName("post_post1btn")
        self.post_post1btn.clicked.connect(lambda: postfromdata1())
        
        #Post-Post2btn
        self.post_post2btn = QtWidgets.QPushButton(self.postscreen)
        self.post_post2btn.setGeometry(QtCore.QRect(164, 120, 162, 162))
        self.post_post2btn.setStyleSheet("background:transparent")
        self.post_post2btn.setText("")
        self.post_post2btn.setObjectName("post_post2btn")
        self.post_post2btn.clicked.connect(lambda: postfromdata2())
        
        #Post-Post3btn
        self.post_post3btn = QtWidgets.QPushButton(self.postscreen)
        self.post_post3btn.setGeometry(QtCore.QRect(323, 120, 162, 162))
        self.post_post3btn.setStyleSheet("background:transparent")
        self.post_post3btn.setText("")
        self.post_post3btn.setObjectName("post_post3btn")
        self.post_post3btn.clicked.connect(lambda: postfromdata3())
        
        #Post-Post4btn
        self.post_post4btn = QtWidgets.QPushButton(self.postscreen)
        self.post_post4btn.setGeometry(QtCore.QRect(482, 120, 162, 162))
        self.post_post4btn.setStyleSheet("background:transparent")
        self.post_post4btn.setText("")
        self.post_post4btn.setObjectName("post_post4btn")
        self.post_post4btn.clicked.connect(lambda: postfromdata4())
        
        #Post-Post5btn
        self.post_post5btn = QtWidgets.QPushButton(self.postscreen)
        self.post_post5btn.setGeometry(QtCore.QRect(641, 120, 162, 162))
        self.post_post5btn.setStyleSheet("background:transparent")
        self.post_post5btn.setText("")
        self.post_post5btn.setObjectName("post_post5btn")
        self.post_post5btn.clicked.connect(lambda: postfromdata5())
              
        #Post-Post6btn
        self.post_post6btn = QtWidgets.QPushButton(self.postscreen)
        self.post_post6btn.setGeometry(QtCore.QRect(5, 280, 162, 162))
        self.post_post6btn.setStyleSheet("background:transparent")
        self.post_post6btn.setText("")
        self.post_post6btn.setObjectName("post_post6btn")
        self.post_post6btn.clicked.connect(lambda: postfromdata6())
              
        #Post-Post7btn
        self.post_post7btn = QtWidgets.QPushButton(self.postscreen)
        self.post_post7btn.setGeometry(QtCore.QRect(164, 280, 162, 162))
        self.post_post7btn.setStyleSheet("background:transparent")
        self.post_post7btn.setText("")
        self.post_post7btn.setObjectName("post_post7btn")
        self.post_post7btn.clicked.connect(lambda: postfromdata7())
        
        #Post-Post8btn
        self.post_post8btn = QtWidgets.QPushButton(self.postscreen)
        self.post_post8btn.setGeometry(QtCore.QRect(323, 280, 162, 162))
        self.post_post8btn.setStyleSheet("background:transparent")
        self.post_post8btn.setText("")
        self.post_post8btn.setObjectName("post_post8")
        self.post_post8btn.clicked.connect(lambda: postfromdata8())
        
        #Post-Post9btn
        self.post_post9btn = QtWidgets.QPushButton(self.postscreen)
        self.post_post9btn.setGeometry(QtCore.QRect(482, 280, 162, 162))
        self.post_post9btn.setStyleSheet("background:transparent")
        self.post_post9btn.setText("")
        self.post_post9btn.setObjectName("post_post9btn")
        self.post_post9btn.clicked.connect(lambda: postfromdata9())
        
        #Post-Post10btn
        self.post_post10btn = QtWidgets.QPushButton(self.postscreen)
        self.post_post10btn.setGeometry(QtCore.QRect(641, 280, 162, 162))
        self.post_post10btn.setStyleSheet("background:transparent")
        self.post_post10btn.setText("")
        self.post_post10btn.setObjectName("post_post10btn")
        self.post_post10btn.clicked.connect(lambda: postfromdata10())


        #Post- Next Button
        self.post_next = QtWidgets.QPushButton(self.postscreen)
        self.post_next.setGeometry(QtCore.QRect(730, 448, 71, 28))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.post_next.setFont(font)
        self.post_next.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.post_next.setObjectName("post_next")
        self.post_next.clicked.connect(lambda: next_posts())
        #Post- PAGE NO.
        self.post_page = QtWidgets.QLabel(self.postscreen)
        self.post_page.setGeometry(QtCore.QRect(320, 440, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.post_page.setFont(font)
        self.post_page.setStyleSheet("background:transparent;")
        self.post_page.setScaledContents(True)
        self.post_page.setObjectName("post_page")


        #Post- Back Button
        self.post_back = QtWidgets.QPushButton(self.postscreen)
        self.post_back.setGeometry(QtCore.QRect(10, 448, 71, 28))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.post_back.setFont(font)
        self.post_back.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.post_back.setObjectName("post_back")
        self.post_back.clicked.connect(lambda: back_posts())
        #TaskBar  
        self.TB = QtWidgets.QLabel(self.postscreen)
        self.TB.setGeometry(QtCore.QRect(-40, 480, 861, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.TB.setFont(font)
        self.TB.setStyleSheet("background:rgb(36, 36, 36);")
        self.TB.setScaledContents(True)
        self.TB.setObjectName("TB")



        
        self.TB_Home = QtWidgets.QPushButton(self.postscreen)
        self.TB_Home.setGeometry(QtCore.QRect(10, 490, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.TB_Home.setFont(font)
        self.TB_Home.setStyleSheet("QPushButton{background-color:rgb(50, 50, 50);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.TB_Home.setObjectName("TB_Home")
        self.TB_Home.clicked.connect(lambda: setscreen_feed())

        
        self.TB_Search = QtWidgets.QPushButton(self.postscreen)
        self.TB_Search.setGeometry(QtCore.QRect(170, 490, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.TB_Search.setFont(font)
        self.TB_Search.setStyleSheet("QPushButton{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.TB_Search.setObjectName("TB_Search")
        self.TB_Search.clicked.connect(lambda: setscreen_searchmain())


        
        self.TB_Profile = QtWidgets.QPushButton(self.postscreen)
        self.TB_Profile.setGeometry(QtCore.QRect(490, 490, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.TB_Profile.setFont(font)
        self.TB_Profile.setStyleSheet("QPushButton{background-color:rgb(50, 50, 50);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.TB_Profile.setObjectName("TB_Profile")
        self.TB_Profile.clicked.connect(lambda: setscreen_profile())

        
        self.TB_Timeline = QtWidgets.QPushButton(self.postscreen)
        self.TB_Timeline.setGeometry(QtCore.QRect(330, 490, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.TB_Timeline.setFont(font)
        self.TB_Timeline.setStyleSheet("QPushButton{background-color:rgb(50, 50, 50);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.TB_Timeline.setObjectName("TB_Timeline")
        #self.TB_Timeline.clicked.connect(lambda: setscreen_posts_screen())


        
        self.TB_Settings = QtWidgets.QPushButton(self.postscreen)
        self.TB_Settings.setGeometry(QtCore.QRect(650, 490, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.TB_Settings.setFont(font)
        self.TB_Settings.setStyleSheet("QPushButton{background-color:rgb(50, 50, 50);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.TB_Settings.setObjectName("TB_Settings")
        #self.TB_Timeline.clicked.connect(lambda: setscreen_posts_screen())


        #Translates Texts
        self.post_textlogo.setText(_translate("MainWindow", " SuperInsta"))
        self.post_signout.setText(_translate("MainWindow", "Sign Out"))
        self.post_username.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">@username</span></p></body></html>"))
        self.TB_Home.setText(_translate("MainWindow", "Home"))
        self.TB_Search.setText(_translate("MainWindow", "Search"))
        self.TB_Profile.setText(_translate("MainWindow", "Your Profile"))
        self.TB_Timeline.setText(_translate("MainWindow", "Timeline"))
        self.TB_Settings.setText(_translate("MainWindow", "SuperInsta"))
        self.post_close.setText(_translate("MainWindow", "x"))
        self.post_next.setText(_translate("MainWindow", ">"))
        self.post_page.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Page 1</span></p></body></html>"))
        self.post_back.setText(_translate("MainWindow", "<"))

########################################### Post screen################################################
        #Post Screen
        self.mypostscreen = QtWidgets.QWidget(MainWindow)
        self.mypostscreen.setObjectName("mypostscreen")



        #mypost Logo
        self.mypost_logo = QtWidgets.QLabel(self.mypostscreen)
        self.mypost_logo.setGeometry(QtCore.QRect(10, 10, 41, 41))
        self.mypost_logo.setText("")
        self.mypost_logo.setPixmap(QtGui.QPixmap(":/elem/logo.png"))
        self.mypost_logo.setScaledContents(True)
        self.mypost_logo.setObjectName("mypost_logo")



        #Post Text Logo
        self.mypost_textlogo = QtWidgets.QLabel(self.mypostscreen)
        self.mypost_textlogo.setGeometry(QtCore.QRect(50, 10, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Billabong")
        font.setPointSize(41)
        self.mypost_textlogo.setFont(font)
        self.mypost_textlogo.setStyleSheet("background:transparent;")
        self.mypost_textlogo.setScaledContents(True)
        self.mypost_textlogo.setObjectName("mypost_textlogo")



        #POst Signout
        self.mypost_signout = QtWidgets.QPushButton(self.mypostscreen)
        self.mypost_signout.setGeometry(QtCore.QRect(680, 10, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.mypost_signout.setFont(font)
        self.mypost_signout.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-radius:15px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));color:rgb(255, 142, 231);}")
        self.mypost_signout.setObjectName("mypost_signout")
        self.mypost_signout.clicked.connect(lambda:logout_instagram())



        #Post Username
        self.mypost_username = QtWidgets.QLabel(self.mypostscreen)
        self.mypost_username.setGeometry(QtCore.QRect(60, 70, 741, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.mypost_username.setFont(font)
        self.mypost_username.setStyleSheet("QLabel{background-color:rgb(26, 26, 26);border-radius:9px;color:white;}")
        self.mypost_username.setScaledContents(True)
        self.mypost_username.setObjectName("mypost_username")



        #Post Close Button
        self.mypost_close = QtWidgets.QPushButton(self.mypostscreen)
        self.mypost_close.setGeometry(QtCore.QRect(10, 70, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.mypost_close.setFont(font)
        self.mypost_close.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.mypost_close.setObjectName("mypost_close")
        self.mypost_close.clicked.connect(lambda: myposts_close())



        #Post-Post1
        self.mypost_mypost1 = QtWidgets.QLabel(self.mypostscreen)
        self.mypost_mypost1.setGeometry(QtCore.QRect(5, 120, 162, 162))
        self.mypost_mypost1.setStyleSheet("border:3px solid rgb(29, 29, 29);")
        self.mypost_mypost1.setText("")
        self.mypost_mypost1.setScaledContents(True)
        self.mypost_mypost1.setObjectName("mypost_mypost1")

        #Post-Post2
        self.mypost_mypost2 = QtWidgets.QLabel(self.mypostscreen)
        self.mypost_mypost2.setGeometry(QtCore.QRect(164, 120, 162, 162))
        self.mypost_mypost2.setStyleSheet("border:3px solid rgb(29, 29, 29);")
        self.mypost_mypost2.setText("")
        self.mypost_mypost2.setScaledContents(True)
        self.mypost_mypost2.setObjectName("mypost_mypost2")

        #mypost-mypost3
        self.mypost_mypost3 = QtWidgets.QLabel(self.mypostscreen)
        self.mypost_mypost3.setGeometry(QtCore.QRect(323, 120, 162, 162))
        self.mypost_mypost3.setStyleSheet("border:3px solid rgb(29, 29, 29);")
        self.mypost_mypost3.setText("")
        self.mypost_mypost3.setScaledContents(True)
        self.mypost_mypost3.setObjectName("mypost_mypost3")

        #mypost-mypost4
        self.mypost_mypost4 = QtWidgets.QLabel(self.mypostscreen)
        self.mypost_mypost4.setGeometry(QtCore.QRect(482, 120, 162, 162))
        self.mypost_mypost4.setStyleSheet("border:3px solid rgb(29, 29, 29);")
        self.mypost_mypost4.setText("")
        self.mypost_mypost4.setScaledContents(True)
        self.mypost_mypost4.setObjectName("mypost_mypost4")

        #mypost-mypost5
        self.mypost_mypost5 = QtWidgets.QLabel(self.mypostscreen)
        self.mypost_mypost5.setGeometry(QtCore.QRect(641, 120, 162, 162))
        self.mypost_mypost5.setStyleSheet("border:3px solid rgb(29, 29, 29);")
        self.mypost_mypost5.setText("")
        self.mypost_mypost5.setScaledContents(True)
        self.mypost_mypost5.setObjectName("mypost_mypost5")
        
        #mypost-mypost6
        self.mypost_mypost6 = QtWidgets.QLabel(self.mypostscreen)
        self.mypost_mypost6.setGeometry(QtCore.QRect(5, 280, 162, 162))
        self.mypost_mypost6.setStyleSheet("border:3px solid rgb(29, 29, 29);")
        self.mypost_mypost6.setText("")
        self.mypost_mypost6.setScaledContents(True)
        self.mypost_mypost6.setObjectName("mypost_mypost6")
        
        #mypost-mypost7
        self.mypost_mypost7 = QtWidgets.QLabel(self.mypostscreen)
        self.mypost_mypost7.setGeometry(QtCore.QRect(164, 280, 162, 162))
        self.mypost_mypost7.setStyleSheet("border:3px solid rgb(29, 29, 29);")
        self.mypost_mypost7.setText("")
        self.mypost_mypost7.setScaledContents(True)
        self.mypost_mypost7.setObjectName("mypost_mypost7")

        #mypost-mypost8
        self.mypost_mypost8 = QtWidgets.QLabel(self.mypostscreen)
        self.mypost_mypost8.setGeometry(QtCore.QRect(323, 280, 162, 162))
        self.mypost_mypost8.setStyleSheet("border:3px solid rgb(29, 29, 29);")
        self.mypost_mypost8.setText("")
        self.mypost_mypost8.setScaledContents(True)
        self.mypost_mypost8.setObjectName("mypost_mypost8")

        #mypost-mypost9
        self.mypost_mypost9 = QtWidgets.QLabel(self.mypostscreen)
        self.mypost_mypost9.setGeometry(QtCore.QRect(482, 280, 162, 162))
        self.mypost_mypost9.setStyleSheet("border:3px solid rgb(29, 29, 29);")
        self.mypost_mypost9.setText("")
        self.mypost_mypost9.setScaledContents(True)
        self.mypost_mypost9.setObjectName("mypost_mypost9")

        #mypost-mypost10
        self.mypost_mypost10 = QtWidgets.QLabel(self.mypostscreen)
        self.mypost_mypost10.setGeometry(QtCore.QRect(641, 280, 162, 162))
        self.mypost_mypost10.setStyleSheet("border:3px solid rgb(29, 29, 29);")
        self.mypost_mypost10.setText("")
        self.mypost_mypost10.setScaledContents(True)
        self.mypost_mypost10.setObjectName("mypost_mypost10")






        self.mypost_type1 = QtWidgets.QLabel(self.mypostscreen)
        self.mypost_type1.setGeometry(QtCore.QRect(127, 131, 31, 31))
        self.mypost_type1.setStyleSheet("background:transparent")
        self.mypost_type1.setText("")
        self.mypost_type1.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
        self.mypost_type1.setScaledContents(True)
        self.mypost_type1.setObjectName("mypost_type1")
        self.mypost_type2 = QtWidgets.QLabel(self.mypostscreen)
        self.mypost_type2.setGeometry(QtCore.QRect(288, 131, 31, 31))
        self.mypost_type2.setStyleSheet("background:transparent")
        self.mypost_type2.setText("")
        self.mypost_type2.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
        self.mypost_type2.setScaledContents(True)
        self.mypost_type2.setObjectName("mypost_type2")
        self.mypost_type4 = QtWidgets.QLabel(self.mypostscreen)
        self.mypost_type4.setGeometry(QtCore.QRect(607, 131, 31, 31))
        self.mypost_type4.setStyleSheet("background:transparent")
        self.mypost_type4.setText("")
        self.mypost_type4.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
        self.mypost_type4.setScaledContents(True)
        self.mypost_type4.setObjectName("mypost_type4")
        self.mypost_type3 = QtWidgets.QLabel(self.mypostscreen)
        self.mypost_type3.setGeometry(QtCore.QRect(449, 131, 31, 31))
        self.mypost_type3.setStyleSheet("background:transparent")
        self.mypost_type3.setText("")
        self.mypost_type3.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
        self.mypost_type3.setScaledContents(True)
        self.mypost_type3.setObjectName("mypost_type3")
        self.mypost_type5 = QtWidgets.QLabel(self.mypostscreen)
        self.mypost_type5.setGeometry(QtCore.QRect(766, 131, 31, 31))
        self.mypost_type5.setStyleSheet("background:transparent")
        self.mypost_type5.setText("")
        self.mypost_type5.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
        self.mypost_type5.setScaledContents(True)
        self.mypost_type5.setObjectName("mypost_type5")
        self.mypost_type9 = QtWidgets.QLabel(self.mypostscreen)
        self.mypost_type9.setGeometry(QtCore.QRect(607, 290, 31, 31))
        self.mypost_type9.setStyleSheet("background:transparent")
        self.mypost_type9.setText("")
        self.mypost_type9.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
        self.mypost_type9.setScaledContents(True)
        self.mypost_type9.setObjectName("mypost_type9")
        self.mypost_type8 = QtWidgets.QLabel(self.mypostscreen)
        self.mypost_type8.setGeometry(QtCore.QRect(449, 290, 31, 31))
        self.mypost_type8.setStyleSheet("background:transparent")
        self.mypost_type8.setText("")
        self.mypost_type8.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
        self.mypost_type8.setScaledContents(True)
        self.mypost_type8.setObjectName("mypost_type8")
        self.mypost_type7 = QtWidgets.QLabel(self.mypostscreen)
        self.mypost_type7.setGeometry(QtCore.QRect(288, 290, 31, 31))
        self.mypost_type7.setStyleSheet("background:transparent")
        self.mypost_type7.setText("")
        self.mypost_type7.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
        self.mypost_type7.setScaledContents(True)
        self.mypost_type7.setObjectName("mypost_type7")
        self.mypost_type6 = QtWidgets.QLabel(self.mypostscreen)
        self.mypost_type6.setGeometry(QtCore.QRect(131, 290, 31, 31))
        self.mypost_type6.setStyleSheet("background:transparent")
        self.mypost_type6.setText("")
        self.mypost_type6.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
        self.mypost_type6.setScaledContents(True)
        self.mypost_type6.setObjectName("mypost_type6")
        self.mypost_type10 = QtWidgets.QLabel(self.mypostscreen)
        self.mypost_type10.setGeometry(QtCore.QRect(766, 290, 31, 31))
        self.mypost_type10.setStyleSheet("background:transparent")
        self.mypost_type10.setText("")
        self.mypost_type10.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
        self.mypost_type10.setScaledContents(True)
        self.mypost_type10.setObjectName("mypost_type10")



        #mypost-mypost1btn
        self.mypost_mypost1btn = QtWidgets.QPushButton(self.mypostscreen)
        self.mypost_mypost1btn.setGeometry(QtCore.QRect(5, 120, 162, 162))
        self.mypost_mypost1btn.setStyleSheet("background:transparent")
        self.mypost_mypost1btn.setText("")
        self.mypost_mypost1btn.setObjectName("mypost_mypost1btn")
        self.mypost_mypost1btn.clicked.connect(lambda: mypostfromdata1())
        
        #mypost-mypost2btn
        self.mypost_mypost2btn = QtWidgets.QPushButton(self.mypostscreen)
        self.mypost_mypost2btn.setGeometry(QtCore.QRect(164, 120, 162, 162))
        self.mypost_mypost2btn.setStyleSheet("background:transparent")
        self.mypost_mypost2btn.setText("")
        self.mypost_mypost2btn.setObjectName("mypost_mypost2btn")
        self.mypost_mypost2btn.clicked.connect(lambda: mypostfromdata2())
        
        #mypost-mypost3btn
        self.mypost_mypost3btn = QtWidgets.QPushButton(self.mypostscreen)
        self.mypost_mypost3btn.setGeometry(QtCore.QRect(323, 120, 162, 162))
        self.mypost_mypost3btn.setStyleSheet("background:transparent")
        self.mypost_mypost3btn.setText("")
        self.mypost_mypost3btn.setObjectName("mypost_mypost3btn")
        self.mypost_mypost3btn.clicked.connect(lambda: mypostfromdata3())
        
        #mypost-mypost4btn
        self.mypost_mypost4btn = QtWidgets.QPushButton(self.mypostscreen)
        self.mypost_mypost4btn.setGeometry(QtCore.QRect(482, 120, 162, 162))
        self.mypost_mypost4btn.setStyleSheet("background:transparent")
        self.mypost_mypost4btn.setText("")
        self.mypost_mypost4btn.setObjectName("mypost_mypost4btn")
        self.mypost_mypost4btn.clicked.connect(lambda: mypostfromdata4())
        
        #mypost-mypost5btn
        self.mypost_mypost5btn = QtWidgets.QPushButton(self.mypostscreen)
        self.mypost_mypost5btn.setGeometry(QtCore.QRect(641, 120, 162, 162))
        self.mypost_mypost5btn.setStyleSheet("background:transparent")
        self.mypost_mypost5btn.setText("")
        self.mypost_mypost5btn.setObjectName("mypost_mypost5btn")
        self.mypost_mypost5btn.clicked.connect(lambda: mypostfromdata5())
              
        #mypost-mypost6btn
        self.mypost_mypost6btn = QtWidgets.QPushButton(self.mypostscreen)
        self.mypost_mypost6btn.setGeometry(QtCore.QRect(5, 280, 162, 162))
        self.mypost_mypost6btn.setStyleSheet("background:transparent")
        self.mypost_mypost6btn.setText("")
        self.mypost_mypost6btn.setObjectName("mypost_mypost6btn")
        self.mypost_mypost6btn.clicked.connect(lambda: mypostfromdata6())
              
        #mypost-mypost7btn
        self.mypost_mypost7btn = QtWidgets.QPushButton(self.mypostscreen)
        self.mypost_mypost7btn.setGeometry(QtCore.QRect(164, 280, 162, 162))
        self.mypost_mypost7btn.setStyleSheet("background:transparent")
        self.mypost_mypost7btn.setText("")
        self.mypost_mypost7btn.setObjectName("mypost_mypost7btn")
        self.mypost_mypost7btn.clicked.connect(lambda: mypostfromdata7())
        
        #mypost-mypost8btn
        self.mypost_mypost8btn = QtWidgets.QPushButton(self.mypostscreen)
        self.mypost_mypost8btn.setGeometry(QtCore.QRect(323, 280, 162, 162))
        self.mypost_mypost8btn.setStyleSheet("background:transparent")
        self.mypost_mypost8btn.setText("")
        self.mypost_mypost8btn.setObjectName("mypost_mypost8")
        self.mypost_mypost8btn.clicked.connect(lambda: mypostfromdata8())
        
        #mypost-mypost9btn
        self.mypost_mypost9btn = QtWidgets.QPushButton(self.mypostscreen)
        self.mypost_mypost9btn.setGeometry(QtCore.QRect(482, 280, 162, 162))
        self.mypost_mypost9btn.setStyleSheet("background:transparent")
        self.mypost_mypost9btn.setText("")
        self.mypost_mypost9btn.setObjectName("mypost_mypost9btn")
        self.mypost_mypost9btn.clicked.connect(lambda: mypostfromdata9())
        
        #mypost-mypost10btn
        self.mypost_mypost10btn = QtWidgets.QPushButton(self.mypostscreen)
        self.mypost_mypost10btn.setGeometry(QtCore.QRect(641, 280, 162, 162))
        self.mypost_mypost10btn.setStyleSheet("background:transparent")
        self.mypost_mypost10btn.setText("")
        self.mypost_mypost10btn.setObjectName("mypost_mypost10btn")
        self.mypost_mypost10btn.clicked.connect(lambda: mypostfromdata10())
        

        #mypost- Next Button
        self.mypost_next = QtWidgets.QPushButton(self.mypostscreen)
        self.mypost_next.setGeometry(QtCore.QRect(730, 448, 71, 28))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.mypost_next.setFont(font)
        self.mypost_next.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.mypost_next.setObjectName("mypost_next")
        self.mypost_next.clicked.connect(lambda: next_myposts())
        #mypost- PAGE NO.
        self.mypost_page = QtWidgets.QLabel(self.mypostscreen)
        self.mypost_page.setGeometry(QtCore.QRect(320, 440, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.mypost_page.setFont(font)
        self.mypost_page.setStyleSheet("background:transparent;")
        self.mypost_page.setScaledContents(True)
        self.mypost_page.setObjectName("mypost_page")


        #mypost- Back Button
        self.mypost_back = QtWidgets.QPushButton(self.mypostscreen)
        self.mypost_back.setGeometry(QtCore.QRect(10, 448, 71, 28))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.mypost_back.setFont(font)
        self.mypost_back.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.mypost_back.setObjectName("mypost_back")
        self.mypost_back.clicked.connect(lambda: back_myposts())
        #TaskBar  
        self.TB = QtWidgets.QLabel(self.mypostscreen)
        self.TB.setGeometry(QtCore.QRect(-40, 480, 861, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.TB.setFont(font)
        self.TB.setStyleSheet("background:rgb(36, 36, 36);")
        self.TB.setScaledContents(True)
        self.TB.setObjectName("TB")



        
        self.TB_Home = QtWidgets.QPushButton(self.mypostscreen)
        self.TB_Home.setGeometry(QtCore.QRect(10, 490, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.TB_Home.setFont(font)
        self.TB_Home.setStyleSheet("QPushButton{background-color:rgb(50, 50, 50);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.TB_Home.setObjectName("TB_Home")
        self.TB_Home.clicked.connect(lambda: setscreen_feed())

        
        self.TB_Search = QtWidgets.QPushButton(self.mypostscreen)
        self.TB_Search.setGeometry(QtCore.QRect(170, 490, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.TB_Search.setFont(font)
        self.TB_Search.setStyleSheet("QPushButton{background-color:rgb(50, 50, 50);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.TB_Search.setObjectName("TB_Search")
        self.TB_Search.clicked.connect(lambda: setscreen_search())


        
        self.TB_Profile = QtWidgets.QPushButton(self.mypostscreen)
        self.TB_Profile.setGeometry(QtCore.QRect(490, 490, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.TB_Profile.setFont(font)
        self.TB_Profile.setStyleSheet("QPushButton{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.TB_Profile.setObjectName("TB_Profile")
        self.TB_Profile.clicked.connect(lambda: setscreen_profilemain())

        
        self.TB_Timeline = QtWidgets.QPushButton(self.mypostscreen)
        self.TB_Timeline.setGeometry(QtCore.QRect(330, 490, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.TB_Timeline.setFont(font)
        self.TB_Timeline.setStyleSheet("QPushButton{background-color:rgb(50, 50, 50);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.TB_Timeline.setObjectName("TB_Timeline")
        #self.TB_Timeline.clicked.connect(lambda: timelinescreen())


        
        self.TB_Settings = QtWidgets.QPushButton(self.mypostscreen)
        self.TB_Settings.setGeometry(QtCore.QRect(650, 490, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.TB_Settings.setFont(font)
        self.TB_Settings.setStyleSheet("QPushButton{background-color:rgb(50, 50, 50);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.TB_Settings.setObjectName("TB_Settings")
        #self.TB_Timeline.clicked.connect(lambda: settingscreen())




        #Translates Texts
        self.mypost_textlogo.setText(_translate("MainWindow", " SuperInsta"))
        self.mypost_signout.setText(_translate("MainWindow", "Sign Out"))
        self.mypost_username.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">@username</span></p></body></html>"))
        self.TB_Home.setText(_translate("MainWindow", "Home"))
        self.TB_Search.setText(_translate("MainWindow", "Search"))
        self.TB_Profile.setText(_translate("MainWindow", "Your Profile"))
        self.TB_Timeline.setText(_translate("MainWindow", "Timeline"))
        self.TB_Settings.setText(_translate("MainWindow", "SuperInsta"))
        self.mypost_close.setText(_translate("MainWindow", "x"))
        self.mypost_next.setText(_translate("MainWindow", ">"))
        self.mypost_page.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Page 1</span></p></body></html>"))
        self.mypost_back.setText(_translate("MainWindow", "<"))

        
########################################### OnePost Screen ################################################

        #One Post Screen
        self.onepostscreen = QtWidgets.QWidget(MainWindow)
        self.onepostscreen.setObjectName("onepostscreen")

        #One Post Logo
        self.onepost_logo = QtWidgets.QLabel(self.onepostscreen)
        self.onepost_logo.setGeometry(QtCore.QRect(10, 10, 41, 41))
        self.onepost_logo.setText("")
        self.onepost_logo.setPixmap(QtGui.QPixmap(":/elem/logo.png"))
        self.onepost_logo.setScaledContents(True)
        self.onepost_logo.setObjectName("onepost_logo")


        #Text Logo
        self.onepost_textlogo = QtWidgets.QLabel(self.onepostscreen)
        self.onepost_textlogo.setGeometry(QtCore.QRect(50, 10, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Billabong")
        font.setPointSize(41)
        self.onepost_textlogo.setFont(font)
        self.onepost_textlogo.setStyleSheet("background:transparent;")
        self.onepost_textlogo.setScaledContents(True)
        self.onepost_textlogo.setObjectName("onepost_textlogo")

        #Signout                  
        self.onepost_signout = QtWidgets.QPushButton(self.onepostscreen)
        self.onepost_signout.setGeometry(QtCore.QRect(680, 10, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.onepost_signout.setFont(font)
        self.onepost_signout.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-radius:15px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));color:rgb(255, 142, 231);}")
        self.onepost_signout.setObjectName("onepost_signout")
        self.onepost_signout.clicked.connect(lambda:logout_instagram())


        #Username
        self.onepost_username = QtWidgets.QLabel(self.onepostscreen)
        self.onepost_username.setGeometry(QtCore.QRect(60, 70, 731, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.onepost_username.setFont(font)
        self.onepost_username.setStyleSheet("QLabel{background-color:rgb(26, 26, 26);border-radius:9px;color:white;}")
        self.onepost_username.setScaledContents(True)
        self.onepost_username.setObjectName("onepost_username")


        #CloseButton
        self.onepost_close = QtWidgets.QPushButton(self.onepostscreen)
        self.onepost_close.setGeometry(QtCore.QRect(10, 70, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.onepost_close.setFont(font)
        self.onepost_close.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.onepost_close.setObjectName("onepost_close")
        self.onepost_close.clicked.connect(lambda: onepost_close())
        
        
        #Image Background
        self.onepost_image_bg = QtWidgets.QLabel(self.onepostscreen)
        self.onepost_image_bg.setGeometry(QtCore.QRect(10, 120, 331, 331))
        self.onepost_image_bg.setStyleSheet("border:3px solid rgb(29, 29, 29);")
        self.onepost_image_bg.setText("")
        self.onepost_image_bg.setScaledContents(True)
        self.onepost_image_bg.setObjectName("onepost_image_bg")
        
        #Image
        self.onepost_image = QtWidgets.QLabel(self.onepostscreen)
        self.onepost_image.setGeometry(QtCore.QRect(10, 120, 331, 331))
        self.onepost_image.setStyleSheet("border:3px solid rgb(29, 29, 29);")
        self.onepost_image.setText("")
        self.onepost_image.setScaledContents(True)
        self.onepost_image.setObjectName("onepost_image")


        #Background for OPtions
        self.onepost_toolcase = QtWidgets.QLabel(self.onepostscreen)
        self.onepost_toolcase.setGeometry(QtCore.QRect(350, 390, 441, 61))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.onepost_toolcase.setFont(font)
        self.onepost_toolcase.setStyleSheet("QLabel{background-color:rgb(26, 26, 26);border-radius:9px;color:white;}")
        self.onepost_toolcase.setScaledContents(True)
        self.onepost_toolcase.setObjectName("onepost_toolcase")

        #Like Button
        self.onepost_like = QtWidgets.QLabel(self.onepostscreen)
        self.onepost_like.setGeometry(QtCore.QRect(370, 400, 44, 40))
        self.onepost_like.setStyleSheet("background:transparent;")
        self.onepost_like.setText("")
        self.onepost_like.setPixmap(QtGui.QPixmap(":/elem/unlike.png"))
        self.onepost_like.setScaledContents(True)
        self.onepost_like.setObjectName("onepost_like")

        self.onepost_view = QtWidgets.QLabel(self.onepostscreen)
        self.onepost_view.setGeometry(QtCore.QRect(135, 234, 100, 100))
        self.onepost_view.setStyleSheet("background:transparent;")
        self.onepost_view.setText("")
        self.onepost_view.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
        self.onepost_view.setScaledContents(True)
        self.onepost_view.setObjectName("onepost_like")

        self.onepost_view_btn = QtWidgets.QPushButton(self.onepostscreen)
        self.onepost_view_btn.setGeometry(QtCore.QRect(135, 234, 100, 100))
        self.onepost_view_btn.setStyleSheet("background:transparent;")
        self.onepost_view_btn.clicked.connect(lambda: view_video())





        self.onepost_like_btn = QtWidgets.QPushButton(self.onepostscreen)
        self.onepost_like_btn.setGeometry(QtCore.QRect(370, 400, 44, 40))
        self.onepost_like_btn.setStyleSheet("background:transparent;")
        self.onepost_like_btn.clicked.connect(lambda:like_media())
        
        #Save Button
        self.onepost_save = QtWidgets.QLabel(self.onepostscreen)
        self.onepost_save.setGeometry(QtCore.QRect(500, 401, 28, 40))
        self.onepost_save.setStyleSheet("background:transparent;")
        self.onepost_save.setText("")
        self.onepost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
        self.onepost_save.setScaledContents(True)
        self.onepost_save.setObjectName("onepost_save")

        self.onepost_save_btn = QtWidgets.QPushButton(self.onepostscreen)
        self.onepost_save_btn.setGeometry(QtCore.QRect(500, 401, 28, 40))
        self.onepost_save_btn.setStyleSheet("background:transparent;")
        self.onepost_save_btn.clicked.connect(lambda:save_media())

        #Comment Button
        self.onepost_comment = QtWidgets.QLabel(self.onepostscreen)
        self.onepost_comment.setGeometry(QtCore.QRect(430, 400, 42, 41))
        self.onepost_comment.setStyleSheet("background:transparent;")
        self.onepost_comment.setText("")
        self.onepost_comment.setPixmap(QtGui.QPixmap(":/elem/comment.png"))
        self.onepost_comment.setScaledContents(True)
        self.onepost_comment.setObjectName("onepost_comment")

        self.onepost_comment_btn = QtWidgets.QPushButton(self.onepostscreen)
        self.onepost_comment_btn.setGeometry(QtCore.QRect(430, 400, 42, 41))
        self.onepost_comment_btn.setStyleSheet("background:transparent;")

        
        #Copy Hashtag Button
        self.onepost_copyhash = QtWidgets.QLabel(self.onepostscreen)
        self.onepost_copyhash.setGeometry(QtCore.QRect(550, 400, 37, 45))
        self.onepost_copyhash.setStyleSheet("background:transparent;")
        self.onepost_copyhash.setText("")
        self.onepost_copyhash.setPixmap(QtGui.QPixmap(":/elem/uncopy.png"))
        self.onepost_copyhash.setScaledContents(True)
        self.onepost_copyhash.setObjectName("onepost_copyhash")
        
        self.onepost_copyhash_btn = QtWidgets.QPushButton(self.onepostscreen)
        self.onepost_copyhash_btn.setGeometry(QtCore.QRect(550, 400, 37, 45))
        self.onepost_copyhash_btn.setStyleSheet("background:transparent;")
        self.onepost_copyhash_btn.clicked.connect(lambda: copyhashtag())

        #Traslate Caption Button
        self.onepost_translate = QtWidgets.QLabel(self.onepostscreen)
        self.onepost_translate.setGeometry(QtCore.QRect(610, 400, 41, 41))
        self.onepost_translate.setStyleSheet("background:transparent;")
        self.onepost_translate.setText("")
        self.onepost_translate.setPixmap(QtGui.QPixmap(":/elem/untranslate.png"))
        self.onepost_translate.setScaledContents(True)
        self.onepost_translate.setObjectName("onepost_translate")
        
        
        self.onepost_translate_btn = QtWidgets.QPushButton(self.onepostscreen)
        self.onepost_translate_btn.setGeometry(QtCore.QRect(610, 400, 41, 41))
        self.onepost_translate_btn.setStyleSheet("background:transparent;")
        self.onepost_translate_btn.clicked.connect(lambda: translate_eng())

        #Download Post Button
        self.onepost_download = QtWidgets.QLabel(self.onepostscreen)
        self.onepost_download.setGeometry(QtCore.QRect(670, 400, 37, 41))
        self.onepost_download.setStyleSheet("background:transparent;")
        self.onepost_download.setText("")
        self.onepost_download.setPixmap(QtGui.QPixmap(":/elem/download.png"))
        self.onepost_download.setScaledContents(True)
        self.onepost_download.setObjectName("onepost_download")

        self.onepost_download_btn = QtWidgets.QPushButton(self.onepostscreen)
        self.onepost_download_btn.setGeometry(QtCore.QRect(670, 400, 37, 41))
        self.onepost_download_btn.setStyleSheet("background:transparent;")
        self.onepost_download_btn.clicked.connect(lambda:download_media())


        #Caption Bg
        self.onepost_caption_2 = QtWidgets.QLabel(self.onepostscreen)
        self.onepost_caption_2.setGeometry(QtCore.QRect(350, 120, 439, 165))
        self.onepost_caption_2.setMaximumSize(QtCore.QSize(440, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.onepost_caption_2.setFont(font)
        self.onepost_caption_2.setStyleSheet("QLabel{background-color:rgb(26, 26, 26);border-radius:9px;color:white;padding:10px; padding-bottom:30px}")
        self.onepost_caption_2.setScaledContents(True)
        self.onepost_caption_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.onepost_caption_2.setWordWrap(True)
        self.onepost_caption_2.setObjectName("onepost_caption_2")
        #Caption
        self.onepost_edit = QtWidgets.QLabel(self.onepostscreen)
        self.onepost_edit.setGeometry(QtCore.QRect(360, 260, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.onepost_edit.setFont(font)
        self.onepost_edit.setStyleSheet("background:transparent;")
        self.onepost_edit.setScaledContents(True)
        self.onepost_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.onepost_edit.setWordWrap(True)
        self.onepost_edit.setObjectName("onepost_edit")
        self.onepost_date = QtWidgets.QLabel(self.onepostscreen)
        self.onepost_date.setGeometry(QtCore.QRect(534, 260, 231, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.onepost_date.setFont(font)
        self.onepost_date.setStyleSheet("background:transparent;")
        self.onepost_date.setScaledContents(True)
        self.onepost_date.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.onepost_date.setWordWrap(True)
        self.onepost_date.setObjectName("onepost_date")
        self.caption_scrollarea = QtWidgets.QScrollArea(self.onepostscreen)
        self.caption_scrollarea.setGeometry(QtCore.QRect(350, 120, 434, 130))#191
        self.caption_scrollarea.setStyleSheet("background:transparent")
        self.caption_scrollarea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.caption_scrollarea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.caption_scrollarea.setLineWidth(0)
        self.caption_scrollarea.setWidgetResizable(True)
        self.caption_scrollarea.setObjectName("caption_scrollarea")
        self.caption_scrollcontent = QtWidgets.QWidget()
        self.caption_scrollcontent.setGeometry(QtCore.QRect(0, 0, 418, 260))
        self.caption_scrollcontent.setObjectName("caption_scrollcontent")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.caption_scrollcontent)
        self.verticalLayout.setObjectName("verticalLayout")
        self.onepost_caption = QtWidgets.QLabel(self.caption_scrollcontent)
        self.onepost_caption.setMaximumSize(QtCore.QSize(440, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.onepost_caption.setFont(font)
        self.onepost_caption.setStyleSheet("QLabel{background-color:transparent;border-radius:9px;color:white;padding:3px}")
        self.onepost_caption.setScaledContents(True)
        self.onepost_caption.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.onepost_caption.setWordWrap(True)
        self.onepost_caption.setObjectName("onepost_caption")
        self.verticalLayout.addWidget(self.onepost_caption)
        self.caption_scrollarea.setWidget(self.caption_scrollcontent)
        self.scrolllbar = QtWidgets.QScrollBar(self.searchscreen)
        self.scrolllbar.setStyleSheet("QScrollBar:vertical{border: none;background: rgb(45,45,45);width: 10px;margin: 0px 0 0px 0;}QScrollBar::handle:vertical{background: dark grey;min-height: 26px;border-radius: 5px;}QScrollBar::add-line:vertical{background: none;height: 26px;subcontrol-position: bottom;subcontrol-origin: margin;}QScrollBar::sub-line:vertical{background: none;height: 0px;subcontrol-position: top left;subcontrol-origin: margin;position: absolute;}QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical{background: rgb(45,45,45);}")
        self.caption_scrollarea.setVerticalScrollBar(self.scrolllbar)

        #likedby_bg Bg
        self.likedby_bg = QtWidgets.QLabel(self.onepostscreen)
        self.likedby_bg.setGeometry(QtCore.QRect(350, 291, 439, 48))
        self.likedby_bg.setMaximumSize(QtCore.QSize(440, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.likedby_bg.setFont(font)
        self.likedby_bg.setStyleSheet("QLabel{background-color:rgb(26, 26, 26);border-radius:9px;color:white;padding:10px; padding-bottom:30px}")
        self.likedby_bg.setScaledContents(True)
        self.likedby_bg.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.likedby_bg.setWordWrap(True)
        self.likedby_bg.setObjectName("likedby_bg")


        self.onepost_lb_caption = QtWidgets.QLabel(self.onepostscreen)
        self.onepost_lb_caption.setGeometry(QtCore.QRect(350, 297, 439, 40))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        self.onepost_lb_caption.setFont(font)
        self.onepost_lb_caption.setStyleSheet("background:transparent;padding-left:6px;padding-right:6px")
        self.onepost_lb_caption.setScaledContents(True)
        self.onepost_lb_caption.setWordWrap(True)
        self.onepost_lb_caption.setObjectName("onepost_date")











        #Like Count
        self.onepost_likecount = QtWidgets.QLabel(self.onepostscreen)
        self.onepost_likecount.setGeometry(QtCore.QRect(350, 350, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.onepost_likecount.setFont(font)
        self.onepost_likecount.setStyleSheet("QLabel{background-color:rgb(26, 26, 26);border-radius:5px;color:white;}")
        self.onepost_likecount.setScaledContents(True)
        self.onepost_likecount.setAlignment(QtCore.Qt.AlignCenter)
        self.onepost_likecount.setWordWrap(True)
        self.onepost_likecount.setObjectName("onepost_likecount")

        #Comment Count
        self.onepost_commentcount = QtWidgets.QLabel(self.onepostscreen)
        self.onepost_commentcount.setGeometry(QtCore.QRect(570, 350, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.onepost_commentcount.setFont(font)
        self.onepost_commentcount.setStyleSheet("QLabel{background-color:rgb(26, 26, 26);border-radius:5px;color:white;}")
        self.onepost_commentcount.setScaledContents(True)
        self.onepost_commentcount.setAlignment(QtCore.Qt.AlignCenter)
        self.onepost_commentcount.setWordWrap(True)
        self.onepost_commentcount.setObjectName("onepost_commentcount")


        #Corousell Post Count
        self.onepost_postcount = QtWidgets.QLabel(self.onepostscreen)
        self.onepost_postcount.setGeometry(QtCore.QRect(228, 134, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.onepost_postcount.setFont(font)
        self.onepost_postcount.setStyleSheet("QLabel{background-color:rgb(88, 88, 88);border-radius:9px;color:white;}")
        self.onepost_postcount.setScaledContents(True)
        self.onepost_postcount.setAlignment(QtCore.Qt.AlignCenter)
        self.onepost_postcount.setWordWrap(True)
        self.onepost_postcount.setObjectName("onepost_postcount")


        #Next Button
        self.onepost_next = QtWidgets.QPushButton(self.onepostscreen)
        self.onepost_next.setGeometry(QtCore.QRect(290, 400, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.onepost_next.setFont(font)
        self.onepost_next.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.onepost_next.setObjectName("onepost_next")
        self.onepost_next.clicked.connect(lambda:next_corousell())

        #Back Button
        self.onepost_back = QtWidgets.QPushButton(self.onepostscreen)
        self.onepost_back.setGeometry(QtCore.QRect(20, 400, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.onepost_back.setFont(font)
        self.onepost_back.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.onepost_back.setObjectName("onepost_back")
        self.onepost_back.clicked.connect(lambda:back_corousell())


        
        #TaskBar  
        self.TB = QtWidgets.QLabel(self.onepostscreen)
        self.TB.setGeometry(QtCore.QRect(-40, 480, 861, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.TB.setFont(font)
        self.TB.setStyleSheet("background:rgb(36, 36, 36);")
        self.TB.setScaledContents(True)
        self.TB.setObjectName("TB")



        
        self.TB_Home = QtWidgets.QPushButton(self.onepostscreen)
        self.TB_Home.setGeometry(QtCore.QRect(10, 490, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.TB_Home.setFont(font)
        self.TB_Home.setStyleSheet("QPushButton{background-color:rgb(50, 50, 50);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.TB_Home.setObjectName("TB_Home")
        self.TB_Home.clicked.connect(lambda: setscreen_feed())

        
        self.TB_Search = QtWidgets.QPushButton(self.onepostscreen)
        self.TB_Search.setGeometry(QtCore.QRect(170, 490, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.TB_Search.setFont(font)
        self.TB_Search.setStyleSheet("QPushButton{background-color:rgb(50, 50, 50);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.TB_Search.setObjectName("TB_Search")
        self.TB_Search.clicked.connect(lambda: setscreen_searchmain())
        self.TB_Search.setStyleSheet("QPushButton{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")


        
        self.TB_Profile = QtWidgets.QPushButton(self.onepostscreen)
        self.TB_Profile.setGeometry(QtCore.QRect(490, 490, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.TB_Profile.setFont(font)
        self.TB_Profile.setStyleSheet("QPushButton{background-color:rgb(50, 50, 50);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.TB_Profile.setObjectName("TB_Profile")
        self.TB_Profile.clicked.connect(lambda: setscreen_profile())

        
        self.TB_Timeline = QtWidgets.QPushButton(self.onepostscreen)
        self.TB_Timeline.setGeometry(QtCore.QRect(330, 490, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.TB_Timeline.setFont(font)
        self.TB_Timeline.setStyleSheet("QPushButton{background-color:rgb(50, 50, 50);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.TB_Timeline.setObjectName("TB_Timeline")
        #self.TB_Timeline.clicked.connect(lambda: timelinescreen())


        
        self.TB_Settings = QtWidgets.QPushButton(self.onepostscreen)
        self.TB_Settings.setGeometry(QtCore.QRect(650, 490, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.TB_Settings.setFont(font)
        self.TB_Settings.setStyleSheet("QPushButton{background-color:rgb(50, 50, 50);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.TB_Settings.setObjectName("TB_Settings")
        #self.TB_Timeline.clicked.connect(lambda: settingscreen())


        self.onepost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\">Edited</span></p></body></html>"))
        self.onepost_textlogo.setText(_translate("MainWindow", " SuperInsta"))
        self.onepost_signout.setText(_translate("MainWindow", "Sign Out"))
        self.onepost_username.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">@username  - Location, Location</span></p></body></html>"))
        self.onepost_close.setText(_translate("MainWindow", "x"))
        self.onepost_toolcase.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.onepost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#f1f1f1;\">Caption Here.</span></p></body></html>"))
        self.onepost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by @mostuselessboy1hfk35hch4h1h2b2h, @mostuselessboy1hfk35hch4h1h2b2h and 1,342 others. </span></p></body></html>"))
        self.onepost_likecount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Likes: 1,234</span></p></body></html>"))
        self.onepost_commentcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Comments: 234</span></p></body></html>"))
        self.onepost_postcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Post 10/10</span></p></body></html>"))
        self.onepost_next.setText(_translate("MainWindow", ">"))
        self.onepost_back.setText(_translate("MainWindow", "<"))
        self.onepost_date.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" color:#919191;\">24 May 2020</span></p></body></html>"))
        self.TB_Home.setText(_translate("MainWindow", "Home"))
        self.TB_Search.setText(_translate("MainWindow", "Search"))
        self.TB_Profile.setText(_translate("MainWindow", "Your Profile"))
        self.TB_Timeline.setText(_translate("MainWindow", "Timeline"))
        self.TB_Settings.setText(_translate("MainWindow", "SuperInsta"))


########################################### Onemypost Screen ################################################

        #One mypost Screen
        self.onemypostscreen = QtWidgets.QWidget(MainWindow)
        self.onemypostscreen.setObjectName("onemypostscreen")

        #One mypost Logo
        self.onemypost_logo = QtWidgets.QLabel(self.onemypostscreen)
        self.onemypost_logo.setGeometry(QtCore.QRect(10, 10, 41, 41))
        self.onemypost_logo.setText("")
        self.onemypost_logo.setPixmap(QtGui.QPixmap(":/elem/logo.png"))
        self.onemypost_logo.setScaledContents(True)
        self.onemypost_logo.setObjectName("onemypost_logo")


        #Text Logo
        self.onemypost_textlogo = QtWidgets.QLabel(self.onemypostscreen)
        self.onemypost_textlogo.setGeometry(QtCore.QRect(50, 10, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Billabong")
        font.setPointSize(41)
        self.onemypost_textlogo.setFont(font)
        self.onemypost_textlogo.setStyleSheet("background:transparent;")
        self.onemypost_textlogo.setScaledContents(True)
        self.onemypost_textlogo.setObjectName("onemypost_textlogo")

        #Signout                  
        self.onemypost_signout = QtWidgets.QPushButton(self.onemypostscreen)
        self.onemypost_signout.setGeometry(QtCore.QRect(680, 10, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.onemypost_signout.setFont(font)
        self.onemypost_signout.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-radius:15px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));color:rgb(255, 142, 231);}")
        self.onemypost_signout.setObjectName("onemypost_signout")
        self.onemypost_signout.clicked.connect(lambda:logout_instagram())

        #Username
        self.onemypost_username = QtWidgets.QLabel(self.onemypostscreen)
        self.onemypost_username.setGeometry(QtCore.QRect(60, 70, 731, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.onemypost_username.setFont(font)
        self.onemypost_username.setStyleSheet("QLabel{background-color:rgb(26, 26, 26);border-radius:9px;color:white;}")
        self.onemypost_username.setScaledContents(True)
        self.onemypost_username.setObjectName("onemypost_username")


        #CloseButton
        self.onemypost_close = QtWidgets.QPushButton(self.onemypostscreen)
        self.onemypost_close.setGeometry(QtCore.QRect(10, 70, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.onemypost_close.setFont(font)
        self.onemypost_close.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.onemypost_close.setObjectName("onemypost_close")
        self.onemypost_close.clicked.connect(lambda: onemypost_close())
        
        
        #Image Background
        self.onemypost_image_bg = QtWidgets.QLabel(self.onemypostscreen)
        self.onemypost_image_bg.setGeometry(QtCore.QRect(10, 120, 331, 331))
        self.onemypost_image_bg.setStyleSheet("border:3px solid rgb(29, 29, 29);")
        self.onemypost_image_bg.setText("")
        self.onemypost_image_bg.setScaledContents(True)
        self.onemypost_image_bg.setObjectName("onemypost_image_bg")
        
        #Image
        self.onemypost_image = QtWidgets.QLabel(self.onemypostscreen)
        self.onemypost_image.setGeometry(QtCore.QRect(10, 120, 331, 331))
        self.onemypost_image.setStyleSheet("border:3px solid rgb(29, 29, 29);")
        self.onemypost_image.setText("")
        self.onemypost_image.setScaledContents(True)
        self.onemypost_image.setObjectName("onemypost_image")


        #Background for OPtions
        self.onemypost_toolcase = QtWidgets.QLabel(self.onemypostscreen)
        self.onemypost_toolcase.setGeometry(QtCore.QRect(350, 390, 441, 61))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.onemypost_toolcase.setFont(font)
        self.onemypost_toolcase.setStyleSheet("QLabel{background-color:rgb(26, 26, 26);border-radius:9px;color:white;}")
        self.onemypost_toolcase.setScaledContents(True)
        self.onemypost_toolcase.setObjectName("onemypost_toolcase")

        #Like Button
        self.onemypost_like = QtWidgets.QLabel(self.onemypostscreen)
        self.onemypost_like.setGeometry(QtCore.QRect(370, 400, 44, 40))
        self.onemypost_like.setStyleSheet("background:transparent;")
        self.onemypost_like.setText("")
        self.onemypost_like.setPixmap(QtGui.QPixmap(":/elem/unlike.png"))
        self.onemypost_like.setScaledContents(True)
        self.onemypost_like.setObjectName("onemypost_like")

        self.onemypost_view = QtWidgets.QLabel(self.onemypostscreen)
        self.onemypost_view.setGeometry(QtCore.QRect(135, 234, 100, 100))
        self.onemypost_view.setStyleSheet("background:transparent;")
        self.onemypost_view.setText("")
        self.onemypost_view.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
        self.onemypost_view.setScaledContents(True)
        self.onemypost_view.setObjectName("onemypost_like")

        self.onemypost_view_btn = QtWidgets.QPushButton(self.onemypostscreen)
        self.onemypost_view_btn.setGeometry(QtCore.QRect(135, 234, 100, 100))
        self.onemypost_view_btn.setStyleSheet("background:transparent;")
        self.onemypost_view_btn.clicked.connect(lambda: myview_video())





        self.onemypost_like_btn = QtWidgets.QPushButton(self.onemypostscreen)
        self.onemypost_like_btn.setGeometry(QtCore.QRect(370, 400, 44, 40))
        self.onemypost_like_btn.setStyleSheet("background:transparent;")
        self.onemypost_like_btn.clicked.connect(lambda:mylike_media())
        
        #Save Button
        self.onemypost_save = QtWidgets.QLabel(self.onemypostscreen)
        self.onemypost_save.setGeometry(QtCore.QRect(500, 401, 28, 40))
        self.onemypost_save.setStyleSheet("background:transparent;")
        self.onemypost_save.setText("")
        self.onemypost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
        self.onemypost_save.setScaledContents(True)
        self.onemypost_save.setObjectName("onemypost_save")

        self.onemypost_save_btn = QtWidgets.QPushButton(self.onemypostscreen)
        self.onemypost_save_btn.setGeometry(QtCore.QRect(500, 401, 28, 40))
        self.onemypost_save_btn.setStyleSheet("background:transparent;")
        self.onemypost_save_btn.clicked.connect(lambda:mysave_media())

        #Comment Button
        self.onemypost_comment = QtWidgets.QLabel(self.onemypostscreen)
        self.onemypost_comment.setGeometry(QtCore.QRect(430, 400, 42, 41))
        self.onemypost_comment.setStyleSheet("background:transparent;")
        self.onemypost_comment.setText("")
        self.onemypost_comment.setPixmap(QtGui.QPixmap(":/elem/comment.png"))
        self.onemypost_comment.setScaledContents(True)
        self.onemypost_comment.setObjectName("onemypost_comment")

        self.onemypost_comment_btn = QtWidgets.QPushButton(self.onemypostscreen)
        self.onemypost_comment_btn.setGeometry(QtCore.QRect(430, 400, 42, 41))
        self.onemypost_comment_btn.setStyleSheet("background:transparent;")

        
        #Copy Hashtag Button
        self.onemypost_copyhash = QtWidgets.QLabel(self.onemypostscreen)
        self.onemypost_copyhash.setGeometry(QtCore.QRect(550, 400, 37, 45))
        self.onemypost_copyhash.setStyleSheet("background:transparent;")
        self.onemypost_copyhash.setText("")
        self.onemypost_copyhash.setPixmap(QtGui.QPixmap(":/elem/uncopy.png"))
        self.onemypost_copyhash.setScaledContents(True)
        self.onemypost_copyhash.setObjectName("onemypost_copyhash")
        
        self.onemypost_copyhash_btn = QtWidgets.QPushButton(self.onemypostscreen)
        self.onemypost_copyhash_btn.setGeometry(QtCore.QRect(550, 400, 37, 45))
        self.onemypost_copyhash_btn.setStyleSheet("background:transparent;")
        self.onemypost_copyhash_btn.clicked.connect(lambda: mycopyhashtag())

        #Traslate Caption Button
        self.onemypost_translate = QtWidgets.QLabel(self.onemypostscreen)
        self.onemypost_translate.setGeometry(QtCore.QRect(610, 400, 41, 41))
        self.onemypost_translate.setStyleSheet("background:transparent;")
        self.onemypost_translate.setText("")
        self.onemypost_translate.setPixmap(QtGui.QPixmap(":/elem/untranslate.png"))
        self.onemypost_translate.setScaledContents(True)
        self.onemypost_translate.setObjectName("onemypost_translate")
        
        
        self.onemypost_translate_btn = QtWidgets.QPushButton(self.onemypostscreen)
        self.onemypost_translate_btn.setGeometry(QtCore.QRect(610, 400, 41, 41))
        self.onemypost_translate_btn.setStyleSheet("background:transparent;")
        self.onemypost_translate_btn.clicked.connect(lambda: mytranslate_eng())

        #Download mypost Button
        self.onemypost_download = QtWidgets.QLabel(self.onemypostscreen)
        self.onemypost_download.setGeometry(QtCore.QRect(670, 400, 37, 41))
        self.onemypost_download.setStyleSheet("background:transparent;")
        self.onemypost_download.setText("")
        self.onemypost_download.setPixmap(QtGui.QPixmap(":/elem/download.png"))
        self.onemypost_download.setScaledContents(True)
        self.onemypost_download.setObjectName("onemypost_download")

        self.onemypost_download_btn = QtWidgets.QPushButton(self.onemypostscreen)
        self.onemypost_download_btn.setGeometry(QtCore.QRect(670, 400, 37, 41))
        self.onemypost_download_btn.setStyleSheet("background:transparent;")
        self.onemypost_download_btn.clicked.connect(lambda:mydownload_media())


        #Caption Bg
        self.onemypost_caption_2 = QtWidgets.QLabel(self.onemypostscreen)
        self.onemypost_caption_2.setGeometry(QtCore.QRect(350, 120, 439, 165))
        self.onemypost_caption_2.setMaximumSize(QtCore.QSize(440, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.onemypost_caption_2.setFont(font)
        self.onemypost_caption_2.setStyleSheet("QLabel{background-color:rgb(26, 26, 26);border-radius:9px;color:white;padding:10px; padding-bottom:30px}")
        self.onemypost_caption_2.setScaledContents(True)
        self.onemypost_caption_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.onemypost_caption_2.setWordWrap(True)
        self.onemypost_caption_2.setObjectName("onemypost_caption_2")
        #Caption
        self.onemypost_edit = QtWidgets.QLabel(self.onemypostscreen)
        self.onemypost_edit.setGeometry(QtCore.QRect(360, 260, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.onemypost_edit.setFont(font)
        self.onemypost_edit.setStyleSheet("background:transparent;")
        self.onemypost_edit.setScaledContents(True)
        self.onemypost_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.onemypost_edit.setWordWrap(True)
        self.onemypost_edit.setObjectName("onemypost_edit")
        self.onemypost_date = QtWidgets.QLabel(self.onemypostscreen)
        self.onemypost_date.setGeometry(QtCore.QRect(534, 260, 231, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.onemypost_date.setFont(font)
        self.onemypost_date.setStyleSheet("background:transparent;")
        self.onemypost_date.setScaledContents(True)
        self.onemypost_date.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.onemypost_date.setWordWrap(True)
        self.onemypost_date.setObjectName("onemypost_date")
        self.caption_scrollarea = QtWidgets.QScrollArea(self.onemypostscreen)
        self.caption_scrollarea.setGeometry(QtCore.QRect(350, 120, 434, 130))#191
        self.caption_scrollarea.setStyleSheet("background:transparent")
        self.caption_scrollarea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.caption_scrollarea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.caption_scrollarea.setLineWidth(0)
        self.caption_scrollarea.setWidgetResizable(True)
        self.caption_scrollarea.setObjectName("caption_scrollarea")
        self.caption_scrollcontent = QtWidgets.QWidget()
        self.caption_scrollcontent.setGeometry(QtCore.QRect(0, 0, 418, 260))
        self.caption_scrollcontent.setObjectName("caption_scrollcontent")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.caption_scrollcontent)
        self.verticalLayout.setObjectName("verticalLayout")
        self.onemypost_caption = QtWidgets.QLabel(self.caption_scrollcontent)
        self.onemypost_caption.setMaximumSize(QtCore.QSize(440, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.onemypost_caption.setFont(font)
        self.onemypost_caption.setStyleSheet("QLabel{background-color:transparent;border-radius:9px;color:white;padding:3px}")
        self.onemypost_caption.setScaledContents(True)
        self.onemypost_caption.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.onemypost_caption.setWordWrap(True)
        self.onemypost_caption.setObjectName("onemypost_caption")
        self.verticalLayout.addWidget(self.onemypost_caption)
        self.caption_scrollarea.setWidget(self.caption_scrollcontent)
        self.scrolllbar = QtWidgets.QScrollBar(self.searchscreen)
        self.scrolllbar.setStyleSheet("QScrollBar:vertical{border: none;background: rgb(45,45,45);width: 10px;margin: 0px 0 0px 0;}QScrollBar::handle:vertical{background: dark grey;min-height: 26px;border-radius: 5px;}QScrollBar::add-line:vertical{background: none;height: 26px;subcontrol-position: bottom;subcontrol-origin: margin;}QScrollBar::sub-line:vertical{background: none;height: 0px;subcontrol-position: top left;subcontrol-origin: margin;position: absolute;}QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical{background: rgb(45,45,45);}")
        self.caption_scrollarea.setVerticalScrollBar(self.scrolllbar)

        #likedby_bg Bg
        self.likedby_bg = QtWidgets.QLabel(self.onemypostscreen)
        self.likedby_bg.setGeometry(QtCore.QRect(350, 291, 439, 48))
        self.likedby_bg.setMaximumSize(QtCore.QSize(440, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.likedby_bg.setFont(font)
        self.likedby_bg.setStyleSheet("QLabel{background-color:rgb(26, 26, 26);border-radius:9px;color:white;padding:10px; padding-bottom:30px}")
        self.likedby_bg.setScaledContents(True)
        self.likedby_bg.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.likedby_bg.setWordWrap(True)
        self.likedby_bg.setObjectName("likedby_bg")


        self.onemypost_lb_caption = QtWidgets.QLabel(self.onemypostscreen)
        self.onemypost_lb_caption.setGeometry(QtCore.QRect(350, 297, 439, 40))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        self.onemypost_lb_caption.setFont(font)
        self.onemypost_lb_caption.setStyleSheet("background:transparent;padding-left:6px;padding-right:6px")
        self.onemypost_lb_caption.setScaledContents(True)
        self.onemypost_lb_caption.setWordWrap(True)
        self.onemypost_lb_caption.setObjectName("onemypost_date")











        #Like Count
        self.onemypost_likecount = QtWidgets.QLabel(self.onemypostscreen)
        self.onemypost_likecount.setGeometry(QtCore.QRect(350, 350, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.onemypost_likecount.setFont(font)
        self.onemypost_likecount.setStyleSheet("QLabel{background-color:rgb(26, 26, 26);border-radius:5px;color:white;}")
        self.onemypost_likecount.setScaledContents(True)
        self.onemypost_likecount.setAlignment(QtCore.Qt.AlignCenter)
        self.onemypost_likecount.setWordWrap(True)
        self.onemypost_likecount.setObjectName("onemypost_likecount")

        #Comment Count
        self.onemypost_commentcount = QtWidgets.QLabel(self.onemypostscreen)
        self.onemypost_commentcount.setGeometry(QtCore.QRect(570, 350, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.onemypost_commentcount.setFont(font)
        self.onemypost_commentcount.setStyleSheet("QLabel{background-color:rgb(26, 26, 26);border-radius:5px;color:white;}")
        self.onemypost_commentcount.setScaledContents(True)
        self.onemypost_commentcount.setAlignment(QtCore.Qt.AlignCenter)
        self.onemypost_commentcount.setWordWrap(True)
        self.onemypost_commentcount.setObjectName("onemypost_commentcount")


        #Corousell mypost Count
        self.onemypost_mypostcount = QtWidgets.QLabel(self.onemypostscreen)
        self.onemypost_mypostcount.setGeometry(QtCore.QRect(228, 134, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.onemypost_mypostcount.setFont(font)
        self.onemypost_mypostcount.setStyleSheet("QLabel{background-color:rgb(88, 88, 88);border-radius:9px;color:white;}")
        self.onemypost_mypostcount.setScaledContents(True)
        self.onemypost_mypostcount.setAlignment(QtCore.Qt.AlignCenter)
        self.onemypost_mypostcount.setWordWrap(True)
        self.onemypost_mypostcount.setObjectName("onemypost_mypostcount")


        #Next Button
        self.onemypost_next = QtWidgets.QPushButton(self.onemypostscreen)
        self.onemypost_next.setGeometry(QtCore.QRect(290, 400, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.onemypost_next.setFont(font)
        self.onemypost_next.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.onemypost_next.setObjectName("onemypost_next")
        self.onemypost_next.clicked.connect(lambda:next_mycorousell())

        #Back Button
        self.onemypost_back = QtWidgets.QPushButton(self.onemypostscreen)
        self.onemypost_back.setGeometry(QtCore.QRect(20, 400, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.onemypost_back.setFont(font)
        self.onemypost_back.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.onemypost_back.setObjectName("onemypost_back")
        self.onemypost_back.clicked.connect(lambda:back_mycorousell())


        
        #TaskBar  
        self.TB = QtWidgets.QLabel(self.onemypostscreen)
        self.TB.setGeometry(QtCore.QRect(-40, 480, 861, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.TB.setFont(font)
        self.TB.setStyleSheet("background:rgb(36, 36, 36);")
        self.TB.setScaledContents(True)
        self.TB.setObjectName("TB")



        
        self.TB_Home = QtWidgets.QPushButton(self.onemypostscreen)
        self.TB_Home.setGeometry(QtCore.QRect(10, 490, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.TB_Home.setFont(font)
        self.TB_Home.setStyleSheet("QPushButton{background-color:rgb(50, 50, 50);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.TB_Home.setObjectName("TB_Home")
        self.TB_Home.clicked.connect(lambda: setscreen_feed())

        
        self.TB_Search = QtWidgets.QPushButton(self.onemypostscreen)
        self.TB_Search.setGeometry(QtCore.QRect(170, 490, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.TB_Search.setFont(font)
        self.TB_Search.setStyleSheet("QPushButton{background-color:rgb(50, 50, 50);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.TB_Search.setObjectName("TB_Search")
        self.TB_Search.clicked.connect(lambda: setscreen_search())


        
        self.TB_Profile = QtWidgets.QPushButton(self.onemypostscreen)
        self.TB_Profile.setGeometry(QtCore.QRect(490, 490, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.TB_Profile.setFont(font)
        self.TB_Profile.setObjectName("TB_Profile")
        self.TB_Profile.clicked.connect(lambda: setscreen_profilemain())
        self.TB_Profile.setStyleSheet("QPushButton{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")

        
        self.TB_Timeline = QtWidgets.QPushButton(self.onemypostscreen)
        self.TB_Timeline.setGeometry(QtCore.QRect(330, 490, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.TB_Timeline.setFont(font)
        self.TB_Timeline.setStyleSheet("QPushButton{background-color:rgb(50, 50, 50);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.TB_Timeline.setObjectName("TB_Timeline")
        #self.TB_Timeline.clicked.connect(lambda: timelinescreen())


        
        self.TB_Settings = QtWidgets.QPushButton(self.onemypostscreen)
        self.TB_Settings.setGeometry(QtCore.QRect(650, 490, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.TB_Settings.setFont(font)
        self.TB_Settings.setStyleSheet("QPushButton{background-color:rgb(50, 50, 50);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.TB_Settings.setObjectName("TB_Settings")
        #self.TB_Timeline.clicked.connect(lambda: settingscreen())


        self.onemypost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\">Edited</span></p></body></html>"))
        self.onemypost_textlogo.setText(_translate("MainWindow", " SuperInsta"))
        self.onemypost_signout.setText(_translate("MainWindow", "Sign Out"))
        self.onemypost_username.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">@username  - Location, Location</span></p></body></html>"))
        self.onemypost_close.setText(_translate("MainWindow", "x"))
        self.onemypost_toolcase.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.onemypost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#f1f1f1;\">Caption Here.</span></p></body></html>"))
        self.onemypost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by @mostuselessboy1hfk35hch4h1h2b2h, @mostuselessboy1hfk35hch4h1h2b2h and 1,342 others. </span></p></body></html>"))
        self.onemypost_likecount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Likes: 1,234</span></p></body></html>"))
        self.onemypost_commentcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Comments: 234</span></p></body></html>"))
        self.onemypost_mypostcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">mypost 10/10</span></p></body></html>"))
        self.onemypost_next.setText(_translate("MainWindow", ">"))
        self.onemypost_back.setText(_translate("MainWindow", "<"))
        self.onemypost_date.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" color:#919191;\">24 May 2020</span></p></body></html>"))
        self.TB_Home.setText(_translate("MainWindow", "Home"))
        self.TB_Search.setText(_translate("MainWindow", "Search"))
        self.TB_Profile.setText(_translate("MainWindow", "Your Profile"))
        self.TB_Timeline.setText(_translate("MainWindow", "Timeline"))
        self.TB_Settings.setText(_translate("MainWindow", "SuperInsta"))


########################################### Loading Screen ################################################
        #Screen
        self.loadingscreen = QtWidgets.QWidget(MainWindow)
        self.loadingscreen.setObjectName("loadingscreen")

        #Logo
        self.loadingscreen_logo = QtWidgets.QLabel(self.loadingscreen)
        self.loadingscreen_logo.setGeometry(QtCore.QRect(310, 180, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Billabong")
        font.setPointSize(41)
        self.loadingscreen_logo.setFont(font)
        self.loadingscreen_logo.setStyleSheet("background:transparent;")
        self.loadingscreen_logo.setScaledContents(True)
        self.loadingscreen_logo.setObjectName("loadingscreen_logo")


        #Detailed Text
        self.loadingscreen_text = QtWidgets.QLabel(self.loadingscreen)
        self.loadingscreen_text.setGeometry(QtCore.QRect(210, 500, 431, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.loadingscreen_text.setFont(font)
        self.loadingscreen_text.setStyleSheet("background:transparent;")
        self.loadingscreen_text.setScaledContents(True)
        self.loadingscreen_text.setAlignment(QtCore.Qt.AlignCenter)
        self.loadingscreen_text.setWordWrap(True)
        self.loadingscreen_text.setObjectName("loadingscreen_text")


        #ProgressBar
        self.loadingscreen_progress = QtWidgets.QProgressBar(self.loadingscreen)
        self.loadingscreen_progress.setGeometry(QtCore.QRect(150, 250, 501, 23))
        self.loadingscreen_progress.setStyleSheet("QProgressBar {border: 1px solid black;text-align: top;padding: 1px;border-radius:7px;background: rgb(241, 241, 241);width: 15px;}QProgressBar::chunk{background:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:7px;border: 1px solid black;}")
        self.loadingscreen_progress.setValue(0)
        self.loadingscreen_progress.setMaximum(10)
        #self.likepost_scan_progress.set(0)
        self.loadingscreen_progress.setTextVisible(False)
        self.loadingscreen_progress.setInvertedAppearance(False)
        self.loadingscreen_progress.setObjectName("loadingscreen_progress")


        #Translatables Text
        self.loadingscreen_logo.setText(_translate("MainWindow", "SuperInsta"))
        self.loadingscreen_text.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\">Hold on while we collect feeds for you..</span></p></body></html>"))

########################################### Like Post Scan Screen ################################################

        #Screen
        self.likepostscanscreen = QtWidgets.QWidget(MainWindow)
        self.likepostscanscreen.setObjectName("likepostscanscreen")

        #Logo
        self.likepost_scan_logo = QtWidgets.QLabel(self.likepostscanscreen)
        self.likepost_scan_logo.setGeometry(QtCore.QRect(310, 180, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Billabong")
        font.setPointSize(41)
        self.likepost_scan_logo.setFont(font)
        self.likepost_scan_logo.setStyleSheet("background:transparent;")
        self.likepost_scan_logo.setScaledContents(True)
        self.likepost_scan_logo.setObjectName("likepost_scan_logo")


        #Detailed Text
        self.likepost_scan_details = QtWidgets.QLabel(self.likepostscanscreen)
        self.likepost_scan_details.setGeometry(QtCore.QRect(210, 500, 431, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.likepost_scan_details.setFont(font)
        self.likepost_scan_details.setStyleSheet("background:transparent;")
        self.likepost_scan_details.setScaledContents(True)
        self.likepost_scan_details.setAlignment(QtCore.Qt.AlignCenter)
        self.likepost_scan_details.setWordWrap(True)
        self.likepost_scan_details.setObjectName("likepost_scan_details")


        #ProgressBar
        self.likepost_scan_progress = QtWidgets.QProgressBar(self.likepostscanscreen)
        self.likepost_scan_progress.setGeometry(QtCore.QRect(150, 250, 501, 23))
        self.likepost_scan_progress.setStyleSheet("QProgressBar {border: 1px solid black;text-align: top;padding: 1px;border-radius:7px;background: rgb(241, 241, 241);width: 15px;}QProgressBar::chunk{background:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:7px;border: 1px solid black;}")
        self.likepost_scan_progress.setValue(0)
        self.likepost_scan_progress.setMaximum(200)
        #self.likepost_scan_progress.set(0)
        self.likepost_scan_progress.setTextVisible(False)
        self.likepost_scan_progress.setInvertedAppearance(False)
        self.likepost_scan_progress.setObjectName("likepost_scan_progress")

        #Stop Scan Button
        self.likepost_scan_stop = QtWidgets.QPushButton(self.likepostscanscreen)
        self.likepost_scan_stop.setGeometry(QtCore.QRect(350, 290, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.likepost_scan_stop.setFont(font)
        self.likepost_scan_stop.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-radius:15px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));color:rgb(255, 142, 231);}")
        self.likepost_scan_stop.setObjectName("likepost_scan_stop")
        self.likepost_scan_stop.clicked.connect(lambda:stop_likedpost_scan())

        #Translatables Text
        self.likepost_scan_logo.setText(_translate("MainWindow", "SuperInsta"))
        self.likepost_scan_details.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\">Stop Scan will return the post that is scanned till now.</span></p></body></html>"))
        self.likepost_scan_stop.setText(_translate("MainWindow", "Stop Scan"))########################################### LikedPost Scan ################################################

        


        
########################################### Feed Screen ################################################




        self.feed_screen = QtWidgets.QWidget(MainWindow)
        self.feed_screen.setObjectName("feed_screen")



        self.feed_logo = QtWidgets.QLabel(self.feed_screen)
        self.feed_logo.setGeometry(QtCore.QRect(10, 10, 41, 41))
        self.feed_logo.setText("")
        self.feed_logo.setPixmap(QtGui.QPixmap(":/elem/logo.png"))
        self.feed_logo.setScaledContents(True)
        self.feed_logo.setObjectName("feed_logo")


        
        self.feed_textlogo = QtWidgets.QLabel(self.feed_screen)
        self.feed_textlogo.setGeometry(QtCore.QRect(60, 10, 201, 51))
        font = QtGui.QFont()
        font.setFamily("Billabong")
        font.setPointSize(41)
        self.feed_textlogo.setFont(font)
        self.feed_textlogo.setStyleSheet("background:transparent;")
        self.feed_textlogo.setScaledContents(True)
        self.feed_textlogo.setObjectName("feed_textlogo")


        
        self.feed_signout = QtWidgets.QPushButton(self.feed_screen)
        self.feed_signout.setGeometry(QtCore.QRect(680, 10, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.feed_signout.setFont(font)
        self.feed_signout.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-radius:15px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));color:rgb(255, 142, 231);}")
        self.feed_signout.setObjectName("feed_signout")
        self.feed_signout.clicked.connect(lambda:logout_instagram())


        
        self.reels_tray = QtWidgets.QLabel(self.feed_screen)
        self.reels_tray.setGeometry(QtCore.QRect(20, 70, 781, 91))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.reels_tray.setFont(font)
        self.reels_tray.setStyleSheet("QLabel{background-color:rgb(29, 29, 29);border-radius:20px;color:white;}")
        self.reels_tray.setScaledContents(True)
        self.reels_tray.setObjectName("reels_tray")





        
        self.reel_1 = QtWidgets.QLabel(self.feed_screen)
        self.reel_1.setGeometry(QtCore.QRect(60, 77, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.reel_1.setFont(font)
        self.reel_1.setStyleSheet("background:transparent;border:3px solid rgb(77, 77, 77);border-radius:35px")
        self.reel_1.setText("")
        #self.reel_1.setPixmap(QtGui.QPixmap(":/elem/result.png"))
        self.reel_1.setScaledContents(True)
        self.reel_1.setObjectName("reel_1")
        self.reel_2 = QtWidgets.QLabel(self.feed_screen)
        self.reel_2.setGeometry(QtCore.QRect(150, 80, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.reel_2.setFont(font)
        self.reel_2.setStyleSheet("background:transparent;border:3px solid rgb(77, 77, 77);border-radius:35px")
        self.reel_2.setText("")
        #self.reel_2.setPixmap(QtGui.QPixmap(":/elem/result.png"))
        self.reel_2.setScaledContents(True)
        self.reel_2.setObjectName("reel_2")
        self.reel_3 = QtWidgets.QLabel(self.feed_screen)
        self.reel_3.setGeometry(QtCore.QRect(240, 80, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.reel_3.setFont(font)
        self.reel_3.setStyleSheet("background:transparent;border:3px solid rgb(77, 77, 77);border-radius:35px")
        self.reel_3.setText("")
        #self.reel_3.setPixmap(QtGui.QPixmap(":/elem/result.png"))
        self.reel_3.setScaledContents(True)
        self.reel_3.setObjectName("reel_3")
        self.reel_4 = QtWidgets.QLabel(self.feed_screen)
        self.reel_4.setGeometry(QtCore.QRect(330, 80, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.reel_4.setFont(font)
        self.reel_4.setStyleSheet("background:transparent;border:3px solid rgb(77, 77, 77);border-radius:35px")
        self.reel_4.setText("")
        #self.reel_4.setPixmap(QtGui.QPixmap(":/elem/result.png"))
        self.reel_4.setScaledContents(True)
        self.reel_4.setObjectName("reel_4")
        self.reel_5 = QtWidgets.QLabel(self.feed_screen)
        self.reel_5.setGeometry(QtCore.QRect(420, 80, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.reel_5.setFont(font)
        self.reel_5.setStyleSheet("background:transparent;border:3px solid rgb(77, 77, 77);border-radius:35px")
        self.reel_5.setText("")
        #self.reel_5.setPixmap(QtGui.QPixmap(":/elem/result.png"))
        self.reel_5.setScaledContents(True)
        self.reel_5.setObjectName("reel_5")
        self.reel_6 = QtWidgets.QLabel(self.feed_screen)
        self.reel_6.setGeometry(QtCore.QRect(510, 80, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.reel_6.setFont(font)
        self.reel_6.setStyleSheet("background:transparent;border:3px solid rgb(77, 77, 77);border-radius:35px")
        self.reel_6.setText("")
        #self.reel_6.setPixmap(QtGui.QPixmap(":/elem/result.png"))
        self.reel_6.setScaledContents(True)
        self.reel_6.setObjectName("reel_6")


        self.reel_7 = QtWidgets.QLabel(self.feed_screen)
        self.reel_7.setGeometry(QtCore.QRect(600, 80, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.reel_7.setFont(font)
        self.reel_7.setStyleSheet("background:transparent;border:3px solid rgb(77, 77, 77);border-radius:35px")
        self.reel_7.setText("")
        #self.reel_7.setPixmap(QtGui.QPixmap(":/elem/result.png"))
        self.reel_7.setScaledContents(True)
        self.reel_7.setObjectName("reel_7")

        self.reel_8 = QtWidgets.QLabel(self.feed_screen)
        self.reel_8.setGeometry(QtCore.QRect(690, 80, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.reel_8.setFont(font)
        self.reel_8.setStyleSheet("background:transparent;border:3px solid rgb(77, 77, 77);border-radius:35px")
        self.reel_8.setText("")
        self.reel_8.setScaledContents(True)
        self.reel_8.setObjectName("reel_8")
        
        self.feed_seenall = QtWidgets.QPushButton(self.feed_screen)
        self.feed_seenall.setGeometry(QtCore.QRect(530, 10, 141, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.feed_seenall.setFont(font)
        self.feed_seenall.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-radius:15px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));color:rgb(255, 142, 231);}")
        self.feed_seenall.setObjectName("feed_seenall")
        self.feed_seenall.clicked.connect(lambda:watch_all_story())

        
        self.reels_back = QtWidgets.QPushButton(self.feed_screen)
        self.reels_back.setGeometry(QtCore.QRect(20, 70, 31, 91))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.reels_back.setFont(font)
        self.reels_back.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-radius:15px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));color:rgb(255, 142, 231);}")
        self.reels_back.setObjectName("reels_back")
        self.reels_back.clicked.connect(lambda:back_story())




        self.reels_next = QtWidgets.QPushButton(self.feed_screen)
        self.reels_next.setGeometry(QtCore.QRect(770, 70, 31, 91))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.reels_next.setFont(font)
        self.reels_next.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-radius:15px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));color:rgb(255, 142, 231);}")
        self.reels_next.setObjectName("reels_next")
        self.reels_next.clicked.connect(lambda:next_story())


        
        self.scrollArea = QtWidgets.QScrollArea(self.feed_screen)
        self.scrollArea.setGeometry(QtCore.QRect(10, 162, 781, 311))
        self.scrollArea.setStyleSheet("background:transparent;")
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.scrollArea.setLineWidth(1)
        self.scrollArea.setMidLineWidth(0)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")


        
        self.card_scrollarea = QtWidgets.QWidget()
        self.card_scrollarea.setGeometry(QtCore.QRect(-1459, 0, 2240, 303))
        self.card_scrollarea.setObjectName("card_scrollarea")
        self.scrolllbar2 = QtWidgets.QScrollBar(self.searchscreen)
        self.scrolllbar2.setStyleSheet(
"        QScrollBar:horizontal {\n"
"            border: none;\n"
"             background: rgb(45,45,45);\n"
"            height: 10px;\n"
"            margin: 0px 0 0px 0;\n"
"        }\n"
"\n"
"        QScrollBar::handle:horizontal {\n"
"            background: dark grey;\n"
"            min-width: 26px;\n"
"            border-radius: 5px;\n"
"        }\n"
"\n"
"        QScrollBar::add-line:horizontal {\n"
"            background: none;\n"
"            width: 26px;\n"
"            subcontrol-position: bottom;\n"
"            subcontrol-origin: margin;\n"
"        }\n"
"\n"
"        QScrollBar::sub-line:horizontal {\n"
"            background: none;\n"
"            width: 0px;\n"
"            subcontrol-position: top left;\n"
"            subcontrol-origin: margin;\n"
"            position: absolute;\n"
"        }\n"
"\n"
"\n"
"        QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {\n"
"            background: rgb(45,45,45);\n"
"        }")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.card_scrollarea)
        self.verticalLayout.setObjectName("verticalLayout")


        
        self.card_holder = QtWidgets.QHBoxLayout()
        self.card_holder.setSpacing(10)
        self.card_holder.setObjectName("card_holder")
        self.scrollArea.setHorizontalScrollBar(self.scrolllbar2)
        
        self.card1 = QtWidgets.QVBoxLayout()
        self.card1.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.card1.setSpacing(0)
        self.card1.setObjectName("card1")
        self.card_header1 = QtWidgets.QPushButton(self.card_scrollarea)
        self.card_header1.setMinimumSize(QtCore.QSize(211, 35))
        self.card_header1.setMaximumSize(QtCore.QSize(211, 35))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.card_header1.setFont(font)
        self.card_header1.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-top-left-radius:9px;border-top-right-radius:9px;color:white;}QPushButton::hover{background-color:qradialgradient(spread:pad, cx:0, cy:1, radius:2, fx:1, fy:0.251, stop:0 rgba(241, 39, 17, 255), stop:1 rgba(245, 25, 137, 255));color:white;}")
        self.card_header1.setObjectName("card_header1")
        self.card1.addWidget(self.card_header1)
        self.card_img1 = QtWidgets.QLabel(self.card_scrollarea)
        self.card_img1.setMinimumSize(QtCore.QSize(211, 211))
        self.card_img1.setMaximumSize(QtCore.QSize(211, 211))
        self.card_img1.setText("")
        #self.card_img1.setPixmap(QtGui.QPixmap(":/elem/liam.jpg"))
        self.card_img1.setStyleSheet("border:30px solid rgb(29, 29, 29);background: rgb(29, 29, 29);")
        self.card_img1.setScaledContents(True)
        self.card_img1.setObjectName("card_img1")
        self.card1.addWidget(self.card_img1)
        self.card_footer1 = QtWidgets.QPushButton(self.card_scrollarea)
        self.card_footer1.setMinimumSize(QtCore.QSize(211, 35))
        self.card_footer1.setMaximumSize(QtCore.QSize(211, 35))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.card_footer1.setFont(font)
        self.card_footer1.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-bottom-left-radius:9px;border-bottom-right-radius:9px;color:white;}QPushButton::hover{background-color:qradialgradient(spread:pad, cx:0, cy:1, radius:2, fx:1, fy:0.251, stop:0 rgba(241, 39, 17, 255), stop:1 rgba(245, 25, 137, 255));color:white;}")
        self.card_footer1.setObjectName("card_footer1")
        self.card1.addWidget(self.card_footer1)




        
        self.card_holder.addLayout(self.card1)
        self.card2 = QtWidgets.QVBoxLayout()
        self.card2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.card2.setSpacing(0)
        self.card2.setObjectName("card2")
        self.card_header2 = QtWidgets.QPushButton(self.card_scrollarea)
        self.card_header2.setMinimumSize(QtCore.QSize(211, 35))
        self.card_header2.setMaximumSize(QtCore.QSize(211, 35))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.card_header2.setFont(font)
        self.card_header2.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-top-left-radius:9px;border-top-right-radius:9px;color:white;}QPushButton::hover{background-color:qradialgradient(spread:pad, cx:0, cy:1, radius:2, fx:1, fy:0.251, stop:0 rgba(241, 39, 17, 255), stop:1 rgba(245, 25, 137, 255));color:white;}")
        self.card_header2.setObjectName("card_header2")
        self.card2.addWidget(self.card_header2)
        self.card_img2 = QtWidgets.QLabel(self.card_scrollarea)
        self.card_img2.setMinimumSize(QtCore.QSize(211, 211))
        self.card_img2.setMaximumSize(QtCore.QSize(211, 211))
        self.card_img2.setStyleSheet("border:30px solid rgb(29, 29, 29);background: rgb(29, 29, 29);")
        self.card_img2.setText("")
        #self.card_img2.setPixmap(QtGui.QPixmap(":/elem/result.png"))
        self.card_img2.setScaledContents(True)
        self.card_img2.setObjectName("card_img2")
        self.card2.addWidget(self.card_img2)
        self.card_footer2 = QtWidgets.QPushButton(self.card_scrollarea)
        self.card_footer2.setMinimumSize(QtCore.QSize(211, 35))
        self.card_footer2.setMaximumSize(QtCore.QSize(211, 35))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.card_footer2.setFont(font)
        self.card_footer2.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-bottom-left-radius:9px;border-bottom-right-radius:9px;color:white;}QPushButton::hover{background-color:qradialgradient(spread:pad, cx:0, cy:1, radius:2, fx:1, fy:0.251, stop:0 rgba(241, 39, 17, 255), stop:1 rgba(245, 25, 137, 255));color:white;}")
        self.card_footer2.setObjectName("card_footer2")
        self.card2.addWidget(self.card_footer2)
        self.card_holder.addLayout(self.card2)




        
        self.card3 = QtWidgets.QVBoxLayout()
        self.card3.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.card3.setSpacing(0)
        self.card3.setObjectName("card3")
        self.card_header3 = QtWidgets.QPushButton(self.card_scrollarea)
        self.card_header3.setMinimumSize(QtCore.QSize(211, 35))
        self.card_header3.setMaximumSize(QtCore.QSize(211, 35))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.card_header3.setFont(font)
        self.card_header3.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-top-left-radius:9px;border-top-right-radius:9px;color:white;}QPushButton::hover{background-color:qradialgradient(spread:pad, cx:0, cy:1, radius:2, fx:1, fy:0.251, stop:0 rgba(241, 39, 17, 255), stop:1 rgba(245, 25, 137, 255));color:white;}")
        self.card_header3.setObjectName("card_header3")
        self.card3.addWidget(self.card_header3)
        self.card_img3 = QtWidgets.QLabel(self.card_scrollarea)
        self.card_img3.setMinimumSize(QtCore.QSize(211, 211))
        self.card_img3.setMaximumSize(QtCore.QSize(211, 211))
        self.card_img3.setStyleSheet("border:0px solid rgb(29, 29, 29);background: rgb(29, 29, 29);")
        self.card_img3.setText("")
        #self.card_img3.setPixmap(QtGui.QPixmap(":/elem/liam.jpg"))
        self.card_img3.setScaledContents(True)
        self.card_img3.setObjectName("card_img3")
        self.card3.addWidget(self.card_img3)
        self.card_footer3 = QtWidgets.QPushButton(self.card_scrollarea)
        self.card_footer3.setMinimumSize(QtCore.QSize(211, 35))
        self.card_footer3.setMaximumSize(QtCore.QSize(211, 35))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.card_footer3.setFont(font)
        self.card_footer3.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-bottom-left-radius:9px;border-bottom-right-radius:9px;color:white;}QPushButton::hover{background-color:qradialgradient(spread:pad, cx:0, cy:1, radius:2, fx:1, fy:0.251, stop:0 rgba(241, 39, 17, 255), stop:1 rgba(245, 25, 137, 255));color:white;}")
        self.card_footer3.setObjectName("card_footer3")
        self.card3.addWidget(self.card_footer3)
        self.card_holder.addLayout(self.card3)




        
        self.card4 = QtWidgets.QVBoxLayout()
        self.card4.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.card4.setSpacing(0)
        self.card4.setObjectName("card4")
        self.card_header4 = QtWidgets.QPushButton(self.card_scrollarea)
        self.card_header4.setMinimumSize(QtCore.QSize(211, 35))
        self.card_header4.setMaximumSize(QtCore.QSize(211, 35))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.card_header4.setFont(font)
        self.card_header4.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-top-left-radius:9px;border-top-right-radius:9px;color:white;}QPushButton::hover{background-color:qradialgradient(spread:pad, cx:0, cy:1, radius:2, fx:1, fy:0.251, stop:0 rgba(241, 39, 17, 255), stop:1 rgba(245, 25, 137, 255));color:white;}")
        self.card_header4.setObjectName("card_header4")
        self.card4.addWidget(self.card_header4)
        self.card_img4 = QtWidgets.QLabel(self.card_scrollarea)
        self.card_img4.setMinimumSize(QtCore.QSize(211, 211))
        self.card_img4.setMaximumSize(QtCore.QSize(211, 211))
        self.card_img4.setStyleSheet("border:0px solid rgb(29, 29, 29);background: rgb(29, 29, 29);")
        self.card_img4.setText("")
        #self.card_img4.setPixmap(QtGui.QPixmap(":/elem/liam.jpg"))
        self.card_img4.setScaledContents(True)
        self.card_img4.setObjectName("card_img4")
        self.card4.addWidget(self.card_img4)
        self.card_footer4 = QtWidgets.QPushButton(self.card_scrollarea)
        self.card_footer4.setMinimumSize(QtCore.QSize(211, 35))
        self.card_footer4.setMaximumSize(QtCore.QSize(211, 35))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.card_footer4.setFont(font)
        self.card_footer4.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-bottom-left-radius:9px;border-bottom-right-radius:9px;color:white;}QPushButton::hover{background-color:qradialgradient(spread:pad, cx:0, cy:1, radius:2, fx:1, fy:0.251, stop:0 rgba(241, 39, 17, 255), stop:1 rgba(245, 25, 137, 255));color:white;}")
        self.card_footer4.setObjectName("card_footer4")
        self.card4.addWidget(self.card_footer4)
        self.card_holder.addLayout(self.card4)



        
        self.card5 = QtWidgets.QVBoxLayout()
        self.card5.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.card5.setSpacing(0)
        self.card5.setObjectName("card5")
        self.card_header5 = QtWidgets.QPushButton(self.card_scrollarea)
        self.card_header5.setMinimumSize(QtCore.QSize(211, 35))
        self.card_header5.setMaximumSize(QtCore.QSize(211, 35))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.card_header5.setFont(font)
        self.card_header5.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-top-left-radius:9px;border-top-right-radius:9px;color:white;}QPushButton::hover{background-color:qradialgradient(spread:pad, cx:0, cy:1, radius:2, fx:1, fy:0.251, stop:0 rgba(241, 39, 17, 255), stop:1 rgba(245, 25, 137, 255));color:white;}")
        self.card_header5.setObjectName("card_header5")
        self.card5.addWidget(self.card_header5)
        self.card_img5 = QtWidgets.QLabel(self.card_scrollarea)
        self.card_img5.setMinimumSize(QtCore.QSize(211, 211))
        self.card_img5.setMaximumSize(QtCore.QSize(211, 211))
        self.card_img5.setStyleSheet("border:0px solid rgb(29, 29, 29);background: rgb(29, 29, 29);")
        self.card_img5.setText("")
        #self.card_img5.setPixmap(QtGui.QPixmap(":/elem/liam.jpg"))
        self.card_img5.setScaledContents(True)
        self.card_img5.setObjectName("card_img5")
        self.card5.addWidget(self.card_img5)
        self.card_footer5 = QtWidgets.QPushButton(self.card_scrollarea)
        self.card_footer5.setMinimumSize(QtCore.QSize(211, 35))
        self.card_footer5.setMaximumSize(QtCore.QSize(211, 35))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.card_footer5.setFont(font)
        self.card_footer5.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-bottom-left-radius:9px;border-bottom-right-radius:9px;color:white;}QPushButton::hover{background-color:qradialgradient(spread:pad, cx:0, cy:1, radius:2, fx:1, fy:0.251, stop:0 rgba(241, 39, 17, 255), stop:1 rgba(245, 25, 137, 255));color:white;}")
        self.card_footer5.setObjectName("card_footer5")
        self.card5.addWidget(self.card_footer5)
        self.card_holder.addLayout(self.card5)




        
        self.card6 = QtWidgets.QVBoxLayout()
        self.card6.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.card6.setSpacing(0)
        self.card6.setObjectName("card6")
        self.card_header6 = QtWidgets.QPushButton(self.card_scrollarea)
        self.card_header6.setMinimumSize(QtCore.QSize(211, 35))
        self.card_header6.setMaximumSize(QtCore.QSize(211, 35))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.card_header6.setFont(font)
        self.card_header6.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-top-left-radius:9px;border-top-right-radius:9px;color:white;}QPushButton::hover{background-color:qradialgradient(spread:pad, cx:0, cy:1, radius:2, fx:1, fy:0.251, stop:0 rgba(241, 39, 17, 255), stop:1 rgba(245, 25, 137, 255));color:white;}")
        self.card_header6.setObjectName("card_header6")
        self.card6.addWidget(self.card_header6)
        self.card_img6 = QtWidgets.QLabel(self.card_scrollarea)
        self.card_img6.setMinimumSize(QtCore.QSize(211, 211))
        self.card_img6.setMaximumSize(QtCore.QSize(211, 211))
        self.card_img6.setStyleSheet("border:0px solid rgb(29, 29, 29);background: rgb(29, 29, 29);")
        self.card_img6.setText("")
        #self.card_img6.setPixmap(QtGui.QPixmap(":/elem/liam.jpg"))
        self.card_img6.setScaledContents(True)
        self.card_img6.setObjectName("card_img6")
        self.card6.addWidget(self.card_img6)
        self.card_footer6 = QtWidgets.QPushButton(self.card_scrollarea)
        self.card_footer6.setMinimumSize(QtCore.QSize(211, 35))
        self.card_footer6.setMaximumSize(QtCore.QSize(211, 35))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.card_footer6.setFont(font)
        self.card_footer6.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-bottom-left-radius:9px;border-bottom-right-radius:9px;color:white;}QPushButton::hover{background-color:qradialgradient(spread:pad, cx:0, cy:1, radius:2, fx:1, fy:0.251, stop:0 rgba(241, 39, 17, 255), stop:1 rgba(245, 25, 137, 255));color:white;}")
        self.card_footer6.setObjectName("card_footer6")
        self.card6.addWidget(self.card_footer6)
        self.card_holder.addLayout(self.card6)




        
        self.card_7 = QtWidgets.QVBoxLayout()
        self.card_7.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.card_7.setSpacing(0)
        self.card_7.setObjectName("card_7")
        self.card_header7 = QtWidgets.QPushButton(self.card_scrollarea)
        self.card_header7.setMinimumSize(QtCore.QSize(211, 35))
        self.card_header7.setMaximumSize(QtCore.QSize(211, 35))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.card_header7.setFont(font)
        self.card_header7.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-top-left-radius:9px;border-top-right-radius:9px;color:white;}QPushButton::hover{background-color:qradialgradient(spread:pad, cx:0, cy:1, radius:2, fx:1, fy:0.251, stop:0 rgba(241, 39, 17, 255), stop:1 rgba(245, 25, 137, 255));color:white;}")
        self.card_header7.setObjectName("card_header7")
        self.card_7.addWidget(self.card_header7)
        self.card_img7 = QtWidgets.QLabel(self.card_scrollarea)
        self.card_img7.setMinimumSize(QtCore.QSize(211, 211))
        self.card_img7.setMaximumSize(QtCore.QSize(211, 211))
        self.card_img7.setStyleSheet("border:0px solid rgb(29, 29, 29);background: rgb(29, 29, 29);")
        self.card_img7.setText("")
        #self.card_img7.setPixmap(QtGui.QPixmap(":/elem/liam.jpg"))
        self.card_img7.setScaledContents(True)
        self.card_img7.setObjectName("card_img7")
        self.card_7.addWidget(self.card_img7)
        self.card_footer7 = QtWidgets.QPushButton(self.card_scrollarea)
        self.card_footer7.setMinimumSize(QtCore.QSize(211, 35))
        self.card_footer7.setMaximumSize(QtCore.QSize(211, 35))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.card_footer7.setFont(font)
        self.card_footer7.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-bottom-left-radius:9px;border-bottom-right-radius:9px;color:white;}QPushButton::hover{background-color:qradialgradient(spread:pad, cx:0, cy:1, radius:2, fx:1, fy:0.251, stop:0 rgba(241, 39, 17, 255), stop:1 rgba(245, 25, 137, 255));color:white;}")
        self.card_footer7.setObjectName("card_footer7")
        self.card_7.addWidget(self.card_footer7)
        self.card_holder.addLayout(self.card_7)



        
        self.card8 = QtWidgets.QVBoxLayout()
        self.card8.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.card8.setSpacing(0)
        self.card8.setObjectName("card8")
        self.card_header8 = QtWidgets.QPushButton(self.card_scrollarea)
        self.card_header8.setMinimumSize(QtCore.QSize(211, 35))
        self.card_header8.setMaximumSize(QtCore.QSize(211, 35))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.card_header8.setFont(font)
        self.card_header8.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-top-left-radius:9px;border-top-right-radius:9px;color:white;}QPushButton::hover{background-color:qradialgradient(spread:pad, cx:0, cy:1, radius:2, fx:1, fy:0.251, stop:0 rgba(241, 39, 17, 255), stop:1 rgba(245, 25, 137, 255));color:white;}")
        self.card_header8.setObjectName("card_header8")
        self.card8.addWidget(self.card_header8)
        self.card_img8 = QtWidgets.QLabel(self.card_scrollarea)
        self.card_img8.setMinimumSize(QtCore.QSize(211, 211))
        self.card_img8.setMaximumSize(QtCore.QSize(211, 211))
        self.card_img8.setStyleSheet("border:0px solid rgb(29, 29, 29);background: rgb(29, 29, 29);")
        self.card_img8.setText("")
        #self.card_img8.setPixmap(QtGui.QPixmap(":/elem/liam.jpg"))
        self.card_img8.setScaledContents(True)
        self.card_img8.setObjectName("card_img8")
        self.card8.addWidget(self.card_img8)
        self.card_footer8 = QtWidgets.QPushButton(self.card_scrollarea)
        self.card_footer8.setMinimumSize(QtCore.QSize(211, 35))
        self.card_footer8.setMaximumSize(QtCore.QSize(211, 35))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.card_footer8.setFont(font)
        self.card_footer8.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-bottom-left-radius:9px;border-bottom-right-radius:9px;color:white;}QPushButton::hover{background-color:qradialgradient(spread:pad, cx:0, cy:1, radius:2, fx:1, fy:0.251, stop:0 rgba(241, 39, 17, 255), stop:1 rgba(245, 25, 137, 255));color:white;}")
        self.card_footer8.setObjectName("card_footer8")
        self.card8.addWidget(self.card_footer8)
        self.card_holder.addLayout(self.card8)



        
        self.card9 = QtWidgets.QVBoxLayout()
        self.card9.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.card9.setSpacing(0)
        self.card9.setObjectName("card9")
        self.card_header9 = QtWidgets.QPushButton(self.card_scrollarea)
        self.card_header9.setMinimumSize(QtCore.QSize(211, 35))
        self.card_header9.setMaximumSize(QtCore.QSize(211, 35))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.card_header9.setFont(font)
        self.card_header9.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-top-left-radius:9px;border-top-right-radius:9px;color:white;}QPushButton::hover{background-color:qradialgradient(spread:pad, cx:0, cy:1, radius:2, fx:1, fy:0.251, stop:0 rgba(241, 39, 17, 255), stop:1 rgba(245, 25, 137, 255));color:white;}")
        self.card_header9.setObjectName("card_header9")
        self.card9.addWidget(self.card_header9)
        self.card_img9 = QtWidgets.QLabel(self.card_scrollarea)
        self.card_img9.setMinimumSize(QtCore.QSize(211, 211))
        self.card_img9.setMaximumSize(QtCore.QSize(211, 211))
        self.card_img9.setStyleSheet("border:0px solid rgb(29, 29, 29);background: rgb(29, 29, 29);")
        self.card_img9.setText("")
        #self.card_img9.setPixmap(QtGui.QPixmap(":/elem/liam.jpg"))
        self.card_img9.setScaledContents(True)
        self.card_img9.setObjectName("card_img9")
        self.card9.addWidget(self.card_img9)
        self.card_footer9 = QtWidgets.QPushButton(self.card_scrollarea)
        self.card_footer9.setMinimumSize(QtCore.QSize(211, 35))
        self.card_footer9.setMaximumSize(QtCore.QSize(211, 35))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.card_footer9.setFont(font)
        self.card_footer9.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-bottom-left-radius:9px;border-bottom-right-radius:9px;color:white;}QPushButton::hover{background-color:qradialgradient(spread:pad, cx:0, cy:1, radius:2, fx:1, fy:0.251, stop:0 rgba(241, 39, 17, 255), stop:1 rgba(245, 25, 137, 255));color:white;}")
        self.card_footer9.setObjectName("card_footer9")
        self.card9.addWidget(self.card_footer9)
        self.card_holder.addLayout(self.card9)




        
        self.card10 = QtWidgets.QVBoxLayout()
        self.card10.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.card10.setSpacing(0)
        self.card10.setObjectName("card10")
        self.card_header10 = QtWidgets.QPushButton(self.card_scrollarea)
        self.card_header10.setMinimumSize(QtCore.QSize(211, 35))
        self.card_header10.setMaximumSize(QtCore.QSize(211, 35))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.card_header10.setFont(font)
        self.card_header10.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-top-left-radius:9px;border-top-right-radius:9px;color:white;}QPushButton::hover{background-color:qradialgradient(spread:pad, cx:0, cy:1, radius:2, fx:1, fy:0.251, stop:0 rgba(241, 39, 17, 255), stop:1 rgba(245, 25, 137, 255));color:white;}")
        self.card_header10.setObjectName("card_header10")
        self.card10.addWidget(self.card_header10)
        self.card_img10 = QtWidgets.QLabel(self.card_scrollarea)
        self.card_img10.setMinimumSize(QtCore.QSize(211, 211))
        self.card_img10.setMaximumSize(QtCore.QSize(211, 211))
        self.card_img10.setStyleSheet("border:0px solid rgb(29, 29, 29);background: rgb(29, 29, 29);")
        self.card_img10.setText("")
        #self.card_img10.setPixmap(QtGui.QPixmap(":/elem/liam.jpg"))
        self.card_img10.setScaledContents(True)
        self.card_img10.setObjectName("card_img10")
        self.card10.addWidget(self.card_img10)
        self.card_footer10 = QtWidgets.QPushButton(self.card_scrollarea)
        self.card_footer10.setMinimumSize(QtCore.QSize(211, 35))
        self.card_footer10.setMaximumSize(QtCore.QSize(211, 35))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.card_footer10.setFont(font)
        self.card_footer10.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-bottom-left-radius:9px;border-bottom-right-radius:9px;color:white;}QPushButton::hover{background-color:qradialgradient(spread:pad, cx:0, cy:1, radius:2, fx:1, fy:0.251, stop:0 rgba(241, 39, 17, 255), stop:1 rgba(245, 25, 137, 255));color:white;}")
        self.card_footer10.setObjectName("card_footer10")
        self.card10.addWidget(self.card_footer10)
        self.card_holder.addLayout(self.card10)
        self.verticalLayout.addLayout(self.card_holder)
        self.scrollArea.setWidget(self.card_scrollarea)
        
        #buttons - Headers
        self.card_header1.clicked.connect(lambda:card_headerbtn1())
        self.card_header2.clicked.connect(lambda:card_headerbtn2())
        self.card_header3.clicked.connect(lambda:card_headerbtn3())
        self.card_header4.clicked.connect(lambda:card_headerbtn4())
        self.card_header5.clicked.connect(lambda:card_headerbtn5())
        self.card_header6.clicked.connect(lambda:card_headerbtn6())
        self.card_header7.clicked.connect(lambda:card_headerbtn7())
        self.card_header8.clicked.connect(lambda:card_headerbtn8())
        self.card_header9.clicked.connect(lambda:card_headerbtn9())
        self.card_header10.clicked.connect(lambda:card_headerbtn10())
        #buttons - Footers
        self.card_footer1.clicked.connect(lambda:card_footerbtn1())
        self.card_footer2.clicked.connect(lambda:card_footerbtn2())
        self.card_footer3.clicked.connect(lambda:card_footerbtn3())
        self.card_footer4.clicked.connect(lambda:card_footerbtn4())
        self.card_footer5.clicked.connect(lambda:card_footerbtn5())
        self.card_footer6.clicked.connect(lambda:card_footerbtn6())
        self.card_footer7.clicked.connect(lambda:card_footerbtn7())
        self.card_footer8.clicked.connect(lambda:card_footerbtn8())
        self.card_footer9.clicked.connect(lambda:card_footerbtn9())
        self.card_footer10.clicked.connect(lambda:card_footerbtn10())


        
        self.feed_refresh = QtWidgets.QPushButton(self.feed_screen)
        self.feed_refresh.setGeometry(QtCore.QRect(400, 10, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.feed_refresh.setFont(font)
        self.feed_refresh.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-radius:15px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));color:rgb(255, 142, 231);}")
        self.feed_refresh.setObjectName("feed_refresh")
        self.feed_refresh.clicked.connect(lambda: loadfeed())



        
        #TaskBar  
        self.TB = QtWidgets.QLabel(self.onemypostscreen)
        self.TB.setGeometry(QtCore.QRect(-40, 480, 861, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.TB.setFont(font)
        self.TB.setStyleSheet("background:rgb(36, 36, 36);")
        self.TB.setScaledContents(True)
        self.TB.setObjectName("TB")



        
        self.TB_Home = QtWidgets.QPushButton(self.feed_screen)
        self.TB_Home.setGeometry(QtCore.QRect(10, 490, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.TB_Home.setFont(font)
        self.TB_Home.setObjectName("TB_Home")
        self.TB_Home.clicked.connect(lambda: setscreen_feed())
        self.TB_Home.setStyleSheet("QPushButton{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")

        
        self.TB_Search = QtWidgets.QPushButton(self.feed_screen)
        self.TB_Search.setGeometry(QtCore.QRect(170, 490, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.TB_Search.setFont(font)
        self.TB_Search.setStyleSheet("QPushButton{background-color:rgb(50, 50, 50);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.TB_Search.setObjectName("TB_Search")
        self.TB_Search.clicked.connect(lambda: setscreen_search())


        
        self.TB_Profile = QtWidgets.QPushButton(self.feed_screen)
        self.TB_Profile.setGeometry(QtCore.QRect(490, 490, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.TB_Profile.setFont(font)
        self.TB_Profile.setObjectName("TB_Profile")
        self.TB_Profile.clicked.connect(lambda: setscreen_profile())
        self.TB_Profile.setStyleSheet("QPushButton{background-color:rgb(50, 50, 50);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")

        
        self.TB_Timeline = QtWidgets.QPushButton(self.feed_screen)
        self.TB_Timeline.setGeometry(QtCore.QRect(330, 490, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.TB_Timeline.setFont(font)
        self.TB_Timeline.setStyleSheet("QPushButton{background-color:rgb(50, 50, 50);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.TB_Timeline.setObjectName("TB_Timeline")
        #self.TB_Timeline.clicked.connect(lambda: timelinescreen())


        
        self.TB_Settings = QtWidgets.QPushButton(self.feed_screen)
        self.TB_Settings.setGeometry(QtCore.QRect(650, 490, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.TB_Settings.setFont(font)
        self.TB_Settings.setStyleSheet("QPushButton{background-color:rgb(50, 50, 50);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.TB_Settings.setObjectName("TB_Settings")
        #self.TB_Timeline.clicked.connect(lambda: settingscreen())

        
        self.reels_tray.raise_()
        self.TB.raise_()
        self.feed_logo.raise_()
        self.feed_textlogo.raise_()
        self.feed_signout.raise_()

        self.reel_1.raise_()
        self.reel_2.raise_()
        self.reel_3.raise_()
        self.reel_4.raise_()
        self.reel_5.raise_()
        self.reel_6.raise_()
        self.reel_8.raise_()
        self.reel_7.raise_()
        self.feed_seenall.raise_()
        self.reels_back.raise_()
        self.reels_next.raise_()
        self.scrollArea.raise_()
        self.feed_refresh.raise_()
        self.TB_Home.raise_()
        self.TB_Search.raise_()
        self.TB_Profile.raise_()
        self.TB_Timeline.raise_()
        self.TB_Settings.raise_()    
        self.feed_textlogo.setText(_translate("MainWindow", "SuperInsta"))
        self.feed_signout.setText(_translate("MainWindow", "Sign Out"))
        self.reels_tray.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.TB.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.TB_Home.setText(_translate("MainWindow", "Home"))
        self.TB_Search.setText(_translate("MainWindow", "Search"))
        self.TB_Profile.setText(_translate("MainWindow", "Your Profile"))
        self.TB_Timeline.setText(_translate("MainWindow", "Timeline"))
        self.TB_Settings.setText(_translate("MainWindow", "SuperInsta"))
        self.feed_seenall.setText(_translate("MainWindow", "See All Story"))
        self.reels_back.setText(_translate("MainWindow", "<"))
        self.reels_next.setText(_translate("MainWindow", ">"))
        self.card_header1.setText(_translate("MainWindow", "@username"))
        self.card_footer1.setText(_translate("MainWindow", "View Post"))
        self.card_header2.setText(_translate("MainWindow", "@username"))
        self.card_footer2.setText(_translate("MainWindow", "Follow"))
        self.card_header3.setText(_translate("MainWindow", "@username"))
        self.card_footer3.setText(_translate("MainWindow", "View Post"))
        self.card_header4.setText(_translate("MainWindow", "@username"))
        self.card_footer4.setText(_translate("MainWindow", "View Post"))
        self.card_header5.setText(_translate("MainWindow", "@username"))
        self.card_footer5.setText(_translate("MainWindow", "View Post"))
        self.card_header6.setText(_translate("MainWindow", "@username"))
        self.card_footer6.setText(_translate("MainWindow", "View Post"))
        self.card_header7.setText(_translate("MainWindow", "@username"))
        self.card_footer7.setText(_translate("MainWindow", "View Post"))
        self.card_header8.setText(_translate("MainWindow", "@username"))
        self.card_footer8.setText(_translate("MainWindow", "View Post"))
        self.card_header9.setText(_translate("MainWindow", "@username"))
        self.card_footer9.setText(_translate("MainWindow", "View Post"))
        self.card_header10.setText(_translate("MainWindow", "@username"))
        self.card_footer10.setText(_translate("MainWindow", "View Post"))
        self.feed_refresh.setText(_translate("MainWindow", "Refresh"))



        
########################################### feedpost Screen ################################################

        #One Post Screen
        self.feed_postscreen = QtWidgets.QWidget(MainWindow)
        self.feed_postscreen.setObjectName("feed_postscreen")

        #One Post Logo
        self.feedpost_logo = QtWidgets.QLabel(self.feed_postscreen)
        self.feedpost_logo.setGeometry(QtCore.QRect(10, 10, 41, 41))
        self.feedpost_logo.setText("")
        self.feedpost_logo.setPixmap(QtGui.QPixmap(":/elem/logo.png"))
        self.feedpost_logo.setScaledContents(True)
        self.feedpost_logo.setObjectName("feedpost_logo")


        #Text Logo
        self.feedpost_textlogo = QtWidgets.QLabel(self.feed_postscreen)
        self.feedpost_textlogo.setGeometry(QtCore.QRect(50, 10, 191, 51))
        font = QtGui.QFont()
        font.setFamily("Billabong")
        font.setPointSize(41)
        self.feedpost_textlogo.setFont(font)
        self.feedpost_textlogo.setStyleSheet("background:transparent;")
        self.feedpost_textlogo.setScaledContents(True)
        self.feedpost_textlogo.setObjectName("feedpost_textlogo")

        #Signout                  
        self.feedpost_signout = QtWidgets.QPushButton(self.feed_postscreen)
        self.feedpost_signout.setGeometry(QtCore.QRect(680, 10, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.feedpost_signout.setFont(font)
        self.feedpost_signout.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-radius:15px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));color:rgb(255, 142, 231);}")
        self.feedpost_signout.setObjectName("feedpost_signout")
        self.feedpost_signout.clicked.connect(lambda:logout_instagram())

        #Username
        self.feedpost_username = QtWidgets.QLabel(self.feed_postscreen)
        self.feedpost_username.setGeometry(QtCore.QRect(60, 70, 731, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.feedpost_username.setFont(font)
        self.feedpost_username.setStyleSheet("QLabel{background-color:rgb(26, 26, 26);border-radius:9px;color:white;}")
        self.feedpost_username.setScaledContents(True)
        self.feedpost_username.setObjectName("feedpost_username")


        #CloseButton
        self.feedpost_close = QtWidgets.QPushButton(self.feed_postscreen)
        self.feedpost_close.setGeometry(QtCore.QRect(10, 70, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.feedpost_close.setFont(font)
        self.feedpost_close.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.feedpost_close.setObjectName("feedpost_close")
        self.feedpost_close.clicked.connect(lambda: feed_post_close())
        
        
        #Image Background
        self.feedpost_image_bg = QtWidgets.QLabel(self.feed_postscreen)
        self.feedpost_image_bg.setGeometry(QtCore.QRect(10, 120, 331, 331))
        self.feedpost_image_bg.setStyleSheet("border:3px solid rgb(29, 29, 29);")
        self.feedpost_image_bg.setText("")
        self.feedpost_image_bg.setScaledContents(True)
        self.feedpost_image_bg.setObjectName("feedpost_image_bg")
        
        #Image
        self.feedpost_image = QtWidgets.QLabel(self.feed_postscreen)
        self.feedpost_image.setGeometry(QtCore.QRect(10, 120, 331, 331))
        self.feedpost_image.setStyleSheet("border:3px solid rgb(29, 29, 29);")
        self.feedpost_image.setText("")
        self.feedpost_image.setScaledContents(True)
        self.feedpost_image.setObjectName("feedpost_image")


        #Background for OPtions
        self.feedpost_toolcase = QtWidgets.QLabel(self.feed_postscreen)
        self.feedpost_toolcase.setGeometry(QtCore.QRect(350, 390, 441, 61))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.feedpost_toolcase.setFont(font)
        self.feedpost_toolcase.setStyleSheet("QLabel{background-color:rgb(26, 26, 26);border-radius:9px;color:white;}")
        self.feedpost_toolcase.setScaledContents(True)
        self.feedpost_toolcase.setObjectName("feedpost_toolcase")

        #Like Button
        self.feedpost_like = QtWidgets.QLabel(self.feed_postscreen)
        self.feedpost_like.setGeometry(QtCore.QRect(370, 400, 44, 40))
        self.feedpost_like.setStyleSheet("background:transparent;")
        self.feedpost_like.setText("")
        self.feedpost_like.setPixmap(QtGui.QPixmap(":/elem/unlike.png"))
        self.feedpost_like.setScaledContents(True)
        self.feedpost_like.setObjectName("feedpost_like")

        self.feedpost_view = QtWidgets.QLabel(self.feed_postscreen)
        self.feedpost_view.setGeometry(QtCore.QRect(135, 234, 100, 100))
        self.feedpost_view.setStyleSheet("background:transparent;")
        self.feedpost_view.setText("")
        self.feedpost_view.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
        self.feedpost_view.setScaledContents(True)
        self.feedpost_view.setObjectName("feedpost_like")

        self.feedpost_view_btn = QtWidgets.QPushButton(self.feed_postscreen)
        self.feedpost_view_btn.setGeometry(QtCore.QRect(135, 234, 100, 100))
        self.feedpost_view_btn.setStyleSheet("background:transparent;")
        self.feedpost_view_btn.clicked.connect(lambda: feed_view_video())





        self.feedpost_like_btn = QtWidgets.QPushButton(self.feed_postscreen)
        self.feedpost_like_btn.setGeometry(QtCore.QRect(370, 400, 44, 40))
        self.feedpost_like_btn.setStyleSheet("background:transparent;")
        self.feedpost_like_btn.clicked.connect(lambda:feed_like_media())
        
        #Save Button
        self.feedpost_save = QtWidgets.QLabel(self.feed_postscreen)
        self.feedpost_save.setGeometry(QtCore.QRect(500, 401, 28, 40))
        self.feedpost_save.setStyleSheet("background:transparent;")
        self.feedpost_save.setText("")
        self.feedpost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
        self.feedpost_save.setScaledContents(True)
        self.feedpost_save.setObjectName("feedpost_save")

        self.feedpost_save_btn = QtWidgets.QPushButton(self.feed_postscreen)
        self.feedpost_save_btn.setGeometry(QtCore.QRect(500, 401, 28, 40))
        self.feedpost_save_btn.setStyleSheet("background:transparent;")
        self.feedpost_save_btn.clicked.connect(lambda:feed_save_media())

        #Comment Button
        self.feedpost_comment = QtWidgets.QLabel(self.feed_postscreen)
        self.feedpost_comment.setGeometry(QtCore.QRect(430, 400, 42, 41))
        self.feedpost_comment.setStyleSheet("background:transparent;")
        self.feedpost_comment.setText("")
        self.feedpost_comment.setPixmap(QtGui.QPixmap(":/elem/comment.png"))
        self.feedpost_comment.setScaledContents(True)
        self.feedpost_comment.setObjectName("feedpost_comment")

        self.feedpost_comment_btn = QtWidgets.QPushButton(self.feed_postscreen)
        self.feedpost_comment_btn.setGeometry(QtCore.QRect(430, 400, 42, 41))
        self.feedpost_comment_btn.setStyleSheet("background:transparent;")

        
        #Copy Hashtag Button
        self.feedpost_copyhash = QtWidgets.QLabel(self.feed_postscreen)
        self.feedpost_copyhash.setGeometry(QtCore.QRect(550, 400, 37, 45))
        self.feedpost_copyhash.setStyleSheet("background:transparent;")
        self.feedpost_copyhash.setText("")
        self.feedpost_copyhash.setPixmap(QtGui.QPixmap(":/elem/uncopy.png"))
        self.feedpost_copyhash.setScaledContents(True)
        self.feedpost_copyhash.setObjectName("feedpost_copyhash")
        
        self.feedpost_copyhash_btn = QtWidgets.QPushButton(self.feed_postscreen)
        self.feedpost_copyhash_btn.setGeometry(QtCore.QRect(550, 400, 37, 45))
        self.feedpost_copyhash_btn.setStyleSheet("background:transparent;")
        self.feedpost_copyhash_btn.clicked.connect(lambda: feed_copyhashtag())

        #Traslate Caption Button
        self.feedpost_translate = QtWidgets.QLabel(self.feed_postscreen)
        self.feedpost_translate.setGeometry(QtCore.QRect(610, 400, 41, 41))
        self.feedpost_translate.setStyleSheet("background:transparent;")
        self.feedpost_translate.setText("")
        self.feedpost_translate.setPixmap(QtGui.QPixmap(":/elem/untranslate.png"))
        self.feedpost_translate.setScaledContents(True)
        self.feedpost_translate.setObjectName("feedpost_translate")
        
        
        self.feedpost_translate_btn = QtWidgets.QPushButton(self.feed_postscreen)
        self.feedpost_translate_btn.setGeometry(QtCore.QRect(610, 400, 41, 41))
        self.feedpost_translate_btn.setStyleSheet("background:transparent;")
        self.feedpost_translate_btn.clicked.connect(lambda: feed_translate_eng())

        #Download Post Button
        self.feedpost_download = QtWidgets.QLabel(self.feed_postscreen)
        self.feedpost_download.setGeometry(QtCore.QRect(670, 400, 37, 41))
        self.feedpost_download.setStyleSheet("background:transparent;")
        self.feedpost_download.setText("")
        self.feedpost_download.setPixmap(QtGui.QPixmap(":/elem/download.png"))
        self.feedpost_download.setScaledContents(True)
        self.feedpost_download.setObjectName("feedpost_download")

        self.feedpost_download_btn = QtWidgets.QPushButton(self.feed_postscreen)
        self.feedpost_download_btn.setGeometry(QtCore.QRect(670, 400, 37, 41))
        self.feedpost_download_btn.setStyleSheet("background:transparent;")
        self.feedpost_download_btn.clicked.connect(lambda:feed_download_media())


        #Caption Bg
        self.feedpost_caption_2 = QtWidgets.QLabel(self.feed_postscreen)
        self.feedpost_caption_2.setGeometry(QtCore.QRect(350, 120, 439, 165))
        self.feedpost_caption_2.setMaximumSize(QtCore.QSize(440, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.feedpost_caption_2.setFont(font)
        self.feedpost_caption_2.setStyleSheet("QLabel{background-color:rgb(26, 26, 26);border-radius:9px;color:white;padding:10px; padding-bottom:30px}")
        self.feedpost_caption_2.setScaledContents(True)
        self.feedpost_caption_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.feedpost_caption_2.setWordWrap(True)
        self.feedpost_caption_2.setObjectName("feedpost_caption_2")
        #Caption
        self.feedpost_edit = QtWidgets.QLabel(self.feed_postscreen)
        self.feedpost_edit.setGeometry(QtCore.QRect(360, 260, 61, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.feedpost_edit.setFont(font)
        self.feedpost_edit.setStyleSheet("background:transparent;")
        self.feedpost_edit.setScaledContents(True)
        self.feedpost_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.feedpost_edit.setWordWrap(True)
        self.feedpost_edit.setObjectName("feedpost_edit")
        self.feedpost_date = QtWidgets.QLabel(self.feed_postscreen)
        self.feedpost_date.setGeometry(QtCore.QRect(534, 260, 231, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.feedpost_date.setFont(font)
        self.feedpost_date.setStyleSheet("background:transparent;")
        self.feedpost_date.setScaledContents(True)
        self.feedpost_date.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.feedpost_date.setWordWrap(True)
        self.feedpost_date.setObjectName("feedpost_date")
        self.caption_scrollarea = QtWidgets.QScrollArea(self.feed_postscreen)
        self.caption_scrollarea.setGeometry(QtCore.QRect(350, 120, 434, 130))#191
        self.caption_scrollarea.setStyleSheet("background:transparent")
        self.caption_scrollarea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.caption_scrollarea.setFrameShadow(QtWidgets.QFrame.Plain)
        self.caption_scrollarea.setLineWidth(0)
        self.caption_scrollarea.setWidgetResizable(True)
        self.caption_scrollarea.setObjectName("caption_scrollarea")
        self.caption_scrollcontent = QtWidgets.QWidget()
        self.caption_scrollcontent.setGeometry(QtCore.QRect(0, 0, 418, 260))
        self.caption_scrollcontent.setObjectName("caption_scrollcontent")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.caption_scrollcontent)
        self.verticalLayout.setObjectName("verticalLayout")
        self.feedpost_caption = QtWidgets.QLabel(self.caption_scrollcontent)
        self.feedpost_caption.setMaximumSize(QtCore.QSize(440, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.feedpost_caption.setFont(font)
        self.feedpost_caption.setStyleSheet("QLabel{background-color:transparent;border-radius:9px;color:white;padding:3px}")
        self.feedpost_caption.setScaledContents(True)
        self.feedpost_caption.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.feedpost_caption.setWordWrap(True)
        self.feedpost_caption.setObjectName("feedpost_caption")
        self.verticalLayout.addWidget(self.feedpost_caption)
        self.caption_scrollarea.setWidget(self.caption_scrollcontent)
        self.scrolllbar = QtWidgets.QScrollBar(self.searchscreen)
        self.scrolllbar.setStyleSheet("QScrollBar:vertical{border: none;background: rgb(45,45,45);width: 10px;margin: 0px 0 0px 0;}QScrollBar::handle:vertical{background: dark grey;min-height: 26px;border-radius: 5px;}QScrollBar::add-line:vertical{background: none;height: 26px;subcontrol-position: bottom;subcontrol-origin: margin;}QScrollBar::sub-line:vertical{background: none;height: 0px;subcontrol-position: top left;subcontrol-origin: margin;position: absolute;}QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical{background: rgb(45,45,45);}")
        self.caption_scrollarea.setVerticalScrollBar(self.scrolllbar)

        #likedby_bg Bg
        self.likedby_bg = QtWidgets.QLabel(self.feed_postscreen)
        self.likedby_bg.setGeometry(QtCore.QRect(350, 291, 439, 48))
        self.likedby_bg.setMaximumSize(QtCore.QSize(440, 16777215))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.likedby_bg.setFont(font)
        self.likedby_bg.setStyleSheet("QLabel{background-color:rgb(26, 26, 26);border-radius:9px;color:white;padding:10px; padding-bottom:30px}")
        self.likedby_bg.setScaledContents(True)
        self.likedby_bg.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.likedby_bg.setWordWrap(True)
        self.likedby_bg.setObjectName("likedby_bg")


        self.feedpost_lb_caption = QtWidgets.QLabel(self.feed_postscreen)
        self.feedpost_lb_caption.setGeometry(QtCore.QRect(350, 297, 439, 40))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(11)
        self.feedpost_lb_caption.setFont(font)
        self.feedpost_lb_caption.setStyleSheet("background:transparent;padding-left:6px;padding-right:6px")
        self.feedpost_lb_caption.setScaledContents(True)
        self.feedpost_lb_caption.setWordWrap(True)
        self.feedpost_lb_caption.setObjectName("feedpost_date")











        #Like Count
        self.feedpost_likecount = QtWidgets.QLabel(self.feed_postscreen)
        self.feedpost_likecount.setGeometry(QtCore.QRect(350, 350, 211, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.feedpost_likecount.setFont(font)
        self.feedpost_likecount.setStyleSheet("QLabel{background-color:rgb(26, 26, 26);border-radius:5px;color:white;}")
        self.feedpost_likecount.setScaledContents(True)
        self.feedpost_likecount.setAlignment(QtCore.Qt.AlignCenter)
        self.feedpost_likecount.setWordWrap(True)
        self.feedpost_likecount.setObjectName("feedpost_likecount")

        #Comment Count
        self.feedpost_commentcount = QtWidgets.QLabel(self.feed_postscreen)
        self.feedpost_commentcount.setGeometry(QtCore.QRect(570, 350, 221, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.feedpost_commentcount.setFont(font)
        self.feedpost_commentcount.setStyleSheet("QLabel{background-color:rgb(26, 26, 26);border-radius:5px;color:white;}")
        self.feedpost_commentcount.setScaledContents(True)
        self.feedpost_commentcount.setAlignment(QtCore.Qt.AlignCenter)
        self.feedpost_commentcount.setWordWrap(True)
        self.feedpost_commentcount.setObjectName("feedpost_commentcount")


        #Corousell Post Count
        self.feedpost_postcount = QtWidgets.QLabel(self.feed_postscreen)
        self.feedpost_postcount.setGeometry(QtCore.QRect(228, 134, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.feedpost_postcount.setFont(font)
        self.feedpost_postcount.setStyleSheet("QLabel{background-color:rgb(88, 88, 88);border-radius:9px;color:white;}")
        self.feedpost_postcount.setScaledContents(True)
        self.feedpost_postcount.setAlignment(QtCore.Qt.AlignCenter)
        self.feedpost_postcount.setWordWrap(True)
        self.feedpost_postcount.setObjectName("feedpost_postcount")


        #Next Button
        self.feedpost_next = QtWidgets.QPushButton(self.feed_postscreen)
        self.feedpost_next.setGeometry(QtCore.QRect(290, 400, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.feedpost_next.setFont(font)
        self.feedpost_next.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.feedpost_next.setObjectName("feedpost_next")
        self.feedpost_next.clicked.connect(lambda:feed_next_corousell())

        #Back Button
        self.feedpost_back = QtWidgets.QPushButton(self.feed_postscreen)
        self.feedpost_back.setGeometry(QtCore.QRect(20, 400, 41, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.feedpost_back.setFont(font)
        self.feedpost_back.setStyleSheet("QPushButton{background-color:rgb(29, 29, 29);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.feedpost_back.setObjectName("feedpost_back")
        self.feedpost_back.clicked.connect(lambda:feed_back_corousell())


        
        #TaskBar  
        self.TB = QtWidgets.QLabel(self.feed_postscreen)
        self.TB.setGeometry(QtCore.QRect(-40, 480, 861, 71))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.TB.setFont(font)
        self.TB.setStyleSheet("background:rgb(36, 36, 36);")
        self.TB.setScaledContents(True)
        self.TB.setObjectName("TB")



        
        self.TB_Home = QtWidgets.QPushButton(self.feed_postscreen)
        self.TB_Home.setGeometry(QtCore.QRect(10, 490, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.TB_Home.setFont(font)
        self.TB_Home.setObjectName("TB_Home")
        self.TB_Home.clicked.connect(lambda: setscreen_feed())
        self.TB_Home.setStyleSheet("QPushButton{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.TB_Home.clicked.connect(lambda: setscreen_feedmain())
        
        self.TB_Search = QtWidgets.QPushButton(self.feed_postscreen)
        self.TB_Search.setGeometry(QtCore.QRect(170, 490, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.TB_Search.setFont(font)
        self.TB_Search.setStyleSheet("QPushButton{background-color:rgb(50, 50, 50);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.TB_Search.setObjectName("TB_Search")
        self.TB_Search.clicked.connect(lambda: setscreen_search())


        
        self.TB_Profile = QtWidgets.QPushButton(self.feed_postscreen)
        self.TB_Profile.setGeometry(QtCore.QRect(490, 490, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.TB_Profile.setFont(font)
        self.TB_Profile.setObjectName("TB_Profile")
        self.TB_Profile.clicked.connect(lambda: setscreen_profile())
        self.TB_Profile.setStyleSheet("QPushButton{background-color:rgb(50, 50, 50);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")

        
        self.TB_Timeline = QtWidgets.QPushButton(self.feed_postscreen)
        self.TB_Timeline.setGeometry(QtCore.QRect(330, 490, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.TB_Timeline.setFont(font)
        self.TB_Timeline.setStyleSheet("QPushButton{background-color:rgb(50, 50, 50);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.TB_Timeline.setObjectName("TB_Timeline")
        #self.TB_Timeline.clicked.connect(lambda: timelinescreen())


        
        self.TB_Settings = QtWidgets.QPushButton(self.feed_postscreen)
        self.TB_Settings.setGeometry(QtCore.QRect(650, 490, 150, 41))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(12)
        self.TB_Settings.setFont(font)
        self.TB_Settings.setStyleSheet("QPushButton{background-color:rgb(50, 50, 50);border-radius:9px;color:white;}QPushButton::hover{background-color:qlineargradient(spread:pad, x1:0, y1:0.699, x2:1, y2:1, stop:0.0568182 rgba(255, 0, 127, 255), stop:1 rgba(144, 0, 255, 255));border-radius:9px;color:rgb(255, 142, 231);}")
        self.TB_Settings.setObjectName("TB_Settings")
        #self.TB_Timeline.clicked.connect(lambda: settingscreen())

        self.feedpost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\">Edited</span></p></body></html>"))
        self.feedpost_textlogo.setText(_translate("MainWindow", " SuperInsta"))
        self.feedpost_signout.setText(_translate("MainWindow", "Sign Out"))
        self.feedpost_username.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">@username  - Location, Location</span></p></body></html>"))
        self.feedpost_close.setText(_translate("MainWindow", "x"))
        self.feedpost_toolcase.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.feedpost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#f1f1f1;\">Caption Here.</span></p></body></html>"))
        self.feedpost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by @mostuselessboy1hfk35hch4h1h2b2h, @mostuselessboy1hfk35hch4h1h2b2h and 1,342 others. </span></p></body></html>"))
        self.feedpost_likecount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Likes: 1,234</span></p></body></html>"))
        self.feedpost_commentcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Comments: 234</span></p></body></html>"))
        self.feedpost_postcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Post 10/10</span></p></body></html>"))
        self.feedpost_next.setText(_translate("MainWindow", ">"))
        self.feedpost_back.setText(_translate("MainWindow", "<"))
        self.feedpost_date.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" color:#919191;\">24 May 2020</span></p></body></html>"))
        self.TB_Home.setText(_translate("MainWindow", "Home"))
        self.TB_Search.setText(_translate("MainWindow", "Search"))
        self.TB_Profile.setText(_translate("MainWindow", "Your Profile"))
        self.TB_Timeline.setText(_translate("MainWindow", "Timeline"))
        self.TB_Settings.setText(_translate("MainWindow", "SuperInsta"))





########################################### FUNCTIONS################################################


        #Adding/Setting Windows
        MainWindow.central_widget.addWidget(self.homescreen)
        MainWindow.central_widget.addWidget(self.loginscreen)
        MainWindow.central_widget.addWidget(self.searchscreen)
        MainWindow.central_widget.addWidget(self.profilescreen)
        MainWindow.central_widget.addWidget(self.postscreen)
        MainWindow.central_widget.addWidget(self.mypostscreen)
        MainWindow.central_widget.addWidget(self.onepostscreen)
        MainWindow.central_widget.addWidget(self.onemypostscreen)
        MainWindow.central_widget.addWidget(self.likepostscanscreen)
        MainWindow.central_widget.addWidget(self.feed_screen)
        MainWindow.central_widget.addWidget(self.loadingscreen)
        MainWindow.central_widget.addWidget(self.feed_postscreen)
        
        
        global feed_seen
        feed_seen = "012345"
        global searchsscr_select
        searchsscr_select = "search"
        global homesscr_select
        homesscr_select = "profile"
        global feedsscr_select
        feedsscr_select = "feed"
        global last_update_profile
        last_update_profile = int(datetime.now(pytz.timezone('Asia/Calcutta')).strftime("%H%M%S"))-25
        def setscreen_search():
            global searchsscr_select
            if searchsscr_select == "search":
                MainWindow.central_widget.setCurrentWidget(self.searchscreen)
            elif searchsscr_select == "profile":
                MainWindow.central_widget.setCurrentWidget(self.homescreen)
            elif searchsscr_select == "posts":
                MainWindow.central_widget.setCurrentWidget(self.postscreen)
            elif searchsscr_select == "onepost":
                MainWindow.central_widget.setCurrentWidget(self.onepostscreen)

        def setscreen_searchmain():
            global searchsscr_select
            searchsscr_select = "search"
            MainWindow.central_widget.setCurrentWidget(self.searchscreen)
        def setscreen_home():
            MainWindow.central_widget.setCurrentWidget(self.homescreen)
        def setscreen_onepost():
            global searchsscr_select
            searchsscr_select = "onepost"
            MainWindow.central_widget.setCurrentWidget(self.onepostscreen)
        def setscreen_onemypost():
            global homesscr_select
            homesscr_select = "onemypost"
            MainWindow.central_widget.setCurrentWidget(self.onemypostscreen)
        def setscreen_posts_screen():
            MainWindow.central_widget.setCurrentWidget(self.postscreen)
            posts_screen()
        def setscreen_feedmain():
            global feedsscr_select
            feedsscr_select = "feed"
            MainWindow.central_widget.setCurrentWidget(self.feed_screen)
        def setscreen_feed():
            global feedsscr_select
            if feedsscr_select == "feed":
                MainWindow.central_widget.setCurrentWidget(self.feed_screen)
            elif feedsscr_select == "post":
                MainWindow.central_widget.setCurrentWidget(self.feed_postscreen)
        def setscreen_feedpost():
            global feedsscr_select
            feedsscr_select = "post"
            MainWindow.central_widget.setCurrentWidget(self.feed_postscreen)
        def setscreen_myposts_screen():
            MainWindow.central_widget.setCurrentWidget(self.mypostscreen)
            myposts_screen()
        def setscreen_likedposts_screen():
            MainWindow.central_widget.setCurrentWidget(self.postscreen)
            likedposts_screen()
        def setscreen_profile():
            global homesscr_select
            if homesscr_select == "profile":
                MainWindow.central_widget.setCurrentWidget(self.profilescreen)
            if homesscr_select == "posts":
                MainWindow.central_widget.setCurrentWidget(self.mypostscreen)
            if homesscr_select == "onemypost":
                MainWindow.central_widget.setCurrentWidget(self.onemypostscreen)
            if self.profile_account.text() == """<html><head/><body><p><span style=" font-size:12pt; color:#757575;">Account Type</span></p></body></html>""":
               update_myprofile()
        def setscreen_profilemain():
            global homesscr_select
            homesscr_select = "profile"
            MainWindow.central_widget.setCurrentWidget(self.profilescreen)
        global user
        global username
        if path.exists("s5a5n5d5w5i5c5h.json"):
           MainWindow.central_widget.setCurrentWidget(self.feed_screen)
           user = cookie.login_instagram(username, password)
           cred_file = open("cred", "r")
           username = cred_file.read()
           cred_file.close()          
        else:
           MainWindow.central_widget.setCurrentWidget(self.loginscreen)

        #Instagram-login
        def login_instagram_thread():
           global user
           global username
           try:
              username = self.login_usernamebox.text()
              password = self.login_passwordbox.text()
              
              user = cookie.login_instagram(username, password)
              cred_file = open("cred", "w")
              cred_file.write(username)
              cred_file.close()
              self.loadingscreen_text.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\">Welcome Bro to SuperInsta</span></p></body></html>"))
              self.login_errormsg.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#eb5659;\"></span></p></body></html>"))
              MainWindow.central_widget.setCurrentWidget(self.feed_screen)
              loadfeed()
           except Exception:
              self.login_errormsg.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#eb5659;\">        Wrong Username or Password!</span></p></body></html>"))
              
        def login_instagram():
           thread2 = threading.Thread(target= login_instagram_thread())
           thread2.start()



        #Follow User
        def follow_user_thread():
           global search_username_id
           global user
           if self.follow.text()== "Follow":
               self.follow.setText(_translate("MainWindow", "Unfollow"))
               user.friendships_create(search_username_id) 

           elif self.follow.text()== "Unfollow":
               self.follow.setText(_translate("MainWindow", "Follow"))
               user.friendships_destroy(search_username_id)
        def follow_user():
           thread5 = threading.Thread(target = follow_user_thread )
           thread5.start()




        #Block User
        def block_user_thread():
           global search_username_id
           global user
           if self.block.text()== "Block":
               self.block.setText(_translate("MainWindow", "Unblock"))
               user.friendships_block(search_username_id) 

           elif self.block.text()== "Unblock":
               self.block.setText(_translate("MainWindow", "Block"))
               user.friendships_unblock(search_username_id)
        def block_user():
           thread5 = threading.Thread(target = block_user_thread )
           thread5.start()




        #Hide/ Unhide Story
        def hide_story_thread():
           global search_username_id
           global user
           if self.hidestory.text()== "Hide Story":
               self.hidestory.setText(_translate("MainWindow", "Unhide Story"))
               user.block_friend_reel(search_username_id) 

           elif self.hidestory.text()== "Unhide Story":
               self.hidestory.setText(_translate("MainWindow", "Hide Story"))
               user.unblock_friend_reel(search_username_id)
        def hide_story():
           thread5 = threading.Thread(target = hide_story_thread)
           thread5.start()



           
        def logout_instagram():
           os.remove("s5a5n5d5w5i5c5h.json")
           os.remove("my_insta_image.png")
           MainWindow.central_widget.setCurrentWidget(self.loginscreen)


        #Function: Search User
        def search_user_thread():
           global searchsscr_select
           searchsscr_select = "profile"
           MainWindow.setGraphicsEffect(self.blur_effect)
           self.blur_effect.setBlurRadius(5)
           MainWindow.setEnabled(False)
           global user
           global usertobesearched
           global search_username_id
           global search_username_status
           global search_username_isprivate
           global search_username_mediacount
           search_username = usertobesearched[1:]
           search_username_info = user.username_info(search_username)
           search_username_url = ((search_username_info['user'])['hd_profile_pic_url_info'])['url']
           keys_check = ((search_username_info['user']).keys())
           search_username_username = ((search_username_info['user'])['username'])
           search_username_id = ((search_username_info['user'])['pk'])
           search_user_extra()
           search_username_mediacount = ((search_username_info['user'])['media_count'])
           search_username_website = ((search_username_info['user'])['external_url'])
           search_username_follower = ((search_username_info['user'])['follower_count'])
           search_username_following = ((search_username_info['user'])['following_count'])
           search_username_isverified = ((search_username_info['user'])['is_verified'])
           search_username_isprivate = ((search_username_info['user'])['is_private'])
           search_username_bio = ((search_username_info['user'])['biography'])
           search_username_mutual = ((search_username_info['user'])['mutual_followers_count'])
           search_username_dp = requests.get(search_username_url)
           self.bio.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#4d4d4d;\">"+search_username_bio+"</span></p></body></html>"))
           self.username.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">@"+search_username_username+"</span></p></body></html>"))
           self.website.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#00aaff;\">"+search_username_website+"</span></p></body></html>"))
           self.following.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Following: "+str(numconv(search_username_following))+"</span></p></body></html>"))
           self.follower.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Followers: "+str(numconv(search_username_follower))+"</span></p></body></html>"))
           self.post.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Total Post: "+str(numconv(search_username_mediacount))+"</span></p></body></html>"))
           with open("insta_image.png", "wb") as insta_dp_cache:
              insta_dp_cache.write(search_username_dp.content)
              insta_dp_cache.close()
           self.image.setPixmap(QtGui.QPixmap("insta_image.png"))

           
           if search_username_isprivate == True:
              self.account.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#757575;\">Private Account</span></p></body></html>"))
           else:
              self.account.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#757575;\">Public Account</span></p></body></html>"))
           if search_username_mutual >= 1:
              search_username_mutual_id = ((search_username_info['user'])['profile_context_mutual_follow_ids'])
              search_username_profile_ctx = ((search_username_info['user'])['profile_context'])
              self.mutual.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#b3b1b1;\">"+search_username_profile_ctx+"</span></p></body></html>"))
           else:
              self.mutual.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#4d4d4d;\">Not followed by anyone you Follow</span></p></body></html>"))
           self.blur_effect.setBlurRadius(0)
           MainWindow.setEnabled(True)
           MainWindow.setEnabled(True)
        def search_user():
           thread1 = threading.Thread(target = search_user_thread)
           thread1.start()


        def search_user_extras_thread():
           global user
           global search_username_id
           global search_username_status
           global search_username_isprivate
           search_username_status = user.friendships_show(search_username_id)
           if search_username_status['following']== False and search_username_isprivate == True:
               self.viewposts.setHidden(True)
           else:
               self.viewposts.setHidden(False)
           if search_username_status['following']== True:
               self.follow.setText(_translate("MainWindow", "Unfollow"))
           elif search_username_status['following']== False:
               self.follow.setText(_translate("MainWindow", "Follow"))
           if search_username_status['followed_by']== True:
               self.followsyou.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Follows You</span></p></body></html>"))
           else:
               self.followsyou.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Not Follows You</span></p></body></html>"))
           if search_username_status['blocking']== True:
              self.block.setText(_translate("MainWindow", "Unblock"))
           elif search_username_status['blocking']== False:
              self.block.setText(_translate("MainWindow", "Block"))
           if search_username_status['is_blocking_reel']== True:
              self.hidestory.setText(_translate("MainWindow", "Unhide Story"))
           elif search_username_status['is_blocking_reel']== False:
              self.hidestory.setText(_translate("MainWindow", "Hide Story"))

        def search_user_extra():
           thread6 = threading.Thread(target = search_user_extras_thread)
           thread6.start()
         
        #Function: Search User
        def update_myprofile_thread():
           global last_update_profile
           update_profile_now_time = datetime.now(pytz.timezone('Asia/Calcutta')).strftime("%H%M%S")
           diff_timestamp = (int(int(update_profile_now_time)-int(last_update_profile)))
           if diff_timestamp < 25:
              pass
           else:
              MainWindow.setGraphicsEffect(self.blur_effect)
              self.blur_effect.setBlurRadius(5)
              self.profile_refresh.setEnabled(False)
              global user
              search_username = username
              #print(username)
              search_username_info = user.username_info(search_username)
              search_username_url = ((search_username_info['user'])['hd_profile_pic_url_info'])['url']
              keys_check = ((search_username_info['user']).keys())
              search_username_username = ((search_username_info['user'])['username'])
              search_username_id = ((search_username_info['user'])['pk'])
              search_username_mediacount = ((search_username_info['user'])['media_count'])
              search_username_website = ((search_username_info['user'])['external_url'])
              search_username_follower = ((search_username_info['user'])['follower_count'])
              search_username_following = ((search_username_info['user'])['following_count'])
              search_username_isverified = ((search_username_info['user'])['is_verified'])
              search_username_isprivate = ((search_username_info['user'])['is_private'])
              search_username_bio = ((search_username_info['user'])['biography'])
              search_username_dp = requests.get(search_username_url)
              self.profile_bio.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#4d4d4d;\">"+search_username_bio+"</span></p></body></html>"))
              self.profile_username.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">@"+search_username_username+"</span></p></body></html>"))
              self.profile_website.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#00aaff;\">"+search_username_website+"</span></p></body></html>"))
              self.profile_following.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Following: "+str(numconv(search_username_following))+"</span></p></body></html>"))
              self.profile_follower.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Followers: "+str(numconv(search_username_follower))+"</span></p></body></html>"))
              self.profile_post.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Total Post: "+str(numconv(search_username_mediacount))+"</span></p></body></html>"))
              #print(user.saved_feed())
              if path.exists("my_insta_image.png"):
                 self.profile_image.setPixmap(QtGui.QPixmap("my_insta_image.png"))
              else:
                 with open("my_insta_image.png", "wb") as insta_mydp_cache:
                    insta_mydp_cache.write(search_username_dp.content)
                    insta_mydp_cache.close()
                 self.profile_image.setPixmap(QtGui.QPixmap("my_insta_image.png"))
              if search_username_isprivate == True:
                 self.profile_account.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#757575;\">Private Account</span></p></body></html>"))
              else:
                 self.profile_account.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; color:#757575;\">Public Account</span></p></body></html>"))
              self.blur_effect.setBlurRadius(0)
              last_update_profile = datetime.now(pytz.timezone('Asia/Calcutta')).strftime("%H%M%S")
              self.profile_refresh.setEnabled(True)
        def update_myprofile():
           thread4 = threading.Thread(target = update_myprofile_thread)
           thread4.start()


  


        #Instagram-Search

        def searchfromhomescreen():
           searchfromhomequery = self.search_box.text()
           searchuser_list(searchfromhomequery)
           self.search_box.setText(searchfromhomequery)
           self.search_search_box.setText(searchfromhomequery)
           MainWindow.central_widget.setCurrentWidget(self.searchscreen)
           
        def searchfromsearchscreen():
           searchfromsearchquery = self.search_search_box.text()
           searchuser_list(searchfromsearchquery)
           self.search_box.setText(searchfromsearchquery)
           self.search_search_box.setText(searchfromsearchquery)
           
        def searchfromfeedscreen():
           searchfromsearchquery = self.search_search_box.text()
           searchuser_list(searchfromsearchquery)
           self.search_box.setText(searchfromsearchquery)
           self.search_search_box.setText(searchfromsearchquery)
           
        def searchuser_list(search_query):
           global searchsscr_select
           searchsscr_select = "search"
           global user
           global username
           global usertobesearched
           self.userlist_user14.setHidden(True)
           self.userlist_user13.setHidden(True)
           self.userlist_user12.setHidden(True)
           self.userlist_user11.setHidden(True)
           self.userlist_user10.setHidden(True)
           self.userlist_user9.setHidden(True)
           self.userlist_user8.setHidden(True)
           self.userlist_user7.setHidden(True)
           self.userlist_user6.setHidden(True)
           self.userlist_user5.setHidden(True)
           self.userlist_user4.setHidden(True)
           self.userlist_user3.setHidden(True)
           self.userlist_user2.setHidden(True)
           self.userlist_user1.setHidden(True)
           
           new_searchuser_list_list = []

           searchuser_list_query = search_query
           searchuser_list_list = (user.search_users(searchuser_list_query))
           x=0
           new_searchlist=[]
           while True:
               try:
                   search_user_for_list = (((searchuser_list_list['users'])[x])['username'])
                   if search_user_for_list != username:
                      new_searchlist.append(search_user_for_list)
                   x=x+1
                   if x ==14:
                       break
               except Exception:
                   break
           if len(new_searchlist) <= 0:
               self.userlist_user1.setHidden(False)
               self.userlist_user1.setText(_translate("MainWindow", "No Result Found!"))
           
           if len(new_searchlist) > 0:
               self.userlist_user1.setHidden(False)
               self.userlist_user1.setText(_translate("MainWindow", "@"+new_searchlist[0]))
               self.userlist_user1.clicked.connect(lambda:userlist_user1_click())
               def userlist_user1_click():
                  global usertobesearched
                  usertobesearched = self.userlist_user1.text()
                  search_user()
                  MainWindow.central_widget.setCurrentWidget(self.homescreen)

               
           if len(new_searchlist) > 1:
               self.userlist_user2.setHidden(False)
               self.userlist_user2.setText(_translate("MainWindow", "@"+new_searchlist[1]))
               self.userlist_user2.clicked.connect(lambda:userlist_user2_click())
               def userlist_user2_click():
                  global usertobesearched
                  usertobesearched = self.userlist_user2.text()
                  search_user()
                  MainWindow.central_widget.setCurrentWidget(self.homescreen)

               
           if len(new_searchlist) > 2:
               self.userlist_user3.setHidden(False)
               self.userlist_user3.setText(_translate("MainWindow", "@"+new_searchlist[2]))
               self.userlist_user3.clicked.connect(lambda:userlist_user3_click())
               def userlist_user3_click():
                  global usertobesearched
                  usertobesearched = self.userlist_user3.text()
                  search_user()
                  MainWindow.central_widget.setCurrentWidget(self.homescreen)
                  
           if len(new_searchlist) > 3:
               self.userlist_user4.setHidden(False)
               self.userlist_user4.setText(_translate("MainWindow", "@"+new_searchlist[3]))
               self.userlist_user4.clicked.connect(lambda:userlist_user4_click())
               def userlist_user4_click():
                  global usertobesearched
                  usertobesearched = self.userlist_user4.text()
                  search_user()
                  MainWindow.central_widget.setCurrentWidget(self.homescreen)               
               
           if len(new_searchlist) > 4:
               self.userlist_user5.setHidden(False)
               self.userlist_user5.setText(_translate("MainWindow", "@"+new_searchlist[4]))
               self.userlist_user5.clicked.connect(lambda:userlist_user5_click())
               def userlist_user5_click():
                  global usertobesearched
                  usertobesearched = self.userlist_user5.text()
                  search_user()
                  MainWindow.central_widget.setCurrentWidget(self.homescreen)
                  
           if len(new_searchlist) > 5:
               self.userlist_user6.setHidden(False)
               self.userlist_user6.setText(_translate("MainWindow", "@"+new_searchlist[5]))
               self.userlist_user6.clicked.connect(lambda:userlist_user6_click())
               def userlist_user6_click():
                  global usertobesearched
                  usertobesearched = self.userlist_user6.text()
                  search_user()
                  MainWindow.central_widget.setCurrentWidget(self.homescreen)
               
           if len(new_searchlist) > 6:
               self.userlist_user7.setHidden(False)
               self.userlist_user7.setText(_translate("MainWindow", "@"+new_searchlist[6]))
               self.userlist_user7.clicked.connect(lambda:userlist_user7_click())
               def userlist_user7_click():
                  global usertobesearched
                  usertobesearched = self.userlist_user7.text()
                  search_user()
                  MainWindow.central_widget.setCurrentWidget(self.homescreen)
               
           if len(new_searchlist) > 7:
               self.userlist_user8.setHidden(False)
               self.userlist_user8.setText(_translate("MainWindow", "@"+new_searchlist[7]))
               self.userlist_user8.clicked.connect(lambda:userlist_user8_click())
               def userlist_user8_click():
                  global usertobesearched
                  usertobesearched = self.userlist_user8.text()
                  search_user()
                  MainWindow.central_widget.setCurrentWidget(self.homescreen)
               
           if len(new_searchlist) > 8:
               self.userlist_user9.setHidden(False)
               self.userlist_user9.setText(_translate("MainWindow", "@"+new_searchlist[8]))
               self.userlist_user9.clicked.connect(lambda:userlist_user9_click())
               def userlist_user9_click():
                  global usertobesearched
                  usertobesearched = self.userlist_user9.text()
                  search_user()
                  MainWindow.central_widget.setCurrentWidget(self.homescreen)

           if len(new_searchlist) > 9:
               self.userlist_user10.setHidden(False)
               self.userlist_user10.setText(_translate("MainWindow", "@"+new_searchlist[9]))
               self.userlist_user10.clicked.connect(lambda:userlist_user10_click())
               def userlist_user10_click():
                  global usertobesearched
                  usertobesearched = self.userlist_user10.text()
                  search_user()
                  MainWindow.central_widget.setCurrentWidget(self.homescreen)

           if len(new_searchlist) > 10:
               self.userlist_user11.setHidden(False)
               self.userlist_user11.setText(_translate("MainWindow", "@"+new_searchlist[10]))
               self.userlist_user11.clicked.connect(lambda:userlist_user11_click())
               def userlist_user11_click():
                  global usertobesearched
                  usertobesearched = self.userlist_user11.text()
                  search_user()
                  MainWindow.central_widget.setCurrentWidget(self.homescreen)

           if len(new_searchlist) > 11:
               self.userlist_user12.setHidden(False)
               self.userlist_user12.setText(_translate("MainWindow", "@"+new_searchlist[11]))
               self.userlist_user12.clicked.connect(lambda:userlist_user12_click())
               def userlist_user12_click():
                  global usertobesearched
                  usertobesearched = self.userlist_user12.text()
                  search_user()
                  MainWindow.central_widget.setCurrentWidget(self.homescreen)

           if len(new_searchlist) > 12:
               self.userlist_user13.setHidden(False)
               self.userlist_user13.setText(_translate("MainWindow", "@"+new_searchlist[12]))
               self.userlist_user13.clicked.connect(lambda:userlist_user13_click())
               def userlist_user13_click():
                  global usertobesearched
                  usertobesearched = self.userlist_user13.text()
                  search_user()
                  MainWindow.central_widget.setCurrentWidget(self.homescreen)

           if len(new_searchlist) > 13:
               self.userlist_user14.setHidden(False)
               self.userlist_user14.setText(_translate("MainWindow", "@"+new_searchlist[13]))
               self.userlist_user14.clicked.connect(lambda:userlist_user14_click())
               def userlist_user14_click():
                  global usertobesearched
                  usertobesearched = self.userlist_user14.text()
                  search_user()
                  MainWindow.central_widget.setCurrentWidget(self.homescreen)



        #Post -Function  
        def posts_screen_thread():
           global searchsscr_select
           searchsscr_select = "posts"
           MainWindow.setGraphicsEffect(self.blur_effect)
           self.blur_effect.setBlurRadius(5)
           MainWindow.setEnabled(False)
           global postofuser
           global feed
           global user
           global posts
           global page_no
           global postno_1
           global postno_2
           global postno_3
           global postno_4
           global postno_5
           global postno_6
           global postno_7
           global postno_8
           global postno_9
           global postno_10
           global usertobesearched
           #print(usertobesearched)
           postno_1 = 0
           postno_2 = 1
           postno_3 = 2
           postno_4 = 3
           postno_5 = 4
           postno_6 = 5
           postno_7 = 6
           postno_8 = 7
           postno_9 = 8
           postno_10 =9
           page_no = 1
           postofuser = usertobesearched[1:]
           feed = user.username_feed(postofuser)
           posts = feed['items']


           self.post_post1.setHidden(True)
           self.post_type1.setHidden(True)
           
           self.post_post2.setHidden(True)
           self.post_type2.setHidden(True)
           
           self.post_post3.setHidden(True)
           self.post_type3.setHidden(True)
           
           self.post_post4.setHidden(True)
           self.post_type4.setHidden(True)
           
           self.post_post5.setHidden(True)
           self.post_type5.setHidden(True)
           
           self.post_post6.setHidden(True)
           self.post_type6.setHidden(True)
           
           self.post_post7.setHidden(True)
           self.post_type7.setHidden(True)
           
           self.post_post8.setHidden(True)
           self.post_type8.setHidden(True)
           
           self.post_post9.setHidden(True)
           self.post_type9.setHidden(True)
           
           self.post_post10.setHidden(True)
           self.post_type10.setHidden(True)
           MainWindow.setEnabled(True)
           self.blur_effect.setBlurRadius(0)
           global postdata1
           global postdata2
           global postdata3
           global postdata4
           global postdata5
           global postdata6
           global postdata7
           global postdata8
           global postdata9
           global postdata10          


           #Post 1 Setup
           self.post_page.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Page 1</span></p></body></html>"))
           self.post_username.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">"+ str(usertobesearched)+"</span></p></body></html>"))
           try:
               postdata1 = (posts[postno_1])
               if int(posts[postno_1]['media_type'])==1:
                   post_req = requests.get((posts[postno_1]['image_versions2']['candidates'][0]['url']))
                   postcache1 = open("post_1.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_1.png")
                   self.post_type1.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                   self.post_post1.setPixmap(QtGui.QPixmap("post_1.png"))
           
               elif int(posts[postno_1]['media_type'])==2:
                   post_req = requests.get(posts[postno_1]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_1.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_1.png")
                   self.post_post1.setPixmap(QtGui.QPixmap("post_1.png"))
                   self.post_type1.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))

                   
               elif int(posts[postno_1]['media_type'])==8:
                   post_req = requests.get(posts[postno_1]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_1.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_1.png")
                   self.post_post1.setPixmap(QtGui.QPixmap("post_1.png"))
                   self.post_type1.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
               self.post_post1.setHidden(False)
               self.post_type1.setHidden(False)

           except Exception:
               postdata1 = None
               pass
           try:
               #Post 2 Setup
               postdata2 = (posts[postno_2])
               if int(posts[postno_2]['media_type'])==1:
                   post_req = requests.get((posts[postno_2]['image_versions2']['candidates'][0]['url']))
                   postcache1 = open("post_2.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_2.png")
                   self.post_post2.setPixmap(QtGui.QPixmap("post_2.png"))
                   self.post_type2.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                   
               elif int(posts[postno_2]['media_type'])==2:
                   post_req = requests.get(posts[postno_2]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_2.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_2.png")
                   self.post_post2.setPixmap(QtGui.QPixmap("post_2.png"))
                   self.post_type2.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                   
               elif int(posts[postno_2]['media_type'])==8:
                   post_req = requests.get(posts[postno_2]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_2.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_2.png")
                   self.post_post2.setPixmap(QtGui.QPixmap("post_2.png"))
                   self.post_type2.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
               self.post_post2.setHidden(False)
               self.post_type2.setHidden(False)
           except Exception:
               postdata2 =None
               pass
            
           try:
               #Post 3 Setup
               postdata3 = (posts[postno_3])
               if int(posts[postno_3]['media_type'])==1:
                   post_req = requests.get((posts[postno_3]['image_versions2']['candidates'][0]['url']))
                   postcache1 = open("post_3.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_3.png")
                   self.post_post3.setPixmap(QtGui.QPixmap("post_3.png"))
                   self.post_type3.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                   
               elif int(posts[postno_3]['media_type'])==2:
                   post_req = requests.get(posts[postno_3]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_3.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_3.png")
                   self.post_post3.setPixmap(QtGui.QPixmap("post_3.png"))
                   self.post_type3.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                   
               elif int(posts[postno_3]['media_type'])==8:
                   post_req = requests.get(posts[postno_3]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_3.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_3.png")
                   self.post_post3.setPixmap(QtGui.QPixmap("post_3.png"))
                   self.post_type3.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
               self.post_post3.setHidden(False)
               self.post_type3.setHidden(False)

           except Exception:
               postdata3 = None
               pass
           try:
               postdata4 = (posts[postno_4])
               #Post 4 Setup
               if int(posts[postno_4]['media_type'])==1:
                   post_req = requests.get((posts[postno_4]['image_versions2']['candidates'][0]['url']))
                   postcache1 = open("post_4.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_4.png")
                   self.post_post4.setPixmap(QtGui.QPixmap("post_4.png"))
                   self.post_type4.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                   
               elif int(posts[postno_4]['media_type'])==2:
                   post_req = requests.get(posts[postno_4]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_4.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_4.png")
                   self.post_post4.setPixmap(QtGui.QPixmap("post_4.png"))
                   self.post_type4.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                   
               elif int(posts[postno_4]['media_type'])==8:
                   post_req = requests.get(posts[postno_4]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_4.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_4.png")
                   self.post_post4.setPixmap(QtGui.QPixmap("post_4.png"))
                   self.post_type4.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
               self.post_post4.setHidden(False)
               self.post_type4.setHidden(False)

           except Exception:
               postdata4 = None
               pass
           try:
               #Post 5 Setup
               postdata5 = (posts[postno_5])
               if int(posts[postno_5]['media_type'])==1:
                   post_req = requests.get((posts[postno_5]['image_versions2']['candidates'][0]['url']))
                   postcache1 = open("post_5.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_5.png")
                   self.post_post5.setPixmap(QtGui.QPixmap("post_5.png"))
                   self.post_type5.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                   
               elif int(posts[postno_5]['media_type'])==2:
                   post_req = requests.get(posts[postno_5]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_5.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_5.png")
                   self.post_post5.setPixmap(QtGui.QPixmap("post_5.png"))
                   self.post_type5.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                   
               elif int(posts[postno_5]['media_type'])==8:
                   post_req = requests.get(posts[postno_5]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_5.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_5.png")
                   self.post_post5.setPixmap(QtGui.QPixmap("post_5.png"))
                   self.post_type5.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
               self.post_post5.setHidden(False)
               self.post_type5.setHidden(False)

           except Exception:
               postdata5 = None
               pass
           try:
               #Post 6 Setup
               postdata6 = (posts[postno_6])
               if int(posts[postno_6]['media_type'])==1:
                   post_req = requests.get((posts[postno_6]['image_versions2']['candidates'][0]['url']))
                   postcache1 = open("post_6.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_6.png")
                   self.post_post6.setPixmap(QtGui.QPixmap("post_6.png"))
                   self.post_type6.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                   
                   
               elif int(posts[postno_6]['media_type'])==2:
                   post_req = requests.get(posts[postno_6]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_6.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_6.png")
                   self.post_post6.setPixmap(QtGui.QPixmap("post_6.png"))
                   self.post_type6.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                   
               elif int(posts[postno_6]['media_type'])==8:
                   post_req = requests.get(posts[postno_6]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_6.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_6.png")
                   self.post_post6.setPixmap(QtGui.QPixmap("post_6.png"))
                   self.post_type6.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
               self.post_post6.setHidden(False)
               self.post_type6.setHidden(False)

           except Exception:
               postdata6 = None
               pass
           try:
               #Post 7 Setup
               postdata7 = (posts[postno_7])
               if int(posts[postno_7]['media_type'])==1:
                   post_req = requests.get((posts[postno_7]['image_versions2']['candidates'][0]['url']))
                   postcache1 = open("post_7.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_7.png")
                   self.post_post7.setPixmap(QtGui.QPixmap("post_7.png"))
                   self.post_type7.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                   
               elif int(posts[postno_7]['media_type'])==2:
                   post_req = requests.get(posts[postno_7]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_7.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_7.png")
                   self.post_post7.setPixmap(QtGui.QPixmap("post_7.png"))
                   self.post_type7.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                   
               elif int(posts[postno_7]['media_type'])==8:
                   post_req = requests.get(posts[postno_7]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_7.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_7.png")
                   self.post_post7.setPixmap(QtGui.QPixmap("post_7.png"))
                   self.post_type7.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
               self.post_post7.setHidden(False)
               self.post_type7.setHidden(False)

           except Exception:
               postdata7 = None
               pass
           try:
               #Post 8 Setup
               postdata8 = (posts[postno_8])
               if int(posts[postno_8]['media_type'])==1:
                   post_req = requests.get((posts[postno_8]['image_versions2']['candidates'][0]['url']))
                   postcache1 = open("post_8.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_8.png")
                   self.post_post8.setPixmap(QtGui.QPixmap("post_8.png"))
                   self.post_type8.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                   
               elif int(posts[postno_8]['media_type'])==2:
                   post_req = requests.get(posts[postno_8]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_8.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_8.png")
                   self.post_post8.setPixmap(QtGui.QPixmap("post_8.png"))
                   self.post_type8.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                   
               elif int(posts[postno_8]['media_type'])==8:
                   post_req = requests.get(posts[postno_8]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_8.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_8.png")
                   self.post_post8.setPixmap(QtGui.QPixmap("post_8.png"))
                   self.post_type8.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
               self.post_post8.setHidden(False)
               self.post_type8.setHidden(False)
           except Exception:
               postdata8 = None
               pass
           try:
               #Post 9 Setup
               postdata9 = (posts[postno_9])
               if int(posts[postno_9]['media_type'])==1:
                   post_req = requests.get((posts[postno_9]['image_versions2']['candidates'][0]['url']))
                   postcache1 = open("post_9.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_9.png")
                   self.post_post9.setPixmap(QtGui.QPixmap("post_9.png"))
                   self.post_type9.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                   
               elif int(posts[postno_9]['media_type'])==2:
                   post_req = requests.get(posts[postno_9]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_9.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_9.png")
                   self.post_post9.setPixmap(QtGui.QPixmap("post_9.png"))
                   self.post_type9.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                   
               elif int(posts[postno_9]['media_type'])==8:
                   post_req = requests.get(posts[postno_9]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_9.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_9.png")
                   self.post_post9.setPixmap(QtGui.QPixmap("post_9.png"))
                   self.post_type9.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
               self.post_post9.setHidden(False)
               self.post_type9.setHidden(False)
           except Exception:
               postdata9 = None
               pass
           try:
               #Post 10 Setup
               postdata10 = (posts[postno_10])
               if int(posts[postno_10]['media_type'])==1:
                   post_req = requests.get((posts[postno_10]['image_versions2']['candidates'][0]['url']))
                   postcache1 = open("post_10.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_10.png")
                   self.post_post10.setPixmap(QtGui.QPixmap("post_10.png"))
                   self.post_type10.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                   
               elif int(posts[postno_10]['media_type'])==2:
                   post_req = requests.get(posts[postno_10]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_10.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_10.png")
                   self.post_post10.setPixmap(QtGui.QPixmap("post_10.png"))
                   self.post_type10.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                   
               elif int(posts[postno_10]['media_type'])==8:
                   post_req = requests.get(posts[postno_10]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_10.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_10.png")
                   self.post_post10.setPixmap(QtGui.QPixmap("post_10.png"))
                   self.post_type10.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
               self.post_post10.setHidden(False)
               self.post_type10.setHidden(False)
           except Exception:
               postdata10 = None
               pass      


           
        def posts_screen():
            thread6 = threading.Thread(target=posts_screen_thread)
            thread6.start()










        def stop_likedpost_scan():
           global likedpost_scan_status
           likedpost_scan_status = "stop"
           MainWindow.central_widget.setCurrentWidget(self.postscreen)

        #Post -Function  
        def likedposts_screen_thread():
           global searchsscr_select
           global search_username_mediacount
           self.likepost_scan_progress.setMaximum(search_username_mediacount)
           
           searchsscr_select = "posts"
           global postofuser
           global likedpost_scan_status
           likedpost_scan_status = "on"
           global feed
           global user
           global posts
           global page_no
           global postno_1
           global postno_2
           global postno_3
           global postno_4
           global postno_5
           global postno_6
           global postno_7
           global postno_8
           global postno_9
           global postno_10
           global usertobesearched
           #print(usertobesearched)
           postno_1 = 0
           postno_2 = 1
           postno_3 = 2
           postno_4 = 3
           postno_5 = 4
           postno_6 = 5
           postno_7 = 6
           postno_8 = 7
           postno_9 = 8
           postno_10 =9
           page_no = 1
           postofuser = usertobesearched[1:]
           x=0
           MainWindow.central_widget.setCurrentWidget(self.likepostscanscreen)
           feed = user.username_feed(postofuser)
           posts = []
           postslist = feed['items']
           self.likepost_scan_progress.setValue(12)
           while likedpost_scan_status == "on":
               try:
                   while likedpost_scan_status == "on":
                       if feed['more_available']:
                           max_id = feed["next_max_id"]
                           feed = user.username_feed(postofuser, max_id = max_id)
                           postslist.extend(feed["items"])
                           self.likepost_scan_progress.setValue(((x+1)*14))
                           #print(x)
                           x=x+1                         
                           
                       else:
                           likedpost_scan_status = "stop"
               except Exception:
                   print("You Connection is not stable. Couldn't retrieve the data")
           y=0
           for p in postslist:
               if postslist[y]['has_liked']==True:
                   posts.append(p)
                   
               if postslist[y]['has_liked']==False:
                   pass
               y=y+1
            
           MainWindow.central_widget.setCurrentWidget(self.postscreen)
           self.post_post1.setHidden(True)
           self.post_type1.setHidden(True)
           
           self.post_post2.setHidden(True)
           self.post_type2.setHidden(True)
           
           self.post_post3.setHidden(True)
           self.post_type3.setHidden(True)
           
           self.post_post4.setHidden(True)
           self.post_type4.setHidden(True)
           
           self.post_post5.setHidden(True)
           self.post_type5.setHidden(True)
           
           self.post_post6.setHidden(True)
           self.post_type6.setHidden(True)
           
           self.post_post7.setHidden(True)
           self.post_type7.setHidden(True)
           
           self.post_post8.setHidden(True)
           self.post_type8.setHidden(True)
           
           self.post_post9.setHidden(True)
           self.post_type9.setHidden(True)
           
           self.post_post10.setHidden(True)
           self.post_type10.setHidden(True)

           global postdata1
           global postdata2
           global postdata3
           global postdata4
           global postdata5
           global postdata6
           global postdata7
           global postdata8
           global postdata9
           global postdata10          
           #Post 1 Setup
           self.post_page.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Page 1</span></p></body></html>"))
           self.post_username.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">"+ str(usertobesearched)+"</span></p></body></html>"))
           try:
               postdata1 = (posts[postno_1])
               if int(posts[postno_1]['media_type'])==1:
                   post_req = requests.get((posts[postno_1]['image_versions2']['candidates'][0]['url']))
                   postcache1 = open("post_1.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_1.png")
                   self.post_type1.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                   self.post_post1.setPixmap(QtGui.QPixmap("post_1.png"))
           
               elif int(posts[postno_1]['media_type'])==2:
                   post_req = requests.get(posts[postno_1]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_1.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_1.png")
                   self.post_post1.setPixmap(QtGui.QPixmap("post_1.png"))
                   self.post_type1.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))

                   
               elif int(posts[postno_1]['media_type'])==8:
                   post_req = requests.get(posts[postno_1]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_1.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_1.png")
                   self.post_post1.setPixmap(QtGui.QPixmap("post_1.png"))
                   self.post_type1.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
               self.post_post1.setHidden(False)
               self.post_type1.setHidden(False)

           except Exception:
               postdata1 = None
               pass
           try:
               #Post 2 Setup
               postdata2 = (posts[postno_2])
               if int(posts[postno_2]['media_type'])==1:
                   post_req = requests.get((posts[postno_2]['image_versions2']['candidates'][0]['url']))
                   postcache1 = open("post_2.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_2.png")
                   self.post_post2.setPixmap(QtGui.QPixmap("post_2.png"))
                   self.post_type2.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                   
               elif int(posts[postno_2]['media_type'])==2:
                   post_req = requests.get(posts[postno_2]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_2.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_2.png")
                   self.post_post2.setPixmap(QtGui.QPixmap("post_2.png"))
                   self.post_type2.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                   
               elif int(posts[postno_2]['media_type'])==8:
                   post_req = requests.get(posts[postno_2]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_2.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_2.png")
                   self.post_post2.setPixmap(QtGui.QPixmap("post_2.png"))
                   self.post_type2.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
               self.post_post2.setHidden(False)
               self.post_type2.setHidden(False)
           except Exception:
               postdata2 =None
               pass
            
           try:
               #Post 3 Setup
               postdata3 = (posts[postno_3])
               if int(posts[postno_3]['media_type'])==1:
                   post_req = requests.get((posts[postno_3]['image_versions2']['candidates'][0]['url']))
                   postcache1 = open("post_3.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_3.png")
                   self.post_post3.setPixmap(QtGui.QPixmap("post_3.png"))
                   self.post_type3.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                   
               elif int(posts[postno_3]['media_type'])==2:
                   post_req = requests.get(posts[postno_3]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_3.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_3.png")
                   self.post_post3.setPixmap(QtGui.QPixmap("post_3.png"))
                   self.post_type3.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                   
               elif int(posts[postno_3]['media_type'])==8:
                   post_req = requests.get(posts[postno_3]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_3.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_3.png")
                   self.post_post3.setPixmap(QtGui.QPixmap("post_3.png"))
                   self.post_type3.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
               self.post_post3.setHidden(False)
               self.post_type3.setHidden(False)

           except Exception:
               postdata3 = None
               pass
           try:
               postdata4 = (posts[postno_4])
               #Post 4 Setup
               if int(posts[postno_4]['media_type'])==1:
                   post_req = requests.get((posts[postno_4]['image_versions2']['candidates'][0]['url']))
                   postcache1 = open("post_4.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_4.png")
                   self.post_post4.setPixmap(QtGui.QPixmap("post_4.png"))
                   self.post_type4.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                   
               elif int(posts[postno_4]['media_type'])==2:
                   post_req = requests.get(posts[postno_4]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_4.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_4.png")
                   self.post_post4.setPixmap(QtGui.QPixmap("post_4.png"))
                   self.post_type4.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                   
               elif int(posts[postno_4]['media_type'])==8:
                   post_req = requests.get(posts[postno_4]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_4.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_4.png")
                   self.post_post4.setPixmap(QtGui.QPixmap("post_4.png"))
                   self.post_type4.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
               self.post_post4.setHidden(False)
               self.post_type4.setHidden(False)

           except Exception:
               postdata4 = None
               pass
           try:
               #Post 5 Setup
               postdata5 = (posts[postno_5])
               if int(posts[postno_5]['media_type'])==1:
                   post_req = requests.get((posts[postno_5]['image_versions2']['candidates'][0]['url']))
                   postcache1 = open("post_5.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_5.png")
                   self.post_post5.setPixmap(QtGui.QPixmap("post_5.png"))
                   self.post_type5.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                   
               elif int(posts[postno_5]['media_type'])==2:
                   post_req = requests.get(posts[postno_5]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_5.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_5.png")
                   self.post_post5.setPixmap(QtGui.QPixmap("post_5.png"))
                   self.post_type5.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                   
               elif int(posts[postno_5]['media_type'])==8:
                   post_req = requests.get(posts[postno_5]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_5.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_5.png")
                   self.post_post5.setPixmap(QtGui.QPixmap("post_5.png"))
                   self.post_type5.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
               self.post_post5.setHidden(False)
               self.post_type5.setHidden(False)

           except Exception:
               postdata5 = None
               pass
           try:
               #Post 6 Setup
               postdata6 = (posts[postno_6])
               if int(posts[postno_6]['media_type'])==1:
                   post_req = requests.get((posts[postno_6]['image_versions2']['candidates'][0]['url']))
                   postcache1 = open("post_6.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_6.png")
                   self.post_post6.setPixmap(QtGui.QPixmap("post_6.png"))
                   self.post_type6.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                   
                   
               elif int(posts[postno_6]['media_type'])==2:
                   post_req = requests.get(posts[postno_6]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_6.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_6.png")
                   self.post_post6.setPixmap(QtGui.QPixmap("post_6.png"))
                   self.post_type6.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                   
               elif int(posts[postno_6]['media_type'])==8:
                   post_req = requests.get(posts[postno_6]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_6.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_6.png")
                   self.post_post6.setPixmap(QtGui.QPixmap("post_6.png"))
                   self.post_type6.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
               self.post_post6.setHidden(False)
               self.post_type6.setHidden(False)

           except Exception:
               postdata6 = None
               pass
           try:
               #Post 7 Setup
               postdata7 = (posts[postno_7])
               if int(posts[postno_7]['media_type'])==1:
                   post_req = requests.get((posts[postno_7]['image_versions2']['candidates'][0]['url']))
                   postcache1 = open("post_7.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_7.png")
                   self.post_post7.setPixmap(QtGui.QPixmap("post_7.png"))
                   self.post_type7.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                   
               elif int(posts[postno_7]['media_type'])==2:
                   post_req = requests.get(posts[postno_7]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_7.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_7.png")
                   self.post_post7.setPixmap(QtGui.QPixmap("post_7.png"))
                   self.post_type7.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                   
               elif int(posts[postno_7]['media_type'])==8:
                   post_req = requests.get(posts[postno_7]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_7.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_7.png")
                   self.post_post7.setPixmap(QtGui.QPixmap("post_7.png"))
                   self.post_type7.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
               self.post_post7.setHidden(False)
               self.post_type7.setHidden(False)

           except Exception:
               postdata7 = None
               pass
           try:
               #Post 8 Setup
               postdata8 = (posts[postno_8])
               if int(posts[postno_8]['media_type'])==1:
                   post_req = requests.get((posts[postno_8]['image_versions2']['candidates'][0]['url']))
                   postcache1 = open("post_8.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_8.png")
                   self.post_post8.setPixmap(QtGui.QPixmap("post_8.png"))
                   self.post_type8.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                   
               elif int(posts[postno_8]['media_type'])==2:
                   post_req = requests.get(posts[postno_8]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_8.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_8.png")
                   self.post_post8.setPixmap(QtGui.QPixmap("post_8.png"))
                   self.post_type8.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                   
               elif int(posts[postno_8]['media_type'])==8:
                   post_req = requests.get(posts[postno_8]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_8.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_8.png")
                   self.post_post8.setPixmap(QtGui.QPixmap("post_8.png"))
                   self.post_type8.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
               self.post_post8.setHidden(False)
               self.post_type8.setHidden(False)
           except Exception:
               postdata8 = None
               pass
           try:
               #Post 9 Setup
               postdata9 = (posts[postno_9])
               if int(posts[postno_9]['media_type'])==1:
                   post_req = requests.get((posts[postno_9]['image_versions2']['candidates'][0]['url']))
                   postcache1 = open("post_9.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_9.png")
                   self.post_post9.setPixmap(QtGui.QPixmap("post_9.png"))
                   self.post_type9.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                   
               elif int(posts[postno_9]['media_type'])==2:
                   post_req = requests.get(posts[postno_9]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_9.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_9.png")
                   self.post_post9.setPixmap(QtGui.QPixmap("post_9.png"))
                   self.post_type9.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                   
               elif int(posts[postno_9]['media_type'])==8:
                   post_req = requests.get(posts[postno_9]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_9.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_9.png")
                   self.post_post9.setPixmap(QtGui.QPixmap("post_9.png"))
                   self.post_type9.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
               self.post_post9.setHidden(False)
               self.post_type9.setHidden(False)
           except Exception:
               postdata9 = None
               pass
           try:
               #Post 10 Setup
               postdata10 = (posts[postno_10])
               if int(posts[postno_10]['media_type'])==1:
                   post_req = requests.get((posts[postno_10]['image_versions2']['candidates'][0]['url']))
                   postcache1 = open("post_10.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_10.png")
                   self.post_post10.setPixmap(QtGui.QPixmap("post_10.png"))
                   self.post_type10.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                   
               elif int(posts[postno_10]['media_type'])==2:
                   post_req = requests.get(posts[postno_10]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_10.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_10.png")
                   self.post_post10.setPixmap(QtGui.QPixmap("post_10.png"))
                   self.post_type10.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                   
               elif int(posts[postno_10]['media_type'])==8:
                   post_req = requests.get(posts[postno_10]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_10.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_10.png")
                   self.post_post10.setPixmap(QtGui.QPixmap("post_10.png"))
                   self.post_type10.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
               self.post_post10.setHidden(False)
               self.post_type10.setHidden(False)
           except Exception:
               postdata10 = None
               pass      


           
        def likedposts_screen():
            thread6 = threading.Thread(target=likedposts_screen_thread)
            thread6.start()












        #Next Post -Function    
        def next_posts_thread():
           MainWindow.setGraphicsEffect(self.blur_effect)
           self.blur_effect.setBlurRadius(5)
           MainWindow.setEnabled(False)
           global postofuser
           global feed
           global user
           global posts
           global page_no
           #post global
           global postno_1
           global postno_2
           global postno_3
           global postno_4
           global postno_5
           global postno_6
           global postno_7
           global postno_8
           global postno_9
           global postno_10         
           if feed['more_available']:
               max_id = feed["next_max_id"]
               feed = user.username_feed(postofuser, max_id = max_id)
               posts.extend(feed["items"])
               
           page_no = page_no + 1
           postno_1 = postno_1+10
           postno_2 = postno_2+10
           postno_3 = postno_3+10
           postno_4 = postno_4+10
           postno_5 = postno_5+10
           postno_6 = postno_6+10
           postno_7 = postno_7+10
           postno_8 = postno_8+10
           postno_9 = postno_9+10
           postno_10 = postno_10+10
           self.post_post1.setHidden(True)
           self.post_type1.setHidden(True)
           
           self.post_post2.setHidden(True)
           self.post_type2.setHidden(True)
           
           self.post_post3.setHidden(True)
           self.post_type3.setHidden(True)
           
           self.post_post4.setHidden(True)
           self.post_type4.setHidden(True)
           
           self.post_post5.setHidden(True)
           self.post_type5.setHidden(True)
           
           self.post_post6.setHidden(True)
           self.post_type6.setHidden(True)
           
           self.post_post7.setHidden(True)
           self.post_type7.setHidden(True)
           
           self.post_post8.setHidden(True)
           self.post_type8.setHidden(True)
           
           self.post_post9.setHidden(True)
           self.post_type9.setHidden(True)
           
           self.post_post10.setHidden(True)
           self.post_type10.setHidden(True)


           global postdata1
           global postdata2
           global postdata3
           global postdata4
           global postdata5
           global postdata6
           global postdata7
           global postdata8
           global postdata9
           global postdata10
           postdata1 = None
           postdata2 = None
           postdata3 = None
           postdata4 = None
           postdata5 = None
           postdata6 = None
           postdata7 = None
           postdata8 = None
           postdata9 = None
           postdata10 = None

           MainWindow.setEnabled(True)
           self.blur_effect.setBlurRadius(0)

           self.post_page.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Page "+str(page_no)+"</span></p></body></html>"))

           #Post 1 Setup
           
           #self.post_username.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">"+ str(usertobesearched)+"</span></p></body></html>"))
           try:
               postdata1 = (posts[postno_1])
               if int(posts[postno_1]['media_type'])==1:
                   post_req = requests.get((posts[postno_1]['image_versions2']['candidates'][0]['url']))
                   postcache1 = open("post_1.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_1.png")
                   self.post_type1.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                   self.post_post1.setPixmap(QtGui.QPixmap("post_1.png"))
           
               elif int(posts[postno_1]['media_type'])==2:
                   post_req = requests.get(posts[postno_1]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_1.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_1.png")
                   self.post_post1.setPixmap(QtGui.QPixmap("post_1.png"))
                   self.post_type1.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))

                   
               elif int(posts[postno_1]['media_type'])==8:
                   post_req = requests.get(posts[postno_1]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_1.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_1.png")
                   self.post_post1.setPixmap(QtGui.QPixmap("post_1.png"))
                   self.post_type1.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
               self.post_post1.setHidden(False)
               self.post_type1.setHidden(False)

           except Exception:
               postdata1 = None
               pass
           try:
               #Post 2 Setup
               postdata2 = (posts[postno_2])
               if int(posts[postno_2]['media_type'])==1:
                   post_req = requests.get((posts[postno_2]['image_versions2']['candidates'][0]['url']))
                   postcache1 = open("post_2.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_2.png")
                   self.post_post2.setPixmap(QtGui.QPixmap("post_2.png"))
                   self.post_type2.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                   
               elif int(posts[postno_2]['media_type'])==2:
                   post_req = requests.get(posts[postno_2]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_2.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_2.png")
                   self.post_post2.setPixmap(QtGui.QPixmap("post_2.png"))
                   self.post_type2.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                   
               elif int(posts[postno_2]['media_type'])==8:
                   post_req = requests.get(posts[postno_2]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_2.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_2.png")
                   self.post_post2.setPixmap(QtGui.QPixmap("post_2.png"))
                   self.post_type2.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
               self.post_post2.setHidden(False)
               self.post_type2.setHidden(False)
           except Exception:
               postdata2 =None
               pass
            
           try:
               #Post 3 Setup
               postdata3 = (posts[postno_3])
               if int(posts[postno_3]['media_type'])==1:
                   post_req = requests.get((posts[postno_3]['image_versions2']['candidates'][0]['url']))
                   postcache1 = open("post_3.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_3.png")
                   self.post_post3.setPixmap(QtGui.QPixmap("post_3.png"))
                   self.post_type3.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                   
               elif int(posts[postno_3]['media_type'])==2:
                   post_req = requests.get(posts[postno_3]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_3.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_3.png")
                   self.post_post3.setPixmap(QtGui.QPixmap("post_3.png"))
                   self.post_type3.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                   
               elif int(posts[postno_3]['media_type'])==8:
                   post_req = requests.get(posts[postno_3]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_3.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_3.png")
                   self.post_post3.setPixmap(QtGui.QPixmap("post_3.png"))
                   self.post_type3.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
               self.post_post3.setHidden(False)
               self.post_type3.setHidden(False)

           except Exception:
               postdata3 = None
               pass
           try:
               postdata4 = (posts[postno_4])
               #Post 4 Setup
               if int(posts[postno_4]['media_type'])==1:
                   post_req = requests.get((posts[postno_4]['image_versions2']['candidates'][0]['url']))
                   postcache1 = open("post_4.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_4.png")
                   self.post_post4.setPixmap(QtGui.QPixmap("post_4.png"))
                   self.post_type4.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                   
               elif int(posts[postno_4]['media_type'])==2:
                   post_req = requests.get(posts[postno_4]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_4.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_4.png")
                   self.post_post4.setPixmap(QtGui.QPixmap("post_4.png"))
                   self.post_type4.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                   
               elif int(posts[postno_4]['media_type'])==8:
                   post_req = requests.get(posts[postno_4]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_4.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_4.png")
                   self.post_post4.setPixmap(QtGui.QPixmap("post_4.png"))
                   self.post_type4.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
               self.post_post4.setHidden(False)
               self.post_type4.setHidden(False)

           except Exception:
               postdata4 = None
               pass
           try:
               #Post 5 Setup
               postdata5 = (posts[postno_5])
               if int(posts[postno_5]['media_type'])==1:
                   post_req = requests.get((posts[postno_5]['image_versions2']['candidates'][0]['url']))
                   postcache1 = open("post_5.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_5.png")
                   self.post_post5.setPixmap(QtGui.QPixmap("post_5.png"))
                   self.post_type5.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                   
               elif int(posts[postno_5]['media_type'])==2:
                   post_req = requests.get(posts[postno_5]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_5.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_5.png")
                   self.post_post5.setPixmap(QtGui.QPixmap("post_5.png"))
                   self.post_type5.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                   
               elif int(posts[postno_5]['media_type'])==8:
                   post_req = requests.get(posts[postno_5]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_5.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_5.png")
                   self.post_post5.setPixmap(QtGui.QPixmap("post_5.png"))
                   self.post_type5.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
               self.post_post5.setHidden(False)
               self.post_type5.setHidden(False)

           except Exception:
               postdata5 = None
               pass
           try:
               #Post 6 Setup
               postdata6 = (posts[postno_6])
               if int(posts[postno_6]['media_type'])==1:
                   post_req = requests.get((posts[postno_6]['image_versions2']['candidates'][0]['url']))
                   postcache1 = open("post_6.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_6.png")
                   self.post_post6.setPixmap(QtGui.QPixmap("post_6.png"))
                   self.post_type6.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                   
                   
               elif int(posts[postno_6]['media_type'])==2:
                   post_req = requests.get(posts[postno_6]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_6.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_6.png")
                   self.post_post6.setPixmap(QtGui.QPixmap("post_6.png"))
                   self.post_type6.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                   
               elif int(posts[postno_6]['media_type'])==8:
                   post_req = requests.get(posts[postno_6]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_6.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_6.png")
                   self.post_post6.setPixmap(QtGui.QPixmap("post_6.png"))
                   self.post_type6.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
               self.post_post6.setHidden(False)
               self.post_type6.setHidden(False)

           except Exception:
               postdata6 = None
               pass
           try:
               #Post 7 Setup
               postdata7 = (posts[postno_7])
               if int(posts[postno_7]['media_type'])==1:
                   post_req = requests.get((posts[postno_7]['image_versions2']['candidates'][0]['url']))
                   postcache1 = open("post_7.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_7.png")
                   self.post_post7.setPixmap(QtGui.QPixmap("post_7.png"))
                   self.post_type7.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                   
               elif int(posts[postno_7]['media_type'])==2:
                   post_req = requests.get(posts[postno_7]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_7.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_7.png")
                   self.post_post7.setPixmap(QtGui.QPixmap("post_7.png"))
                   self.post_type7.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                   
               elif int(posts[postno_7]['media_type'])==8:
                   post_req = requests.get(posts[postno_7]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_7.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_7.png")
                   self.post_post7.setPixmap(QtGui.QPixmap("post_7.png"))
                   self.post_type7.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
               self.post_post7.setHidden(False)
               self.post_type7.setHidden(False)

           except Exception:
               postdata7 = None
               pass
           try:
               #Post 8 Setup
               postdata8 = (posts[postno_8])
               if int(posts[postno_8]['media_type'])==1:
                   post_req = requests.get((posts[postno_8]['image_versions2']['candidates'][0]['url']))
                   postcache1 = open("post_8.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_8.png")
                   self.post_post8.setPixmap(QtGui.QPixmap("post_8.png"))
                   self.post_type8.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                   
               elif int(posts[postno_8]['media_type'])==2:
                   post_req = requests.get(posts[postno_8]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_8.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_8.png")
                   self.post_post8.setPixmap(QtGui.QPixmap("post_8.png"))
                   self.post_type8.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                   
               elif int(posts[postno_8]['media_type'])==8:
                   post_req = requests.get(posts[postno_8]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_8.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_8.png")
                   self.post_post8.setPixmap(QtGui.QPixmap("post_8.png"))
                   self.post_type8.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
               self.post_post8.setHidden(False)
               self.post_type8.setHidden(False)
           except Exception:
               postdata8 = None
               pass
           try:
               #Post 9 Setup
               postdata9 = (posts[postno_9])
               if int(posts[postno_9]['media_type'])==1:
                   post_req = requests.get((posts[postno_9]['image_versions2']['candidates'][0]['url']))
                   postcache1 = open("post_9.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_9.png")
                   self.post_post9.setPixmap(QtGui.QPixmap("post_9.png"))
                   self.post_type9.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                   
               elif int(posts[postno_9]['media_type'])==2:
                   post_req = requests.get(posts[postno_9]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_9.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_9.png")
                   self.post_post9.setPixmap(QtGui.QPixmap("post_9.png"))
                   self.post_type9.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                   
               elif int(posts[postno_9]['media_type'])==8:
                   post_req = requests.get(posts[postno_9]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_9.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_9.png")
                   self.post_post9.setPixmap(QtGui.QPixmap("post_9.png"))
                   self.post_type9.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
               self.post_post9.setHidden(False)
               self.post_type9.setHidden(False)
           except Exception:
               postdata9 = None
               pass
           try:
               #Post 10 Setup
               postdata10 = (posts[postno_10])
               if int(posts[postno_10]['media_type'])==1:
                   post_req = requests.get((posts[postno_10]['image_versions2']['candidates'][0]['url']))
                   postcache1 = open("post_10.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_10.png")
                   self.post_post10.setPixmap(QtGui.QPixmap("post_10.png"))
                   self.post_type10.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                   
               elif int(posts[postno_10]['media_type'])==2:
                   post_req = requests.get(posts[postno_10]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_10.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_10.png")
                   self.post_post10.setPixmap(QtGui.QPixmap("post_10.png"))
                   self.post_type10.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                   
               elif int(posts[postno_10]['media_type'])==8:
                   post_req = requests.get(posts[postno_10]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                   postcache1 = open("post_10.png", "wb")
                   postcache1.write(post_req.content)
                   postcache1.close()
                   #reshape("post_10.png")
                   self.post_post10.setPixmap(QtGui.QPixmap("post_10.png"))
                   self.post_type10.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
               self.post_post10.setHidden(False)
               self.post_type10.setHidden(False)
           except Exception:
               postdata10 = None
               pass      


               
        def next_posts():
            thread6 = threading.Thread(target=next_posts_thread)
            thread6.start()           


        #Back Post -Function    
        def back_posts_thread():
           global postofuser
           global feed
           global user
           global posts
           global page_no
           #post global
           global postno_1
           global postno_2
           global postno_3
           global postno_4
           global postno_5
           global postno_6
           global postno_7
           global postno_8
           global postno_9
           global postno_10
           if self.post_page.text()== ("<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Page 1</span></p></body></html>"):
               pass
           else:
               self.post_post1.setHidden(True)
               self.post_type1.setHidden(True)
               
               self.post_post2.setHidden(True)
               self.post_type2.setHidden(True)
               
               self.post_post3.setHidden(True)
               self.post_type3.setHidden(True)
               
               self.post_post4.setHidden(True)
               self.post_type4.setHidden(True)
               
               self.post_post5.setHidden(True)
               self.post_type5.setHidden(True)
               
               self.post_post6.setHidden(True)
               self.post_type6.setHidden(True)
               
               self.post_post7.setHidden(True)
               self.post_type7.setHidden(True)
               
               self.post_post8.setHidden(True)
               self.post_type8.setHidden(True)
               
               self.post_post9.setHidden(True)
               self.post_type9.setHidden(True)
               
               self.post_post10.setHidden(True)
               self.post_type10.setHidden(True)
               MainWindow.setGraphicsEffect(self.blur_effect)
               self.blur_effect.setBlurRadius(5)
               MainWindow.setEnabled(False)
               page_no = page_no - 1

               postno_1 = postno_1-10
               postno_2 = postno_2-10
               postno_3 = postno_3-10
               postno_4 = postno_4-10
               postno_5 = postno_5-10
               postno_6 = postno_6-10
               postno_7 = postno_7-10
               postno_8 = postno_8-10
               postno_9 = postno_9-10
               postno_10 = postno_10-10

               
               global postdata1
               global postdata2
               global postdata3
               global postdata4
               global postdata5
               global postdata6
               global postdata7
               global postdata8
               global postdata9
               global postdata10          

               postdata1 = None
               postdata2 = None
               postdata3 = None
               postdata4 = None
               postdata5 = None
               postdata6 = None
               postdata7 = None
               postdata8 = None
               postdata9 = None
               postdata10 = None
               #Post 1 Setup

               self.post_page.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Page "+str(page_no)+"</span></p></body></html>"))
               MainWindow.setEnabled(True)
               self.blur_effect.setBlurRadius(0)
               #self.post_username.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">"+ str(usertobesearched)+"</span></p></body></html>"))
               try:
                   postdata1 = (posts[postno_1])
                   if int(posts[postno_1]['media_type'])==1:
                       post_req = requests.get((posts[postno_1]['image_versions2']['candidates'][0]['url']))
                       postcache1 = open("post_1.png", "wb")
                       postcache1.write(post_req.content)
                       postcache1.close()
                       #reshape("post_1.png")
                       self.post_type1.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                       self.post_post1.setPixmap(QtGui.QPixmap("post_1.png"))
               
                   elif int(posts[postno_1]['media_type'])==2:
                       post_req = requests.get(posts[postno_1]['image_versions2']['candidates'][0]['url'])
                       postcache1 = open("post_1.png", "wb")
                       postcache1.write(post_req.content)
                       postcache1.close()
                       #reshape("post_1.png")
                       self.post_post1.setPixmap(QtGui.QPixmap("post_1.png"))
                       self.post_type1.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))

                       
                   elif int(posts[postno_1]['media_type'])==8:
                       post_req = requests.get(posts[postno_1]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                       postcache1 = open("post_1.png", "wb")
                       postcache1.write(post_req.content)
                       postcache1.close()
                       #reshape("post_1.png")
                       self.post_post1.setPixmap(QtGui.QPixmap("post_1.png"))
                       self.post_type1.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
                   self.post_post1.setHidden(False)
                   self.post_type1.setHidden(False)

               except Exception:
                   postdata1 = None
                   pass
               try:
                   #Post 2 Setup
                   postdata2 = (posts[postno_2])
                   if int(posts[postno_2]['media_type'])==1:
                       post_req = requests.get((posts[postno_2]['image_versions2']['candidates'][0]['url']))
                       postcache1 = open("post_2.png", "wb")
                       postcache1.write(post_req.content)
                       postcache1.close()
                       #reshape("post_2.png")
                       self.post_post2.setPixmap(QtGui.QPixmap("post_2.png"))
                       self.post_type2.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                       
                   elif int(posts[postno_2]['media_type'])==2:
                       post_req = requests.get(posts[postno_2]['image_versions2']['candidates'][0]['url'])
                       postcache1 = open("post_2.png", "wb")
                       postcache1.write(post_req.content)
                       postcache1.close()
                       #reshape("post_2.png")
                       self.post_post2.setPixmap(QtGui.QPixmap("post_2.png"))
                       self.post_type2.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                       
                   elif int(posts[postno_2]['media_type'])==8:
                       post_req = requests.get(posts[postno_2]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                       postcache1 = open("post_2.png", "wb")
                       postcache1.write(post_req.content)
                       postcache1.close()
                       #reshape("post_2.png")
                       self.post_post2.setPixmap(QtGui.QPixmap("post_2.png"))
                       self.post_type2.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
                   self.post_post2.setHidden(False)
                   self.post_type2.setHidden(False)
               except Exception:
                   postdata2 =None
                   pass
                
               try:
                   #Post 3 Setup
                   postdata3 = (posts[postno_3])
                   if int(posts[postno_3]['media_type'])==1:
                       post_req = requests.get((posts[postno_3]['image_versions2']['candidates'][0]['url']))
                       postcache1 = open("post_3.png", "wb")
                       postcache1.write(post_req.content)
                       postcache1.close()
                       #reshape("post_3.png")
                       self.post_post3.setPixmap(QtGui.QPixmap("post_3.png"))
                       self.post_type3.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                       
                   elif int(posts[postno_3]['media_type'])==2:
                       post_req = requests.get(posts[postno_3]['image_versions2']['candidates'][0]['url'])
                       postcache1 = open("post_3.png", "wb")
                       postcache1.write(post_req.content)
                       postcache1.close()
                       #reshape("post_3.png")
                       self.post_post3.setPixmap(QtGui.QPixmap("post_3.png"))
                       self.post_type3.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                       
                   elif int(posts[postno_3]['media_type'])==8:
                       post_req = requests.get(posts[postno_3]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                       postcache1 = open("post_3.png", "wb")
                       postcache1.write(post_req.content)
                       postcache1.close()
                       #reshape("post_3.png")
                       self.post_post3.setPixmap(QtGui.QPixmap("post_3.png"))
                       self.post_type3.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
                   self.post_post3.setHidden(False)
                   self.post_type3.setHidden(False)

               except Exception:
                   postdata3 = None
                   pass
               try:
                   postdata4 = (posts[postno_4])
                   #Post 4 Setup
                   if int(posts[postno_4]['media_type'])==1:
                       post_req = requests.get((posts[postno_4]['image_versions2']['candidates'][0]['url']))
                       postcache1 = open("post_4.png", "wb")
                       postcache1.write(post_req.content)
                       postcache1.close()
                       #reshape("post_4.png")
                       self.post_post4.setPixmap(QtGui.QPixmap("post_4.png"))
                       self.post_type4.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                       
                   elif int(posts[postno_4]['media_type'])==2:
                       post_req = requests.get(posts[postno_4]['image_versions2']['candidates'][0]['url'])
                       postcache1 = open("post_4.png", "wb")
                       postcache1.write(post_req.content)
                       postcache1.close()
                       #reshape("post_4.png")
                       self.post_post4.setPixmap(QtGui.QPixmap("post_4.png"))
                       self.post_type4.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                       
                   elif int(posts[postno_4]['media_type'])==8:
                       post_req = requests.get(posts[postno_4]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                       postcache1 = open("post_4.png", "wb")
                       postcache1.write(post_req.content)
                       postcache1.close()
                       #reshape("post_4.png")
                       self.post_post4.setPixmap(QtGui.QPixmap("post_4.png"))
                       self.post_type4.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
                   self.post_post4.setHidden(False)
                   self.post_type4.setHidden(False)

               except Exception:
                   postdata4 = None
                   pass
               try:
                   #Post 5 Setup
                   postdata5 = (posts[postno_5])
                   if int(posts[postno_5]['media_type'])==1:
                       post_req = requests.get((posts[postno_5]['image_versions2']['candidates'][0]['url']))
                       postcache1 = open("post_5.png", "wb")
                       postcache1.write(post_req.content)
                       postcache1.close()
                       #reshape("post_5.png")
                       self.post_post5.setPixmap(QtGui.QPixmap("post_5.png"))
                       self.post_type5.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                       
                   elif int(posts[postno_5]['media_type'])==2:
                       post_req = requests.get(posts[postno_5]['image_versions2']['candidates'][0]['url'])
                       postcache1 = open("post_5.png", "wb")
                       postcache1.write(post_req.content)
                       postcache1.close()
                       #reshape("post_5.png")
                       self.post_post5.setPixmap(QtGui.QPixmap("post_5.png"))
                       self.post_type5.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                       
                   elif int(posts[postno_5]['media_type'])==8:
                       post_req = requests.get(posts[postno_5]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                       postcache1 = open("post_5.png", "wb")
                       postcache1.write(post_req.content)
                       postcache1.close()
                       #reshape("post_5.png")
                       self.post_post5.setPixmap(QtGui.QPixmap("post_5.png"))
                       self.post_type5.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
                   self.post_post5.setHidden(False)
                   self.post_type5.setHidden(False)

               except Exception:
                   postdata5 = None
                   pass
               try:
                   #Post 6 Setup
                   postdata6 = (posts[postno_6])
                   if int(posts[postno_6]['media_type'])==1:
                       post_req = requests.get((posts[postno_6]['image_versions2']['candidates'][0]['url']))
                       postcache1 = open("post_6.png", "wb")
                       postcache1.write(post_req.content)
                       postcache1.close()
                       #reshape("post_6.png")
                       self.post_post6.setPixmap(QtGui.QPixmap("post_6.png"))
                       self.post_type6.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                       
                       
                   elif int(posts[postno_6]['media_type'])==2:
                       post_req = requests.get(posts[postno_6]['image_versions2']['candidates'][0]['url'])
                       postcache1 = open("post_6.png", "wb")
                       postcache1.write(post_req.content)
                       postcache1.close()
                       #reshape("post_6.png")
                       self.post_post6.setPixmap(QtGui.QPixmap("post_6.png"))
                       self.post_type6.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                       
                   elif int(posts[postno_6]['media_type'])==8:
                       post_req = requests.get(posts[postno_6]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                       postcache1 = open("post_6.png", "wb")
                       postcache1.write(post_req.content)
                       postcache1.close()
                       #reshape("post_6.png")
                       self.post_post6.setPixmap(QtGui.QPixmap("post_6.png"))
                       self.post_type6.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
                   self.post_post6.setHidden(False)
                   self.post_type6.setHidden(False)

               except Exception:
                   postdata6 = None
                   pass
               try:
                   #Post 7 Setup
                   postdata7 = (posts[postno_7])
                   if int(posts[postno_7]['media_type'])==1:
                       post_req = requests.get((posts[postno_7]['image_versions2']['candidates'][0]['url']))
                       postcache1 = open("post_7.png", "wb")
                       postcache1.write(post_req.content)
                       postcache1.close()
                       #reshape("post_7.png")
                       self.post_post7.setPixmap(QtGui.QPixmap("post_7.png"))
                       self.post_type7.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                       
                   elif int(posts[postno_7]['media_type'])==2:
                       post_req = requests.get(posts[postno_7]['image_versions2']['candidates'][0]['url'])
                       postcache1 = open("post_7.png", "wb")
                       postcache1.write(post_req.content)
                       postcache1.close()
                       #reshape("post_7.png")
                       self.post_post7.setPixmap(QtGui.QPixmap("post_7.png"))
                       self.post_type7.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                       
                   elif int(posts[postno_7]['media_type'])==8:
                       post_req = requests.get(posts[postno_7]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                       postcache1 = open("post_7.png", "wb")
                       postcache1.write(post_req.content)
                       postcache1.close()
                       #reshape("post_7.png")
                       self.post_post7.setPixmap(QtGui.QPixmap("post_7.png"))
                       self.post_type7.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
                   self.post_post7.setHidden(False)
                   self.post_type7.setHidden(False)

               except Exception:
                   postdata7 = None
                   pass
               try:
                   #Post 8 Setup
                   postdata8 = (posts[postno_8])
                   if int(posts[postno_8]['media_type'])==1:
                       post_req = requests.get((posts[postno_8]['image_versions2']['candidates'][0]['url']))
                       postcache1 = open("post_8.png", "wb")
                       postcache1.write(post_req.content)
                       postcache1.close()
                       #reshape("post_8.png")
                       self.post_post8.setPixmap(QtGui.QPixmap("post_8.png"))
                       self.post_type8.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                       
                   elif int(posts[postno_8]['media_type'])==2:
                       post_req = requests.get(posts[postno_8]['image_versions2']['candidates'][0]['url'])
                       postcache1 = open("post_8.png", "wb")
                       postcache1.write(post_req.content)
                       postcache1.close()
                       #reshape("post_8.png")
                       self.post_post8.setPixmap(QtGui.QPixmap("post_8.png"))
                       self.post_type8.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                       
                   elif int(posts[postno_8]['media_type'])==8:
                       post_req = requests.get(posts[postno_8]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                       postcache1 = open("post_8.png", "wb")
                       postcache1.write(post_req.content)
                       postcache1.close()
                       #reshape("post_8.png")
                       self.post_post8.setPixmap(QtGui.QPixmap("post_8.png"))
                       self.post_type8.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
                   self.post_post8.setHidden(False)
                   self.post_type8.setHidden(False)
               except Exception:
                   postdata8 = None
                   pass
               try:
                   #Post 9 Setup
                   postdata9 = (posts[postno_9])
                   if int(posts[postno_9]['media_type'])==1:
                       post_req = requests.get((posts[postno_9]['image_versions2']['candidates'][0]['url']))
                       postcache1 = open("post_9.png", "wb")
                       postcache1.write(post_req.content)
                       postcache1.close()
                       #reshape("post_9.png")
                       self.post_post9.setPixmap(QtGui.QPixmap("post_9.png"))
                       self.post_type9.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                       
                   elif int(posts[postno_9]['media_type'])==2:
                       post_req = requests.get(posts[postno_9]['image_versions2']['candidates'][0]['url'])
                       postcache1 = open("post_9.png", "wb")
                       postcache1.write(post_req.content)
                       postcache1.close()
                       #reshape("post_9.png")
                       self.post_post9.setPixmap(QtGui.QPixmap("post_9.png"))
                       self.post_type9.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                       
                   elif int(posts[postno_9]['media_type'])==8:
                       post_req = requests.get(posts[postno_9]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                       postcache1 = open("post_9.png", "wb")
                       postcache1.write(post_req.content)
                       postcache1.close()
                       #reshape("post_9.png")
                       self.post_post9.setPixmap(QtGui.QPixmap("post_9.png"))
                       self.post_type9.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
                   self.post_post9.setHidden(False)
                   self.post_type9.setHidden(False)
               except Exception:
                   postdata9 = None
                   pass
               try:
                   #Post 10 Setup
                   postdata10 = (posts[postno_10])
                   if int(posts[postno_10]['media_type'])==1:
                       post_req = requests.get((posts[postno_10]['image_versions2']['candidates'][0]['url']))
                       postcache1 = open("post_10.png", "wb")
                       postcache1.write(post_req.content)
                       postcache1.close()
                       #reshape("post10.png")
                       self.post_post10.setPixmap(QtGui.QPixmap("post_10.png"))
                       self.post_type10.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                       
                   elif int(posts[postno_10]['media_type'])==2:
                       post_req = requests.get(posts[postno_10]['image_versions2']['candidates'][0]['url'])
                       postcache1 = open("post_10.png", "wb")
                       postcache1.write(post_req.content)
                       postcache1.close()
                       #reshape("post10.png")
                       self.post_post10.setPixmap(QtGui.QPixmap("post_10.png"))
                       self.post_type10.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                       
                   elif int(posts[postno_10]['media_type'])==8:
                       post_req = requests.get(posts[postno_10]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                       postcache1 = open("post_10.png", "wb")
                       postcache1.write(post_req.content)
                       postcache1.close()
                       #reshape("post10.png")
                       self.post_post10.setPixmap(QtGui.QPixmap("post_10.png"))
                       self.post_type10.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
                   self.post_post10.setHidden(False)
                   self.post_type10.setHidden(False)
               except Exception:
                   postdata10 = None
                   pass      

        def back_posts():
            thread6 = threading.Thread(target=back_posts_thread)
            thread6.start()      
        def posts_close():
            global searchsscr_select
            searchsscr_select = "profile"
            setscreen_home()





        #mypost -Function  
        def myposts_screen_thread():
           global homesscr_select
           homesscr_select = "myposts"
           MainWindow.setGraphicsEffect(self.blur_effect)
           self.blur_effect.setBlurRadius(5)
           MainWindow.setEnabled(False)
           global mypostofuser
           global feed
           global user
           global myposts
           global page_no
           global mypostno_1
           global mypostno_2
           global mypostno_3
           global mypostno_4
           global mypostno_5
           global mypostno_6
           global mypostno_7
           global mypostno_8
           global mypostno_9
           global mypostno_10
           global username
           #print(usertobesearched)
           mypostno_1 = 0
           mypostno_2 = 1
           mypostno_3 = 2
           mypostno_4 = 3
           mypostno_5 = 4
           mypostno_6 = 5
           mypostno_7 = 6
           mypostno_8 = 7
           mypostno_9 = 8
           mypostno_10 =9
           page_no = 1
           mypostofuser = username
           feed = user.username_feed(mypostofuser)
           myposts = feed['items']

           self.mypost_mypost1.setHidden(True)
           self.mypost_type1.setHidden(True)
           
           self.mypost_mypost2.setHidden(True)
           self.mypost_type2.setHidden(True)
           
           self.mypost_mypost3.setHidden(True)
           self.mypost_type3.setHidden(True)
           
           self.mypost_mypost4.setHidden(True)
           self.mypost_type4.setHidden(True)
           
           self.mypost_mypost5.setHidden(True)
           self.mypost_type5.setHidden(True)
           
           self.mypost_mypost6.setHidden(True)
           self.mypost_type6.setHidden(True)
           
           self.mypost_mypost7.setHidden(True)
           self.mypost_type7.setHidden(True)
           
           self.mypost_mypost8.setHidden(True)
           self.mypost_type8.setHidden(True)
           
           self.mypost_mypost9.setHidden(True)
           self.mypost_type9.setHidden(True)
           
           self.mypost_mypost10.setHidden(True)
           self.mypost_type10.setHidden(True)
           MainWindow.setEnabled(True)
           self.blur_effect.setBlurRadius(0)
           global mypostdata1
           global mypostdata2
           global mypostdata3
           global mypostdata4
           global mypostdata5
           global mypostdata6
           global mypostdata7
           global mypostdata8
           global mypostdata9
           global mypostdata10          


           #mypost 1 Setup
           self.mypost_page.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Page 1</span></p></body></html>"))
           self.mypost_username.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">@"+ str(username)+"</span></p></body></html>"))
           try:
               mypostdata1 = (myposts[mypostno_1])
               if int(myposts[mypostno_1]['media_type'])==1:
                   mypost_req = requests.get((myposts[mypostno_1]['image_versions2']['candidates'][0]['url']))
                   mypostcache1 = open("mypost_1.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_1.png")
                   self.mypost_type1.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                   self.mypost_mypost1.setPixmap(QtGui.QPixmap("mypost_1.png"))
           
               elif int(myposts[mypostno_1]['media_type'])==2:
                   mypost_req = requests.get(myposts[mypostno_1]['image_versions2']['candidates'][0]['url'])
                   mypostcache1 = open("mypost_1.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_1.png")
                   self.mypost_mypost1.setPixmap(QtGui.QPixmap("mypost_1.png"))
                   self.mypost_type1.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))

                   
               elif int(myposts[mypostno_1]['media_type'])==8:
                   mypost_req = requests.get(myposts[mypostno_1]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                   mypostcache1 = open("mypost_1.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_1.png")
                   self.mypost_mypost1.setPixmap(QtGui.QPixmap("mypost_1.png"))
                   self.mypost_type1.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
               self.mypost_mypost1.setHidden(False)
               self.mypost_type1.setHidden(False)

           except Exception:
               mypostdata1 = None
               pass
           try:
               #mypost 2 Setup
               mypostdata2 = (myposts[mypostno_2])
               if int(myposts[mypostno_2]['media_type'])==1:
                   mypost_req = requests.get((myposts[mypostno_2]['image_versions2']['candidates'][0]['url']))
                   mypostcache1 = open("mypost_2.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_2.png")
                   self.mypost_mypost2.setPixmap(QtGui.QPixmap("mypost_2.png"))
                   self.mypost_type2.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                   
               elif int(myposts[mypostno_2]['media_type'])==2:
                   mypost_req = requests.get(myposts[mypostno_2]['image_versions2']['candidates'][0]['url'])
                   mypostcache1 = open("mypost_2.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_2.png")
                   self.mypost_mypost2.setPixmap(QtGui.QPixmap("mypost_2.png"))
                   self.mypost_type2.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                   
               elif int(myposts[mypostno_2]['media_type'])==8:
                   mypost_req = requests.get(myposts[mypostno_2]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                   mypostcache1 = open("mypost_2.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_2.png")
                   self.mypost_mypost2.setPixmap(QtGui.QPixmap("mypost_2.png"))
                   self.mypost_type2.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
               self.mypost_mypost2.setHidden(False)
               self.mypost_type2.setHidden(False)
           except Exception:
               mypostdata2 =None
               pass
            
           try:
               #mypost 3 Setup
               mypostdata3 = (myposts[mypostno_3])
               if int(myposts[mypostno_3]['media_type'])==1:
                   mypost_req = requests.get((myposts[mypostno_3]['image_versions2']['candidates'][0]['url']))
                   mypostcache1 = open("mypost_3.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_3.png")
                   self.mypost_mypost3.setPixmap(QtGui.QPixmap("mypost_3.png"))
                   self.mypost_type3.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                   
               elif int(myposts[mypostno_3]['media_type'])==2:
                   mypost_req = requests.get(myposts[mypostno_3]['image_versions2']['candidates'][0]['url'])
                   mypostcache1 = open("mypost_3.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_3.png")
                   self.mypost_mypost3.setPixmap(QtGui.QPixmap("mypost_3.png"))
                   self.mypost_type3.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                   
               elif int(myposts[mypostno_3]['media_type'])==8:
                   mypost_req = requests.get(myposts[mypostno_3]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                   mypostcache1 = open("mypost_3.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_3.png")
                   self.mypost_mypost3.setPixmap(QtGui.QPixmap("mypost_3.png"))
                   self.mypost_type3.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
               self.mypost_mypost3.setHidden(False)
               self.mypost_type3.setHidden(False)

           except Exception:
               mypostdata3 = None
               pass
           try:
               mypostdata4 = (myposts[mypostno_4])
               #mypost 4 Setup
               if int(myposts[mypostno_4]['media_type'])==1:
                   mypost_req = requests.get((myposts[mypostno_4]['image_versions2']['candidates'][0]['url']))
                   mypostcache1 = open("mypost_4.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_4.png")
                   self.mypost_mypost4.setPixmap(QtGui.QPixmap("mypost_4.png"))
                   self.mypost_type4.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                   
               elif int(myposts[mypostno_4]['media_type'])==2:
                   mypost_req = requests.get(myposts[mypostno_4]['image_versions2']['candidates'][0]['url'])
                   mypostcache1 = open("mypost_4.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_4.png")
                   self.mypost_mypost4.setPixmap(QtGui.QPixmap("mypost_4.png"))
                   self.mypost_type4.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                   
               elif int(myposts[mypostno_4]['media_type'])==8:
                   mypost_req = requests.get(myposts[mypostno_4]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                   mypostcache1 = open("mypost_4.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_4.png")
                   self.mypost_mypost4.setPixmap(QtGui.QPixmap("mypost_4.png"))
                   self.mypost_type4.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
               self.mypost_mypost4.setHidden(False)
               self.mypost_type4.setHidden(False)

           except Exception:
               mypostdata4 = None
               pass
           try:
               #mypost 5 Setup
               mypostdata5 = (myposts[mypostno_5])
               if int(myposts[mypostno_5]['media_type'])==1:
                   mypost_req = requests.get((myposts[mypostno_5]['image_versions2']['candidates'][0]['url']))
                   mypostcache1 = open("mypost_5.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_5.png")
                   self.mypost_mypost5.setPixmap(QtGui.QPixmap("mypost_5.png"))
                   self.mypost_type5.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                   
               elif int(myposts[mypostno_5]['media_type'])==2:
                   mypost_req = requests.get(myposts[mypostno_5]['image_versions2']['candidates'][0]['url'])
                   mypostcache1 = open("mypost_5.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_5.png")
                   self.mypost_mypost5.setPixmap(QtGui.QPixmap("mypost_5.png"))
                   self.mypost_type5.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                   
               elif int(myposts[mypostno_5]['media_type'])==8:
                   mypost_req = requests.get(myposts[mypostno_5]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                   mypostcache1 = open("mypost_5.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_5.png")
                   self.mypost_mypost5.setPixmap(QtGui.QPixmap("mypost_5.png"))
                   self.mypost_type5.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
               self.mypost_mypost5.setHidden(False)
               self.mypost_type5.setHidden(False)

           except Exception:
               mypostdata5 = None
               pass
           try:
               #mypost 6 Setup
               mypostdata6 = (myposts[mypostno_6])
               if int(myposts[mypostno_6]['media_type'])==1:
                   mypost_req = requests.get((myposts[mypostno_6]['image_versions2']['candidates'][0]['url']))
                   mypostcache1 = open("mypost_6.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_6.png")
                   self.mypost_mypost6.setPixmap(QtGui.QPixmap("mypost_6.png"))
                   self.mypost_type6.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                   
                   
               elif int(myposts[mypostno_6]['media_type'])==2:
                   mypost_req = requests.get(myposts[mypostno_6]['image_versions2']['candidates'][0]['url'])
                   mypostcache1 = open("mypost_6.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_6.png")
                   self.mypost_mypost6.setPixmap(QtGui.QPixmap("mypost_6.png"))
                   self.mypost_type6.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                   
               elif int(myposts[mypostno_6]['media_type'])==8:
                   mypost_req = requests.get(myposts[mypostno_6]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                   mypostcache1 = open("mypost_6.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_6.png")
                   self.mypost_mypost6.setPixmap(QtGui.QPixmap("mypost_6.png"))
                   self.mypost_type6.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
               self.mypost_mypost6.setHidden(False)
               self.mypost_type6.setHidden(False)

           except Exception:
               mypostdata6 = None
               pass
           try:
               #mypost 7 Setup
               mypostdata7 = (myposts[mypostno_7])
               if int(myposts[mypostno_7]['media_type'])==1:
                   mypost_req = requests.get((myposts[mypostno_7]['image_versions2']['candidates'][0]['url']))
                   mypostcache1 = open("mypost_7.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_7.png")
                   self.mypost_mypost7.setPixmap(QtGui.QPixmap("mypost_7.png"))
                   self.mypost_type7.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                   
               elif int(myposts[mypostno_7]['media_type'])==2:
                   mypost_req = requests.get(myposts[mypostno_7]['image_versions2']['candidates'][0]['url'])
                   mypostcache1 = open("mypost_7.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_7.png")
                   self.mypost_mypost7.setPixmap(QtGui.QPixmap("mypost_7.png"))
                   self.mypost_type7.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                   
               elif int(myposts[mypostno_7]['media_type'])==8:
                   mypost_req = requests.get(myposts[mypostno_7]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                   mypostcache1 = open("mypost_7.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_7.png")
                   self.mypost_mypost7.setPixmap(QtGui.QPixmap("mypost_7.png"))
                   self.mypost_type7.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
               self.mypost_mypost7.setHidden(False)
               self.mypost_type7.setHidden(False)

           except Exception:
               mypostdata7 = None
               pass
           try:
               #mypost 8 Setup
               mypostdata8 = (myposts[mypostno_8])
               if int(myposts[mypostno_8]['media_type'])==1:
                   mypost_req = requests.get((myposts[mypostno_8]['image_versions2']['candidates'][0]['url']))
                   mypostcache1 = open("mypost_8.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_8.png")
                   self.mypost_mypost8.setPixmap(QtGui.QPixmap("mypost_8.png"))
                   self.mypost_type8.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                   
               elif int(myposts[mypostno_8]['media_type'])==2:
                   mypost_req = requests.get(myposts[mypostno_8]['image_versions2']['candidates'][0]['url'])
                   mypostcache1 = open("mypost_8.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_8.png")
                   self.mypost_mypost8.setPixmap(QtGui.QPixmap("mypost_8.png"))
                   self.mypost_type8.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                   
               elif int(myposts[mypostno_8]['media_type'])==8:
                   mypost_req = requests.get(myposts[mypostno_8]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                   mypostcache1 = open("mypost_8.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_8.png")
                   self.mypost_mypost8.setPixmap(QtGui.QPixmap("mypost_8.png"))
                   self.mypost_type8.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
               self.mypost_mypost8.setHidden(False)
               self.mypost_type8.setHidden(False)
           except Exception:
               mypostdata8 = None
               pass
           try:
               #mypost 9 Setup
               mypostdata9 = (myposts[mypostno_9])
               if int(myposts[mypostno_9]['media_type'])==1:
                   mypost_req = requests.get((myposts[mypostno_9]['image_versions2']['candidates'][0]['url']))
                   mypostcache1 = open("mypost_9.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_9.png")
                   self.mypost_mypost9.setPixmap(QtGui.QPixmap("mypost_9.png"))
                   self.mypost_type9.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                   
               elif int(myposts[mypostno_9]['media_type'])==2:
                   mypost_req = requests.get(myposts[mypostno_9]['image_versions2']['candidates'][0]['url'])
                   mypostcache1 = open("mypost_9.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_9.png")
                   self.mypost_mypost9.setPixmap(QtGui.QPixmap("mypost_9.png"))
                   self.mypost_type9.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                   
               elif int(myposts[mypostno_9]['media_type'])==8:
                   mypost_req = requests.get(myposts[mypostno_9]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                   mypostcache1 = open("mypost_9.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_9.png")
                   self.mypost_mypost9.setPixmap(QtGui.QPixmap("mypost_9.png"))
                   self.mypost_type9.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
               self.mypost_mypost9.setHidden(False)
               self.mypost_type9.setHidden(False)
           except Exception:
               mypostdata9 = None
               pass
           try:
               #mypost 10 Setup
               mypostdata10 = (myposts[mypostno_10])
               if int(myposts[mypostno_10]['media_type'])==1:
                   mypost_req = requests.get((myposts[mypostno_10]['image_versions2']['candidates'][0]['url']))
                   mypostcache1 = open("mypost_10.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_10.png")
                   self.mypost_mypost10.setPixmap(QtGui.QPixmap("mypost_10.png"))
                   self.mypost_type10.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                   
               elif int(myposts[mypostno_10]['media_type'])==2:
                   mypost_req = requests.get(myposts[mypostno_10]['image_versions2']['candidates'][0]['url'])
                   mypostcache1 = open("mypost_10.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_10.png")
                   self.mypost_mypost10.setPixmap(QtGui.QPixmap("mypost_10.png"))
                   self.mypost_type10.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                   
               elif int(myposts[mypostno_10]['media_type'])==8:
                   mypost_req = requests.get(myposts[mypostno_10]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                   mypostcache1 = open("mypost_10.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_10.png")
                   self.mypost_mypost10.setPixmap(QtGui.QPixmap("mypost_10.png"))
                   self.mypost_type10.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
               self.mypost_mypost10.setHidden(False)
               self.mypost_type10.setHidden(False)
           except Exception:
               mypostdata10 = None
               pass      


           
        def myposts_screen():
            thread6 = threading.Thread(target=myposts_screen_thread)
            thread6.start()









        #Next mypost -Function    
        def next_myposts_thread():
           MainWindow.setGraphicsEffect(self.blur_effect)
           self.blur_effect.setBlurRadius(5)
           MainWindow.setEnabled(False)
           global mypostofuser
           global feed
           global user
           global myposts
           global page_no
           #mypost global
           global mypostno_1
           global mypostno_2
           global mypostno_3
           global mypostno_4
           global mypostno_5
           global mypostno_6
           global mypostno_7
           global mypostno_8
           global mypostno_9
           global mypostno_10         
           if feed['more_available']:
               max_id = feed["next_max_id"]
               feed = user.username_feed(mypostofuser, max_id = max_id)
               myposts.extend(feed["items"])
               
           page_no = page_no + 1
           mypostno_1 = mypostno_1+10
           mypostno_2 = mypostno_2+10
           mypostno_3 = mypostno_3+10
           mypostno_4 = mypostno_4+10
           mypostno_5 = mypostno_5+10
           mypostno_6 = mypostno_6+10
           mypostno_7 = mypostno_7+10
           mypostno_8 = mypostno_8+10
           mypostno_9 = mypostno_9+10
           mypostno_10 = mypostno_10+10
           self.mypost_mypost1.setHidden(True)
           self.mypost_type1.setHidden(True)
           
           self.mypost_mypost2.setHidden(True)
           self.mypost_type2.setHidden(True)
           
           self.mypost_mypost3.setHidden(True)
           self.mypost_type3.setHidden(True)
           
           self.mypost_mypost4.setHidden(True)
           self.mypost_type4.setHidden(True)
           
           self.mypost_mypost5.setHidden(True)
           self.mypost_type5.setHidden(True)
           
           self.mypost_mypost6.setHidden(True)
           self.mypost_type6.setHidden(True)
           
           self.mypost_mypost7.setHidden(True)
           self.mypost_type7.setHidden(True)
           
           self.mypost_mypost8.setHidden(True)
           self.mypost_type8.setHidden(True)
           
           self.mypost_mypost9.setHidden(True)
           self.mypost_type9.setHidden(True)
           
           self.mypost_mypost10.setHidden(True)
           self.mypost_type10.setHidden(True)


           global mypostdata1
           global mypostdata2
           global mypostdata3
           global mypostdata4
           global mypostdata5
           global mypostdata6
           global mypostdata7
           global mypostdata8
           global mypostdata9
           global mypostdata10
           mypostdata1 = None
           mypostdata2 = None
           mypostdata3 = None
           mypostdata4 = None
           mypostdata5 = None
           mypostdata6 = None
           mypostdata7 = None
           mypostdata8 = None
           mypostdata9 = None
           mypostdata10 = None

           MainWindow.setEnabled(True)
           self.blur_effect.setBlurRadius(0)

           self.mypost_page.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Page "+str(page_no)+"</span></p></body></html>"))

           #mypost 1 Setup
           
           #self.mypost_username.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">"+ str(usertobesearched)+"</span></p></body></html>"))
           try:
               mypostdata1 = (myposts[mypostno_1])
               if int(myposts[mypostno_1]['media_type'])==1:
                   mypost_req = requests.get((myposts[mypostno_1]['image_versions2']['candidates'][0]['url']))
                   mypostcache1 = open("mypost_1.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_1.png")
                   self.mypost_type1.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                   self.mypost_mypost1.setPixmap(QtGui.QPixmap("mypost_1.png"))
           
               elif int(myposts[mypostno_1]['media_type'])==2:
                   mypost_req = requests.get(myposts[mypostno_1]['image_versions2']['candidates'][0]['url'])
                   mypostcache1 = open("mypost_1.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_1.png")
                   self.mypost_mypost1.setPixmap(QtGui.QPixmap("mypost_1.png"))
                   self.mypost_type1.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))

                   
               elif int(myposts[mypostno_1]['media_type'])==8:
                   mypost_req = requests.get(myposts[mypostno_1]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                   mypostcache1 = open("mypost_1.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_1.png")
                   self.mypost_mypost1.setPixmap(QtGui.QPixmap("mypost_1.png"))
                   self.mypost_type1.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
               self.mypost_mypost1.setHidden(False)
               self.mypost_type1.setHidden(False)

           except Exception:
               mypostdata1 = None
               pass
           try:
               #mypost 2 Setup
               mypostdata2 = (myposts[mypostno_2])
               if int(myposts[mypostno_2]['media_type'])==1:
                   mypost_req = requests.get((myposts[mypostno_2]['image_versions2']['candidates'][0]['url']))
                   mypostcache1 = open("mypost_2.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_2.png")
                   self.mypost_mypost2.setPixmap(QtGui.QPixmap("mypost_2.png"))
                   self.mypost_type2.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                   
               elif int(myposts[mypostno_2]['media_type'])==2:
                   mypost_req = requests.get(myposts[mypostno_2]['image_versions2']['candidates'][0]['url'])
                   mypostcache1 = open("mypost_2.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_2.png")
                   self.mypost_mypost2.setPixmap(QtGui.QPixmap("mypost_2.png"))
                   self.mypost_type2.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                   
               elif int(myposts[mypostno_2]['media_type'])==8:
                   mypost_req = requests.get(myposts[mypostno_2]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                   mypostcache1 = open("mypost_2.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_2.png")
                   self.mypost_mypost2.setPixmap(QtGui.QPixmap("mypost_2.png"))
                   self.mypost_type2.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
               self.mypost_mypost2.setHidden(False)
               self.mypost_type2.setHidden(False)
           except Exception:
               mypostdata2 =None
               pass
            
           try:
               #mypost 3 Setup
               mypostdata3 = (myposts[mypostno_3])
               if int(myposts[mypostno_3]['media_type'])==1:
                   mypost_req = requests.get((myposts[mypostno_3]['image_versions2']['candidates'][0]['url']))
                   mypostcache1 = open("mypost_3.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_3.png")
                   self.mypost_mypost3.setPixmap(QtGui.QPixmap("mypost_3.png"))
                   self.mypost_type3.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                   
               elif int(myposts[mypostno_3]['media_type'])==2:
                   mypost_req = requests.get(myposts[mypostno_3]['image_versions2']['candidates'][0]['url'])
                   mypostcache1 = open("mypost_3.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_3.png")
                   self.mypost_mypost3.setPixmap(QtGui.QPixmap("mypost_3.png"))
                   self.mypost_type3.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                   
               elif int(myposts[mypostno_3]['media_type'])==8:
                   mypost_req = requests.get(myposts[mypostno_3]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                   mypostcache1 = open("mypost_3.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_3.png")
                   self.mypost_mypost3.setPixmap(QtGui.QPixmap("mypost_3.png"))
                   self.mypost_type3.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
               self.mypost_mypost3.setHidden(False)
               self.mypost_type3.setHidden(False)

           except Exception:
               mypostdata3 = None
               pass
           try:
               mypostdata4 = (myposts[mypostno_4])
               #mypost 4 Setup
               if int(myposts[mypostno_4]['media_type'])==1:
                   mypost_req = requests.get((myposts[mypostno_4]['image_versions2']['candidates'][0]['url']))
                   mypostcache1 = open("mypost_4.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_4.png")
                   self.mypost_mypost4.setPixmap(QtGui.QPixmap("mypost_4.png"))
                   self.mypost_type4.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                   
               elif int(myposts[mypostno_4]['media_type'])==2:
                   mypost_req = requests.get(myposts[mypostno_4]['image_versions2']['candidates'][0]['url'])
                   mypostcache1 = open("mypost_4.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_4.png")
                   self.mypost_mypost4.setPixmap(QtGui.QPixmap("mypost_4.png"))
                   self.mypost_type4.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                   
               elif int(myposts[mypostno_4]['media_type'])==8:
                   mypost_req = requests.get(myposts[mypostno_4]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                   mypostcache1 = open("mypost_4.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_4.png")
                   self.mypost_mypost4.setPixmap(QtGui.QPixmap("mypost_4.png"))
                   self.mypost_type4.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
               self.mypost_mypost4.setHidden(False)
               self.mypost_type4.setHidden(False)

           except Exception:
               mypostdata4 = None
               pass
           try:
               #mypost 5 Setup
               mypostdata5 = (myposts[mypostno_5])
               if int(myposts[mypostno_5]['media_type'])==1:
                   mypost_req = requests.get((myposts[mypostno_5]['image_versions2']['candidates'][0]['url']))
                   mypostcache1 = open("mypost_5.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_5.png")
                   self.mypost_mypost5.setPixmap(QtGui.QPixmap("mypost_5.png"))
                   self.mypost_type5.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                   
               elif int(myposts[mypostno_5]['media_type'])==2:
                   mypost_req = requests.get(myposts[mypostno_5]['image_versions2']['candidates'][0]['url'])
                   mypostcache1 = open("mypost_5.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_5.png")
                   self.mypost_mypost5.setPixmap(QtGui.QPixmap("mypost_5.png"))
                   self.mypost_type5.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                   
               elif int(myposts[mypostno_5]['media_type'])==8:
                   mypost_req = requests.get(myposts[mypostno_5]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                   mypostcache1 = open("mypost_5.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_5.png")
                   self.mypost_mypost5.setPixmap(QtGui.QPixmap("mypost_5.png"))
                   self.mypost_type5.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
               self.mypost_mypost5.setHidden(False)
               self.mypost_type5.setHidden(False)

           except Exception:
               mypostdata5 = None
               pass
           try:
               #mypost 6 Setup
               mypostdata6 = (myposts[mypostno_6])
               if int(myposts[mypostno_6]['media_type'])==1:
                   mypost_req = requests.get((myposts[mypostno_6]['image_versions2']['candidates'][0]['url']))
                   mypostcache1 = open("mypost_6.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_6.png")
                   self.mypost_mypost6.setPixmap(QtGui.QPixmap("mypost_6.png"))
                   self.mypost_type6.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                   
                   
               elif int(myposts[mypostno_6]['media_type'])==2:
                   mypost_req = requests.get(myposts[mypostno_6]['image_versions2']['candidates'][0]['url'])
                   mypostcache1 = open("mypost_6.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_6.png")
                   self.mypost_mypost6.setPixmap(QtGui.QPixmap("mypost_6.png"))
                   self.mypost_type6.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                   
               elif int(myposts[mypostno_6]['media_type'])==8:
                   mypost_req = requests.get(myposts[mypostno_6]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                   mypostcache1 = open("mypost_6.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_6.png")
                   self.mypost_mypost6.setPixmap(QtGui.QPixmap("mypost_6.png"))
                   self.mypost_type6.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
               self.mypost_mypost6.setHidden(False)
               self.mypost_type6.setHidden(False)

           except Exception:
               mypostdata6 = None
               pass
           try:
               #mypost 7 Setup
               mypostdata7 = (myposts[mypostno_7])
               if int(myposts[mypostno_7]['media_type'])==1:
                   mypost_req = requests.get((myposts[mypostno_7]['image_versions2']['candidates'][0]['url']))
                   mypostcache1 = open("mypost_7.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_7.png")
                   self.mypost_mypost7.setPixmap(QtGui.QPixmap("mypost_7.png"))
                   self.mypost_type7.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                   
               elif int(myposts[mypostno_7]['media_type'])==2:
                   mypost_req = requests.get(myposts[mypostno_7]['image_versions2']['candidates'][0]['url'])
                   mypostcache1 = open("mypost_7.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_7.png")
                   self.mypost_mypost7.setPixmap(QtGui.QPixmap("mypost_7.png"))
                   self.mypost_type7.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                   
               elif int(myposts[mypostno_7]['media_type'])==8:
                   mypost_req = requests.get(myposts[mypostno_7]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                   mypostcache1 = open("mypost_7.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_7.png")
                   self.mypost_mypost7.setPixmap(QtGui.QPixmap("mypost_7.png"))
                   self.mypost_type7.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
               self.mypost_mypost7.setHidden(False)
               self.mypost_type7.setHidden(False)

           except Exception:
               mypostdata7 = None
               pass
           try:
               #mypost 8 Setup
               mypostdata8 = (myposts[mypostno_8])
               if int(myposts[mypostno_8]['media_type'])==1:
                   mypost_req = requests.get((myposts[mypostno_8]['image_versions2']['candidates'][0]['url']))
                   mypostcache1 = open("mypost_8.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_8.png")
                   self.mypost_mypost8.setPixmap(QtGui.QPixmap("mypost_8.png"))
                   self.mypost_type8.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                   
               elif int(myposts[mypostno_8]['media_type'])==2:
                   mypost_req = requests.get(myposts[mypostno_8]['image_versions2']['candidates'][0]['url'])
                   mypostcache1 = open("mypost_8.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_8.png")
                   self.mypost_mypost8.setPixmap(QtGui.QPixmap("mypost_8.png"))
                   self.mypost_type8.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                   
               elif int(myposts[mypostno_8]['media_type'])==8:
                   mypost_req = requests.get(myposts[mypostno_8]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                   mypostcache1 = open("mypost_8.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_8.png")
                   self.mypost_mypost8.setPixmap(QtGui.QPixmap("mypost_8.png"))
                   self.mypost_type8.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
               self.mypost_mypost8.setHidden(False)
               self.mypost_type8.setHidden(False)
           except Exception:
               mypostdata8 = None
               pass
           try:
               #mypost 9 Setup
               mypostdata9 = (myposts[mypostno_9])
               if int(myposts[mypostno_9]['media_type'])==1:
                   mypost_req = requests.get((myposts[mypostno_9]['image_versions2']['candidates'][0]['url']))
                   mypostcache1 = open("mypost_9.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_9.png")
                   self.mypost_mypost9.setPixmap(QtGui.QPixmap("mypost_9.png"))
                   self.mypost_type9.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                   
               elif int(myposts[mypostno_9]['media_type'])==2:
                   mypost_req = requests.get(myposts[mypostno_9]['image_versions2']['candidates'][0]['url'])
                   mypostcache1 = open("mypost_9.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_9.png")
                   self.mypost_mypost9.setPixmap(QtGui.QPixmap("mypost_9.png"))
                   self.mypost_type9.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                   
               elif int(myposts[mypostno_9]['media_type'])==8:
                   mypost_req = requests.get(myposts[mypostno_9]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                   mypostcache1 = open("mypost_9.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_9.png")
                   self.mypost_mypost9.setPixmap(QtGui.QPixmap("mypost_9.png"))
                   self.mypost_type9.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
               self.mypost_mypost9.setHidden(False)
               self.mypost_type9.setHidden(False)
           except Exception:
               mypostdata9 = None
               pass
           try:
               #mypost 10 Setup
               mypostdata10 = (myposts[mypostno_10])
               if int(myposts[mypostno_10]['media_type'])==1:
                   mypost_req = requests.get((myposts[mypostno_10]['image_versions2']['candidates'][0]['url']))
                   mypostcache1 = open("mypost_10.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_10.png")
                   self.mypost_mypost10.setPixmap(QtGui.QPixmap("mypost_10.png"))
                   self.mypost_type10.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                   
               elif int(myposts[mypostno_10]['media_type'])==2:
                   mypost_req = requests.get(myposts[mypostno_10]['image_versions2']['candidates'][0]['url'])
                   mypostcache1 = open("mypost_10.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_10.png")
                   self.mypost_mypost10.setPixmap(QtGui.QPixmap("mypost_10.png"))
                   self.mypost_type10.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                   
               elif int(myposts[mypostno_10]['media_type'])==8:
                   mypost_req = requests.get(myposts[mypostno_10]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                   mypostcache1 = open("mypost_10.png", "wb")
                   mypostcache1.write(mypost_req.content)
                   mypostcache1.close()
                   #reshape("mypost_10.png")
                   self.mypost_mypost10.setPixmap(QtGui.QPixmap("mypost_10.png"))
                   self.mypost_type10.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
               self.mypost_mypost10.setHidden(False)
               self.mypost_type10.setHidden(False)
           except Exception:
               mypostdata10 = None
               pass      


               
        def next_myposts():
            thread6 = threading.Thread(target=next_myposts_thread)
            thread6.start()           


        #Back mypost -Function    
        def back_myposts_thread():
           global mypostofuser
           global feed
           global user
           global myposts
           global page_no
           #mypost global
           global mypostno_1
           global mypostno_2
           global mypostno_3
           global mypostno_4
           global mypostno_5
           global mypostno_6
           global mypostno_7
           global mypostno_8
           global mypostno_9
           global mypostno_10
           if self.mypost_page.text()== ("<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Page 1</span></p></body></html>"):
               pass
           else:
               self.mypost_mypost1.setHidden(True)
               self.mypost_type1.setHidden(True)
               
               self.mypost_mypost2.setHidden(True)
               self.mypost_type2.setHidden(True)
               
               self.mypost_mypost3.setHidden(True)
               self.mypost_type3.setHidden(True)
               
               self.mypost_mypost4.setHidden(True)
               self.mypost_type4.setHidden(True)
               
               self.mypost_mypost5.setHidden(True)
               self.mypost_type5.setHidden(True)
               
               self.mypost_mypost6.setHidden(True)
               self.mypost_type6.setHidden(True)
               
               self.mypost_mypost7.setHidden(True)
               self.mypost_type7.setHidden(True)
               
               self.mypost_mypost8.setHidden(True)
               self.mypost_type8.setHidden(True)
               
               self.mypost_mypost9.setHidden(True)
               self.mypost_type9.setHidden(True)
               
               self.mypost_mypost10.setHidden(True)
               self.mypost_type10.setHidden(True)
               MainWindow.setGraphicsEffect(self.blur_effect)
               self.blur_effect.setBlurRadius(5)
               MainWindow.setEnabled(False)
               page_no = page_no - 1

               mypostno_1 = mypostno_1-10
               mypostno_2 = mypostno_2-10
               mypostno_3 = mypostno_3-10
               mypostno_4 = mypostno_4-10
               mypostno_5 = mypostno_5-10
               mypostno_6 = mypostno_6-10
               mypostno_7 = mypostno_7-10
               mypostno_8 = mypostno_8-10
               mypostno_9 = mypostno_9-10
               mypostno_10 = mypostno_10-10

               
               global mypostdata1
               global mypostdata2
               global mypostdata3
               global mypostdata4
               global mypostdata5
               global mypostdata6
               global mypostdata7
               global mypostdata8
               global mypostdata9
               global mypostdata10          

               mypostdata1 = None
               mypostdata2 = None
               mypostdata3 = None
               mypostdata4 = None
               mypostdata5 = None
               mypostdata6 = None
               mypostdata7 = None
               mypostdata8 = None
               mypostdata9 = None
               mypostdata10 = None
               #mypost 1 Setup

               self.mypost_page.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Page "+str(page_no)+"</span></p></body></html>"))
               MainWindow.setEnabled(True)
               self.blur_effect.setBlurRadius(0)
               #self.mypost_username.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">"+ str(usertobesearched)+"</span></p></body></html>"))
               try:
                   mypostdata1 = (myposts[mypostno_1])
                   if int(myposts[mypostno_1]['media_type'])==1:
                       mypost_req = requests.get((myposts[mypostno_1]['image_versions2']['candidates'][0]['url']))
                       mypostcache1 = open("mypost_1.png", "wb")
                       mypostcache1.write(mypost_req.content)
                       mypostcache1.close()
                       #reshape("mypost_1.png")
                       self.mypost_type1.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                       self.mypost_mypost1.setPixmap(QtGui.QPixmap("mypost_1.png"))
               
                   elif int(myposts[mypostno_1]['media_type'])==2:
                       mypost_req = requests.get(myposts[mypostno_1]['image_versions2']['candidates'][0]['url'])
                       mypostcache1 = open("mypost_1.png", "wb")
                       mypostcache1.write(mypost_req.content)
                       mypostcache1.close()
                       #reshape("mypost_1.png")
                       self.mypost_mypost1.setPixmap(QtGui.QPixmap("mypost_1.png"))
                       self.mypost_type1.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))

                       
                   elif int(myposts[mypostno_1]['media_type'])==8:
                       mypost_req = requests.get(myposts[mypostno_1]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                       mypostcache1 = open("mypost_1.png", "wb")
                       mypostcache1.write(mypost_req.content)
                       mypostcache1.close()
                       #reshape("mypost_1.png")
                       self.mypost_mypost1.setPixmap(QtGui.QPixmap("mypost_1.png"))
                       self.mypost_type1.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
                   self.mypost_mypost1.setHidden(False)
                   self.mypost_type1.setHidden(False)

               except Exception:
                   mypostdata1 = None
                   pass
               try:
                   #mypost 2 Setup
                   mypostdata2 = (myposts[mypostno_2])
                   if int(myposts[mypostno_2]['media_type'])==1:
                       mypost_req = requests.get((myposts[mypostno_2]['image_versions2']['candidates'][0]['url']))
                       mypostcache1 = open("mypost_2.png", "wb")
                       mypostcache1.write(mypost_req.content)
                       mypostcache1.close()
                       #reshape("mypost_2.png")
                       self.mypost_mypost2.setPixmap(QtGui.QPixmap("mypost_2.png"))
                       self.mypost_type2.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                       
                   elif int(myposts[mypostno_2]['media_type'])==2:
                       mypost_req = requests.get(myposts[mypostno_2]['image_versions2']['candidates'][0]['url'])
                       mypostcache1 = open("mypost_2.png", "wb")
                       mypostcache1.write(mypost_req.content)
                       mypostcache1.close()
                       #reshape("mypost_2.png")
                       self.mypost_mypost2.setPixmap(QtGui.QPixmap("mypost_2.png"))
                       self.mypost_type2.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                       
                   elif int(myposts[mypostno_2]['media_type'])==8:
                       mypost_req = requests.get(myposts[mypostno_2]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                       mypostcache1 = open("mypost_2.png", "wb")
                       mypostcache1.write(mypost_req.content)
                       mypostcache1.close()
                       #reshape("mypost_2.png")
                       self.mypost_mypost2.setPixmap(QtGui.QPixmap("mypost_2.png"))
                       self.mypost_type2.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
                   self.mypost_mypost2.setHidden(False)
                   self.mypost_type2.setHidden(False)
               except Exception:
                   mypostdata2 =None
                   pass
                
               try:
                   #mypost 3 Setup
                   mypostdata3 = (myposts[mypostno_3])
                   if int(myposts[mypostno_3]['media_type'])==1:
                       mypost_req = requests.get((myposts[mypostno_3]['image_versions2']['candidates'][0]['url']))
                       mypostcache1 = open("mypost_3.png", "wb")
                       mypostcache1.write(mypost_req.content)
                       mypostcache1.close()
                       #reshape("mypost_3.png")
                       self.mypost_mypost3.setPixmap(QtGui.QPixmap("mypost_3.png"))
                       self.mypost_type3.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                       
                   elif int(myposts[mypostno_3]['media_type'])==2:
                       mypost_req = requests.get(myposts[mypostno_3]['image_versions2']['candidates'][0]['url'])
                       mypostcache1 = open("mypost_3.png", "wb")
                       mypostcache1.write(mypost_req.content)
                       mypostcache1.close()
                       #reshape("mypost_3.png")
                       self.mypost_mypost3.setPixmap(QtGui.QPixmap("mypost_3.png"))
                       self.mypost_type3.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                       
                   elif int(myposts[mypostno_3]['media_type'])==8:
                       mypost_req = requests.get(myposts[mypostno_3]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                       mypostcache1 = open("mypost_3.png", "wb")
                       mypostcache1.write(mypost_req.content)
                       mypostcache1.close()
                       #reshape("mypost_3.png")
                       self.mypost_mypost3.setPixmap(QtGui.QPixmap("mypost_3.png"))
                       self.mypost_type3.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
                   self.mypost_mypost3.setHidden(False)
                   self.mypost_type3.setHidden(False)

               except Exception:
                   mypostdata3 = None
                   pass
               try:
                   mypostdata4 = (myposts[mypostno_4])
                   #mypost 4 Setup
                   if int(myposts[mypostno_4]['media_type'])==1:
                       mypost_req = requests.get((myposts[mypostno_4]['image_versions2']['candidates'][0]['url']))
                       mypostcache1 = open("mypost_4.png", "wb")
                       mypostcache1.write(mypost_req.content)
                       mypostcache1.close()
                       #reshape("mypost_4.png")
                       self.mypost_mypost4.setPixmap(QtGui.QPixmap("mypost_4.png"))
                       self.mypost_type4.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                       
                   elif int(myposts[mypostno_4]['media_type'])==2:
                       mypost_req = requests.get(myposts[mypostno_4]['image_versions2']['candidates'][0]['url'])
                       mypostcache1 = open("mypost_4.png", "wb")
                       mypostcache1.write(mypost_req.content)
                       mypostcache1.close()
                       #reshape("mypost_4.png")
                       self.mypost_mypost4.setPixmap(QtGui.QPixmap("mypost_4.png"))
                       self.mypost_type4.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                       
                   elif int(myposts[mypostno_4]['media_type'])==8:
                       mypost_req = requests.get(myposts[mypostno_4]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                       mypostcache1 = open("mypost_4.png", "wb")
                       mypostcache1.write(mypost_req.content)
                       mypostcache1.close()
                       #reshape("mypost_4.png")
                       self.mypost_mypost4.setPixmap(QtGui.QPixmap("mypost_4.png"))
                       self.mypost_type4.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
                   self.mypost_mypost4.setHidden(False)
                   self.mypost_type4.setHidden(False)

               except Exception:
                   mypostdata4 = None
                   pass
               try:
                   #mypost 5 Setup
                   mypostdata5 = (myposts[mypostno_5])
                   if int(myposts[mypostno_5]['media_type'])==1:
                       mypost_req = requests.get((myposts[mypostno_5]['image_versions2']['candidates'][0]['url']))
                       mypostcache1 = open("mypost_5.png", "wb")
                       mypostcache1.write(mypost_req.content)
                       mypostcache1.close()
                       #reshape("mypost_5.png")
                       self.mypost_mypost5.setPixmap(QtGui.QPixmap("mypost_5.png"))
                       self.mypost_type5.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                       
                   elif int(myposts[mypostno_5]['media_type'])==2:
                       mypost_req = requests.get(myposts[mypostno_5]['image_versions2']['candidates'][0]['url'])
                       mypostcache1 = open("mypost_5.png", "wb")
                       mypostcache1.write(mypost_req.content)
                       mypostcache1.close()
                       #reshape("mypost_5.png")
                       self.mypost_mypost5.setPixmap(QtGui.QPixmap("mypost_5.png"))
                       self.mypost_type5.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                       
                   elif int(myposts[mypostno_5]['media_type'])==8:
                       mypost_req = requests.get(myposts[mypostno_5]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                       mypostcache1 = open("mypost_5.png", "wb")
                       mypostcache1.write(mypost_req.content)
                       mypostcache1.close()
                       #reshape("mypost_5.png")
                       self.mypost_mypost5.setPixmap(QtGui.QPixmap("mypost_5.png"))
                       self.mypost_type5.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
                   self.mypost_mypost5.setHidden(False)
                   self.mypost_type5.setHidden(False)

               except Exception:
                   mypostdata5 = None
                   pass
               try:
                   #mypost 6 Setup
                   mypostdata6 = (myposts[mypostno_6])
                   if int(myposts[mypostno_6]['media_type'])==1:
                       mypost_req = requests.get((myposts[mypostno_6]['image_versions2']['candidates'][0]['url']))
                       mypostcache1 = open("mypost_6.png", "wb")
                       mypostcache1.write(mypost_req.content)
                       mypostcache1.close()
                       #reshape("mypost_6.png")
                       self.mypost_mypost6.setPixmap(QtGui.QPixmap("mypost_6.png"))
                       self.mypost_type6.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                       
                       
                   elif int(myposts[mypostno_6]['media_type'])==2:
                       mypost_req = requests.get(myposts[mypostno_6]['image_versions2']['candidates'][0]['url'])
                       mypostcache1 = open("mypost_6.png", "wb")
                       mypostcache1.write(mypost_req.content)
                       mypostcache1.close()
                       #reshape("mypost_6.png")
                       self.mypost_mypost6.setPixmap(QtGui.QPixmap("mypost_6.png"))
                       self.mypost_type6.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                       
                   elif int(myposts[mypostno_6]['media_type'])==8:
                       mypost_req = requests.get(myposts[mypostno_6]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                       mypostcache1 = open("mypost_6.png", "wb")
                       mypostcache1.write(mypost_req.content)
                       mypostcache1.close()
                       #reshape("mypost_6.png")
                       self.mypost_mypost6.setPixmap(QtGui.QPixmap("mypost_6.png"))
                       self.mypost_type6.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
                   self.mypost_mypost6.setHidden(False)
                   self.mypost_type6.setHidden(False)

               except Exception:
                   mypostdata6 = None
                   pass
               try:
                   #mypost 7 Setup
                   mypostdata7 = (myposts[mypostno_7])
                   if int(myposts[mypostno_7]['media_type'])==1:
                       mypost_req = requests.get((myposts[mypostno_7]['image_versions2']['candidates'][0]['url']))
                       mypostcache1 = open("mypost_7.png", "wb")
                       mypostcache1.write(mypost_req.content)
                       mypostcache1.close()
                       #reshape("mypost_7.png")
                       self.mypost_mypost7.setPixmap(QtGui.QPixmap("mypost_7.png"))
                       self.mypost_type7.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                       
                   elif int(myposts[mypostno_7]['media_type'])==2:
                       mypost_req = requests.get(myposts[mypostno_7]['image_versions2']['candidates'][0]['url'])
                       mypostcache1 = open("mypost_7.png", "wb")
                       mypostcache1.write(mypost_req.content)
                       mypostcache1.close()
                       #reshape("mypost_7.png")
                       self.mypost_mypost7.setPixmap(QtGui.QPixmap("mypost_7.png"))
                       self.mypost_type7.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                       
                   elif int(myposts[mypostno_7]['media_type'])==8:
                       mypost_req = requests.get(myposts[mypostno_7]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                       mypostcache1 = open("mypost_7.png", "wb")
                       mypostcache1.write(mypost_req.content)
                       mypostcache1.close()
                       #reshape("mypost_7.png")
                       self.mypost_mypost7.setPixmap(QtGui.QPixmap("mypost_7.png"))
                       self.mypost_type7.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
                   self.mypost_mypost7.setHidden(False)
                   self.mypost_type7.setHidden(False)

               except Exception:
                   mypostdata7 = None
                   pass
               try:
                   #mypost 8 Setup
                   mypostdata8 = (myposts[mypostno_8])
                   if int(myposts[mypostno_8]['media_type'])==1:
                       mypost_req = requests.get((myposts[mypostno_8]['image_versions2']['candidates'][0]['url']))
                       mypostcache1 = open("mypost_8.png", "wb")
                       mypostcache1.write(mypost_req.content)
                       mypostcache1.close()
                       #reshape("mypost_8.png")
                       self.mypost_mypost8.setPixmap(QtGui.QPixmap("mypost_8.png"))
                       self.mypost_type8.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                       
                   elif int(myposts[mypostno_8]['media_type'])==2:
                       mypost_req = requests.get(myposts[mypostno_8]['image_versions2']['candidates'][0]['url'])
                       mypostcache1 = open("mypost_8.png", "wb")
                       mypostcache1.write(mypost_req.content)
                       mypostcache1.close()
                       #reshape("mypost_8.png")
                       self.mypost_mypost8.setPixmap(QtGui.QPixmap("mypost_8.png"))
                       self.mypost_type8.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                       
                   elif int(myposts[mypostno_8]['media_type'])==8:
                       mypost_req = requests.get(myposts[mypostno_8]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                       mypostcache1 = open("mypost_8.png", "wb")
                       mypostcache1.write(mypost_req.content)
                       mypostcache1.close()
                       #reshape("mypost_8.png")
                       self.mypost_mypost8.setPixmap(QtGui.QPixmap("mypost_8.png"))
                       self.mypost_type8.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
                   self.mypost_mypost8.setHidden(False)
                   self.mypost_type8.setHidden(False)
               except Exception:
                   mypostdata8 = None
                   pass
               try:
                   #mypost 9 Setup
                   mypostdata9 = (myposts[mypostno_9])
                   if int(myposts[mypostno_9]['media_type'])==1:
                       mypost_req = requests.get((myposts[mypostno_9]['image_versions2']['candidates'][0]['url']))
                       mypostcache1 = open("mypost_9.png", "wb")
                       mypostcache1.write(mypost_req.content)
                       mypostcache1.close()
                       #reshape("mypost_9.png")
                       self.mypost_mypost9.setPixmap(QtGui.QPixmap("mypost_9.png"))
                       self.mypost_type9.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                       
                   elif int(myposts[mypostno_9]['media_type'])==2:
                       mypost_req = requests.get(myposts[mypostno_9]['image_versions2']['candidates'][0]['url'])
                       mypostcache1 = open("mypost_9.png", "wb")
                       mypostcache1.write(mypost_req.content)
                       mypostcache1.close()
                       #reshape("mypost_9.png")
                       self.mypost_mypost9.setPixmap(QtGui.QPixmap("mypost_9.png"))
                       self.mypost_type9.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                       
                   elif int(myposts[mypostno_9]['media_type'])==8:
                       mypost_req = requests.get(myposts[mypostno_9]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                       mypostcache1 = open("mypost_9.png", "wb")
                       mypostcache1.write(mypost_req.content)
                       mypostcache1.close()
                       #reshape("mypost_9.png")
                       self.mypost_mypost9.setPixmap(QtGui.QPixmap("mypost_9.png"))
                       self.mypost_type9.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
                   self.mypost_mypost9.setHidden(False)
                   self.mypost_type9.setHidden(False)
               except Exception:
                   mypostdata9 = None
                   pass
               try:
                   #mypost 10 Setup
                   mypostdata10 = (myposts[mypostno_10])
                   if int(myposts[mypostno_10]['media_type'])==1:
                       mypost_req = requests.get((myposts[mypostno_10]['image_versions2']['candidates'][0]['url']))
                       mypostcache1 = open("mypost_10.png", "wb")
                       mypostcache1.write(mypost_req.content)
                       mypostcache1.close()
                       #reshape("mypost_10.png")
                       self.mypost_mypost10.setPixmap(QtGui.QPixmap("mypost_10.png"))
                       self.mypost_type10.setPixmap(QtGui.QPixmap(":/elem/video_icon2.png"))
                       
                   elif int(myposts[mypostno_10]['media_type'])==2:
                       mypost_req = requests.get(myposts[mypostno_10]['image_versions2']['candidates'][0]['url'])
                       mypostcache1 = open("mypost_10.png", "wb")
                       mypostcache1.write(mypost_req.content)
                       mypostcache1.close()
                       #reshape("mypost_10.png")
                       self.mypost_mypost10.setPixmap(QtGui.QPixmap("mypost_10.png"))
                       self.mypost_type10.setPixmap(QtGui.QPixmap(":/elem/video_icon.png"))
                       
                   elif int(myposts[mypostno_10]['media_type'])==8:
                       mypost_req = requests.get(myposts[mypostno_10]['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                       mypostcache1 = open("mypost_10.png", "wb")
                       mypostcache1.write(mypost_req.content)
                       mypostcache1.close()
                       #reshape("mypost_10.png")
                       self.mypost_mypost10.setPixmap(QtGui.QPixmap("mypost_10.png"))
                       self.mypost_type10.setPixmap(QtGui.QPixmap(":/elem/corousell_icon.png"))
                   self.mypost_mypost10.setHidden(False)
                   self.mypost_type10.setHidden(False)
               except Exception:
                   mypostdata10 = None
                   pass      

        def back_myposts():
            thread6 = threading.Thread(target=back_myposts_thread)
            thread6.start()      
        def myposts_close():
            global homesscr_select
            homesscr_select = "profile"
            setscreen_profile()
            
        def onepost_corousell():
            self.onepost_postcount.setHidden(False)
            self.onepost_back.setHidden(False)
            self.onepost_next.setHidden(False)
            self.onepost_view.setHidden(True)
            self.onepost_view_btn.setHidden(True)
        def onepost_not_corousell():
            self.onepost_postcount.setHidden(True)
            self.onepost_back.setHidden(True)
            self.onepost_next.setHidden(True)
            self.onepost_view.setHidden(True)
            self.onepost_view_btn.setHidden(True)
        def onepost_video():
            self.onepost_postcount.setHidden(True)
            self.onepost_back.setHidden(True)
            self.onepost_next.setHidden(True)
            self.onepost_view.setHidden(False)
            self.onepost_view_btn.setHidden(False)
        def onepost_video_with_corousell():
            self.onepost_postcount.setHidden(False)
            self.onepost_back.setHidden(False)
            self.onepost_next.setHidden(False)
            self.onepost_view.setHidden(False)
            self.onepost_view_btn.setHidden(False)
        def next_corousell():
            global postdata
            global total_corousell
            global post_req
            global corousell_count
            global postdataurl

            if corousell_count==total_corousell:
                pass
            else:
                corousell_count = corousell_count+1
                print(corousell_count)
                post_req = requests.get(postdata['carousel_media'][corousell_count-1]['image_versions2']['candidates'][0]['url'])
                postcache1 = open("onepost.png", "wb")
                postcache1.write(post_req.content)
                postcache1.close()
                reshape("onepost.png")
                if postdata['carousel_media'][corousell_count-1]['media_type'] ==2:
                    onepost_video_with_corousell()
                    postdataurl = postdata['carousel_media'][corousell_count-1]['video_versions'][1]['url']         
                else:
                    pass
                self.onepost_image.setPixmap(QtGui.QPixmap("onepost.png"))
                self.onepost_postcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Post "+ str(corousell_count) + "/" + str(total_corousell)+ "</span></p></body></html>"))
        def onepost_close():
            global searchsscr_select
            searchsscr_select = "posts"
            MainWindow.central_widget.setCurrentWidget(self.postscreen)
        def back_corousell():
            global postdata
            global post_req
            global total_corousell
            global corousell_count
            global postdataurl

                
            if corousell_count==1:
                pass
            else:
                corousell_count = corousell_count-1
                print(corousell_count)
                post_req = requests.get(postdata['carousel_media'][corousell_count-1]['image_versions2']['candidates'][0]['url'])
                postcache1 = open("onepost.png", "wb")
                postcache1.write(post_req.content)
                postcache1.close()
                reshape("onepost.png")
                if postdata['carousel_media'][corousell_count-1]['media_type'] ==2:
                    onemypost_mycorousell()
                    postdataurl = postdata['carousel_media'][corousell_count-1]['video_versions'][1]['url']         
                else:
                    pass
                self.onepost_image.setPixmap(QtGui.QPixmap("onepost.png"))
                self.onepost_postcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Post "+ str(corousell_count) + "/" + str(total_corousell)+ "</span></p></body></html>"))

        def like_media():
            global media_id
            global user
            global has_liked
            global like_count
            #print("kjshdjk")
            if has_liked == False:
                self.onepost_like.setPixmap(QtGui.QPixmap(":/elem/like.png"))
                user.post_like(media_id)
                has_liked = True
                like_count = like_count+1
                self.onepost_likecount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Likes: "+str(numconv(like_count))+"</span></p></body></html>"))
            else:
                self.onepost_like.setPixmap(QtGui.QPixmap(":/elem/unlike.png"))
                user.delete_like(media_id)
                has_liked = False
                like_count = like_count-1
                self.onepost_likecount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Likes: "+str(numconv(like_count))+"</span></p></body></html>"))



        def save_media():
            global media_id
            global user
            global has_saved
            if has_saved == True:
                self.onepost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
                user.unsave_photo(media_id)
                has_saved = False
            else:
                self.onepost_save.setPixmap(QtGui.QPixmap(":/elem/save.png"))
                user.save_photo(media_id)
                has_saved = True

        def download_media():
            global post_req
            saveas_dialog = QFileDialog()
            desktop_location = os.path.expanduser("~/Desktop")
            open_path = desktop_location
            filter_ext = "Image Files(*.png)"
            save_location = QFileDialog.getSaveFileName(saveas_dialog, "Download Post", open_path, "Image Files (*.png);;")
            if (save_location[0]) == "":
                pass
            else:
               active_file = open(save_location[0], "wb")
               active_file_data = active_file.write(post_req.content)
               active_file.close()

        def view_video():
            global postdataurl
            videourl = requests.get(postdataurl)
            videodownload = open("video.mp4", "wb")
            videodownload.write(videourl.content)
            videodownload.close()
            os.startfile("video.mp4")
            










            
        def copyhashtag():
            global postdata
            caption = postdata['caption']['text']
            copyhashlist_old = caption.split()
            copyhashlist_new=[]
            for item in copyhashlist_old:
               if item.startswith("#") and len(item)>1:
                  copyhashlist_new.append(item)
               else:
                  pass
            copyhash =  ' '.join(map(str, copyhashlist_new))
            pc.copy(copyhash)
            
        def translate_eng():
            global postdata
            caption = postdata['caption']['text']

            
        def postfromdata1():
            try:
                global media_id
                global postdata10
                global has_liked
                global like_count
                global corousell_count
                global usertobesearched
                global postdata
                global has_saved
                global total_corousell
                global postdataurl
                setscreen_onepost()
                postdata = postdata1
                corousell_count = 1
                global post_req
                self.onepost_username.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">"+ str(usertobesearched)+"</span></p></body></html>"))
                if postdata1['media_type'] == 8:
                    total_corousell = len(postdata1['carousel_media'])
                    post_req = requests.get(postdata1['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                    postcache1 = open("onepost.png", "wb")
                    postcache1.write(post_req.content)
                    postcache1.close()
                    reshape("onepost.png")
                    self.onepost_image.setPixmap(QtGui.QPixmap("onepost.png"))
                    if postdata1['carousel_media'][0]['media_type'] ==2:
                        onepost_video_with_corousell()
                    else:
                        onepost_corousell()
                    self.onepost_postcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Post 1/" + str(total_corousell)+ "</span></p></body></html>"))
                elif postdata1['media_type'] == 2:
                    postdataurl = postdata['video_versions'][2]['url']
                    onepost_video()
                    post_req = requests.get((postdata1['image_versions2']['candidates'][0]['url']))
                    postcache1 = open("onepost.png", "wb")
                    postcache1.write(post_req.content)
                    postcache1.close()
                    reshape("onepost.png")
                    self.onepost_image.setPixmap(QtGui.QPixmap("onepost.png"))
                    
                    
                else:
                    onepost_not_corousell()
                    post_req = requests.get((postdata1['image_versions2']['candidates'][0]['url']))
                    postcache1 = open("onepost.png", "wb")
                    postcache1.write(post_req.content)
                    postcache1.close()
                    reshape("onepost.png")
                    self.onepost_image.setPixmap(QtGui.QPixmap("onepost.png"))
                like_count = postdata1['like_count']
                try:
                    self.onepost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#f1f1f1;\">"+postdata1['caption']['text']+"</span></p></body></html>"))
                except Exception:
                    self.onepost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">This Post has no Caption.</span></p></body></html>"))
                self.onepost_likecount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Likes: "+str(numconv(like_count))+"</span></p></body></html>"))
                self.onepost_commentcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Comments: "+str(numconv(postdata1['comment_count']))+"</span></p></body></html>"))
                has_liked = (postdata1['has_liked'])
                try:
                    has_saved = postdata1['has_viewer_saved']
                    if has_saved == True:
                        self.onepost_save.setPixmap(QtGui.QPixmap(":/elem/save.png"))
                    else:
                        self.onepost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
                except Exception:
                    self.onepost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
                    has_saved = False
                if has_liked == True:
                    self.onepost_like.setPixmap(QtGui.QPixmap(":/elem/like.png"))
                else:
                    self.onepost_like.setPixmap(QtGui.QPixmap(":/elem/unlike.png"))
                media_id = postdata1['pk']
                if (postdata1['caption_is_edited']) == True:
                    self.onepost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\">Edited</span></p></body></html>"))
                else:
                    self.onepost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\"></span></p></body></html>"))
                try:
                    try:
                        self.onepost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + postdata1['facepile_top_likers'][0]['username'] + " and " +postdata1['facepile_top_likers'][1]['username'] +"</span></p></body></html>"))
                    except Exception:
                        self.onepost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + postdata1['top_likers'][0]+"</span></p></body></html>"))
                except Exception:
                    self.onepost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Not liked by anyone you follow</span></p></body></html>"))
                timestamp = time.ctime(postdata1['taken_at'])
                timestamp24hr = datetime.strptime(timestamp[11:16], "%H:%M")
                self.onepost_date.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" color:#919191;\">"+(timestamp24hr.strftime("%#I:%M%p")+ " "+timestamp[:3]+", "+timestamp[8:10]+" "+timestamp[4:7]+" "+timestamp[20:24])+"</span></p></body></html>"))


            except Exception:
                global searchsscr_select
                MainWindow.central_widget.setCurrentWidget(self.postscreen)
                pass


        def postfromdata2():
            try:
                global media_id
                global postdata2
                global has_liked
                global like_count
                global corousell_count
                global usertobesearched
                global postdata
                global has_saved
                global total_corousell
                global postdataurl
                setscreen_onepost()
                postdata = postdata2
                corousell_count = 1
                global post_req
                self.onepost_username.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">"+ str(usertobesearched)+"</span></p></body></html>"))
                if postdata2['media_type'] == 8:
                    total_corousell = len(postdata2['carousel_media'])
                    post_req = requests.get(postdata2['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                    postcache1 = open("onepost.png", "wb")
                    postcache1.write(post_req.content)
                    postcache1.close()
                    reshape("onepost.png")
                    self.onepost_image.setPixmap(QtGui.QPixmap("onepost.png"))
                    if postdata2['carousel_media'][0]['media_type'] ==2:
                        onepost_video_with_corousell()
                    else:
                        onepost_corousell()
                    self.onepost_postcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Post 1/" + str(total_corousell)+ "</span></p></body></html>"))
                elif postdata2['media_type'] == 2:
                    postdataurl = postdata['video_versions'][2]['url']
                    onepost_video()
                    post_req = requests.get((postdata2['image_versions2']['candidates'][0]['url']))
                    postcache1 = open("onepost.png", "wb")
                    postcache1.write(post_req.content)
                    postcache1.close()
                    reshape("onepost.png")
                    self.onepost_image.setPixmap(QtGui.QPixmap("onepost.png"))
                    
                    
                else:
                    onepost_not_corousell()
                    post_req = requests.get((postdata2['image_versions2']['candidates'][0]['url']))
                    postcache1 = open("onepost.png", "wb")
                    postcache1.write(post_req.content)
                    postcache1.close()
                    reshape("onepost.png")
                    self.onepost_image.setPixmap(QtGui.QPixmap("onepost.png"))
                like_count = postdata2['like_count']
                try:
                    self.onepost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#f1f1f1;\">"+postdata2['caption']['text']+"</span></p></body></html>"))
                except Exception:
                    self.onepost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">This Post has no Caption.</span></p></body></html>"))
                self.onepost_likecount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Likes: "+str(numconv(like_count))+"</span></p></body></html>"))
                self.onepost_commentcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Comments: "+str(numconv(postdata2['comment_count']))+"</span></p></body></html>"))
                has_liked = (postdata2['has_liked'])
                try:
                    has_saved = postdata2['has_viewer_saved']
                    if has_saved == True:
                        self.onepost_save.setPixmap(QtGui.QPixmap(":/elem/save.png"))
                    else:
                        self.onepost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
                except Exception:
                    self.onepost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
                    has_saved = False
                if has_liked == True:
                    self.onepost_like.setPixmap(QtGui.QPixmap(":/elem/like.png"))
                else:
                    self.onepost_like.setPixmap(QtGui.QPixmap(":/elem/unlike.png"))
                media_id = postdata2['pk']
                if (postdata2['caption_is_edited']) == True:
                    self.onepost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\">Edited</span></p></body></html>"))
                else:
                    self.onepost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\"></span></p></body></html>"))
                try:
                    try:
                        self.onepost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + postdata2['facepile_top_likers'][0]['username'] + " and " +postdata2['facepile_top_likers'][1]['username'] +"</span></p></body></html>"))
                    except Exception:
                        self.onepost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + postdata2['top_likers'][0]+"</span></p></body></html>"))
                except Exception:
                    self.onepost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Not liked by anyone you follow</span></p></body></html>"))
                timestamp = time.ctime(postdata2['taken_at'])
                timestamp24hr = datetime.strptime(timestamp[11:16], "%H:%M")
                self.onepost_date.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" color:#919191;\">"+(timestamp24hr.strftime("%#I:%M%p")+ " "+timestamp[:3]+", "+timestamp[8:10]+" "+timestamp[4:7]+" "+timestamp[20:24])+"</span></p></body></html>"))


            except Exception:
                global searchsscr_select
                MainWindow.central_widget.setCurrentWidget(self.postscreen)
                pass

        def postfromdata3():
            try:
                global media_id
                global postdata3
                global has_liked
                global like_count
                global corousell_count
                global usertobesearched
                global postdata
                global has_saved
                global total_corousell
                global postdataurl
                setscreen_onepost()
                postdata = postdata3
                corousell_count = 1
                global post_req
                self.onepost_username.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">"+ str(usertobesearched)+"</span></p></body></html>"))
                if postdata3['media_type'] == 8:
                    total_corousell = len(postdata3['carousel_media'])
                    post_req = requests.get(postdata3['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                    postcache1 = open("onepost.png", "wb")
                    postcache1.write(post_req.content)
                    postcache1.close()
                    reshape("onepost.png")
                    self.onepost_image.setPixmap(QtGui.QPixmap("onepost.png"))
                    if postdata3['carousel_media'][0]['media_type'] ==2:
                        onepost_video_with_corousell()
                    else:
                        onepost_corousell()
                    self.onepost_postcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Post 1/" + str(total_corousell)+ "</span></p></body></html>"))
                elif postdata3['media_type'] == 2:
                    postdataurl = postdata['video_versions'][2]['url']
                    onepost_video()
                    post_req = requests.get((postdata3['image_versions2']['candidates'][0]['url']))
                    postcache1 = open("onepost.png", "wb")
                    postcache1.write(post_req.content)
                    postcache1.close()
                    reshape("onepost.png")
                    self.onepost_image.setPixmap(QtGui.QPixmap("onepost.png"))
                    
                    
                else:
                    onepost_not_corousell()
                    post_req = requests.get((postdata3['image_versions2']['candidates'][0]['url']))
                    postcache1 = open("onepost.png", "wb")
                    postcache1.write(post_req.content)
                    postcache1.close()
                    reshape("onepost.png")
                    self.onepost_image.setPixmap(QtGui.QPixmap("onepost.png"))
                like_count = postdata3['like_count']
                try:
                    self.onepost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#f1f1f1;\">"+postdata3['caption']['text']+"</span></p></body></html>"))
                except Exception:
                    self.onepost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">This Post has no Caption.</span></p></body></html>"))
                self.onepost_likecount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Likes: "+str(numconv(like_count))+"</span></p></body></html>"))
                self.onepost_commentcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Comments: "+str(numconv(postdata3['comment_count']))+"</span></p></body></html>"))
                has_liked = (postdata3['has_liked'])
                try:
                    has_saved = postdata3['has_viewer_saved']
                    if has_saved == True:
                        self.onepost_save.setPixmap(QtGui.QPixmap(":/elem/save.png"))
                    else:
                        self.onepost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
                except Exception:
                    self.onepost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
                    has_saved = False
                if has_liked == True:
                    self.onepost_like.setPixmap(QtGui.QPixmap(":/elem/like.png"))
                else:
                    self.onepost_like.setPixmap(QtGui.QPixmap(":/elem/unlike.png"))
                media_id = postdata3['pk']
                if (postdata3['caption_is_edited']) == True:
                    self.onepost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\">Edited</span></p></body></html>"))
                else:
                    self.onepost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\"></span></p></body></html>"))
                try:
                    try:
                        self.onepost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + postdata3['facepile_top_likers'][0]['username'] + " and " +postdata3['facepile_top_likers'][1]['username'] +"</span></p></body></html>"))
                    except Exception:
                        self.onepost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + postdata3['top_likers'][0]+"</span></p></body></html>"))
                except Exception:
                    self.onepost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Not liked by anyone you follow</span></p></body></html>"))
                timestamp = time.ctime(postdata3['taken_at'])
                timestamp24hr = datetime.strptime(timestamp[11:16], "%H:%M")
                self.onepost_date.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" color:#919191;\">"+(timestamp24hr.strftime("%#I:%M%p")+ " "+timestamp[:3]+", "+timestamp[8:10]+" "+timestamp[4:7]+" "+timestamp[20:24])+"</span></p></body></html>"))


            except Exception:
                global searchsscr_select
                MainWindow.central_widget.setCurrentWidget(self.postscreen)
                pass


        def postfromdata4():
            try:
                global media_id
                global postdata4
                global has_liked
                global like_count
                global corousell_count
                global usertobesearched
                global postdata
                global has_saved
                global total_corousell
                global postdataurl
                setscreen_onepost()
                postdata = postdata4
                corousell_count = 1
                global post_req
                self.onepost_username.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">"+ str(usertobesearched)+"</span></p></body></html>"))
                if postdata4['media_type'] == 8:
                    total_corousell = len(postdata4['carousel_media'])
                    post_req = requests.get(postdata4['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                    postcache1 = open("onepost.png", "wb")
                    postcache1.write(post_req.content)
                    postcache1.close()
                    reshape("onepost.png")
                    self.onepost_image.setPixmap(QtGui.QPixmap("onepost.png"))
                    if postdata4['carousel_media'][0]['media_type'] ==2:
                        onepost_video_with_corousell()
                    else:
                        onepost_corousell()
                    self.onepost_postcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Post 1/" + str(total_corousell)+ "</span></p></body></html>"))
                elif postdata4['media_type'] == 2:
                    postdataurl = postdata['video_versions'][2]['url']
                    onepost_video()
                    post_req = requests.get((postdata4['image_versions2']['candidates'][0]['url']))
                    postcache1 = open("onepost.png", "wb")
                    postcache1.write(post_req.content)
                    postcache1.close()
                    reshape("onepost.png")
                    self.onepost_image.setPixmap(QtGui.QPixmap("onepost.png"))
                    
                    
                else:
                    onepost_not_corousell()
                    post_req = requests.get((postdata4['image_versions2']['candidates'][0]['url']))
                    postcache1 = open("onepost.png", "wb")
                    postcache1.write(post_req.content)
                    postcache1.close()
                    reshape("onepost.png")
                    self.onepost_image.setPixmap(QtGui.QPixmap("onepost.png"))
                like_count = postdata4['like_count']
                try:
                    self.onepost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#f1f1f1;\">"+postdata4['caption']['text']+"</span></p></body></html>"))
                except Exception:
                    self.onepost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">This Post has no Caption.</span></p></body></html>"))
                self.onepost_likecount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Likes: "+str(numconv(like_count))+"</span></p></body></html>"))
                self.onepost_commentcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Comments: "+str(numconv(postdata4['comment_count']))+"</span></p></body></html>"))
                has_liked = (postdata4['has_liked'])
                try:
                    has_saved = postdata4['has_viewer_saved']
                    if has_saved == True:
                        self.onepost_save.setPixmap(QtGui.QPixmap(":/elem/save.png"))
                    else:
                        self.onepost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
                except Exception:
                    self.onepost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
                    has_saved = False
                if has_liked == True:
                    self.onepost_like.setPixmap(QtGui.QPixmap(":/elem/like.png"))
                else:
                    self.onepost_like.setPixmap(QtGui.QPixmap(":/elem/unlike.png"))
                media_id = postdata4['pk']
                if (postdata4['caption_is_edited']) == True:
                    self.onepost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\">Edited</span></p></body></html>"))
                else:
                    self.onepost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\"></span></p></body></html>"))
                try:
                    try:
                        self.onepost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + postdata4['facepile_top_likers'][0]['username'] + " and " +postdata4['facepile_top_likers'][1]['username'] +"</span></p></body></html>"))
                    except Exception:
                        self.onepost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + postdata4['top_likers'][0]+"</span></p></body></html>"))
                except Exception:
                    self.onepost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Not liked by anyone you follow</span></p></body></html>"))
                timestamp = time.ctime(postdata4['taken_at'])
                timestamp24hr = datetime.strptime(timestamp[11:16], "%H:%M")
                self.onepost_date.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" color:#919191;\">"+(timestamp24hr.strftime("%#I:%M%p")+ " "+timestamp[:3]+", "+timestamp[8:10]+" "+timestamp[4:7]+" "+timestamp[20:24])+"</span></p></body></html>"))


            except Exception:
                global searchsscr_select
                MainWindow.central_widget.setCurrentWidget(self.postscreen)
                pass
        def postfromdata5():
            try:
                global media_id
                global postdata5
                global has_liked
                global like_count
                global corousell_count
                global usertobesearched
                global postdata
                global has_saved
                global total_corousell
                global postdataurl
                setscreen_onepost()
                postdata = postdata5
                corousell_count = 1
                global post_req
                self.onepost_username.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">"+ str(usertobesearched)+"</span></p></body></html>"))
                if postdata5['media_type'] == 8:
                    total_corousell = len(postdata5['carousel_media'])
                    post_req = requests.get(postdata5['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                    postcache1 = open("onepost.png", "wb")
                    postcache1.write(post_req.content)
                    postcache1.close()
                    reshape("onepost.png")
                    self.onepost_image.setPixmap(QtGui.QPixmap("onepost.png"))
                    if postdata5['carousel_media'][0]['media_type'] ==2:
                        onepost_video_with_corousell()
                    else:
                        onepost_corousell()
                    self.onepost_postcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Post 1/" + str(total_corousell)+ "</span></p></body></html>"))
                elif postdata5['media_type'] == 2:
                    postdataurl = postdata['video_versions'][2]['url']
                    onepost_video()
                    post_req = requests.get((postdata5['image_versions2']['candidates'][0]['url']))
                    postcache1 = open("onepost.png", "wb")
                    postcache1.write(post_req.content)
                    postcache1.close()
                    reshape("onepost.png")
                    self.onepost_image.setPixmap(QtGui.QPixmap("onepost.png"))
                    
                    
                else:
                    onepost_not_corousell()
                    post_req = requests.get((postdata5['image_versions2']['candidates'][0]['url']))
                    postcache1 = open("onepost.png", "wb")
                    postcache1.write(post_req.content)
                    postcache1.close()
                    reshape("onepost.png")
                    self.onepost_image.setPixmap(QtGui.QPixmap("onepost.png"))
                like_count = postdata5['like_count']
                try:
                    self.onepost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#f1f1f1;\">"+postdata5['caption']['text']+"</span></p></body></html>"))
                except Exception:
                    self.onepost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">This Post has no Caption.</span></p></body></html>"))
                self.onepost_likecount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Likes: "+str(numconv(like_count))+"</span></p></body></html>"))
                self.onepost_commentcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Comments: "+str(numconv(postdata5['comment_count']))+"</span></p></body></html>"))
                has_liked = (postdata5['has_liked'])
                try:
                    has_saved = postdata5['has_viewer_saved']
                    if has_saved == True:
                        self.onepost_save.setPixmap(QtGui.QPixmap(":/elem/save.png"))
                    else:
                        self.onepost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
                except Exception:
                    self.onepost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
                    has_saved = False
                if has_liked == True:
                    self.onepost_like.setPixmap(QtGui.QPixmap(":/elem/like.png"))
                else:
                    self.onepost_like.setPixmap(QtGui.QPixmap(":/elem/unlike.png"))
                media_id = postdata5['pk']
                if (postdata5['caption_is_edited']) == True:
                    self.onepost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\">Edited</span></p></body></html>"))
                else:
                    self.onepost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\"></span></p></body></html>"))
                try:
                    try:
                        self.onepost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + postdata5['facepile_top_likers'][0]['username'] + " and " +postdata5['facepile_top_likers'][1]['username'] +"</span></p></body></html>"))
                    except Exception:
                        self.onepost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + postdata5['top_likers'][0]+"</span></p></body></html>"))
                except Exception:
                    self.onepost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Not liked by anyone you follow</span></p></body></html>"))
                timestamp = time.ctime(postdata5['taken_at'])
                timestamp24hr = datetime.strptime(timestamp[11:16], "%H:%M")
                self.onepost_date.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" color:#919191;\">"+(timestamp24hr.strftime("%#I:%M%p")+ " "+timestamp[:3]+", "+timestamp[8:10]+" "+timestamp[4:7]+" "+timestamp[20:24])+"</span></p></body></html>"))


            except Exception:
                global searchsscr_select
                MainWindow.central_widget.setCurrentWidget(self.postscreen)
                pass
        def postfromdata6():
            try:
                global media_id
                global postdata6
                global has_liked
                global like_count
                global corousell_count
                global usertobesearched
                global postdata
                global has_saved
                global total_corousell
                global postdataurl
                setscreen_onepost()
                postdata = postdata6
                corousell_count = 1
                global post_req
                self.onepost_username.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">"+ str(usertobesearched)+"</span></p></body></html>"))
                if postdata6['media_type'] == 8:
                    total_corousell = len(postdata6['carousel_media'])
                    post_req = requests.get(postdata6['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                    postcache1 = open("onepost.png", "wb")
                    postcache1.write(post_req.content)
                    postcache1.close()
                    reshape("onepost.png")
                    self.onepost_image.setPixmap(QtGui.QPixmap("onepost.png"))
                    if postdata6['carousel_media'][0]['media_type'] ==2:
                        onepost_video_with_corousell()
                    else:
                        onepost_corousell()
                    self.onepost_postcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Post 1/" + str(total_corousell)+ "</span></p></body></html>"))
                elif postdata6['media_type'] == 2:
                    postdataurl = postdata['video_versions'][2]['url']
                    onepost_video()
                    post_req = requests.get((postdata6['image_versions2']['candidates'][0]['url']))
                    postcache1 = open("onepost.png", "wb")
                    postcache1.write(post_req.content)
                    postcache1.close()
                    reshape("onepost.png")
                    self.onepost_image.setPixmap(QtGui.QPixmap("onepost.png"))
                    
                    
                else:
                    onepost_not_corousell()
                    post_req = requests.get((postdata6['image_versions2']['candidates'][0]['url']))
                    postcache1 = open("onepost.png", "wb")
                    postcache1.write(post_req.content)
                    postcache1.close()
                    reshape("onepost.png")
                    self.onepost_image.setPixmap(QtGui.QPixmap("onepost.png"))
                like_count = postdata6['like_count']
                try:
                    self.onepost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#f1f1f1;\">"+postdata6['caption']['text']+"</span></p></body></html>"))
                except Exception:
                    self.onepost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">This Post has no Caption.</span></p></body></html>"))
                self.onepost_likecount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Likes: "+str(numconv(like_count))+"</span></p></body></html>"))
                self.onepost_commentcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Comments: "+str(numconv(postdata6['comment_count']))+"</span></p></body></html>"))
                has_liked = (postdata6['has_liked'])
                try:
                    has_saved = postdata6['has_viewer_saved']
                    if has_saved == True:
                        self.onepost_save.setPixmap(QtGui.QPixmap(":/elem/save.png"))
                    else:
                        self.onepost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
                except Exception:
                    self.onepost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
                    has_saved = False
                if has_liked == True:
                    self.onepost_like.setPixmap(QtGui.QPixmap(":/elem/like.png"))
                else:
                    self.onepost_like.setPixmap(QtGui.QPixmap(":/elem/unlike.png"))
                media_id = postdata6['pk']
                if (postdata6['caption_is_edited']) == True:
                    self.onepost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\">Edited</span></p></body></html>"))
                else:
                    self.onepost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\"></span></p></body></html>"))
                try:
                    try:
                        self.onepost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + postdata6['facepile_top_likers'][0]['username'] + " and " +postdata6['facepile_top_likers'][1]['username'] +"</span></p></body></html>"))
                    except Exception:
                        self.onepost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + postdata6['top_likers'][0]+"</span></p></body></html>"))
                except Exception:
                    self.onepost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Not liked by anyone you follow</span></p></body></html>"))
                timestamp = time.ctime(postdata6['taken_at'])
                timestamp24hr = datetime.strptime(timestamp[11:16], "%H:%M")
                self.onepost_date.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" color:#919191;\">"+(timestamp24hr.strftime("%#I:%M%p")+ " "+timestamp[:3]+", "+timestamp[8:10]+" "+timestamp[4:7]+" "+timestamp[20:24])+"</span></p></body></html>"))


            except Exception:
                global searchsscr_select
                MainWindow.central_widget.setCurrentWidget(self.postscreen)
                pass

        def postfromdata7():
            try:
                global media_id
                global postdata7
                global has_liked
                global like_count
                global corousell_count
                global usertobesearched
                global postdata
                global has_saved
                global total_corousell
                global postdataurl
                setscreen_onepost()
                postdata = postdata7
                corousell_count = 1
                global post_req
                self.onepost_username.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">"+ str(usertobesearched)+"</span></p></body></html>"))
                if postdata7['media_type'] == 8:
                    total_corousell = len(postdata7['carousel_media'])
                    post_req = requests.get(postdata7['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                    postcache1 = open("onepost.png", "wb")
                    postcache1.write(post_req.content)
                    postcache1.close()
                    reshape("onepost.png")
                    self.onepost_image.setPixmap(QtGui.QPixmap("onepost.png"))
                    if postdata7['carousel_media'][0]['media_type'] ==2:
                        onepost_video_with_corousell()
                    else:
                        onepost_corousell()
                    self.onepost_postcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Post 1/" + str(total_corousell)+ "</span></p></body></html>"))
                elif postdata7['media_type'] == 2:
                    postdataurl = postdata['video_versions'][2]['url']
                    onepost_video()
                    post_req = requests.get((postdata7['image_versions2']['candidates'][0]['url']))
                    postcache1 = open("onepost.png", "wb")
                    postcache1.write(post_req.content)
                    postcache1.close()
                    reshape("onepost.png")
                    self.onepost_image.setPixmap(QtGui.QPixmap("onepost.png"))
                    
                    
                else:
                    onepost_not_corousell()
                    post_req = requests.get((postdata7['image_versions2']['candidates'][0]['url']))
                    postcache1 = open("onepost.png", "wb")
                    postcache1.write(post_req.content)
                    postcache1.close()
                    reshape("onepost.png")
                    self.onepost_image.setPixmap(QtGui.QPixmap("onepost.png"))
                like_count = postdata7['like_count']
                try:
                    self.onepost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#f1f1f1;\">"+postdata7['caption']['text']+"</span></p></body></html>"))
                except Exception:
                    self.onepost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">This Post has no Caption.</span></p></body></html>"))
                self.onepost_likecount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Likes: "+str(numconv(like_count))+"</span></p></body></html>"))
                self.onepost_commentcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Comments: "+str(numconv(postdata7['comment_count']))+"</span></p></body></html>"))
                has_liked = (postdata7['has_liked'])
                try:
                    has_saved = postdata7['has_viewer_saved']
                    if has_saved == True:
                        self.onepost_save.setPixmap(QtGui.QPixmap(":/elem/save.png"))
                    else:
                        self.onepost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
                except Exception:
                    self.onepost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
                    has_saved = False
                if has_liked == True:
                    self.onepost_like.setPixmap(QtGui.QPixmap(":/elem/like.png"))
                else:
                    self.onepost_like.setPixmap(QtGui.QPixmap(":/elem/unlike.png"))
                media_id = postdata7['pk']
                if (postdata7['caption_is_edited']) == True:
                    self.onepost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\">Edited</span></p></body></html>"))
                else:
                    self.onepost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\"></span></p></body></html>"))
                try:
                    try:
                        self.onepost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + postdata7['facepile_top_likers'][0]['username'] + " and " +postdata7['facepile_top_likers'][1]['username'] +"</span></p></body></html>"))
                    except Exception:
                        self.onepost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + postdata7['top_likers'][0]+"</span></p></body></html>"))
                except Exception:
                    self.onepost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Not liked by anyone you follow</span></p></body></html>"))
                timestamp = time.ctime(postdata7['taken_at'])
                timestamp24hr = datetime.strptime(timestamp[11:16], "%H:%M")
                self.onepost_date.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" color:#919191;\">"+(timestamp24hr.strftime("%#I:%M%p")+ " "+timestamp[:3]+", "+timestamp[8:10]+" "+timestamp[4:7]+" "+timestamp[20:24])+"</span></p></body></html>"))


            except Exception:
                global searchsscr_select
                MainWindow.central_widget.setCurrentWidget(self.postscreen)
                pass
        def postfromdata8():
            try:
                global media_id
                global postdata8
                global has_liked
                global like_count
                global corousell_count
                global usertobesearched
                global postdata
                global has_saved
                global total_corousell
                global postdataurl
                setscreen_onepost()
                postdata = postdata8
                corousell_count = 1
                global post_req
                self.onepost_username.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">"+ str(usertobesearched)+"</span></p></body></html>"))
                if postdata8['media_type'] == 8:
                    total_corousell = len(postdata8['carousel_media'])
                    post_req = requests.get(postdata8['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                    postcache1 = open("onepost.png", "wb")
                    postcache1.write(post_req.content)
                    postcache1.close()
                    reshape("onepost.png")
                    self.onepost_image.setPixmap(QtGui.QPixmap("onepost.png"))
                    if postdata8['carousel_media'][0]['media_type'] ==2:
                        onepost_video_with_corousell()
                    else:
                        onepost_corousell()
                    self.onepost_postcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Post 1/" + str(total_corousell)+ "</span></p></body></html>"))
                elif postdata8['media_type'] == 2:
                    postdataurl = postdata['video_versions'][2]['url']
                    onepost_video()
                    post_req = requests.get((postdata8['image_versions2']['candidates'][0]['url']))
                    postcache1 = open("onepost.png", "wb")
                    postcache1.write(post_req.content)
                    postcache1.close()
                    reshape("onepost.png")
                    self.onepost_image.setPixmap(QtGui.QPixmap("onepost.png"))
                    
                    
                else:
                    onepost_not_corousell()
                    post_req = requests.get((postdata8['image_versions2']['candidates'][0]['url']))
                    postcache1 = open("onepost.png", "wb")
                    postcache1.write(post_req.content)
                    postcache1.close()
                    reshape("onepost.png")
                    self.onepost_image.setPixmap(QtGui.QPixmap("onepost.png"))
                like_count = postdata8['like_count']
                try:
                    self.onepost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#f1f1f1;\">"+postdata8['caption']['text']+"</span></p></body></html>"))
                except Exception:
                    self.onepost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">This Post has no Caption.</span></p></body></html>"))
                self.onepost_likecount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Likes: "+str(numconv(like_count))+"</span></p></body></html>"))
                self.onepost_commentcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Comments: "+str(numconv(postdata8['comment_count']))+"</span></p></body></html>"))
                has_liked = (postdata8['has_liked'])
                try:
                    has_saved = postdata8['has_viewer_saved']
                    if has_saved == True:
                        self.onepost_save.setPixmap(QtGui.QPixmap(":/elem/save.png"))
                    else:
                        self.onepost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
                except Exception:
                    self.onepost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
                    has_saved = False
                if has_liked == True:
                    self.onepost_like.setPixmap(QtGui.QPixmap(":/elem/like.png"))
                else:
                    self.onepost_like.setPixmap(QtGui.QPixmap(":/elem/unlike.png"))
                media_id = postdata8['pk']
                if (postdata8['caption_is_edited']) == True:
                    self.onepost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\">Edited</span></p></body></html>"))
                else:
                    self.onepost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\"></span></p></body></html>"))
                try:
                    try:
                        self.onepost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + postdata8['facepile_top_likers'][0]['username'] + " and " +postdata8['facepile_top_likers'][1]['username'] +"</span></p></body></html>"))
                    except Exception:
                        self.onepost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + postdata8['top_likers'][0]+"</span></p></body></html>"))
                except Exception:
                    self.onepost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Not liked by anyone you follow</span></p></body></html>"))
                timestamp = time.ctime(postdata8['taken_at'])
                timestamp24hr = datetime.strptime(timestamp[11:16], "%H:%M")
                self.onepost_date.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" color:#919191;\">"+(timestamp24hr.strftime("%#I:%M%p")+ " "+timestamp[:3]+", "+timestamp[8:10]+" "+timestamp[4:7]+" "+timestamp[20:24])+"</span></p></body></html>"))


            except Exception:
                global searchsscr_select
                MainWindow.central_widget.setCurrentWidget(self.postscreen)
                pass

        def postfromdata9():
            try:
                global media_id
                global postdata9
                global has_liked
                global like_count
                global corousell_count
                global usertobesearched
                global postdata
                global has_saved
                global total_corousell
                global postdataurl
                setscreen_onepost()
                postdata = postdata9
                corousell_count = 1
                global post_req
                self.onepost_username.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">"+ str(usertobesearched)+"</span></p></body></html>"))
                if postdata9['media_type'] == 8:
                    total_corousell = len(postdata9['carousel_media'])
                    post_req = requests.get(postdata9['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                    postcache1 = open("onepost.png", "wb")
                    postcache1.write(post_req.content)
                    postcache1.close()
                    reshape("onepost.png")
                    self.onepost_image.setPixmap(QtGui.QPixmap("onepost.png"))
                    if postdata9['carousel_media'][0]['media_type'] ==2:
                        onepost_video_with_corousell()
                    else:
                        onepost_corousell()
                    self.onepost_postcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Post 1/" + str(total_corousell)+ "</span></p></body></html>"))
                elif postdata9['media_type'] == 2:
                    postdataurl = postdata['video_versions'][2]['url']
                    onepost_video()
                    post_req = requests.get((postdata9['image_versions2']['candidates'][0]['url']))
                    postcache1 = open("onepost.png", "wb")
                    postcache1.write(post_req.content)
                    postcache1.close()
                    reshape("onepost.png")
                    self.onepost_image.setPixmap(QtGui.QPixmap("onepost.png"))
                    
                    
                else:
                    onepost_not_corousell()
                    post_req = requests.get((postdata9['image_versions2']['candidates'][0]['url']))
                    postcache1 = open("onepost.png", "wb")
                    postcache1.write(post_req.content)
                    postcache1.close()
                    reshape("onepost.png")
                    self.onepost_image.setPixmap(QtGui.QPixmap("onepost.png"))
                like_count = postdata9['like_count']
                try:
                    self.onepost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#f1f1f1;\">"+postdata9['caption']['text']+"</span></p></body></html>"))
                except Exception:
                    self.onepost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">This Post has no Caption.</span></p></body></html>"))
                self.onepost_likecount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Likes: "+str(numconv(like_count))+"</span></p></body></html>"))
                self.onepost_commentcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Comments: "+str(numconv(postdata9['comment_count']))+"</span></p></body></html>"))
                has_liked = (postdata9['has_liked'])
                try:
                    has_saved = postdata9['has_viewer_saved']
                    if has_saved == True:
                        self.onepost_save.setPixmap(QtGui.QPixmap(":/elem/save.png"))
                    else:
                        self.onepost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
                except Exception:
                    self.onepost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
                    has_saved = False
                if has_liked == True:
                    self.onepost_like.setPixmap(QtGui.QPixmap(":/elem/like.png"))
                else:
                    self.onepost_like.setPixmap(QtGui.QPixmap(":/elem/unlike.png"))
                media_id = postdata9['pk']
                if (postdata9['caption_is_edited']) == True:
                    self.onepost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\">Edited</span></p></body></html>"))
                else:
                    self.onepost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\"></span></p></body></html>"))
                try:
                    try:
                        self.onepost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + postdata9['facepile_top_likers'][0]['username'] + " and " +postdata9['facepile_top_likers'][1]['username'] +"</span></p></body></html>"))
                    except Exception:
                        self.onepost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + postdata9['top_likers'][0]+"</span></p></body></html>"))
                except Exception:
                    self.onepost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Not liked by anyone you follow</span></p></body></html>"))
                timestamp = time.ctime(postdata9['taken_at'])
                timestamp24hr = datetime.strptime(timestamp[11:16], "%H:%M")
                self.onepost_date.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" color:#919191;\">"+(timestamp24hr.strftime("%#I:%M%p")+ " "+timestamp[:3]+", "+timestamp[8:10]+" "+timestamp[4:7]+" "+timestamp[20:24])+"</span></p></body></html>"))


            except Exception:
                global searchsscr_select
                MainWindow.central_widget.setCurrentWidget(self.postscreen)
                pass
        def postfromdata10():
            try:
                global media_id
                global postdata10
                global has_liked
                global like_count
                global corousell_count
                global usertobesearched
                global postdata
                global has_saved
                global total_corousell
                global postdataurl
                setscreen_onepost()
                postdata = postdata10
                corousell_count = 1
                global post_req
                self.onepost_username.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">"+ str(usertobesearched)+"</span></p></body></html>"))
                if postdata10['media_type'] == 8:
                    total_corousell = len(postdata10['carousel_media'])
                    post_req = requests.get(postdata10['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                    postcache1 = open("onepost.png", "wb")
                    postcache1.write(post_req.content)
                    postcache1.close()
                    reshape("onepost.png")
                    self.onepost_image.setPixmap(QtGui.QPixmap("onepost.png"))
                    if postdata10['carousel_media'][0]['media_type'] ==2:
                        onepost_video_with_corousell()
                    else:
                        onepost_corousell()
                    self.onepost_postcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Post 1/" + str(total_corousell)+ "</span></p></body></html>"))
                elif postdata10['media_type'] == 2:
                    postdataurl = postdata['video_versions'][2]['url']
                    onepost_video()
                    post_req = requests.get((postdata10['image_versions2']['candidates'][0]['url']))
                    postcache1 = open("onepost.png", "wb")
                    postcache1.write(post_req.content)
                    postcache1.close()
                    reshape("onepost.png")
                    self.onepost_image.setPixmap(QtGui.QPixmap("onepost.png"))
                    
                    
                else:
                    onepost_not_corousell()
                    post_req = requests.get((postdata10['image_versions2']['candidates'][0]['url']))
                    postcache1 = open("onepost.png", "wb")
                    postcache1.write(post_req.content)
                    postcache1.close()
                    reshape("onepost.png")
                    self.onepost_image.setPixmap(QtGui.QPixmap("onepost.png"))
                like_count = postdata10['like_count']
                try:
                    self.onepost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#f1f1f1;\">"+postdata10['caption']['text']+"</span></p></body></html>"))
                except Exception:
                    self.onepost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">This Post has no Caption.</span></p></body></html>"))
                self.onepost_likecount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Likes: "+str(numconv(like_count))+"</span></p></body></html>"))
                self.onepost_commentcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Comments: "+str(numconv(postdata10['comment_count']))+"</span></p></body></html>"))
                has_liked = (postdata10['has_liked'])
                try:
                    has_saved = postdata10['has_viewer_saved']
                    if has_saved == True:
                        self.onepost_save.setPixmap(QtGui.QPixmap(":/elem/save.png"))
                    else:
                        self.onepost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
                except Exception:
                    self.onepost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
                    has_saved = False
                if has_liked == True:
                    self.onepost_like.setPixmap(QtGui.QPixmap(":/elem/like.png"))
                else:
                    self.onepost_like.setPixmap(QtGui.QPixmap(":/elem/unlike.png"))
                media_id = postdata10['pk']
                if (postdata10['caption_is_edited']) == True:
                    self.onepost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\">Edited</span></p></body></html>"))
                else:
                    self.onepost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\"></span></p></body></html>"))
                try:
                    try:
                        self.onepost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + postdata10['facepile_top_likers'][0]['username'] + " and " +postdata10['facepile_top_likers'][1]['username'] +"</span></p></body></html>"))
                    except Exception:
                        self.onepost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + postdata10['top_likers'][0]+"</span></p></body></html>"))
                except Exception:
                    self.onepost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Not liked by anyone you follow</span></p></body></html>"))
                timestamp = time.ctime(postdata10['taken_at'])
                timestamp24hr = datetime.strptime(timestamp[11:16], "%H:%M")
                self.onepost_date.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" color:#919191;\">"+(timestamp24hr.strftime("%#I:%M%p")+ " "+timestamp[:3]+", "+timestamp[8:10]+" "+timestamp[4:7]+" "+timestamp[20:24])+"</span></p></body></html>"))


            except Exception:
                global searchsscr_select
                MainWindow.central_widget.setCurrentWidget(self.postscreen)
                pass

        def onemypost_mycorousell():
            self.onemypost_mypostcount.setHidden(False)
            self.onemypost_back.setHidden(False)
            self.onemypost_next.setHidden(False)
            self.onemypost_view.setHidden(True)
            self.onemypost_view_btn.setHidden(True)
        def onemypost_not_mycorousell():
            self.onemypost_mypostcount.setHidden(True)
            self.onemypost_back.setHidden(True)
            self.onemypost_next.setHidden(True)
            self.onemypost_view.setHidden(True)
            self.onemypost_view_btn.setHidden(True)
        def onemypost_video():
            self.onemypost_mypostcount.setHidden(True)
            self.onemypost_back.setHidden(True)
            self.onemypost_next.setHidden(True)
            self.onemypost_view.setHidden(False)
            self.onemypost_view_btn.setHidden(False)
        def onemypost_video_with_mycorousell():
            self.onemypost_mypostcount.setHidden(False)
            self.onemypost_back.setHidden(False)
            self.onemypost_next.setHidden(False)
            self.onemypost_view.setHidden(False)
            self.onemypost_view_btn.setHidden(False)
        def next_mycorousell():
            global mypostdata
            global total_mycorousell
            global mypost_req
            global mycorousell_count
            global mypostdataurl

            if mycorousell_count==total_mycorousell:
                pass
            else:
                mycorousell_count = mycorousell_count+1
                print(mycorousell_count)
                mypost_req = requests.get(mypostdata['carousel_media'][mycorousell_count-1]['image_versions2']['candidates'][0]['url'])
                mypostcache1 = open("onemypost.png", "wb")
                mypostcache1.write(mypost_req.content)
                mypostcache1.close()
                reshape("onemypost.png")
                if mypostdata['carousel_media'][mycorousell_count-1]['media_type'] ==2:
                    onemypost_video_with_mycorousell()
                    mypostdataurl = mypostdata['carousel_media'][mycorousell_count-1]['video_versions'][1]['url']         
                else:
                    pass
                self.onemypost_image.setPixmap(QtGui.QPixmap("onemypost.png"))
                self.onemypost_mypostcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Post "+ str(mycorousell_count) + "/" + str(total_mycorousell)+ "</span></p></body></html>"))
        def onemypost_close():
            global homesscr_select
            homesscr_select = "posts"
            MainWindow.central_widget.setCurrentWidget(self.mypostscreen)
        def back_mycorousell():
            global mypostdata
            global mypost_req
            global total_mycorousell
            global mycorousell_count
            global mypostdataurl

                
            if mycorousell_count==1:
                pass
            else:
                mycorousell_count = mycorousell_count-1
                print(mycorousell_count)
                mypost_req = requests.get(mypostdata['carousel_media'][mycorousell_count-1]['image_versions2']['candidates'][0]['url'])
                mypostcache1 = open("onemypost.png", "wb")
                mypostcache1.write(mypost_req.content)
                mypostcache1.close()
                reshape("onemypost.png")
                if mypostdata['carousel_media'][mycorousell_count-1]['media_type'] ==2:
                    onemypost_mycorousell()
                    mypostdataurl = mypostdata['carousel_media'][mycorousell_count-1]['video_versions'][1]['url']         
                else:
                    pass
                self.onemypost_image.setPixmap(QtGui.QPixmap("onemypost.png"))
                self.onemypost_mypostcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Post "+ str(mycorousell_count) + "/" + str(total_mycorousell)+ "</span></p></body></html>"))

        def mylike_media():
            global mymedia_id
            global user
            global myhas_liked
            global mylike_count
            #print("kjshdjk")
            if myhas_liked == False:
                self.onemypost_like.setPixmap(QtGui.QPixmap(":/elem/like.png"))
                user.mypost_like(mymedia_id)
                myhas_liked = True
                mylike_count = mylike_count+1
                self.onemypost_likecount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Likes: "+str(numconv(mylike_count))+"</span></p></body></html>"))
            else:
                self.onemypost_like.setPixmap(QtGui.QPixmap(":/elem/unlike.png"))
                user.delete_like(mymedia_id)
                myhas_liked = False
                mylike_count = mylike_count-1
                self.onemypost_likecount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Likes: "+str(numconv(mylike_count))+"</span></p></body></html>"))



        def mysave_media():
            global mymedia_id
            global user
            global myhas_saved
            if myhas_saved == True:
                self.onemypost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
                user.unsave_photo(mymedia_id)
                myhas_saved = False
            else:
                self.onemypost_save.setPixmap(QtGui.QPixmap(":/elem/save.png"))
                user.save_photo(mymedia_id)
                myhas_saved = True

        def mydownload_media():
            global mypost_req
            saveas_dialog = QFileDialog()
            desktop_location = os.path.expanduser("~/Desktop")
            open_path = desktop_location
            filter_ext = "Image Files(*.png)"
            save_location = QFileDialog.getSaveFileName(saveas_dialog, "Download Post", open_path, "Image Files (*.png);;")
            if (save_location[0]) == "":
                pass
            else:
               active_file = open(save_location[0], "wb")
               active_file_data = active_file.write(mypost_req.content)
               active_file.close()

        def myview_video():
            global mypostdataurl
            videourl = requests.get(mypostdataurl)
            videodownload = open("video.mp4", "wb")
            videodownload.write(videourl.content)
            videodownload.close()
            os.startfile("video.mp4")
            










            
        def mycopyhashtag():
            global mypostdata
            caption = mypostdata['caption']['text']
            copyhashlist_old = caption.split()
            copyhashlist_new=[]
            for item in copyhashlist_old:
               if item.startswith("#") and len(item)>1:
                  copyhashlist_new.append(item)
               else:
                  pass
            copyhash =  ' '.join(map(str, copyhashlist_new))
            pc.copy(copyhash)
            
        def mytranslate_eng():
            global mypostdata
            caption = mypostdata['caption']['text']

            
        def mypostfromdata1():
            try:
                global mymedia_id
                global mypostdata10
                global myhas_liked
                global mylike_count
                global mycorousell_count
                global username
                global mypostdata
                global myhas_saved
                global total_mycorousell
                global mypostdataurl
                setscreen_onemypost()
                mypostdata = mypostdata1
                mycorousell_count = 1
                global mypost_req
                self.onemypost_username.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">"+ str(username)+"</span></p></body></html>"))
                if mypostdata1['media_type'] == 8:
                    total_mycorousell = len(mypostdata1['carousel_media'])
                    mypost_req = requests.get(mypostdata1['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                    mypostcache1 = open("onemypost.png", "wb")
                    mypostcache1.write(mypost_req.content)
                    mypostcache1.close()
                    reshape("onemypost.png")
                    self.onemypost_image.setPixmap(QtGui.QPixmap("onemypost.png"))
                    if mypostdata1['carousel_media'][0]['media_type'] ==2:
                        onemypost_video_with_mycorousell()
                    else:
                        onemypost_mycorousell()
                    self.onemypost_mypostcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Post 1/" + str(total_mycorousell)+ "</span></p></body></html>"))
                elif mypostdata1['media_type'] == 2:
                    mypostdataurl = mypostdata['video_versions'][2]['url']
                    onemypost_video()
                    mypost_req = requests.get((mypostdata1['image_versions2']['candidates'][0]['url']))
                    mypostcache1 = open("onemypost.png", "wb")
                    mypostcache1.write(mypost_req.content)
                    mypostcache1.close()
                    reshape("onemypost.png")
                    self.onemypost_image.setPixmap(QtGui.QPixmap("onemypost.png"))
                    
                    
                else:
                    onemypost_not_mycorousell()
                    mypost_req = requests.get((mypostdata1['image_versions2']['candidates'][0]['url']))
                    mypostcache1 = open("onemypost.png", "wb")
                    mypostcache1.write(mypost_req.content)
                    mypostcache1.close()
                    reshape("onemypost.png")
                    self.onemypost_image.setPixmap(QtGui.QPixmap("onemypost.png"))
                    mylike_count = mypostdata1['like_count']
                try:
                    self.onemypost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#f1f1f1;\">"+mypostdata1['caption']['text']+"</span></p></body></html>"))
                except Exception:
                    self.onemypost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">This mypost has no Caption.</span></p></body></html>"))
                self.onemypost_likecount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Likes: "+str(numconv(mylike_count))+"</span></p></body></html>"))
                self.onemypost_commentcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Comments: "+str(numconv(mypostdata1['comment_count']))+"</span></p></body></html>"))
                myhas_liked = (mypostdata1['has_liked'])
                try:
                    myhas_saved = mypostdata1['has_viewer_saved']
                    if myhas_saved == True:
                        self.onemypost_save.setPixmap(QtGui.QPixmap(":/elem/save.png"))
                    else:
                        self.onemypost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
                except Exception:
                    self.onemypost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
                    myhas_saved = False
                if myhas_liked == True:
                    self.onemypost_like.setPixmap(QtGui.QPixmap(":/elem/like.png"))
                else:
                    self.onemypost_like.setPixmap(QtGui.QPixmap(":/elem/unlike.png"))
                    mymedia_id = mypostdata1['pk']
                if (mypostdata1['caption_is_edited']) == True:
                    self.onemypost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\">Edited</span></p></body></html>"))
                else:
                    self.onemypost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\"></span></p></body></html>"))
                try:
                    try:
                        self.onemypost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + mypostdata1['facepile_top_likers'][0]['username'] + " and " +mypostdata1['facepile_top_likers'][1]['username'] +"</span></p></body></html>"))
                    except Exception:
                        self.onemypost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + mypostdata1['top_likers'][0]+"</span></p></body></html>"))
                except Exception:
                    self.onemypost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Not liked by anyone you follow</span></p></body></html>"))
                timestamp = time.ctime(mypostdata1['taken_at'])
                timestamp24hr = datetime.strptime(timestamp[11:16], "%H:%M")
                self.onemypost_date.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" color:#919191;\">"+(timestamp24hr.strftime("%#I:%M%p")+ " "+timestamp[:3]+", "+timestamp[8:10]+" "+timestamp[4:7]+" "+timestamp[20:24])+"</span></p></body></html>"))


            except Exception:
                global searchsscr_select
                MainWindow.central_widget.setCurrentWidget(self.mypostscreen)
                pass


        def mypostfromdata2():
            try:
                global mymedia_id
                global mypostdata2
                global mymyhas_liked
                global mylike_count
                global mycorousell_count
                global username
                global mypostdata
                global myhas_saved
                global total_mycorousell
                global mypostdataurl
                setscreen_onemypost()
                mypostdata = mypostdata2
                mycorousell_count = 1
                global mypost_req
                self.onemypost_username.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">"+ str(username)+"</span></p></body></html>"))
                if mypostdata2['media_type'] == 8:
                    total_mycorousell = len(mypostdata2['carousel_media'])
                    mypost_req = requests.get(mypostdata2['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                    mypostcache1 = open("onemypost.png", "wb")
                    mypostcache1.write(mypost_req.content)
                    mypostcache1.close()
                    reshape("onemypost.png")
                    self.onemypost_image.setPixmap(QtGui.QPixmap("onemypost.png"))
                    if mypostdata2['carousel_media'][0]['media_type'] ==2:
                        onemypost_video_with_mycorousell()
                    else:
                        onemypost_mycorousell()
                    self.onemypost_mypostcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Post 1/" + str(total_mycorousell)+ "</span></p></body></html>"))
                elif mypostdata2['media_type'] == 2:
                    mypostdataurl = mypostdata['video_versions'][2]['url']
                    onemypost_video()
                    mypost_req = requests.get((mypostdata2['image_versions2']['candidates'][0]['url']))
                    mypostcache1 = open("onemypost.png", "wb")
                    mypostcache1.write(mypost_req.content)
                    mypostcache1.close()
                    reshape("onemypost.png")
                    self.onemypost_image.setPixmap(QtGui.QPixmap("onemypost.png"))
                    
                    
                else:
                    onemypost_not_mycorousell()
                    mypost_req = requests.get((mypostdata2['image_versions2']['candidates'][0]['url']))
                    mypostcache1 = open("onemypost.png", "wb")
                    mypostcache1.write(mypost_req.content)
                    mypostcache1.close()
                    reshape("onemypost.png")
                    self.onemypost_image.setPixmap(QtGui.QPixmap("onemypost.png"))
                    mylike_count = mypostdata2['like_count']
                try:
                    self.onemypost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#f1f1f1;\">"+mypostdata2['caption']['text']+"</span></p></body></html>"))
                except Exception:
                    self.onemypost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">This mypost has no Caption.</span></p></body></html>"))
                self.onemypost_likecount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Likes: "+str(numconv(mylike_count))+"</span></p></body></html>"))
                self.onemypost_commentcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Comments: "+str(numconv(mypostdata2['comment_count']))+"</span></p></body></html>"))
                myhas_liked = (mypostdata2['has_liked'])
                try:
                    myhas_saved = mypostdata2['has_viewer_saved']
                    if myhas_saved == True:
                        self.onemypost_save.setPixmap(QtGui.QPixmap(":/elem/save.png"))
                    else:
                        self.onemypost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
                except Exception:
                    self.onemypost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
                    myhas_saved = False
                if myhas_liked == True:
                    self.onemypost_like.setPixmap(QtGui.QPixmap(":/elem/like.png"))
                else:
                    self.onemypost_like.setPixmap(QtGui.QPixmap(":/elem/unlike.png"))
                    mymedia_id = mypostdata2['pk']
                if (mypostdata2['caption_is_edited']) == True:
                    self.onemypost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\">Edited</span></p></body></html>"))
                else:
                    self.onemypost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\"></span></p></body></html>"))
                try:
                    try:
                        self.onemypost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + mypostdata2['facepile_top_likers'][0]['username'] + " and " +mypostdata2['facepile_top_likers'][1]['username'] +"</span></p></body></html>"))
                    except Exception:
                        self.onemypost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + mypostdata2['top_likers'][0]+"</span></p></body></html>"))
                except Exception:
                    self.onemypost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Not liked by anyone you follow</span></p></body></html>"))
                timestamp = time.ctime(mypostdata2['taken_at'])
                timestamp24hr = datetime.strptime(timestamp[11:16], "%H:%M")
                self.onemypost_date.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" color:#919191;\">"+(timestamp24hr.strftime("%#I:%M%p")+ " "+timestamp[:3]+", "+timestamp[8:10]+" "+timestamp[4:7]+" "+timestamp[20:24])+"</span></p></body></html>"))


            except Exception:
                global searchsscr_select
                MainWindow.central_widget.setCurrentWidget(self.mypostscreen)
                pass

        def mypostfromdata3():
            try:
                global mymedia_id
                global mypostdata3
                global myhas_liked
                global mylike_count
                global mycorousell_count
                global username
                global mypostdata
                global myhas_saved
                global total_mycorousell
                global mypostdataurl
                setscreen_onemypost()
                mypostdata = mypostdata3
                mycorousell_count = 1
                global mypost_req
                self.onemypost_username.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">"+ str(username)+"</span></p></body></html>"))
                if mypostdata3['media_type'] == 8:
                    total_mycorousell = len(mypostdata3['carousel_media'])
                    mypost_req = requests.get(mypostdata3['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                    mypostcache1 = open("onemypost.png", "wb")
                    mypostcache1.write(mypost_req.content)
                    mypostcache1.close()
                    reshape("onemypost.png")
                    self.onemypost_image.setPixmap(QtGui.QPixmap("onemypost.png"))
                    if mypostdata3['carousel_media'][0]['media_type'] ==2:
                        onemypost_video_with_mycorousell()
                    else:
                        onemypost_mycorousell()
                    self.onemypost_mypostcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Post 1/" + str(total_mycorousell)+ "</span></p></body></html>"))
                elif mypostdata3['media_type'] == 2:
                    mypostdataurl = mypostdata['video_versions'][2]['url']
                    onemypost_video()
                    mypost_req = requests.get((mypostdata3['image_versions2']['candidates'][0]['url']))
                    mypostcache1 = open("onemypost.png", "wb")
                    mypostcache1.write(mypost_req.content)
                    mypostcache1.close()
                    reshape("onemypost.png")
                    self.onemypost_image.setPixmap(QtGui.QPixmap("onemypost.png"))
                    
                    
                else:
                    onemypost_not_mycorousell()
                    mypost_req = requests.get((mypostdata3['image_versions2']['candidates'][0]['url']))
                    mypostcache1 = open("onemypost.png", "wb")
                    mypostcache1.write(mypost_req.content)
                    mypostcache1.close()
                    reshape("onemypost.png")
                    self.onemypost_image.setPixmap(QtGui.QPixmap("onemypost.png"))
                    mylike_count = mypostdata3['like_count']
                try:
                    self.onemypost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#f1f1f1;\">"+mypostdata3['caption']['text']+"</span></p></body></html>"))
                except Exception:
                    self.onemypost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">This mypost has no Caption.</span></p></body></html>"))
                self.onemypost_likecount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Likes: "+str(numconv(mylike_count))+"</span></p></body></html>"))
                self.onemypost_commentcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Comments: "+str(numconv(mypostdata3['comment_count']))+"</span></p></body></html>"))
                myhas_liked = (mypostdata3['has_liked'])
                try:
                    myhas_saved = mypostdata3['has_viewer_saved']
                    if myhas_saved == True:
                        self.onemypost_save.setPixmap(QtGui.QPixmap(":/elem/save.png"))
                    else:
                        self.onemypost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
                except Exception:
                    self.onemypost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
                    myhas_saved = False
                if myhas_liked == True:
                    self.onemypost_like.setPixmap(QtGui.QPixmap(":/elem/like.png"))
                else:
                    self.onemypost_like.setPixmap(QtGui.QPixmap(":/elem/unlike.png"))
                    mymedia_id = mypostdata3['pk']
                if (mypostdata3['caption_is_edited']) == True:
                    self.onemypost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\">Edited</span></p></body></html>"))
                else:
                    self.onemypost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\"></span></p></body></html>"))
                try:
                    try:
                        self.onemypost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + mypostdata3['facepile_top_likers'][0]['username'] + " and " +mypostdata3['facepile_top_likers'][1]['username'] +"</span></p></body></html>"))
                    except Exception:
                        self.onemypost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + mypostdata3['top_likers'][0]+"</span></p></body></html>"))
                except Exception:
                    self.onemypost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Not liked by anyone you follow</span></p></body></html>"))
                timestamp = time.ctime(mypostdata3['taken_at'])
                timestamp24hr = datetime.strptime(timestamp[11:16], "%H:%M")
                self.onemypost_date.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" color:#919191;\">"+(timestamp24hr.strftime("%#I:%M%p")+ " "+timestamp[:3]+", "+timestamp[8:10]+" "+timestamp[4:7]+" "+timestamp[20:24])+"</span></p></body></html>"))


            except Exception:
                global searchsscr_select
                MainWindow.central_widget.setCurrentWidget(self.mypostscreen)
                pass


        def mypostfromdata4():
            try:
                global mymedia_id
                global mypostdata4
                global myhas_liked
                global mylike_count
                global mycorousell_count
                global username
                global mypostdata
                global myhas_saved
                global total_mycorousell
                global mypostdataurl
                setscreen_onemypost()
                mypostdata = mypostdata4
                mycorousell_count = 1
                global mypost_req
                self.onemypost_username.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">"+ str(username)+"</span></p></body></html>"))
                if mypostdata4['media_type'] == 8:
                    total_mycorousell = len(mypostdata4['carousel_media'])
                    mypost_req = requests.get(mypostdata4['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                    mypostcache1 = open("onemypost.png", "wb")
                    mypostcache1.write(mypost_req.content)
                    mypostcache1.close()
                    reshape("onemypost.png")
                    self.onemypost_image.setPixmap(QtGui.QPixmap("onemypost.png"))
                    if mypostdata4['carousel_media'][0]['media_type'] ==2:
                        onemypost_video_with_mycorousell()
                    else:
                        onemypost_mycorousell()
                    self.onemypost_mypostcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Post 1/" + str(total_mycorousell)+ "</span></p></body></html>"))
                elif mypostdata4['media_type'] == 2:
                    mypostdataurl = mypostdata['video_versions'][2]['url']
                    onemypost_video()
                    mypost_req = requests.get((mypostdata4['image_versions2']['candidates'][0]['url']))
                    mypostcache1 = open("onemypost.png", "wb")
                    mypostcache1.write(mypost_req.content)
                    mypostcache1.close()
                    reshape("onemypost.png")
                    self.onemypost_image.setPixmap(QtGui.QPixmap("onemypost.png"))
                    
                    
                else:
                    onemypost_not_mycorousell()
                    mypost_req = requests.get((mypostdata4['image_versions2']['candidates'][0]['url']))
                    mypostcache1 = open("onemypost.png", "wb")
                    mypostcache1.write(mypost_req.content)
                    mypostcache1.close()
                    reshape("onemypost.png")
                    self.onemypost_image.setPixmap(QtGui.QPixmap("onemypost.png"))
                    mylike_count = mypostdata4['like_count']
                try:
                    self.onemypost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#f1f1f1;\">"+mypostdata4['caption']['text']+"</span></p></body></html>"))
                except Exception:
                    self.onemypost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">This mypost has no Caption.</span></p></body></html>"))
                self.onemypost_likecount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Likes: "+str(numconv(mylike_count))+"</span></p></body></html>"))
                self.onemypost_commentcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Comments: "+str(numconv(mypostdata4['comment_count']))+"</span></p></body></html>"))
                myhas_liked = (mypostdata4['has_liked'])
                try:
                    myhas_saved = mypostdata4['has_viewer_saved']
                    if myhas_saved == True:
                        self.onemypost_save.setPixmap(QtGui.QPixmap(":/elem/save.png"))
                    else:
                        self.onemypost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
                except Exception:
                    self.onemypost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
                    myhas_saved = False
                if myhas_liked == True:
                    self.onemypost_like.setPixmap(QtGui.QPixmap(":/elem/like.png"))
                else:
                    self.onemypost_like.setPixmap(QtGui.QPixmap(":/elem/unlike.png"))
                    mymedia_id = mypostdata4['pk']
                if (mypostdata4['caption_is_edited']) == True:
                    self.onemypost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\">Edited</span></p></body></html>"))
                else:
                    self.onemypost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\"></span></p></body></html>"))
                try:
                    try:
                        self.onemypost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + mypostdata4['facepile_top_likers'][0]['username'] + " and " +mypostdata4['facepile_top_likers'][1]['username'] +"</span></p></body></html>"))
                    except Exception:
                        self.onemypost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + mypostdata4['top_likers'][0]+"</span></p></body></html>"))
                except Exception:
                    self.onemypost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Not liked by anyone you follow</span></p></body></html>"))
                timestamp = time.ctime(mypostdata4['taken_at'])
                timestamp24hr = datetime.strptime(timestamp[11:16], "%H:%M")
                self.onemypost_date.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" color:#919191;\">"+(timestamp24hr.strftime("%#I:%M%p")+ " "+timestamp[:3]+", "+timestamp[8:10]+" "+timestamp[4:7]+" "+timestamp[20:24])+"</span></p></body></html>"))


            except Exception:
                global searchsscr_select
                MainWindow.central_widget.setCurrentWidget(self.mypostscreen)
                pass
        def mypostfromdata5():
            try:
                global mymedia_id
                global mypostdata5
                global myhas_liked
                global mylike_count
                global mycorousell_count
                global username
                global mypostdata
                global myhas_saved
                global total_mycorousell
                global mypostdataurl
                setscreen_onemypost()
                mypostdata = mypostdata5
                mycorousell_count = 1
                global mypost_req
                self.onemypost_username.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">"+ str(username)+"</span></p></body></html>"))
                if mypostdata5['media_type'] == 8:
                    total_mycorousell = len(mypostdata5['carousel_media'])
                    mypost_req = requests.get(mypostdata5['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                    mypostcache1 = open("onemypost.png", "wb")
                    mypostcache1.write(mypost_req.content)
                    mypostcache1.close()
                    reshape("onemypost.png")
                    self.onemypost_image.setPixmap(QtGui.QPixmap("onemypost.png"))
                    if mypostdata5['carousel_media'][0]['media_type'] ==2:
                        onemypost_video_with_mycorousell()
                    else:
                        onemypost_mycorousell()
                    self.onemypost_mypostcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Post 1/" + str(total_mycorousell)+ "</span></p></body></html>"))
                elif mypostdata5['media_type'] == 2:
                    mypostdataurl = mypostdata['video_versions'][2]['url']
                    onemypost_video()
                    mypost_req = requests.get((mypostdata5['image_versions2']['candidates'][0]['url']))
                    mypostcache1 = open("onemypost.png", "wb")
                    mypostcache1.write(mypost_req.content)
                    mypostcache1.close()
                    reshape("onemypost.png")
                    self.onemypost_image.setPixmap(QtGui.QPixmap("onemypost.png"))
                    
                    
                else:
                    onemypost_not_mycorousell()
                    mypost_req = requests.get((mypostdata5['image_versions2']['candidates'][0]['url']))
                    mypostcache1 = open("onemypost.png", "wb")
                    mypostcache1.write(mypost_req.content)
                    mypostcache1.close()
                    reshape("onemypost.png")
                    self.onemypost_image.setPixmap(QtGui.QPixmap("onemypost.png"))
                    mylike_count = mypostdata5['like_count']
                try:
                    self.onemypost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#f1f1f1;\">"+mypostdata5['caption']['text']+"</span></p></body></html>"))
                except Exception:
                    self.onemypost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">This mypost has no Caption.</span></p></body></html>"))
                self.onemypost_likecount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Likes: "+str(numconv(mylike_count))+"</span></p></body></html>"))
                self.onemypost_commentcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Comments: "+str(numconv(mypostdata5['comment_count']))+"</span></p></body></html>"))
                myhas_liked = (mypostdata5['has_liked'])
                try:
                    myhas_saved = mypostdata5['has_viewer_saved']
                    if myhas_saved == True:
                        self.onemypost_save.setPixmap(QtGui.QPixmap(":/elem/save.png"))
                    else:
                        self.onemypost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
                except Exception:
                    self.onemypost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
                    myhas_saved = False
                if myhas_liked == True:
                    self.onemypost_like.setPixmap(QtGui.QPixmap(":/elem/like.png"))
                else:
                    self.onemypost_like.setPixmap(QtGui.QPixmap(":/elem/unlike.png"))
                    mymedia_id = mypostdata5['pk']
                if (mypostdata5['caption_is_edited']) == True:
                    self.onemypost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\">Edited</span></p></body></html>"))
                else:
                    self.onemypost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\"></span></p></body></html>"))
                try:
                    try:
                        self.onemypost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + mypostdata5['facepile_top_likers'][0]['username'] + " and " +mypostdata5['facepile_top_likers'][1]['username'] +"</span></p></body></html>"))
                    except Exception:
                        self.onemypost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + mypostdata5['top_likers'][0]+"</span></p></body></html>"))
                except Exception:
                    self.onemypost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Not liked by anyone you follow</span></p></body></html>"))
                timestamp = time.ctime(mypostdata5['taken_at'])
                timestamp24hr = datetime.strptime(timestamp[11:16], "%H:%M")
                self.onemypost_date.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" color:#919191;\">"+(timestamp24hr.strftime("%#I:%M%p")+ " "+timestamp[:3]+", "+timestamp[8:10]+" "+timestamp[4:7]+" "+timestamp[20:24])+"</span></p></body></html>"))


            except Exception:
                global searchsscr_select
                MainWindow.central_widget.setCurrentWidget(self.mypostscreen)
                pass
        def mypostfromdata6():
            try:
                global mymedia_id
                global mypostdata6
                global myhas_liked
                global mylike_count
                global mycorousell_count
                global username
                global mypostdata
                global myhas_saved
                global total_mycorousell
                global mypostdataurl
                setscreen_onemypost()
                mypostdata = mypostdata6
                mycorousell_count = 1
                global mypost_req
                self.onemypost_username.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">"+ str(username)+"</span></p></body></html>"))
                if mypostdata6['media_type'] == 8:
                    total_mycorousell = len(mypostdata6['carousel_media'])
                    mypost_req = requests.get(mypostdata6['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                    mypostcache1 = open("onemypost.png", "wb")
                    mypostcache1.write(mypost_req.content)
                    mypostcache1.close()
                    reshape("onemypost.png")
                    self.onemypost_image.setPixmap(QtGui.QPixmap("onemypost.png"))
                    if mypostdata6['carousel_media'][0]['media_type'] ==2:
                        onemypost_video_with_mycorousell()
                    else:
                        onemypost_mycorousell()
                    self.onemypost_mypostcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Post 1/" + str(total_mycorousell)+ "</span></p></body></html>"))
                elif mypostdata6['media_type'] == 2:
                    mypostdataurl = mypostdata['video_versions'][2]['url']
                    onemypost_video()
                    mypost_req = requests.get((mypostdata6['image_versions2']['candidates'][0]['url']))
                    mypostcache1 = open("onemypost.png", "wb")
                    mypostcache1.write(mypost_req.content)
                    mypostcache1.close()
                    reshape("onemypost.png")
                    self.onemypost_image.setPixmap(QtGui.QPixmap("onemypost.png"))
                    
                    
                else:
                    onemypost_not_mycorousell()
                    mypost_req = requests.get((mypostdata6['image_versions2']['candidates'][0]['url']))
                    mypostcache1 = open("onemypost.png", "wb")
                    mypostcache1.write(mypost_req.content)
                    mypostcache1.close()
                    reshape("onemypost.png")
                    self.onemypost_image.setPixmap(QtGui.QPixmap("onemypost.png"))
                    mylike_count = mypostdata6['like_count']
                try:
                    self.onemypost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#f1f1f1;\">"+mypostdata6['caption']['text']+"</span></p></body></html>"))
                except Exception:
                    self.onemypost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">This mypost has no Caption.</span></p></body></html>"))
                self.onemypost_likecount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Likes: "+str(numconv(mylike_count))+"</span></p></body></html>"))
                self.onemypost_commentcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Comments: "+str(numconv(mypostdata6['comment_count']))+"</span></p></body></html>"))
                myhas_liked = (mypostdata6['has_liked'])
                try:
                    myhas_saved = mypostdata6['has_viewer_saved']
                    if myhas_saved == True:
                        self.onemypost_save.setPixmap(QtGui.QPixmap(":/elem/save.png"))
                    else:
                        self.onemypost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
                except Exception:
                    self.onemypost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
                    myhas_saved = False
                if myhas_liked == True:
                    self.onemypost_like.setPixmap(QtGui.QPixmap(":/elem/like.png"))
                else:
                    self.onemypost_like.setPixmap(QtGui.QPixmap(":/elem/unlike.png"))
                    mymedia_id = mypostdata6['pk']
                if (mypostdata6['caption_is_edited']) == True:
                    self.onemypost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\">Edited</span></p></body></html>"))
                else:
                    self.onemypost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\"></span></p></body></html>"))
                try:
                    try:
                        self.onemypost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + mypostdata6['facepile_top_likers'][0]['username'] + " and " +mypostdata6['facepile_top_likers'][1]['username'] +"</span></p></body></html>"))
                    except Exception:
                        self.onemypost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + mypostdata6['top_likers'][0]+"</span></p></body></html>"))
                except Exception:
                    self.onemypost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Not liked by anyone you follow</span></p></body></html>"))
                timestamp = time.ctime(mypostdata6['taken_at'])
                timestamp24hr = datetime.strptime(timestamp[11:16], "%H:%M")
                self.onemypost_date.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" color:#919191;\">"+(timestamp24hr.strftime("%#I:%M%p")+ " "+timestamp[:3]+", "+timestamp[8:10]+" "+timestamp[4:7]+" "+timestamp[20:24])+"</span></p></body></html>"))


            except Exception:
                global searchsscr_select
                MainWindow.central_widget.setCurrentWidget(self.mypostscreen)
                pass

        def mypostfromdata7():
            try:
                    global mymedia_id
                    global mypostdata7
                    global myhas_liked
                    global mylike_count
                    global mycorousell_count
                    global username
                    global mypostdata
                    global myhas_saved
                    global total_mycorousell
                    global mypostdataurl
                    setscreen_onemypost()
                    mypostdata = mypostdata7
                    mycorousell_count = 1
                    global mypost_req
                    self.onemypost_username.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">"+ str(username)+"</span></p></body></html>"))
                    if mypostdata7['media_type'] == 8:
                        total_mycorousell = len(mypostdata7['carousel_media'])
                        mypost_req = requests.get(mypostdata7['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                        mypostcache1 = open("onemypost.png", "wb")
                        mypostcache1.write(mypost_req.content)
                        mypostcache1.close()
                        reshape("onemypost.png")
                        self.onemypost_image.setPixmap(QtGui.QPixmap("onemypost.png"))
                        if mypostdata7['carousel_media'][0]['media_type'] ==2:
                            onemypost_video_with_mycorousell()
                        else:
                            onemypost_mycorousell()
                        self.onemypost_mypostcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Post 1/" + str(total_mycorousell)+ "</span></p></body></html>"))
                    elif mypostdata7['media_type'] == 2:
                        mypostdataurl = mypostdata['video_versions'][2]['url']
                        onemypost_video()
                        mypost_req = requests.get((mypostdata7['image_versions2']['candidates'][0]['url']))
                        mypostcache1 = open("onemypost.png", "wb")
                        mypostcache1.write(mypost_req.content)
                        mypostcache1.close()
                        reshape("onemypost.png")
                        self.onemypost_image.setPixmap(QtGui.QPixmap("onemypost.png"))
                        
                        
                    else:
                        onemypost_not_mycorousell()
                        mypost_req = requests.get((mypostdata7['image_versions2']['candidates'][0]['url']))
                        mypostcache1 = open("onemypost.png", "wb")
                        mypostcache1.write(mypost_req.content)
                        mypostcache1.close()
                        reshape("onemypost.png")
                        self.onemypost_image.setPixmap(QtGui.QPixmap("onemypost.png"))
                        mylike_count = mypostdata7['like_count']
                    try:
                        self.onemypost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#f1f1f1;\">"+mypostdata7['caption']['text']+"</span></p></body></html>"))
                    except Exception:
                        self.onemypost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">This mypost has no Caption.</span></p></body></html>"))
                    self.onemypost_likecount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Likes: "+str(numconv(mylike_count))+"</span></p></body></html>"))
                    self.onemypost_commentcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Comments: "+str(numconv(mypostdata7['comment_count']))+"</span></p></body></html>"))
                    myhas_liked = (mypostdata7['has_liked'])
                    try:
                        myhas_saved = mypostdata7['has_viewer_saved']
                        if myhas_saved == True:
                            self.onemypost_save.setPixmap(QtGui.QPixmap(":/elem/save.png"))
                        else:
                            self.onemypost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
                    except Exception:
                        self.onemypost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
                        myhas_saved = False
                    if myhas_liked == True:
                        self.onemypost_like.setPixmap(QtGui.QPixmap(":/elem/like.png"))
                    else:
                        self.onemypost_like.setPixmap(QtGui.QPixmap(":/elem/unlike.png"))
                        mymedia_id = mypostdata7['pk']
                    if (mypostdata7['caption_is_edited']) == True:
                        self.onemypost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\">Edited</span></p></body></html>"))
                    else:
                        self.onemypost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\"></span></p></body></html>"))
                    try:
                        try:
                            self.onemypost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + mypostdata7['facepile_top_likers'][0]['username'] + " and " +mypostdata7['facepile_top_likers'][1]['username'] +"</span></p></body></html>"))
                        except Exception:
                            self.onemypost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + mypostdata7['top_likers'][0]+"</span></p></body></html>"))
                    except Exception:
                        self.onemypost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Not liked by anyone you follow</span></p></body></html>"))
                    timestamp = time.ctime(mypostdata7['taken_at'])
                    timestamp24hr = datetime.strptime(timestamp[11:16], "%H:%M")
                    self.onemypost_date.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" color:#919191;\">"+(timestamp24hr.strftime("%#I:%M%p")+ " "+timestamp[:3]+", "+timestamp[8:10]+" "+timestamp[4:7]+" "+timestamp[20:24])+"</span></p></body></html>"))


            except Exception:
                global searchsscr_select
                MainWindow.central_widget.setCurrentWidget(self.mypostscreen)
                pass
        def mypostfromdata8():
            try:
                global mymedia_id
                global mypostdata8
                global myhas_liked
                global mylike_count
                global mycorousell_count
                global username
                global mypostdata
                global myhas_saved
                global total_mycorousell
                global mypostdataurl
                setscreen_onemypost()
                mypostdata = mypostdata8
                mycorousell_count = 1
                global mypost_req
                self.onemypost_username.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">"+ str(username)+"</span></p></body></html>"))
                if mypostdata8['media_type'] == 8:
                    total_mycorousell = len(mypostdata8['carousel_media'])
                    mypost_req = requests.get(mypostdata8['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                    mypostcache1 = open("onemypost.png", "wb")
                    mypostcache1.write(mypost_req.content)
                    mypostcache1.close()
                    reshape("onemypost.png")
                    self.onemypost_image.setPixmap(QtGui.QPixmap("onemypost.png"))
                    if mypostdata8['carousel_media'][0]['media_type'] ==2:
                        onemypost_video_with_mycorousell()
                    else:
                        onemypost_mycorousell()
                    self.onemypost_mypostcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Post 1/" + str(total_mycorousell)+ "</span></p></body></html>"))
                elif mypostdata8['media_type'] == 2:
                    mypostdataurl = mypostdata['video_versions'][2]['url']
                    onemypost_video()
                    mypost_req = requests.get((mypostdata8['image_versions2']['candidates'][0]['url']))
                    mypostcache1 = open("onemypost.png", "wb")
                    mypostcache1.write(mypost_req.content)
                    mypostcache1.close()
                    reshape("onemypost.png")
                    self.onemypost_image.setPixmap(QtGui.QPixmap("onemypost.png"))
                    
                    
                else:
                    onemypost_not_mycorousell()
                    mypost_req = requests.get((mypostdata8['image_versions2']['candidates'][0]['url']))
                    mypostcache1 = open("onemypost.png", "wb")
                    mypostcache1.write(mypost_req.content)
                    mypostcache1.close()
                    reshape("onemypost.png")
                    self.onemypost_image.setPixmap(QtGui.QPixmap("onemypost.png"))
                    mylike_count = mypostdata8['like_count']
                try:
                    self.onemypost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#f1f1f1;\">"+mypostdata8['caption']['text']+"</span></p></body></html>"))
                except Exception:
                    self.onemypost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">This mypost has no Caption.</span></p></body></html>"))
                self.onemypost_likecount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Likes: "+str(numconv(mylike_count))+"</span></p></body></html>"))
                self.onemypost_commentcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Comments: "+str(numconv(mypostdata8['comment_count']))+"</span></p></body></html>"))
                myhas_liked = (mypostdata8['has_liked'])
                try:
                    myhas_saved = mypostdata8['has_viewer_saved']
                    if myhas_saved == True:
                        self.onemypost_save.setPixmap(QtGui.QPixmap(":/elem/save.png"))
                    else:
                        self.onemypost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
                except Exception:
                    self.onemypost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
                    myhas_saved = False
                if myhas_liked == True:
                    self.onemypost_like.setPixmap(QtGui.QPixmap(":/elem/like.png"))
                else:
                    self.onemypost_like.setPixmap(QtGui.QPixmap(":/elem/unlike.png"))
                    mymedia_id = mypostdata8['pk']
                if (mypostdata8['caption_is_edited']) == True:
                    self.onemypost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\">Edited</span></p></body></html>"))
                else:
                    self.onemypost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\"></span></p></body></html>"))
                try:
                    try:
                        self.onemypost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + mypostdata8['facepile_top_likers'][0]['username'] + " and " +mypostdata8['facepile_top_likers'][1]['username'] +"</span></p></body></html>"))
                    except Exception:
                        self.onemypost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + mypostdata8['top_likers'][0]+"</span></p></body></html>"))
                except Exception:
                    self.onemypost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Not liked by anyone you follow</span></p></body></html>"))
                timestamp = time.ctime(mypostdata8['taken_at'])
                timestamp24hr = datetime.strptime(timestamp[11:16], "%H:%M")
                self.onemypost_date.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" color:#919191;\">"+(timestamp24hr.strftime("%#I:%M%p")+ " "+timestamp[:3]+", "+timestamp[8:10]+" "+timestamp[4:7]+" "+timestamp[20:24])+"</span></p></body></html>"))


            except Exception:
                global searchsscr_select
                MainWindow.central_widget.setCurrentWidget(self.mypostscreen)
                pass

        def mypostfromdata9():
            try:
                global mymedia_id
                global mypostdata9
                global myhas_liked
                global mylike_count
                global mycorousell_count
                global username
                global mypostdata
                global myhas_saved
                global total_mycorousell
                global mypostdataurl
                setscreen_onemypost()
                mypostdata = mypostdata9
                mycorousell_count = 1
                global mypost_req
                self.onemypost_username.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">"+ str(username)+"</span></p></body></html>"))
                if mypostdata9['media_type'] == 8:
                    total_mycorousell = len(mypostdata9['carousel_media'])
                    mypost_req = requests.get(mypostdata9['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                    mypostcache1 = open("onemypost.png", "wb")
                    mypostcache1.write(mypost_req.content)
                    mypostcache1.close()
                    reshape("onemypost.png")
                    self.onemypost_image.setPixmap(QtGui.QPixmap("onemypost.png"))
                    if mypostdata9['carousel_media'][0]['media_type'] ==2:
                        onemypost_video_with_mycorousell()
                    else:
                        onemypost_mycorousell()
                    self.onemypost_mypostcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Post 1/" + str(total_mycorousell)+ "</span></p></body></html>"))
                elif mypostdata9['media_type'] == 2:
                    mypostdataurl = mypostdata['video_versions'][2]['url']
                    onemypost_video()
                    mypost_req = requests.get((mypostdata9['image_versions2']['candidates'][0]['url']))
                    mypostcache1 = open("onemypost.png", "wb")
                    mypostcache1.write(mypost_req.content)
                    mypostcache1.close()
                    reshape("onemypost.png")
                    self.onemypost_image.setPixmap(QtGui.QPixmap("onemypost.png"))
                    
                    
                else:
                    onemypost_not_mycorousell()
                    mypost_req = requests.get((mypostdata9['image_versions2']['candidates'][0]['url']))
                    mypostcache1 = open("onemypost.png", "wb")
                    mypostcache1.write(mypost_req.content)
                    mypostcache1.close()
                    reshape("onemypost.png")
                    self.onemypost_image.setPixmap(QtGui.QPixmap("onemypost.png"))
                    mylike_count = mypostdata9['like_count']
                try:
                    self.onemypost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#f1f1f1;\">"+mypostdata9['caption']['text']+"</span></p></body></html>"))
                except Exception:
                    self.onemypost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">This mypost has no Caption.</span></p></body></html>"))
                self.onemypost_likecount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Likes: "+str(numconv(mylike_count))+"</span></p></body></html>"))
                self.onemypost_commentcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Comments: "+str(numconv(mypostdata9['comment_count']))+"</span></p></body></html>"))
                myhas_liked = (mypostdata9['has_liked'])
                try:
                    myhas_saved = mypostdata9['has_viewer_saved']
                    if myhas_saved == True:
                        self.onemypost_save.setPixmap(QtGui.QPixmap(":/elem/save.png"))
                    else:
                        self.onemypost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
                except Exception:
                    self.onemypost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
                    myhas_saved = False
                if myhas_liked == True:
                    self.onemypost_like.setPixmap(QtGui.QPixmap(":/elem/like.png"))
                else:
                    self.onemypost_like.setPixmap(QtGui.QPixmap(":/elem/unlike.png"))
                    mymedia_id = mypostdata9['pk']
                if (mypostdata9['caption_is_edited']) == True:
                    self.onemypost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\">Edited</span></p></body></html>"))
                else:
                    self.onemypost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\"></span></p></body></html>"))
                try:
                    try:
                        self.onemypost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + mypostdata9['facepile_top_likers'][0]['username'] + " and " +mypostdata9['facepile_top_likers'][1]['username'] +"</span></p></body></html>"))
                    except Exception:
                        self.onemypost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + mypostdata9['top_likers'][0]+"</span></p></body></html>"))
                except Exception:
                    self.onemypost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Not liked by anyone you follow</span></p></body></html>"))
                timestamp = time.ctime(mypostdata10['taken_at'])
                timestamp24hr = datetime.strptime(timestamp[11:16], "%H:%M")
                self.onemypost_date.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" color:#919191;\">"+(timestamp24hr.strftime("%#I:%M%p")+ " "+timestamp[:3]+", "+timestamp[8:10]+" "+timestamp[4:7]+" "+timestamp[20:24])+"</span></p></body></html>"))


            except Exception:
                global searchsscr_select
                MainWindow.central_widget.setCurrentWidget(self.mypostscreen)
                pass

        def mypostfromdata10():
            try:
                global mymedia_id
                global mypostdata10
                global myhas_liked
                global mylike_count
                global mycorousell_count
                global username
                global mypostdata
                global myhas_saved
                global total_mycorousell
                global mypostdataurl
                setscreen_onemypost()
                mypostdata = mypostdata10
                mycorousell_count = 1
                global mypost_req
                self.onemypost_username.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">"+ str(username)+"</span></p></body></html>"))
                if mypostdata10['media_type'] == 8:
                    total_mycorousell = len(mypostdata10['carousel_media'])
                    mypost_req = requests.get(mypostdata10['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                    mypostcache1 = open("onemypost.png", "wb")
                    mypostcache1.write(mypost_req.content)
                    mypostcache1.close()
                    reshape("onemypost.png")
                    self.onemypost_image.setPixmap(QtGui.QPixmap("onemypost.png"))
                    if mypostdata10['carousel_media'][0]['media_type'] ==2:
                        onemypost_video_with_mycorousell()
                    else:
                        onemypost_mycorousell()
                    self.onemypost_mypostcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Post 1/" + str(total_mycorousell)+ "</span></p></body></html>"))
                elif mypostdata10['media_type'] == 2:
                    mypostdataurl = mypostdata['video_versions'][2]['url']
                    onemypost_video()
                    mypost_req = requests.get((mypostdata10['image_versions2']['candidates'][0]['url']))
                    mypostcache1 = open("onemypost.png", "wb")
                    mypostcache1.write(mypost_req.content)
                    mypostcache1.close()
                    reshape("onemypost.png")
                    self.onemypost_image.setPixmap(QtGui.QPixmap("onemypost.png"))
                    
                    
                else:
                    onemypost_not_mycorousell()
                    mypost_req = requests.get((mypostdata10['image_versions2']['candidates'][0]['url']))
                    mypostcache1 = open("onemypost.png", "wb")
                    mypostcache1.write(mypost_req.content)
                    mypostcache1.close()
                    reshape("onemypost.png")
                    self.onemypost_image.setPixmap(QtGui.QPixmap("onemypost.png"))
                    mylike_count = mypostdata10['like_count']
                try:
                    self.onemypost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#f1f1f1;\">"+mypostdata10['caption']['text']+"</span></p></body></html>"))
                except Exception:
                    self.onemypost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">This mypost has no Caption.</span></p></body></html>"))
                self.onemypost_likecount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Likes: "+str(numconv(mylike_count))+"</span></p></body></html>"))
                self.onemypost_commentcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Comments: "+str(numconv(mypostdata10['comment_count']))+"</span></p></body></html>"))
                myhas_liked = (mypostdata10['has_liked'])
                try:
                    myhas_saved = mypostdata10['has_viewer_saved']
                    if myhas_saved == True:
                        self.onemypost_save.setPixmap(QtGui.QPixmap(":/elem/save.png"))
                    else:
                        self.onemypost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
                except Exception:
                    self.onemypost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
                    myhas_saved = False
                if myhas_liked == True:
                    self.onemypost_like.setPixmap(QtGui.QPixmap(":/elem/like.png"))
                else:
                    self.onemypost_like.setPixmap(QtGui.QPixmap(":/elem/unlike.png"))
                    mymedia_id = mypostdata10['pk']
                if (mypostdata10['caption_is_edited']) == True:
                    self.onemypost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\">Edited</span></p></body></html>"))
                else:
                    self.onemypost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\"></span></p></body></html>"))
                try:
                    try:
                        self.onemypost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + mypostdata10['facepile_top_likers'][0]['username'] + " and " +mypostdata10['facepile_top_likers'][1]['username'] +"</span></p></body></html>"))
                    except Exception:
                        self.onemypost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + mypostdata10['top_likers'][0]+"</span></p></body></html>"))
                except Exception:
                    self.onemypost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Not liked by anyone you follow</span></p></body></html>"))
                timestamp = time.ctime(mypostdata10['taken_at'])
                timestamp24hr = datetime.strptime(timestamp[11:16], "%H:%M")
                self.onemypost_date.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" color:#919191;\">"+(timestamp24hr.strftime("%#I:%M%p")+ " "+timestamp[:3]+", "+timestamp[8:10]+" "+timestamp[4:7]+" "+timestamp[20:24])+"</span></p></body></html>"))


            except Exception:
                global searchsscr_select
                MainWindow.central_widget.setCurrentWidget(self.mypostscreen)
                pass



        def feed_load_image_thread():
            try:
                reshape("feedpost1.png")
                self.card_img1.setPixmap(QtGui.QPixmap("feedpost1.png"))
            except Exception:
                pass
            try:
                reshape("feedpost3.png")
                self.card_img3.setPixmap(QtGui.QPixmap("feedpost3.png"))
            except Exception:
                pass

            try:
                reshape("feedpost5.png")
                self.card_img5.setPixmap(QtGui.QPixmap("feedpost5.png"))
            except Exception:
                pass

            try:
                reshape("feedpost7.png")
                self.card_img7.setPixmap(QtGui.QPixmap("feedpost7.png"))
            except Exception:
                pass

            try:
                reshape("feedpost9.png")
                self.card_img9.setPixmap(QtGui.QPixmap("feedpost9.png"))
            except Exception:
                pass



        def feed_load_image_thread2():
            try:
                reshape("feedpost2.png")
                self.card_img2.setPixmap(QtGui.QPixmap("feedpost2.png"))
            except Exception:
                pass

            try:
                reshape("feedpost4.png")
                self.card_img4.setPixmap(QtGui.QPixmap("feedpost4.png"))
            except Exception:
                pass

            try:
                reshape("feedpost6.png")
                self.card_img6.setPixmap(QtGui.QPixmap("feedpost6.png"))
            except Exception:
                pass

            try:
                reshape("feedpost8.png")
                self.card_img8.setPixmap(QtGui.QPixmap("feedpost8.png"))
            except Exception:
                pass

            try:
                reshape("feedpost10.png")
                self.card_img10.setPixmap(QtGui.QPixmap("feedpost10.png"))
            except Exception:
                pass



           
        def loadfeed_thread():
            #self.loadingscreen_progress.setValue(0)
            global user
            global feed1
            global feed2
            global feed3
            global feed4
            global feed5
            global feed6
            global feed7
            global feed8
            global feed9
            global feed10
            global feed_seen
            #global feed_media_id 
            #MainWindow.central_widget.setCurrentWidget(self.loadingscreen)
            MainWindow.setGraphicsEffect(self.blur_effect)
            self.blur_effect.setBlurRadius(5)
            MainWindow.setEnabled(False)
            load_story()
            feed_timeline=[]
            feed_timeline_old =(user.feed_timeline(seen_posts=feed_seen))['feed_items']
            x=0
            while x != (len(feed_timeline_old)):
               try:
                  feeditem = feed_timeline_old[x]['media_or_ad']['product_type']
                  if feeditem != "ad":
                     feed_timeline.append(feed_timeline_old[x])
               except Exception:
                   pass
                  #feed_timeline.append(feed_timeline_old[x])
                  #print(feed_timeline_old[x])
               x=x+1
            feed_seen = "0123"
            try:
                self.card_img1.setHidden(False)
                self.card_footer1.setHidden(False)
                self.card_header1.setHidden(False)
                try:
                    if feed_timeline[0]['media_or_ad']:
                        feed1 = feed_timeline[0]['media_or_ad']
                        feedcard_username2 = "@" + (feed_timeline[0]['media_or_ad']['user']['username'])
                        self.card_header1.setText(_translate("MainWindow", feedcard_username2))
                        self.card_footer1.setText(_translate("MainWindow", "View Post"))
                        self.card_img1.setStyleSheet("border:0px solid rgb(29, 29, 29);background: rgb(29, 29, 29);")
                        if feed_timeline[0]['media_or_ad']['media_type'] == 8:
                            feed_req = requests.get((feed_timeline[0]['media_or_ad']['carousel_media'][0]['image_versions2']['candidates'][0]['url']))
                            feedcache = open("feedpost1.png", "wb")
                            feedcache.write(feed_req.content)
                            feedcache.close()
                            
                        else:
                            feed_req = requests.get((feed_timeline[0]['media_or_ad']['image_versions2']['candidates'][0]['url']))
                            feedcache = open("feedpost1.png", "wb")
                            feedcache.write(feed_req.content)
                            feedcache.close()

                        feed_media_id= feed_timeline[0]['media_or_ad']['pk']
                        feed_seen = feed_seen +", " +str(feed_media_id)

                except Exception:
                    feedcard_username2 = "@" + (feed_timeline[0]['suggested_users']['suggestion_cards'][0]['user_card']['user']['username'])
                    feed_req = requests.get((feed_timeline[0]['suggested_users']['suggestion_cards'][0]['user_card']['user']['profile_pic_url']))
                    self.card_footer1.setText(_translate("MainWindow", feedcard_username2))
                    self.card_header1.setText(_translate("MainWindow", "Suggested User"))
                    feedcache = open("feedpost1.png", "wb")
                    feedcache.write(feed_req.content)
                    feedcache.close()
                    circularimg("feedpost1.png")
                    self.card_img1.setPixmap(QtGui.QPixmap("feedpost1.png"))
                    self.card_img1.setStyleSheet("border:30px solid rgb(29, 29, 29);background: rgb(29, 29, 29);")
            except Exception:
                self.card_img1.setHidden(True)
                self.card_footer1.setHidden(True)
                self.card_header1.setHidden(True)
            #self.loadingscreen_progress.setValue(1)
            try:
                self.card_img2.setHidden(False)
                self.card_footer2.setHidden(False)
                self.card_header2.setHidden(False)
                try:
                    if feed_timeline[1]['media_or_ad']:
                        feed2 = feed_timeline[1]['media_or_ad']
                        feedcard_username2 = "@" + (feed_timeline[1]['media_or_ad']['user']['username'])
                        self.card_header2.setText(_translate("MainWindow", feedcard_username2))
                        self.card_footer2.setText(_translate("MainWindow", "View Post"))
                        self.card_img2.setStyleSheet("border:0px solid rgb(29, 29, 29);background: rgb(29, 29, 29);")
                        if feed_timeline[1]['media_or_ad']['media_type'] == 8:
                            feed_req = requests.get((feed_timeline[1]['media_or_ad']['carousel_media'][0]['image_versions2']['candidates'][0]['url']))
                            feedcache = open("feedpost2.png", "wb")
                            feedcache.write(feed_req.content)
                            feedcache.close()
                            
                        else:
                            feed_req = requests.get((feed_timeline[1]['media_or_ad']['image_versions2']['candidates'][0]['url']))
                            feedcache = open("feedpost2.png", "wb")
                            feedcache.write(feed_req.content)
                            feedcache.close()

                        feed_media_id= feed_timeline[1]['media_or_ad']['pk']
                        feed_seen = feed_seen +", " +str(feed_media_id)

                except Exception:
                    feedcard_username2 = "@" + (feed_timeline[1]['suggested_users']['suggestion_cards'][0]['user_card']['user']['username'])
                    feed_req = requests.get((feed_timeline[1]['suggested_users']['suggestion_cards'][0]['user_card']['user']['profile_pic_url']))
                    self.card_footer2.setText(_translate("MainWindow", feedcard_username2))
                    self.card_img2.setText(_translate("MainWindow", "Suggested User"))
                    feedcache = open("feedpost2.png", "wb")
                    feedcache.write(feed_req.content)
                    feedcache.close()
                    circularimg("feedpost2.png")
                    self.card_img2.setPixmap(QtGui.QPixmap("feedpost2.png"))
                    self.card_img2.setStyleSheet("border:30px solid rgb(29, 29, 29);background: rgb(29, 29, 29);")
            except Exception:
                self.card_img2.setHidden(True)
                self.card_footer2.setHidden(True)
                self.card_header2.setHidden(True)
            #self.loadingscreen_progress.setValue(4)

            try:
                self.card_img3.setHidden(False)
                self.card_footer3.setHidden(False)
                self.card_header3.setHidden(False)
                try:
                    if feed_timeline[2]['media_or_ad']:
                        feed3 = feed_timeline[2]['media_or_ad']
                        feedcard_username2 = "@" + (feed_timeline[2]['media_or_ad']['user']['username'])
                        self.card_header3.setText(_translate("MainWindow", feedcard_username2))
                        self.card_footer3.setText(_translate("MainWindow", "View Post"))
                        self.card_img3.setStyleSheet("border:0px solid rgb(29, 29, 29);background: rgb(29, 29, 29);")
                        if feed_timeline[2]['media_or_ad']['media_type'] == 8:
                            feed_req = requests.get((feed_timeline[2]['media_or_ad']['carousel_media'][0]['image_versions2']['candidates'][0]['url']))
                            feedcache = open("feedpost3.png", "wb")
                            feedcache.write(feed_req.content)
                            
                        else:
                            feed_req = requests.get((feed_timeline[2]['media_or_ad']['image_versions2']['candidates'][0]['url']))
                            feedcache = open("feedpost3.png", "wb")
                            feedcache.write(feed_req.content)
                            feedcache.close()

                        feed_media_id= feed_timeline[2]['media_or_ad']['pk']
                        feed_seen = feed_seen +", " +str(feed_media_id)

                except Exception:
                    feedcard_username2 = "@" + (feed_timeline[2]['suggested_users']['suggestion_cards'][0]['user_card']['user']['username'])
                    feed_req = requests.get((feed_timeline[2]['suggested_users']['suggestion_cards'][0]['user_card']['user']['profile_pic_url']))
                    self.card_footer3.setText(_translate("MainWindow", feedcard_username2))
                    self.card_header3.setText(_translate("MainWindow", "Suggested User"))
                    feedcache = open("feedpost3.png", "wb")
                    feedcache.write(feed_req.content)
                    feedcache.close()
                    circularimg("feedpost3.png")
                    self.card_img3.setPixmap(QtGui.QPixmap("feedpost3.png"))
                    self.card_img3.setStyleSheet("border:30px solid rgb(29, 29, 29);background: rgb(29, 29, 29);")
            except Exception:
                self.card_img3.setHidden(True)
                self.card_footer3.setHidden(True)
                self.card_header3.setHidden(True)

            try:
                self.card_img4.setHidden(False)
                self.card_footer4.setHidden(False)
                self.card_header4.setHidden(False)
                try:
                    if feed_timeline[3]['media_or_ad']:
                        feed4 = feed_timeline[3]['media_or_ad']
                        feedcard_username2 = "@" + (feed_timeline[3]['media_or_ad']['user']['username'])
                        self.card_header4.setText(_translate("MainWindow", feedcard_username2))
                        self.card_footer4.setText(_translate("MainWindow", "View Post"))
                        self.card_img4.setStyleSheet("border:0px solid rgb(29, 29, 29);background: rgb(29, 29, 29);")
                        if feed_timeline[3]['media_or_ad']['media_type'] == 8:
                            feed_req = requests.get((feed_timeline[3]['media_or_ad']['carousel_media'][0]['image_versions2']['candidates'][0]['url']))
                            feedcache = open("feedpost4.png", "wb")
                            feedcache.write(feed_req.content)
                            feedcache.close()

                            
                        else:
                            feed_req = requests.get((feed_timeline[3]['media_or_ad']['image_versions2']['candidates'][0]['url']))
                            feedcache = open("feedpost4.png", "wb")
                            feedcache.write(feed_req.content)
                            feedcache.close()


                        feed_media_id= feed_timeline[3]['media_or_ad']['pk']
                        feed_seen = feed_seen +", " +str(feed_media_id)

                except Exception:
                    feedcard_username2 = "@" + (feed_timeline[3]['suggested_users']['suggestion_cards'][0]['user_card']['user']['username'])
                    feed_req = requests.get((feed_timeline[3]['suggested_users']['suggestion_cards'][0]['user_card']['user']['profile_pic_url']))
                    self.card_footer4.setText(_translate("MainWindow", feedcard_username2))
                    self.card_header4.setText(_translate("MainWindow", "Suggested User"))
                    feedcache = open("feedpost4.png", "wb")
                    feedcache.write(feed_req.content)
                    feedcache.close()
                    circularimg("feedpost4.png")
                    self.card_img4.setPixmap(QtGui.QPixmap("feedpost4.png"))
                    self.card_img4.setStyleSheet("border:30px solid rgb(29, 29, 29);background: rgb(29, 29, 29);")
            except Exception:
                self.card_img4.setHidden(True)
                self.card_footer4.setHidden(True)
                self.card_header4.setHidden(True)
            try:
                self.card_img5.setHidden(False)
                self.card_footer5.setHidden(False)
                self.card_header5.setHidden(False)
                try:
                    if feed_timeline[4]['media_or_ad']:
                        feed5 = feed_timeline[4]['media_or_ad']
                        feedcard_username2 = "@" + (feed_timeline[4]['media_or_ad']['user']['username'])
                        self.card_header5.setText(_translate("MainWindow", feedcard_username2))
                        self.card_footer5.setText(_translate("MainWindow", "View Post"))
                        self.card_img5.setStyleSheet("border:0px solid rgb(29, 29, 29);background: rgb(29, 29, 29);")
                        if feed_timeline[4]['media_or_ad']['media_type'] == 8:
                            feed_req = requests.get((feed_timeline[4]['media_or_ad']['carousel_media'][0]['image_versions2']['candidates'][0]['url']))
                            feedcache = open("feedpost5.png", "wb")
                            feedcache.write(feed_req.content)
                            feedcache.close()

                            
                        else:
                            feed_req = requests.get((feed_timeline[4]['media_or_ad']['image_versions2']['candidates'][0]['url']))
                            feedcache = open("feedpost5.png", "wb")
                            feedcache.write(feed_req.content)
                            feedcache.close()


                        feed_media_id= feed_timeline[4]['media_or_ad']['pk']
                        feed_seen = feed_seen +", " +str(feed_media_id)

                except Exception:
                    feedcard_username2 = "@" + (feed_timeline[4]['suggested_users']['suggestion_cards'][0]['user_card']['user']['username'])
                    feed_req = requests.get((feed_timeline[4]['suggested_users']['suggestion_cards'][0]['user_card']['user']['profile_pic_url']))
                    self.card_footer5.setText(_translate("MainWindow", feedcard_username2))
                    self.card_header5.setText(_translate("MainWindow", "Suggested User"))
                    feedcache = open("feedpost5.png", "wb")
                    feedcache.write(feed_req.content)
                    feedcache.close()
                    circularimg("feedpost5.png")
                    self.card_img5.setPixmap(QtGui.QPixmap("feedpost5.png"))
                    self.card_img5.setStyleSheet("border:30px solid rgb(29, 29, 29);background: rgb(29, 29, 29);")
            except Exception:
                self.card_img5.setHidden(True)
                self.card_footer5.setHidden(True)
                self.card_header5.setHidden(True)
            try:
                self.card_img6.setHidden(False)
                self.card_footer6.setHidden(False)
                self.card_header6.setHidden(False)
                try:
                    if feed_timeline[5]['media_or_ad']:
                        feed6 = feed_timeline[5]['media_or_ad']
                        feedcard_username2 = "@" + (feed_timeline[5]['media_or_ad']['user']['username'])
                        self.card_header6.setText(_translate("MainWindow", feedcard_username2))
                        self.card_footer6.setText(_translate("MainWindow", "View Post"))
                        self.card_img6.setStyleSheet("border:0px solid rgb(29, 29, 29);background: rgb(29, 29, 29);")
                        if feed_timeline[5]['media_or_ad']['media_type'] == 8:
                            feed_req = requests.get((feed_timeline[5]['media_or_ad']['carousel_media'][0]['image_versions2']['candidates'][0]['url']))
                            feedcache = open("feedpost6.png", "wb")
                            feedcache.write(feed_req.content)
                            feedcache.close()

                            
                        else:
                            feed_req = requests.get((feed_timeline[5]['media_or_ad']['image_versions2']['candidates'][0]['url']))
                            feedcache = open("feedpost6.png", "wb")
                            feedcache.write(feed_req.content)
                            feedcache.close()


                        feed_media_id= feed_timeline[5]['media_or_ad']['pk']
                        feed_seen = feed_seen +", " +str(feed_media_id)

                except Exception:
                    feedcard_username2 = "@" + (feed_timeline[5]['suggested_users']['suggestion_cards'][0]['user_card']['user']['username'])
                    feed_req = requests.get((feed_timeline[5]['suggested_users']['suggestion_cards'][0]['user_card']['user']['profile_pic_url']))
                    self.card_footer6.setText(_translate("MainWindow", feedcard_username2))
                    self.card_header6.setText(_translate("MainWindow", "Suggested User"))
                    feedcache = open("feedpost6.png", "wb")
                    feedcache.write(feed_req.content)
                    feedcache.close()
                    circularimg("feedpost6.png")
                    self.card_img6.setPixmap(QtGui.QPixmap("feedpost6.png"))
                    self.card_img6.setStyleSheet("border:30px solid rgb(29, 29, 29);background: rgb(29, 29, 29);")
            except Exception:
                self.card_img6.setHidden(True)
                self.card_footer6.setHidden(True)
                self.card_header6.setHidden(True)
            #self.loadingscreen_progress.setValue(9)
            try:
                self.card_img7.setHidden(False)
                self.card_footer7.setHidden(False)
                self.card_header7.setHidden(False)
                try:
                    if feed_timeline[6]['media_or_ad']:
                        feed7 = feed_timeline[6]['media_or_ad']
                        feedcard_username2 = "@" + (feed_timeline[6]['media_or_ad']['user']['username'])
                        self.card_header7.setText(_translate("MainWindow", feedcard_username2))
                        self.card_footer7.setText(_translate("MainWindow", "View Post"))
                        self.card_img7.setStyleSheet("border:0px solid rgb(29, 29, 29);background: rgb(29, 29, 29);")
                        if feed_timeline[6]['media_or_ad']['media_type'] == 8:
                            feed_req = requests.get((feed_timeline[6]['media_or_ad']['carousel_media'][0]['image_versions2']['candidates'][0]['url']))
                            feedcache = open("feedpost7.png", "wb")
                            feedcache.write(feed_req.content)
                            feedcache.close()

                            
                        else:
                            feed_req = requests.get((feed_timeline[6]['media_or_ad']['image_versions2']['candidates'][0]['url']))
                            feedcache = open("feedpost7.png", "wb")
                            feedcache.write(feed_req.content)
                            feedcache.close()


                        feed_media_id= feed_timeline[6]['media_or_ad']['pk']
                        feed_seen = feed_seen +", " +str(feed_media_id)

                except Exception:
                    feedcard_username2 = "@" + (feed_timeline[6]['suggested_users']['suggestion_cards'][0]['user_card']['user']['username'])
                    feed_req = requests.get((feed_timeline[6]['suggested_users']['suggestion_cards'][0]['user_card']['user']['profile_pic_url']))
                    self.card_footer7.setText(_translate("MainWindow", feedcard_username2))
                    self.card_header7.setText(_translate("MainWindow", "Suggested User"))
                    feedcache = open("feedpost7.png", "wb")
                    feedcache.write(feed_req.content)
                    feedcache.close()
                    circularimg("feedpost7.png")
                    self.card_img7.setPixmap(QtGui.QPixmap("feedpost7.png"))
                    self.card_img7.setStyleSheet("border:30px solid rgb(29, 29, 29);background: rgb(29, 29, 29);")
            except Exception:
                self.card_img7.setHidden(True)
                self.card_footer7.setHidden(True)
                self.card_header7.setHidden(True)
            try:
                self.card_img8.setHidden(False)
                self.card_footer8.setHidden(False)
                self.card_header8.setHidden(False)
                try:
                    if feed_timeline[7]['media_or_ad']:
                        feed8 = feed_timeline[7]['media_or_ad']
                        feedcard_username2 = "@" + (feed_timeline[7]['media_or_ad']['user']['username'])
                        self.card_header8.setText(_translate("MainWindow", feedcard_username2))
                        self.card_footer8.setText(_translate("MainWindow", "View Post"))
                        self.card_img8.setStyleSheet("border:0px solid rgb(29, 29, 29);background: rgb(29, 29, 29);")
                        if feed_timeline[7]['media_or_ad']['media_type'] == 8:
                            feed_req = requests.get((feed_timeline[7]['media_or_ad']['carousel_media'][0]['image_versions2']['candidates'][0]['url']))
                            feedcache = open("feedpost8.png", "wb")
                            feedcache.write(feed_req.content)
                            feedcache.close()

                            
                        else:
                            feed_req = requests.get((feed_timeline[7]['media_or_ad']['image_versions2']['candidates'][0]['url']))
                            feedcache = open("feedpost8.png", "wb")
                            feedcache.write(feed_req.content)
                            feedcache.close()

                        feed_media_id= feed_timeline[7]['media_or_ad']['pk']
                        feed_seen = feed_seen +", " +str(feed_media_id)
                except Exception:
                    feedcard_username2 = "@" + (feed_timeline[7]['suggested_users']['suggestion_cards'][0]['user_card']['user']['username'])
                    feed_req = requests.get((feed_timeline[7]['suggested_users']['suggestion_cards'][0]['user_card']['user']['profile_pic_url']))
                    self.card_footer8.setText(_translate("MainWindow", feedcard_username2))
                    self.card_header8.setText(_translate("MainWindow", "Suggested User"))
                    feedcache = open("feedpost8.png", "wb")
                    feedcache.write(feed_req.content)
                    feedcache.close()
                    circularimg("feedpost8.png")
                    self.card_img8.setPixmap(QtGui.QPixmap("feedpost8.png"))
                    self.card_img8.setStyleSheet("border:30px solid rgb(29, 29, 29);background: rgb(29, 29, 29);")
            except Exception:
                self.card_img8.setHidden(True)
                self.card_footer8.setHidden(True)
                self.card_header8.setHidden(True)
            try:
                self.card_img9.setHidden(False)
                self.card_footer9.setHidden(False)
                self.card_header9.setHidden(False)
                try:
                    if feed_timeline[8]['media_or_ad']:
                        feed9 = feed_timeline[8]['media_or_ad']
                        feedcard_username2 = "@" + (feed_timeline[8]['media_or_ad']['user']['username'])
                        self.card_header9.setText(_translate("MainWindow", feedcard_username2))
                        self.card_footer9.setText(_translate("MainWindow", "View Post"))
                        self.card_img9.setStyleSheet("border:0px solid rgb(29, 29, 29);background: rgb(29, 29, 29);")
                        if feed_timeline[8]['media_or_ad']['media_type'] == 8:
                            feed_req = requests.get((feed_timeline[8]['media_or_ad']['carousel_media'][0]['image_versions2']['candidates'][0]['url']))
                            feedcache = open("feedpost9.png", "wb")
                            feedcache.write(feed_req.content)
                            feedcache.close()

                        else:
                            feed_req = requests.get((feed_timeline[8]['media_or_ad']['image_versions2']['candidates'][0]['url']))
                            feedcache = open("feedpost9.png", "wb")
                            feedcache.write(feed_req.content)
                            feedcache.close()


                        feed_media_id= feed_timeline[8]['media_or_ad']['pk']
                        feed_seen = feed_seen +", " +str(feed_media_id)

                except Exception:
                    feedcard_username2 = "@" + (feed_timeline[8]['suggested_users']['suggestion_cards'][0]['user_card']['user']['username'])
                    feed_req = requests.get((feed_timeline[8]['suggested_users']['suggestion_cards'][0]['user_card']['user']['profile_pic_url']))
                    self.card_footer9.setText(_translate("MainWindow", feedcard_username2))
                    self.card_header9.setText(_translate("MainWindow", "Suggested User"))
                    feedcache = open("feedpost9.png", "wb")
                    feedcache.write(feed_req.content)
                    feedcache.close()
                    circularimg("feedpost9.png")
                    self.card_img9.setPixmap(QtGui.QPixmap("feedpost9.png"))
                    self.card_img9.setStyleSheet("border:30px solid rgb(29, 29, 29);background: rgb(29, 29, 29);")

            except Exception:
                self.card_img9.setHidden(True)
                self.card_footer9.setHidden(True)
                self.card_header9.setHidden(True)
            try:
                self.card_img10.setHidden(False)
                self.card_footer10.setHidden(False)
                self.card_header10.setHidden(False)
                try:
                    if feed_timeline[9]['media_or_ad']:
                        feed10 = feed_timeline[9]['media_or_ad']
                        feedcard_username2 = "@" + (feed_timeline[9]['media_or_ad']['user']['username'])
                        self.card_header10.setText(_translate("MainWindow", feedcard_username2))
                        self.card_footer10.setText(_translate("MainWindow", "View Post"))
                        self.card_img10.setStyleSheet("border:0px solid rgb(29, 29, 29);background: rgb(29, 29, 29);")
                        if feed_timeline[9]['media_or_ad']['media_type'] == 8:
                            feed_req = requests.get((feed_timeline[9]['media_or_ad']['carousel_media'][0]['image_versions2']['candidates'][0]['url']))
                            feedcache = open("feedpost10.png", "wb")
                            feedcache.write(feed_req.content)
                            feedcache.close()

                            
                        else:
                            feed_req = requests.get((feed_timeline[9]['media_or_ad']['image_versions2']['candidates'][0]['url']))
                            feedcache = open("feedpost10.png", "wb")
                            feedcache.write(feed_req.content)
                            feedcache.close()


                        feed_media_id= feed_timeline[9]['media_or_ad']['pk']
                        feed_seen = feed_seen +", " +str(feed_media_id)

                except Exception:
                    feedcard_username2 = "@" + (feed_timeline[9]['suggested_users']['suggestion_cards'][0]['user_card']['user']['username'])
                    feed_req = requests.get((feed_timeline[9]['suggested_users']['suggestion_cards'][0]['user_card']['user']['profile_pic_url']))
                    self.card_footer10.setText(_translate("MainWindow", feedcard_username2))
                    self.card_header10.setText(_translate("MainWindow", "Suggested User"))
                    feedcache = open("feedpost10.png", "wb")
                    feedcache.write(feed_req.content)
                    feedcache.close()
                    circularimg("feedpost10.png")
                    self.card_img10.setPixmap(QtGui.QPixmap("feedpost10.png"))
                    self.card_img10.setStyleSheet("border:30px solid rgb(29, 29, 29);background: rgb(29, 29, 29);")
            except Exception:
                self.card_img10.setHidden(True)
                self.card_footer10.setHidden(True)
                self.card_header10.setHidden(True)
            #self.loadingscreen_progress.setValue(10)
            feed_load_image()
            feed_load_image2()
            self.blur_effect.setBlurRadius(0)
            MainWindow.setEnabled(True)
            #MainWindow.central_widget.setCurrentWidget(self.feed_screen)
        def feed_load_image():
            thread10 = threading.Thread(target = feed_load_image_thread)
            thread10.start()
        def feed_load_image2():
            thread11 = threading.Thread(target = feed_load_image_thread2)
            thread11.start()            
        def loadfeed():
            thread7 = threading.Thread(target = loadfeed_thread)
            thread7.start()

        def card_headerbtn1():
           global usertobesearched
           searchfromsearchquery = self.card_header1.text()
           searchuser_list(searchfromsearchquery)
           self.search_box.setText(searchfromsearchquery)
           self.search_search_box.setText(searchfromsearchquery)
           usertobesearched = self.card_header1.text()
           search_user()
           MainWindow.central_widget.setCurrentWidget(self.homescreen)
           
        def card_headerbtn2():
           global usertobesearched
           searchfromsearchquery = self.card_header2.text()
           searchuser_list(searchfromsearchquery)
           self.search_box.setText(searchfromsearchquery)
           self.search_search_box.setText(searchfromsearchquery)
           usertobesearched = self.card_header2.text()
           search_user()
           MainWindow.central_widget.setCurrentWidget(self.homescreen)
        def card_headerbtn3():
           global usertobesearched
           searchfromsearchquery = self.card_header3.text()
           searchuser_list(searchfromsearchquery)
           self.search_box.setText(searchfromsearchquery)
           self.search_search_box.setText(searchfromsearchquery)
           usertobesearched = self.card_header3.text()
           search_user()
           MainWindow.central_widget.setCurrentWidget(self.homescreen)
        def card_headerbtn4():
           global usertobesearched
           searchfromsearchquery = self.card_header4.text()
           searchuser_list(searchfromsearchquery)
           self.search_box.setText(searchfromsearchquery)
           self.search_search_box.setText(searchfromsearchquery)
           usertobesearched = self.card_header4.text()
           search_user()
           MainWindow.central_widget.setCurrentWidget(self.homescreen)
        def card_headerbtn5():
           global usertobesearched
           searchfromsearchquery = self.card_header5.text()
           searchuser_list(searchfromsearchquery)
           self.search_box.setText(searchfromsearchquery)
           self.search_search_box.setText(searchfromsearchquery)
           usertobesearched = self.card_header5.text()
           search_user()
           MainWindow.central_widget.setCurrentWidget(self.homescreen)
        def card_headerbtn6():
           global usertobesearched
           searchfromsearchquery = self.card_header6.text()
           searchuser_list(searchfromsearchquery)
           self.search_box.setText(searchfromsearchquery)
           self.search_search_box.setText(searchfromsearchquery)
           usertobesearched = self.card_header6.text()
           search_user()
           MainWindow.central_widget.setCurrentWidget(self.homescreen)
           
        def card_headerbtn7():
           global usertobesearched
           searchfromsearchquery = self.card_header7.text()
           searchuser_list(searchfromsearchquery)
           self.search_box.setText(searchfromsearchquery)
           self.search_search_box.setText(searchfromsearchquery)
           usertobesearched = self.card_header7.text()
           search_user()
           MainWindow.central_widget.setCurrentWidget(self.homescreen)

        def card_headerbtn8():
           global usertobesearched
           searchfromsearchquery = self.card_header8.text()
           searchuser_list(searchfromsearchquery)
           self.search_box.setText(searchfromsearchquery)
           self.search_search_box.setText(searchfromsearchquery)
           usertobesearched = self.card_header8.text()
           search_user()
           MainWindow.central_widget.setCurrentWidget(self.homescreen)


        def card_headerbtn9():
           global usertobesearched
           searchfromsearchquery = self.card_header9.text()
           searchuser_list(searchfromsearchquery)
           self.search_box.setText(searchfromsearchquery)
           self.search_search_box.setText(searchfromsearchquery)
           usertobesearched = self.card_header9.text()
           search_user()
           MainWindow.central_widget.setCurrentWidget(self.homescreen)

        def card_headerbtn10():
           global usertobesearched
           searchfromsearchquery = self.card_header10.text()
           searchuser_list(searchfromsearchquery)
           self.search_box.setText(searchfromsearchquery)
           self.search_search_box.setText(searchfromsearchquery)
           usertobesearched = self.card_header10.text()
           search_user()
           MainWindow.central_widget.setCurrentWidget(self.homescreen)






        def feedpost_corousell():
            self.feedpost_postcount.setHidden(False)
            self.feedpost_back.setHidden(False)
            self.feedpost_next.setHidden(False)
            self.feedpost_view.setHidden(True)
            self.feedpost_view_btn.setHidden(True)
        def feedpost_not_corousell():
            self.feedpost_postcount.setHidden(True)
            self.feedpost_back.setHidden(True)
            self.feedpost_next.setHidden(True)
            self.feedpost_view.setHidden(True)
            self.feedpost_view_btn.setHidden(True)
        def feedpost_video():
            self.feedpost_postcount.setHidden(True)
            self.feedpost_back.setHidden(True)
            self.feedpost_next.setHidden(True)
            self.feedpost_view.setHidden(False)
            self.feedpost_view_btn.setHidden(False)
        def feedpost_video_with_corousell():
            self.feedpost_postcount.setHidden(False)
            self.feedpost_back.setHidden(False)
            self.feedpost_next.setHidden(False)
            self.feedpost_view.setHidden(False)
            self.feedpost_view_btn.setHidden(False)

        def feed_like_media():
            global feed_media_id
            global user
            global feed_has_liked
            global feed_like_count
            #print("kjshdjk")
            if feed_has_liked == False:
                user.post_like(feed_media_id)
                self.feedpost_like.setPixmap(QtGui.QPixmap(":/elem/like.png"))
                feed_has_liked = True
                feed_like_count = feed_like_count+1
                self.feedpost_likecount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Likes: "+str(numconv(feed_like_count))+"</span></p></body></html>"))
            else:
                user.delete_like(feed_media_id)
                self.feedpost_like.setPixmap(QtGui.QPixmap(":/elem/unlike.png"))
                feed_has_liked = False
                feed_like_count = feed_like_count-1
                self.feedpost_likecount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Likes: "+str(numconv(feed_like_count))+"</span></p></body></html>"))



        def feed_save_media():
            global feed_media_id
            global user
            global feed_has_saved
            if feed_has_saved == True:
                self.feedpost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
                user.unsave_photo(feed_media_id)
                feed_has_saved = False
            else:
                self.feedpost_save.setPixmap(QtGui.QPixmap(":/elem/save.png"))
                user.save_photo(feed_media_id)
                feed_has_saved = True

        def feed_download_media():
            global post_req
            saveas_dialog = QFileDialog()
            desktop_location = os.path.expanduser("~/Desktop")
            open_path = desktop_location
            filter_ext = "Image Files(*.png)"
            save_location = QFileDialog.getSaveFileName(saveas_dialog, "Download Post", open_path, "Image Files (*.png);;")
            if (save_location[0]) == "":
                pass
            else:
               active_file = open(save_location[0], "wb")
               active_file_data = active_file.write(post_req.content)
               active_file.close()

        def feed_view_video():
            global feed_feed_postdataurl
            videourl = requests.get(feed_feed_postdataurl)
            videodownload = open("video.mp4", "wb")
            videodownload.write(videourl.content)
            videodownload.close()
            os.startfile("playvideo.pyw")
            
        def feed_copyhashtag():
            global feed_postdata
            caption = feed_postdata['caption']['text']
            copyhashlist_old = caption.split()
            copyhashlist_new=[]
            for item in copyhashlist_old:
               if item.startswith("#") and len(item)>1:
                  copyhashlist_new.append(item)
               else:
                  pass
            copyhash =  ' '.join(map(str, copyhashlist_new))
            pc.copy(copyhash)
            
        def feed_translate_eng():
            global feed_postdata
            caption = feed_postdata['caption']['text']

        def feed_next_corousell():
            global feed_postdata
            global feed_total_corousell
            global post_req
            global feed_corousell_count
            global feed_feed_postdataurl

            if feed_corousell_count==feed_total_corousell:
                pass
            else:
                feed_corousell_count = feed_corousell_count+1
                print(feed_corousell_count)
                post_req = requests.get(feed_postdata['carousel_media'][feed_corousell_count-1]['image_versions2']['candidates'][0]['url'])
                postcache1 = open("feedpost.png", "wb")
                postcache1.write(post_req.content)
                postcache1.close()
                reshape("feedpost.png")
                if feed_postdata['carousel_media'][feed_corousell_count-1]['media_type'] ==2:
                    feedpost_video_with_corousell()
                    feed_feed_postdataurl = feed_postdata['carousel_media'][feed_corousell_count-1]['video_versions'][1]['url']         
                else:
                    pass
                self.feedpost_image.setPixmap(QtGui.QPixmap("feedpost.png"))
                self.feedpost_postcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Post "+ str(feed_corousell_count) + "/" + str(feed_total_corousell)+ "</span></p></body></html>"))
        def feed_post_close():
            global feedsscr_select
            feedsscr_select = "feed"
            MainWindow.central_widget.setCurrentWidget(self.feed_screen)
        def feed_back_corousell():
            global feed_postdata
            global post_req
            global feed_total_corousell
            global feed_corousell_count
            global feed_feed_postdataurl

                
            if feed_corousell_count==1:
                pass
            else:
                feed_corousell_count = feed_corousell_count-1
                print(feed_corousell_count)
                post_req = requests.get(feed_postdata['carousel_media'][feed_corousell_count-1]['image_versions2']['candidates'][0]['url'])
                postcache1 = open("feedpost.png", "wb")
                postcache1.write(post_req.content)
                postcache1.close()
                reshape("feedpost.png")
                if feed_postdata['carousel_media'][feed_corousell_count-1]['media_type'] ==2:
                    onemypost_mycorousell()
                    feed_feed_postdataurl = feed_postdata['carousel_media'][feed_corousell_count-1]['video_versions'][1]['url']         
                else:
                    pass
                self.feedpost_image.setPixmap(QtGui.QPixmap("feedpost.png"))
                self.feedpost_postcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Post "+ str(feed_corousell_count) + "/" + str(feed_total_corousell)+ "</span></p></body></html>"))
           
        def card_footerbtn1_thread():
            MainWindow.setGraphicsEffect(self.blur_effect)
            self.blur_effect.setBlurRadius(5)
            MainWindow.setEnabled(False)
            global feedsscr
            feedsscr = "post"
            global feed_media_id
            global feed1
            global feed_has_liked
            global feed_like_count
            global feed_corousell_count
            #global usertobesearched
            global feed_postdata
            global feed_has_saved
            global feed_total_corousell
            global feed_feed_postdataurl
            global feed_seen
            feed_postdata = feed1
            feed_corousell_count = 1
            global post_req
            feed_media_id = feed_postdata['pk']
            self.feedpost_username.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">@"+ feed_postdata['user']['username']+"</span></p></body></html>"))
            if feed_postdata['media_type'] == 8:
                feed_total_corousell = len(feed_postdata['carousel_media'])
                post_req = requests.get(feed_postdata['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                postcache1 = open("feedpost.png", "wb")
                postcache1.write(post_req.content)
                postcache1.close()
                reshape("feedpost.png")
                self.feedpost_image.setPixmap(QtGui.QPixmap("feedpost.png"))
                if feed_postdata['carousel_media'][0]['media_type'] ==2:
                    feedpost_video_with_corousell()
                else:
                    feedpost_corousell()
                self.feedpost_postcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Post 1/" + str(feed_total_corousell)+ "</span></p></body></html>"))
            elif feed_postdata['media_type'] == 2:
                feed_feed_postdataurl = feed_postdata['video_versions'][2]['url']
                feedpost_video()
                post_req = requests.get((feed_postdata['image_versions2']['candidates'][0]['url']))
                postcache1 = open("feedpost.png", "wb")
                postcache1.write(post_req.content)
                postcache1.close()
                reshape("feedpost.png")
                self.feedpost_image.setPixmap(QtGui.QPixmap("feedpost.png"))
                
                
            else:
                feedpost_not_corousell()
                post_req = requests.get((feed_postdata['image_versions2']['candidates'][0]['url']))
                postcache1 = open("feedpost.png", "wb")
                postcache1.write(post_req.content)
                postcache1.close()
                reshape("feedpost.png")
                self.feedpost_image.setPixmap(QtGui.QPixmap("feedpost.png"))
            feed_like_count = feed_postdata['like_count']
            setscreen_feedpost()

            try:
                self.feedpost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#f1f1f1;\">"+feed_postdata['caption']['text']+"</span></p></body></html>"))
            except Exception:
                self.feedpost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">This Post has no Caption.</span></p></body></html>"))
            self.feedpost_likecount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Likes: "+str(numconv(feed_like_count))+"</span></p></body></html>"))
            self.feedpost_commentcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Comments: "+str(numconv(feed_postdata['comment_count']))+"</span></p></body></html>"))
            feed_has_liked = (feed_postdata['has_liked'])
            try:
                feed_has_saved = feed_postdata['has_viewer_saved']
                if feed_has_saved == True:
                    self.feedpost_save.setPixmap(QtGui.QPixmap(":/elem/save.png"))
                else:
                    self.feedpost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
            except Exception:
                self.feedpost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
                feed_has_saved = False
            if feed_has_liked == True:
                self.feedpost_like.setPixmap(QtGui.QPixmap(":/elem/like.png"))
            else:
                self.feedpost_like.setPixmap(QtGui.QPixmap(":/elem/unlike.png"))

            if (feed_postdata['caption_is_edited']) == True:
                self.feedpost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\">Edited</span></p></body></html>"))
            else:
                self.feedpost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\"></span></p></body></html>"))
            try:
                try:
                    self.feedpost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + feed_postdata['facepile_top_likers'][0]['username'] + " and " +feed_postdata['facepile_top_likers'][1]['username'] +"</span></p></body></html>"))
                except Exception:
                    self.feedpost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + feed_postdata['top_likers'][0]+"</span></p></body></html>"))
            except Exception:
                self.feedpost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Not liked by anyone you follow</span></p></body></html>"))
            feed_timestamp = time.ctime(feed_postdata['taken_at'])
            feed_timestamp24hr = datetime.strptime(feed_timestamp[11:16], "%H:%M")
            self.feedpost_date.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" color:#919191;\">"+(feed_timestamp24hr.strftime("%#I:%M%p")+ " "+feed_timestamp[:3]+", "+feed_timestamp[8:10]+" "+feed_timestamp[4:7]+" "+feed_timestamp[20:24])+"</span></p></body></html>"))
            MainWindow.setEnabled(True)
            self.blur_effect.setBlurRadius(0)
        def card_footerbtn1():
            thread8 = threading.Thread(target=card_footerbtn1_thread)
            thread8.start()


        def card_footerbtn2_thread():
            MainWindow.setGraphicsEffect(self.blur_effect)
            self.blur_effect.setBlurRadius(5)
            MainWindow.setEnabled(False)
            global feedsscr
            feedsscr = "post"
            global feed_media_id
            global feed2
            global feed_has_liked
            global feed_like_count
            global feed_corousell_count
            #global usertobesearched
            global feed_postdata
            global feed_has_saved
            global feed_total_corousell
            global feed_feed_postdataurl
            global feed_seen
            feed_postdata = feed2
            feed_corousell_count = 1
            global post_req
            feed_media_id = feed_postdata['pk']
            self.feedpost_username.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">@"+ feed_postdata['user']['username']+"</span></p></body></html>"))
            if feed_postdata['media_type'] == 8:
                feed_total_corousell = len(feed_postdata['carousel_media'])
                post_req = requests.get(feed_postdata['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                postcache1 = open("feedpost.png", "wb")
                postcache1.write(post_req.content)
                postcache1.close()
                reshape("feedpost.png")
                self.feedpost_image.setPixmap(QtGui.QPixmap("feedpost.png"))
                if feed_postdata['carousel_media'][0]['media_type'] ==2:
                    feedpost_video_with_corousell()
                else:
                    feedpost_corousell()
                self.feedpost_postcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Post 1/" + str(feed_total_corousell)+ "</span></p></body></html>"))
            elif feed_postdata['media_type'] == 2:
                feed_feed_postdataurl = feed_postdata['video_versions'][2]['url']
                feedpost_video()
                post_req = requests.get((feed_postdata['image_versions2']['candidates'][0]['url']))
                postcache1 = open("feedpost.png", "wb")
                postcache1.write(post_req.content)
                postcache1.close()
                reshape("feedpost.png")
                self.feedpost_image.setPixmap(QtGui.QPixmap("feedpost.png"))
                
                
            else:
                feedpost_not_corousell()
                post_req = requests.get((feed_postdata['image_versions2']['candidates'][0]['url']))
                postcache1 = open("feedpost.png", "wb")
                postcache1.write(post_req.content)
                postcache1.close()
                reshape("feedpost.png")
                self.feedpost_image.setPixmap(QtGui.QPixmap("feedpost.png"))
            feed_like_count = feed_postdata['like_count']
            setscreen_feedpost()

            try:
                self.feedpost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#f1f1f1;\">"+feed_postdata['caption']['text']+"</span></p></body></html>"))
            except Exception:
                self.feedpost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">This Post has no Caption.</span></p></body></html>"))
            self.feedpost_likecount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Likes: "+str(numconv(feed_like_count))+"</span></p></body></html>"))
            self.feedpost_commentcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Comments: "+str(numconv(feed_postdata['comment_count']))+"</span></p></body></html>"))
            feed_has_liked = (feed_postdata['has_liked'])
            try:
                feed_has_saved = feed_postdata['has_viewer_saved']
                if feed_has_saved == True:
                    self.feedpost_save.setPixmap(QtGui.QPixmap(":/elem/save.png"))
                else:
                    self.feedpost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
            except Exception:
                self.feedpost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
                feed_has_saved = False
            if feed_has_liked == True:
                self.feedpost_like.setPixmap(QtGui.QPixmap(":/elem/like.png"))
            else:
                self.feedpost_like.setPixmap(QtGui.QPixmap(":/elem/unlike.png"))

            if (feed_postdata['caption_is_edited']) == True:
                self.feedpost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\">Edited</span></p></body></html>"))
            else:
                self.feedpost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\"></span></p></body></html>"))
            try:
                try:
                    self.feedpost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + feed_postdata['facepile_top_likers'][0]['username'] + " and " +feed_postdata['facepile_top_likers'][1]['username'] +"</span></p></body></html>"))
                except Exception:
                    self.feedpost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + feed_postdata['top_likers'][0]+"</span></p></body></html>"))
            except Exception:
                self.feedpost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Not liked by anyone you follow</span></p></body></html>"))
            feed_timestamp = time.ctime(feed_postdata['taken_at'])
            feed_timestamp24hr = datetime.strptime(feed_timestamp[11:16], "%H:%M")
            self.feedpost_date.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" color:#919191;\">"+(feed_timestamp24hr.strftime("%#I:%M%p")+ " "+feed_timestamp[:3]+", "+feed_timestamp[8:10]+" "+feed_timestamp[4:7]+" "+feed_timestamp[20:24])+"</span></p></body></html>"))
            MainWindow.setEnabled(True)
            self.blur_effect.setBlurRadius(0)
        def card_footerbtn2():
            thread8 = threading.Thread(target=card_footerbtn2_thread)
            thread8.start()

        def card_footerbtn3_thread():
            MainWindow.setGraphicsEffect(self.blur_effect)
            self.blur_effect.setBlurRadius(5)
            MainWindow.setEnabled(False)
            global feedsscr
            feedsscr = "post"
            global feed_media_id
            global feed3
            global feed_has_liked
            global feed_like_count
            global feed_corousell_count
            #global usertobesearched
            global feed_postdata
            global feed_has_saved
            global feed_total_corousell
            global feed_feed_postdataurl
            global feed_seen
            feed_postdata = feed3
            feed_corousell_count = 1
            global post_req
            feed_media_id = feed_postdata['pk']
            self.feedpost_username.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">@"+ feed_postdata['user']['username']+"</span></p></body></html>"))
            if feed_postdata['media_type'] == 8:
                feed_total_corousell = len(feed_postdata['carousel_media'])
                post_req = requests.get(feed_postdata['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                postcache1 = open("feedpost.png", "wb")
                postcache1.write(post_req.content)
                postcache1.close()
                reshape("feedpost.png")
                self.feedpost_image.setPixmap(QtGui.QPixmap("feedpost.png"))
                if feed_postdata['carousel_media'][0]['media_type'] ==2:
                    feedpost_video_with_corousell()
                else:
                    feedpost_corousell()
                self.feedpost_postcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Post 1/" + str(feed_total_corousell)+ "</span></p></body></html>"))
            elif feed_postdata['media_type'] == 2:
                feed_feed_postdataurl = feed_postdata['video_versions'][2]['url']
                feedpost_video()
                post_req = requests.get((feed_postdata['image_versions2']['candidates'][0]['url']))
                postcache1 = open("feedpost.png", "wb")
                postcache1.write(post_req.content)
                postcache1.close()
                reshape("feedpost.png")
                self.feedpost_image.setPixmap(QtGui.QPixmap("feedpost.png"))
                
                
            else:
                feedpost_not_corousell()
                post_req = requests.get((feed_postdata['image_versions2']['candidates'][0]['url']))
                postcache1 = open("feedpost.png", "wb")
                postcache1.write(post_req.content)
                postcache1.close()
                reshape("feedpost.png")
                self.feedpost_image.setPixmap(QtGui.QPixmap("feedpost.png"))
            feed_like_count = feed_postdata['like_count']
            setscreen_feedpost()

            try:
                self.feedpost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#f1f1f1;\">"+feed_postdata['caption']['text']+"</span></p></body></html>"))
            except Exception:
                self.feedpost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">This Post has no Caption.</span></p></body></html>"))
            self.feedpost_likecount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Likes: "+str(numconv(feed_like_count))+"</span></p></body></html>"))
            self.feedpost_commentcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Comments: "+str(numconv(feed_postdata['comment_count']))+"</span></p></body></html>"))
            feed_has_liked = (feed_postdata['has_liked'])
            try:
                feed_has_saved = feed_postdata['has_viewer_saved']
                if feed_has_saved == True:
                    self.feedpost_save.setPixmap(QtGui.QPixmap(":/elem/save.png"))
                else:
                    self.feedpost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
            except Exception:
                self.feedpost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
                feed_has_saved = False
            if feed_has_liked == True:
                self.feedpost_like.setPixmap(QtGui.QPixmap(":/elem/like.png"))
            else:
                self.feedpost_like.setPixmap(QtGui.QPixmap(":/elem/unlike.png"))

            if (feed_postdata['caption_is_edited']) == True:
                self.feedpost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\">Edited</span></p></body></html>"))
            else:
                self.feedpost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\"></span></p></body></html>"))
            try:
                try:
                    self.feedpost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + feed_postdata['facepile_top_likers'][0]['username'] + " and " +feed_postdata['facepile_top_likers'][1]['username'] +"</span></p></body></html>"))
                except Exception:
                    self.feedpost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + feed_postdata['top_likers'][0]+"</span></p></body></html>"))
            except Exception:
                self.feedpost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Not liked by anyone you follow</span></p></body></html>"))
            feed_timestamp = time.ctime(feed_postdata['taken_at'])
            feed_timestamp24hr = datetime.strptime(feed_timestamp[11:16], "%H:%M")
            self.feedpost_date.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" color:#919191;\">"+(feed_timestamp24hr.strftime("%#I:%M%p")+ " "+feed_timestamp[:3]+", "+feed_timestamp[8:10]+" "+feed_timestamp[4:7]+" "+feed_timestamp[20:24])+"</span></p></body></html>"))
            MainWindow.setEnabled(True)
            self.blur_effect.setBlurRadius(0)
        def card_footerbtn3():
            thread8 = threading.Thread(target=card_footerbtn3_thread)
            thread8.start()

        def card_footerbtn4_thread():
            MainWindow.setGraphicsEffect(self.blur_effect)
            self.blur_effect.setBlurRadius(5)
            MainWindow.setEnabled(False)
            global feedsscr
            feedsscr = "post"
            global feed_media_id
            global feed4
            global feed_has_liked
            global feed_like_count
            global feed_corousell_count
            #global usertobesearched
            global feed_postdata
            global feed_has_saved
            global feed_total_corousell
            global feed_feed_postdataurl
            global feed_seen
            feed_postdata = feed4
            feed_corousell_count = 1
            feed_media_id = feed_postdata['pk']
            global post_req
            self.feedpost_username.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">@"+ feed_postdata['user']['username']+"</span></p></body></html>"))
            if feed_postdata['media_type'] == 8:
                feed_total_corousell = len(feed_postdata['carousel_media'])
                post_req = requests.get(feed_postdata['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                postcache1 = open("feedpost.png", "wb")
                postcache1.write(post_req.content)
                postcache1.close()
                reshape("feedpost.png")
                self.feedpost_image.setPixmap(QtGui.QPixmap("feedpost.png"))
                if feed_postdata['carousel_media'][0]['media_type'] ==2:
                    feedpost_video_with_corousell()
                else:
                    feedpost_corousell()
                self.feedpost_postcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Post 1/" + str(feed_total_corousell)+ "</span></p></body></html>"))
            elif feed_postdata['media_type'] == 2:
                feed_feed_postdataurl = feed_postdata['video_versions'][2]['url']
                feedpost_video()
                post_req = requests.get((feed_postdata['image_versions2']['candidates'][0]['url']))
                postcache1 = open("feedpost.png", "wb")
                postcache1.write(post_req.content)
                postcache1.close()
                reshape("feedpost.png")
                self.feedpost_image.setPixmap(QtGui.QPixmap("feedpost.png"))
                
                
            else:
                feedpost_not_corousell()
                post_req = requests.get((feed_postdata['image_versions2']['candidates'][0]['url']))
                postcache1 = open("feedpost.png", "wb")
                postcache1.write(post_req.content)
                postcache1.close()
                reshape("feedpost.png")
                self.feedpost_image.setPixmap(QtGui.QPixmap("feedpost.png"))
            feed_like_count = feed_postdata['like_count']
            setscreen_feedpost()

            try:
                self.feedpost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#f1f1f1;\">"+feed_postdata['caption']['text']+"</span></p></body></html>"))
            except Exception:
                self.feedpost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">This Post has no Caption.</span></p></body></html>"))
            self.feedpost_likecount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Likes: "+str(numconv(feed_like_count))+"</span></p></body></html>"))
            self.feedpost_commentcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Comments: "+str(numconv(feed_postdata['comment_count']))+"</span></p></body></html>"))
            feed_has_liked = (feed_postdata['has_liked'])
            try:
                feed_has_saved = feed_postdata['has_viewer_saved']
                if feed_has_saved == True:
                    self.feedpost_save.setPixmap(QtGui.QPixmap(":/elem/save.png"))
                else:
                    self.feedpost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
            except Exception:
                self.feedpost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
                feed_has_saved = False
            if feed_has_liked == True:
                self.feedpost_like.setPixmap(QtGui.QPixmap(":/elem/like.png"))
            else:
                self.feedpost_like.setPixmap(QtGui.QPixmap(":/elem/unlike.png"))

            if (feed_postdata['caption_is_edited']) == True:
                self.feedpost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\">Edited</span></p></body></html>"))
            else:
                self.feedpost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\"></span></p></body></html>"))
            try:
                try:
                    self.feedpost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + feed_postdata['facepile_top_likers'][0]['username'] + " and " +feed_postdata['facepile_top_likers'][1]['username'] +"</span></p></body></html>"))
                except Exception:
                    self.feedpost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + feed_postdata['top_likers'][0]+"</span></p></body></html>"))
            except Exception:
                self.feedpost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Not liked by anyone you follow</span></p></body></html>"))
            feed_timestamp = time.ctime(feed_postdata['taken_at'])
            feed_timestamp24hr = datetime.strptime(feed_timestamp[11:16], "%H:%M")
            self.feedpost_date.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" color:#919191;\">"+(feed_timestamp24hr.strftime("%#I:%M%p")+ " "+feed_timestamp[:3]+", "+feed_timestamp[8:10]+" "+feed_timestamp[4:7]+" "+feed_timestamp[20:24])+"</span></p></body></html>"))
            MainWindow.setEnabled(True)
            self.blur_effect.setBlurRadius(0)
        def card_footerbtn4():
            thread8 = threading.Thread(target=card_footerbtn4_thread)
            thread8.start()



        def card_footerbtn5_thread():
            MainWindow.setGraphicsEffect(self.blur_effect)
            self.blur_effect.setBlurRadius(5)
            MainWindow.setEnabled(False)
            global feedsscr
            feedsscr = "post"
            global feed_media_id
            global feed5
            global feed_has_liked
            global feed_like_count
            global feed_corousell_count
            #global usertobesearched
            global feed_postdata
            global feed_has_saved
            global feed_total_corousell
            global feed_feed_postdataurl
            global feed_seen
            feed_postdata = feed5
            feed_corousell_count = 1
            global post_req
            feed_media_id = feed_postdata['pk']
            feed_media_id = feed_postdata['pk']
            self.feedpost_username.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">@"+ feed_postdata['user']['username']+"</span></p></body></html>"))
            if feed_postdata['media_type'] == 8:
                feed_total_corousell = len(feed_postdata['carousel_media'])
                post_req = requests.get(feed_postdata['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                postcache1 = open("feedpost.png", "wb")
                postcache1.write(post_req.content)
                postcache1.close()
                reshape("feedpost.png")
                self.feedpost_image.setPixmap(QtGui.QPixmap("feedpost.png"))
                if feed_postdata['carousel_media'][0]['media_type'] ==2:
                    feedpost_video_with_corousell()
                else:
                    feedpost_corousell()
                self.feedpost_postcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Post 1/" + str(feed_total_corousell)+ "</span></p></body></html>"))
            elif feed_postdata['media_type'] == 2:
                feed_feed_postdataurl = feed_postdata['video_versions'][2]['url']
                feedpost_video()
                post_req = requests.get((feed_postdata['image_versions2']['candidates'][0]['url']))
                postcache1 = open("feedpost.png", "wb")
                postcache1.write(post_req.content)
                postcache1.close()
                reshape("feedpost.png")
                self.feedpost_image.setPixmap(QtGui.QPixmap("feedpost.png"))
                
                
            else:
                feedpost_not_corousell()
                post_req = requests.get((feed_postdata['image_versions2']['candidates'][0]['url']))
                postcache1 = open("feedpost.png", "wb")
                postcache1.write(post_req.content)
                postcache1.close()
                reshape("feedpost.png")
                self.feedpost_image.setPixmap(QtGui.QPixmap("feedpost.png"))
            feed_like_count = feed_postdata['like_count']
            setscreen_feedpost()

            try:
                self.feedpost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#f1f1f1;\">"+feed_postdata['caption']['text']+"</span></p></body></html>"))
            except Exception:
                self.feedpost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">This Post has no Caption.</span></p></body></html>"))
            self.feedpost_likecount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Likes: "+str(numconv(feed_like_count))+"</span></p></body></html>"))
            self.feedpost_commentcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Comments: "+str(numconv(feed_postdata['comment_count']))+"</span></p></body></html>"))
            feed_has_liked = (feed_postdata['has_liked'])
            try:
                feed_has_saved = feed_postdata['has_viewer_saved']
                if feed_has_saved == True:
                    self.feedpost_save.setPixmap(QtGui.QPixmap(":/elem/save.png"))
                else:
                    self.feedpost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
            except Exception:
                self.feedpost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
                feed_has_saved = False
            if feed_has_liked == True:
                self.feedpost_like.setPixmap(QtGui.QPixmap(":/elem/like.png"))
            else:
                self.feedpost_like.setPixmap(QtGui.QPixmap(":/elem/unlike.png"))

            if (feed_postdata['caption_is_edited']) == True:
                self.feedpost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\">Edited</span></p></body></html>"))
            else:
                self.feedpost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\"></span></p></body></html>"))
            try:
                try:
                    self.feedpost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + feed_postdata['facepile_top_likers'][0]['username'] + " and " +feed_postdata['facepile_top_likers'][1]['username'] +"</span></p></body></html>"))
                except Exception:
                    self.feedpost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + feed_postdata['top_likers'][0]+"</span></p></body></html>"))
            except Exception:
                self.feedpost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Not liked by anyone you follow</span></p></body></html>"))
            feed_timestamp = time.ctime(feed_postdata['taken_at'])
            feed_timestamp24hr = datetime.strptime(feed_timestamp[11:16], "%H:%M")
            self.feedpost_date.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" color:#919191;\">"+(feed_timestamp24hr.strftime("%#I:%M%p")+ " "+feed_timestamp[:3]+", "+feed_timestamp[8:10]+" "+feed_timestamp[4:7]+" "+feed_timestamp[20:24])+"</span></p></body></html>"))
            MainWindow.setEnabled(True)
            self.blur_effect.setBlurRadius(0)
        def card_footerbtn5():
            thread8 = threading.Thread(target=card_footerbtn5_thread)
            thread8.start()



        def card_footerbtn6_thread():
            MainWindow.setGraphicsEffect(self.blur_effect)
            self.blur_effect.setBlurRadius(5)
            MainWindow.setEnabled(False)
            global feedsscr
            feedsscr = "post"
            global feed_media_id
            global feed6
            global feed_has_liked
            global feed_like_count
            global feed_corousell_count
            #global usertobesearched
            global feed_postdata
            global feed_has_saved
            global feed_total_corousell
            global feed_feed_postdataurl
            global feed_seen
            feed_postdata = feed6
            feed_corousell_count = 1
            global post_req
            feed_media_id = feed_postdata['pk']
            self.feedpost_username.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">@"+ feed_postdata['user']['username']+"</span></p></body></html>"))
            if feed_postdata['media_type'] == 8:
                feed_total_corousell = len(feed_postdata['carousel_media'])
                post_req = requests.get(feed_postdata['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                postcache1 = open("feedpost.png", "wb")
                postcache1.write(post_req.content)
                postcache1.close()
                reshape("feedpost.png")
                self.feedpost_image.setPixmap(QtGui.QPixmap("feedpost.png"))
                if feed_postdata['carousel_media'][0]['media_type'] ==2:
                    feedpost_video_with_corousell()
                else:
                    feedpost_corousell()
                self.feedpost_postcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Post 1/" + str(feed_total_corousell)+ "</span></p></body></html>"))
            elif feed_postdata['media_type'] == 2:
                feed_feed_postdataurl = feed_postdata['video_versions'][2]['url']
                feedpost_video()
                post_req = requests.get((feed_postdata['image_versions2']['candidates'][0]['url']))
                postcache1 = open("feedpost.png", "wb")
                postcache1.write(post_req.content)
                postcache1.close()
                reshape("feedpost.png")
                self.feedpost_image.setPixmap(QtGui.QPixmap("feedpost.png"))
                
                
            else:
                feedpost_not_corousell()
                post_req = requests.get((feed_postdata['image_versions2']['candidates'][0]['url']))
                postcache1 = open("feedpost.png", "wb")
                postcache1.write(post_req.content)
                postcache1.close()
                reshape("feedpost.png")
                self.feedpost_image.setPixmap(QtGui.QPixmap("feedpost.png"))
            feed_like_count = feed_postdata['like_count']
            setscreen_feedpost()

            try:
                self.feedpost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#f1f1f1;\">"+feed_postdata['caption']['text']+"</span></p></body></html>"))
            except Exception:
                self.feedpost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">This Post has no Caption.</span></p></body></html>"))
            self.feedpost_likecount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Likes: "+str(numconv(feed_like_count))+"</span></p></body></html>"))
            self.feedpost_commentcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Comments: "+str(numconv(feed_postdata['comment_count']))+"</span></p></body></html>"))
            feed_has_liked = (feed_postdata['has_liked'])
            try:
                feed_has_saved = feed_postdata['has_viewer_saved']
                if feed_has_saved == True:
                    self.feedpost_save.setPixmap(QtGui.QPixmap(":/elem/save.png"))
                else:
                    self.feedpost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
            except Exception:
                self.feedpost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
                feed_has_saved = False
            if feed_has_liked == True:
                self.feedpost_like.setPixmap(QtGui.QPixmap(":/elem/like.png"))
            else:
                self.feedpost_like.setPixmap(QtGui.QPixmap(":/elem/unlike.png"))

            if (feed_postdata['caption_is_edited']) == True:
                self.feedpost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\">Edited</span></p></body></html>"))
            else:
                self.feedpost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\"></span></p></body></html>"))
            try:
                try:
                    self.feedpost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + feed_postdata['facepile_top_likers'][0]['username'] + " and " +feed_postdata['facepile_top_likers'][1]['username'] +"</span></p></body></html>"))
                except Exception:
                    self.feedpost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + feed_postdata['top_likers'][0]+"</span></p></body></html>"))
            except Exception:
                self.feedpost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Not liked by anyone you follow</span></p></body></html>"))
            feed_timestamp = time.ctime(feed_postdata['taken_at'])
            feed_timestamp24hr = datetime.strptime(feed_timestamp[11:16], "%H:%M")
            self.feedpost_date.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" color:#919191;\">"+(feed_timestamp24hr.strftime("%#I:%M%p")+ " "+feed_timestamp[:3]+", "+feed_timestamp[8:10]+" "+feed_timestamp[4:7]+" "+feed_timestamp[20:24])+"</span></p></body></html>"))
            MainWindow.setEnabled(True)
            self.blur_effect.setBlurRadius(0)
        def card_footerbtn6():
            thread8 = threading.Thread(target=card_footerbtn6_thread)
            thread8.start()




        def card_footerbtn7_thread():
            MainWindow.setGraphicsEffect(self.blur_effect)
            self.blur_effect.setBlurRadius(5)
            MainWindow.setEnabled(False)
            global feedsscr
            feedsscr = "post"
            global feed_media_id
            global feed7
            global feed_has_liked
            global feed_like_count
            global feed_corousell_count
            #global usertobesearched
            global feed_postdata
            global feed_has_saved
            global feed_total_corousell
            global feed_feed_postdataurl
            global feed_seen
            feed_postdata = feed7
            feed_corousell_count = 1
            global post_req
            feed_media_id = feed_postdata['pk']
            self.feedpost_username.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">@"+ feed_postdata['user']['username']+"</span></p></body></html>"))
            if feed_postdata['media_type'] == 8:
                feed_total_corousell = len(feed_postdata['carousel_media'])
                post_req = requests.get(feed_postdata['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                postcache1 = open("feedpost.png", "wb")
                postcache1.write(post_req.content)
                postcache1.close()
                reshape("feedpost.png")
                self.feedpost_image.setPixmap(QtGui.QPixmap("feedpost.png"))
                if feed_postdata['carousel_media'][0]['media_type'] ==2:
                    feedpost_video_with_corousell()
                else:
                    feedpost_corousell()
                self.feedpost_postcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Post 1/" + str(feed_total_corousell)+ "</span></p></body></html>"))
            elif feed_postdata['media_type'] == 2:
                feed_feed_postdataurl = feed_postdata['video_versions'][2]['url']
                feedpost_video()
                post_req = requests.get((feed_postdata['image_versions2']['candidates'][0]['url']))
                postcache1 = open("feedpost.png", "wb")
                postcache1.write(post_req.content)
                postcache1.close()
                reshape("feedpost.png")
                self.feedpost_image.setPixmap(QtGui.QPixmap("feedpost.png"))
                
                
            else:
                feedpost_not_corousell()
                post_req = requests.get((feed_postdata['image_versions2']['candidates'][0]['url']))
                postcache1 = open("feedpost.png", "wb")
                postcache1.write(post_req.content)
                postcache1.close()
                reshape("feedpost.png")
                self.feedpost_image.setPixmap(QtGui.QPixmap("feedpost.png"))
            feed_like_count = feed_postdata['like_count']
            setscreen_feedpost()

            try:
                self.feedpost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#f1f1f1;\">"+feed_postdata['caption']['text']+"</span></p></body></html>"))
            except Exception:
                self.feedpost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">This Post has no Caption.</span></p></body></html>"))
            self.feedpost_likecount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Likes: "+str(numconv(feed_like_count))+"</span></p></body></html>"))
            self.feedpost_commentcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Comments: "+str(numconv(feed_postdata['comment_count']))+"</span></p></body></html>"))
            feed_has_liked = (feed_postdata['has_liked'])
            try:
                feed_has_saved = feed_postdata['has_viewer_saved']
                if feed_has_saved == True:
                    self.feedpost_save.setPixmap(QtGui.QPixmap(":/elem/save.png"))
                else:
                    self.feedpost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
            except Exception:
                self.feedpost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
                feed_has_saved = False
            if feed_has_liked == True:
                self.feedpost_like.setPixmap(QtGui.QPixmap(":/elem/like.png"))
            else:
                self.feedpost_like.setPixmap(QtGui.QPixmap(":/elem/unlike.png"))

            if (feed_postdata['caption_is_edited']) == True:
                self.feedpost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\">Edited</span></p></body></html>"))
            else:
                self.feedpost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\"></span></p></body></html>"))
            try:
                try:
                    self.feedpost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + feed_postdata['facepile_top_likers'][0]['username'] + " and " +feed_postdata['facepile_top_likers'][1]['username'] +"</span></p></body></html>"))
                except Exception:
                    self.feedpost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + feed_postdata['top_likers'][0]+"</span></p></body></html>"))
            except Exception:
                self.feedpost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Not liked by anyone you follow</span></p></body></html>"))
            feed_timestamp = time.ctime(feed_postdata['taken_at'])
            feed_timestamp24hr = datetime.strptime(feed_timestamp[11:16], "%H:%M")
            self.feedpost_date.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" color:#919191;\">"+(feed_timestamp24hr.strftime("%#I:%M%p")+ " "+feed_timestamp[:3]+", "+feed_timestamp[8:10]+" "+feed_timestamp[4:7]+" "+feed_timestamp[20:24])+"</span></p></body></html>"))
            MainWindow.setEnabled(True)
            self.blur_effect.setBlurRadius(0)
        def card_footerbtn7():
            thread8 = threading.Thread(target=card_footerbtn7_thread)
            thread8.start()


        def card_footerbtn8_thread():
            MainWindow.setGraphicsEffect(self.blur_effect)
            self.blur_effect.setBlurRadius(5)
            MainWindow.setEnabled(False)
            global feedsscr
            feedsscr = "post"
            global feed_media_id
            global feed8
            global feed_has_liked
            global feed_like_count
            global feed_corousell_count
            #global usertobesearched
            global feed_postdata
            global feed_has_saved
            global feed_total_corousell
            global feed_feed_postdataurl
            global feed_seen
            feed_postdata = feed8
            feed_corousell_count = 1
            global post_req
            feed_media_id = feed_postdata['pk']
            self.feedpost_username.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">@"+ feed_postdata['user']['username']+"</span></p></body></html>"))
            if feed_postdata['media_type'] == 8:
                feed_total_corousell = len(feed_postdata['carousel_media'])
                post_req = requests.get(feed_postdata['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                postcache1 = open("feedpost.png", "wb")
                postcache1.write(post_req.content)
                postcache1.close()
                reshape("feedpost.png")
                self.feedpost_image.setPixmap(QtGui.QPixmap("feedpost.png"))
                if feed_postdata['carousel_media'][0]['media_type'] ==2:
                    feedpost_video_with_corousell()
                else:
                    feedpost_corousell()
                self.feedpost_postcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Post 1/" + str(feed_total_corousell)+ "</span></p></body></html>"))
            elif feed_postdata['media_type'] == 2:
                feed_feed_postdataurl = feed_postdata['video_versions'][2]['url']
                feedpost_video()
                post_req = requests.get((feed_postdata['image_versions2']['candidates'][0]['url']))
                postcache1 = open("feedpost.png", "wb")
                postcache1.write(post_req.content)
                postcache1.close()
                reshape("feedpost.png")
                self.feedpost_image.setPixmap(QtGui.QPixmap("feedpost.png"))
                
                
            else:
                feedpost_not_corousell()
                post_req = requests.get((feed_postdata['image_versions2']['candidates'][0]['url']))
                postcache1 = open("feedpost.png", "wb")
                postcache1.write(post_req.content)
                postcache1.close()
                reshape("feedpost.png")
                self.feedpost_image.setPixmap(QtGui.QPixmap("feedpost.png"))
            feed_like_count = feed_postdata['like_count']
            setscreen_feedpost()

            try:
                self.feedpost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#f1f1f1;\">"+feed_postdata['caption']['text']+"</span></p></body></html>"))
            except Exception:
                self.feedpost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">This Post has no Caption.</span></p></body></html>"))
            self.feedpost_likecount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Likes: "+str(numconv(feed_like_count))+"</span></p></body></html>"))
            self.feedpost_commentcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Comments: "+str(numconv(feed_postdata['comment_count']))+"</span></p></body></html>"))
            feed_has_liked = (feed_postdata['has_liked'])
            try:
                feed_has_saved = feed_postdata['has_viewer_saved']
                if feed_has_saved == True:
                    self.feedpost_save.setPixmap(QtGui.QPixmap(":/elem/save.png"))
                else:
                    self.feedpost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
            except Exception:
                self.feedpost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
                feed_has_saved = False
            if feed_has_liked == True:
                self.feedpost_like.setPixmap(QtGui.QPixmap(":/elem/like.png"))
            else:
                self.feedpost_like.setPixmap(QtGui.QPixmap(":/elem/unlike.png"))

            if (feed_postdata['caption_is_edited']) == True:
                self.feedpost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\">Edited</span></p></body></html>"))
            else:
                self.feedpost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\"></span></p></body></html>"))
            try:
                try:
                    self.feedpost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + feed_postdata['facepile_top_likers'][0]['username'] + " and " +feed_postdata['facepile_top_likers'][1]['username'] +"</span></p></body></html>"))
                except Exception:
                    self.feedpost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + feed_postdata['top_likers'][0]+"</span></p></body></html>"))
            except Exception:
                self.feedpost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Not liked by anyone you follow</span></p></body></html>"))
            feed_timestamp = time.ctime(feed_postdata['taken_at'])
            feed_timestamp24hr = datetime.strptime(feed_timestamp[11:16], "%H:%M")
            self.feedpost_date.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" color:#919191;\">"+(feed_timestamp24hr.strftime("%#I:%M%p")+ " "+feed_timestamp[:3]+", "+feed_timestamp[8:10]+" "+feed_timestamp[4:7]+" "+feed_timestamp[20:24])+"</span></p></body></html>"))
            MainWindow.setEnabled(True)
            self.blur_effect.setBlurRadius(0)
        def card_footerbtn8():
            thread8 = threading.Thread(target=card_footerbtn8_thread)
            thread8.start()


        def card_footerbtn9_thread():
            MainWindow.setGraphicsEffect(self.blur_effect)
            self.blur_effect.setBlurRadius(5)
            MainWindow.setEnabled(False)
            global feedsscr
            feedsscr = "post"
            global feed_media_id
            global feed9
            global feed_has_liked
            global feed_like_count
            global feed_corousell_count
            #global usertobesearched
            global feed_postdata
            global feed_has_saved
            global feed_total_corousell
            global feed_feed_postdataurl
            global feed_seen
            feed_postdata = feed9
            feed_corousell_count = 1
            global post_req
            feed_media_id = feed_postdata['pk']
            self.feedpost_username.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">@"+ feed_postdata['user']['username']+"</span></p></body></html>"))
            if feed_postdata['media_type'] == 8:
                feed_total_corousell = len(feed_postdata['carousel_media'])
                post_req = requests.get(feed_postdata['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                postcache1 = open("feedpost.png", "wb")
                postcache1.write(post_req.content)
                postcache1.close()
                reshape("feedpost.png")
                self.feedpost_image.setPixmap(QtGui.QPixmap("feedpost.png"))
                if feed_postdata['carousel_media'][0]['media_type'] ==2:
                    feedpost_video_with_corousell()
                else:
                    feedpost_corousell()
                self.feedpost_postcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Post 1/" + str(feed_total_corousell)+ "</span></p></body></html>"))
            elif feed_postdata['media_type'] == 2:
                feed_feed_postdataurl = feed_postdata['video_versions'][2]['url']
                feedpost_video()
                post_req = requests.get((feed_postdata['image_versions2']['candidates'][0]['url']))
                postcache1 = open("feedpost.png", "wb")
                postcache1.write(post_req.content)
                postcache1.close()
                reshape("feedpost.png")
                self.feedpost_image.setPixmap(QtGui.QPixmap("feedpost.png"))
                
                
            else:
                feedpost_not_corousell()
                post_req = requests.get((feed_postdata['image_versions2']['candidates'][0]['url']))
                postcache1 = open("feedpost.png", "wb")
                postcache1.write(post_req.content)
                postcache1.close()
                reshape("feedpost.png")
                self.feedpost_image.setPixmap(QtGui.QPixmap("feedpost.png"))
            feed_like_count = feed_postdata['like_count']
            setscreen_feedpost()

            try:
                self.feedpost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#f1f1f1;\">"+feed_postdata['caption']['text']+"</span></p></body></html>"))
            except Exception:
                self.feedpost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">This Post has no Caption.</span></p></body></html>"))
            self.feedpost_likecount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Likes: "+str(numconv(feed_like_count))+"</span></p></body></html>"))
            self.feedpost_commentcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Comments: "+str(numconv(feed_postdata['comment_count']))+"</span></p></body></html>"))
            feed_has_liked = (feed_postdata['has_liked'])
            try:
                feed_has_saved = feed_postdata['has_viewer_saved']
                if feed_has_saved == True:
                    self.feedpost_save.setPixmap(QtGui.QPixmap(":/elem/save.png"))
                else:
                    self.feedpost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
            except Exception:
                self.feedpost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
                feed_has_saved = False
            if feed_has_liked == True:
                self.feedpost_like.setPixmap(QtGui.QPixmap(":/elem/like.png"))
            else:
                self.feedpost_like.setPixmap(QtGui.QPixmap(":/elem/unlike.png"))

            if (feed_postdata['caption_is_edited']) == True:
                self.feedpost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\">Edited</span></p></body></html>"))
            else:
                self.feedpost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\"></span></p></body></html>"))
            try:
                try:
                    self.feedpost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + feed_postdata['facepile_top_likers'][0]['username'] + " and " +feed_postdata['facepile_top_likers'][1]['username'] +"</span></p></body></html>"))
                except Exception:
                    self.feedpost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + feed_postdata['top_likers'][0]+"</span></p></body></html>"))
            except Exception:
                self.feedpost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Not liked by anyone you follow</span></p></body></html>"))
            feed_timestamp = time.ctime(feed_postdata['taken_at'])
            feed_timestamp24hr = datetime.strptime(feed_timestamp[11:16], "%H:%M")
            self.feedpost_date.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" color:#919191;\">"+(feed_timestamp24hr.strftime("%#I:%M%p")+ " "+feed_timestamp[:3]+", "+feed_timestamp[8:10]+" "+feed_timestamp[4:7]+" "+feed_timestamp[20:24])+"</span></p></body></html>"))
            MainWindow.setEnabled(True)
            self.blur_effect.setBlurRadius(0)
        def card_footerbtn9():
            thread8 = threading.Thread(target=card_footerbtn9_thread)
            thread8.start()



        def card_footerbtn10_thread():
            MainWindow.setGraphicsEffect(self.blur_effect)
            self.blur_effect.setBlurRadius(5)
            MainWindow.setEnabled(False)
            global feedsscr
            feedsscr = "post"
            global feed_media_id
            global feed10
            global feed_has_liked
            global feed_like_count
            global feed_corousell_count
            #global usertobesearched
            global feed_postdata
            global feed_has_saved
            global feed_total_corousell
            global feed_feed_postdataurl
            global feed_seen
            feed_postdata = feed10
            feed_corousell_count = 1
            global post_req
            feed_media_id = feed_postdata['pk']
            self.feedpost_username.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">@"+ feed_postdata['user']['username']+"</span></p></body></html>"))
            if feed_postdata['media_type'] == 8:
                feed_total_corousell = len(feed_postdata['carousel_media'])
                post_req = requests.get(feed_postdata['carousel_media'][0]['image_versions2']['candidates'][0]['url'])
                postcache1 = open("feedpost.png", "wb")
                postcache1.write(post_req.content)
                postcache1.close()
                reshape("feedpost.png")
                self.feedpost_image.setPixmap(QtGui.QPixmap("feedpost.png"))
                if feed_postdata['carousel_media'][0]['media_type'] ==2:
                    feedpost_video_with_corousell()
                else:
                    feedpost_corousell() 
                self.feedpost_postcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Post 1/" + str(feed_total_corousell)+ "</span></p></body></html>"))
            elif feed_postdata['media_type'] == 2:
                feed_feed_postdataurl = feed_postdata['video_versions'][2]['url']
                feedpost_video()
                post_req = requests.get((feed_postdata['image_versions2']['candidates'][0]['url']))
                postcache1 = open("feedpost.png", "wb")
                postcache1.write(post_req.content)
                postcache1.close()
                reshape("feedpost.png")
                self.feedpost_image.setPixmap(QtGui.QPixmap("feedpost.png"))
                
                
            else:
                feedpost_not_corousell()
                post_req = requests.get((feed_postdata['image_versions2']['candidates'][0]['url']))
                postcache1 = open("feedpost.png", "wb")
                postcache1.write(post_req.content)
                postcache1.close()
                reshape("feedpost.png")
                self.feedpost_image.setPixmap(QtGui.QPixmap("feedpost.png"))
            feed_like_count = feed_postdata['like_count']
            setscreen_feedpost()

            try:
                self.feedpost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#f1f1f1;\">"+feed_postdata['caption']['text']+"</span></p></body></html>"))
            except Exception:
                self.feedpost_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">This Post has no Caption.</span></p></body></html>"))
            self.feedpost_likecount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Likes: "+str(numconv(feed_like_count))+"</span></p></body></html>"))
            self.feedpost_commentcount.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#f1f1f1;\">Comments: "+str(numconv(feed_postdata['comment_count']))+"</span></p></body></html>"))
            feed_has_liked = (feed_postdata['has_liked'])
            try:
                feed_has_saved = feed_postdata['has_viewer_saved']
                if feed_has_saved == True:
                    self.feedpost_save.setPixmap(QtGui.QPixmap(":/elem/save.png"))
                else:
                    self.feedpost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
            except Exception:
                self.feedpost_save.setPixmap(QtGui.QPixmap(":/elem/unsave.png"))
                feed_has_saved = False
            if feed_has_liked == True:
                self.feedpost_like.setPixmap(QtGui.QPixmap(":/elem/like.png"))
            else:
                self.feedpost_like.setPixmap(QtGui.QPixmap(":/elem/unlike.png"))

            if (feed_postdata['caption_is_edited']) == True:
                self.feedpost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\">Edited</span></p></body></html>"))
            else:
                self.feedpost_edit.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\"></span></p></body></html>"))
            try:
                try:
                    self.feedpost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + feed_postdata['facepile_top_likers'][0]['username'] + " and " +feed_postdata['facepile_top_likers'][1]['username'] +"</span></p></body></html>"))
                except Exception:
                    self.feedpost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Liked by " + feed_postdata['top_likers'][0]+"</span></p></body></html>"))
            except Exception:
                self.feedpost_lb_caption.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#919191;\">Not liked by anyone you follow</span></p></body></html>"))
            feed_timestamp = time.ctime(feed_postdata['taken_at'])
            feed_timestamp24hr = datetime.strptime(feed_timestamp[11:16], "%H:%M")
            self.feedpost_date.setText(_translate("MainWindow", "<html><head/><body><p align=\"right\"><span style=\" color:#919191;\">"+(feed_timestamp24hr.strftime("%#I:%M%p")+ " "+feed_timestamp[:3]+", "+feed_timestamp[8:10]+" "+feed_timestamp[4:7]+" "+feed_timestamp[20:24])+"</span></p></body></html>"))
            MainWindow.setEnabled(True)
            self.blur_effect.setBlurRadius(0)
        def card_footerbtn10():
            thread8 = threading.Thread(target=card_footerbtn10_thread)
            thread8.start()  


            
        def watch_all_story_thread():
            global user
            global username
            allstoryseen = "NO"
            while allstoryseen == "NO":
               stories = user.reels_tray()['tray']
               #total_stories = len(stories)
               story = (stories[0])
               story_username = story['user']['username']
               if story_username == username:
                   story = (stories[1])
                   story_username = story['user']['username']
               self.loadingscreen_text.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\">Binge Watching @"+str(story_username)+" story for you.</span></p></body></html>"))
               try:
                  if story['latest_reel_media'] == story['seen']:
                     self.loadingscreen_text.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\">Watched All Stories for you Bro..</span></p></body></html>"))
                     allstoryseen = "YES"
                     #print(username)
                     load_story()
                     MainWindow.central_widget.setCurrentWidget(self.feed_screen)
                  else:
                     #print('not seen')
                     total_story = story['media_count']
                     y=0      
                     while y != total_story:  
                        one_story = story['items'][y]
                        one_story_id = one_story['id']
                        one_story_takenat = one_story['taken_at']
                        one_story_seenid = {str(one_story_id):[str(one_story_takenat)+"_"+str(one_story_takenat)]}
                        user.media_seen(one_story_seenid)
                        y=y+1
                     self.loadingscreen_text.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\">Completed Watching @"+str(story_username)+" story.</span></p></body></html>"))

               except Exception:
                  self.loadingscreen_text.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\">Loading Next Story</span></p></body></html>"))

        def watch_all_story():
            self.loadingscreen_text.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#919191;\">Colecting Stories..</span></p></body></html>"))
            MainWindow.central_widget.setCurrentWidget(self.loadingscreen)
            thread9 = threading.Thread(target = watch_all_story_thread)
            thread9.start()

           # Story Tray
        def load_story():
            global user
            global stories
            global story_count
            global story_pageno
            story_pageno = 1
            stories = user.reels_tray()['tray']
            story_count = 0
            try:
               self.reel_1.setHidden(False)
               story_req = requests.get(stories[story_count]['user']['profile_pic_url'])
               story_cover_download = open("story_dp_"+str(story_count+1)+".png", "wb")
               story_cover_download.write(story_req.content)
               story_cover_download.close()
               circularimg("story_dp_"+str(story_count+1)+".png")
               if stories[story_count]['latest_reel_media'] == stories[story_count]['seen']:
                  self.reel_1.setStyleSheet("background:transparent;border:3px solid rgb(77, 77, 77);border-radius:35px")
               else:
                  if stories[story_count]['has_besties_media'] == True:
                     self.reel_1.setStyleSheet("background:transparent;border:3px solid qradialgradient(spread:pad, cx:0.535, cy:0.512, radius:2, fx:0, fy:1, stop:0.0625 rgba(0, 178, 0, 255), stop:1 rgba(50, 223, 0, 255));border-radius:35px")
                  else:
                     self.reel_1.setStyleSheet("background:transparent;border:3px solid qradialgradient(spread:pad, cx:0, cy:1, radius:2, fx:1, fy:0.251, stop:0 rgba(241, 39, 17, 255), stop:1 rgba(245, 25, 137, 255));border-radius:35px")
               self.reel_1.setPixmap(QtGui.QPixmap("story_dp_"+str(story_count+1)+".png"))
               story_count = story_count+1
            except Exception:
                self.reel_1.setHidden(True)
                story_count = story_count+1
            try:
               self.reel_2.setHidden(False)          
               story_req = requests.get(stories[story_count]['user']['profile_pic_url'])
               story_cover_download = open("story_dp_"+str(story_count+1)+".png", "wb")
               story_cover_download.write(story_req.content)
               story_cover_download.close()
               circularimg("story_dp_"+str(story_count+1)+".png")
               if stories[story_count]['latest_reel_media'] == stories[story_count]['seen']:
                  self.reel_2.setStyleSheet("background:transparent;border:3px solid rgb(77, 77, 77);border-radius:35px")
               else:
                  if stories[story_count]['has_besties_media'] == True:
                     self.reel_2.setStyleSheet("background:transparent;border:3px solid qradialgradient(spread:pad, cx:0.535, cy:0.512, radius:2, fx:0, fy:1, stop:0.0625 rgba(0, 178, 0, 255), stop:1 rgba(50, 223, 0, 255));border-radius:35px")
                  else:
                     self.reel_2.setStyleSheet("background:transparent;border:3px solid qradialgradient(spread:pad, cx:0, cy:1, radius:2, fx:1, fy:0.251, stop:0 rgba(241, 39, 17, 255), stop:1 rgba(245, 25, 137, 255));border-radius:35px")
               self.reel_2.setPixmap(QtGui.QPixmap("story_dp_"+str(story_count+1)+".png"))
               story_count = story_count+1      
            except Exception:
                self.reel_2.setHidden(True)
                story_count = story_count+1
            try:
               self.reel_3.setHidden(False)
               story_req = requests.get(stories[story_count]['user']['profile_pic_url'])
               story_cover_download = open("story_dp_"+str(story_count+1)+".png", "wb")
               story_cover_download.write(story_req.content)
               story_cover_download.close()
               circularimg("story_dp_"+str(story_count+1)+".png")
               if stories[story_count]['latest_reel_media'] == stories[story_count]['seen']:
                  self.reel_3.setStyleSheet("background:transparent;border:3px solid rgb(77, 77, 77);border-radius:35px")
               else:
                  if stories[story_count]['has_besties_media'] == True:
                     self.reel_3.setStyleSheet("background:transparent;border:3px solid qradialgradient(spread:pad, cx:0.535, cy:0.512, radius:2, fx:0, fy:1, stop:0.0625 rgba(0, 178, 0, 255), stop:1 rgba(50, 223, 0, 255));border-radius:35px")
                  else:
                     self.reel_3.setStyleSheet("background:transparent;border:3px solid qradialgradient(spread:pad, cx:0, cy:1, radius:2, fx:1, fy:0.251, stop:0 rgba(241, 39, 17, 255), stop:1 rgba(245, 25, 137, 255));border-radius:35px")
               self.reel_3.setPixmap(QtGui.QPixmap("story_dp_"+str(story_count+1)+".png"))
               story_count = story_count+1
            except Exception:
                self.reel_3.setHidden(True)
                story_count = story_count+1
            try:
               self.reel_4.setHidden(False)
               story_req = requests.get(stories[story_count]['user']['profile_pic_url'])
               story_cover_download = open("story_dp_"+str(story_count+1)+".png", "wb")
               story_cover_download.write(story_req.content)
               story_cover_download.close()
               circularimg("story_dp_"+str(story_count+1)+".png")
               if stories[story_count]['latest_reel_media'] == stories[story_count]['seen']:
                  self.reel_4.setStyleSheet("background:transparent;border:3px solid rgb(77, 77, 77);border-radius:35px")
               else:
                  if stories[story_count]['has_besties_media'] == True:
                     self.reel_4.setStyleSheet("background:transparent;border:3px solid qradialgradient(spread:pad, cx:0.535, cy:0.512, radius:2, fx:0, fy:1, stop:0.0625 rgba(0, 178, 0, 255), stop:1 rgba(50, 223, 0, 255));border-radius:35px")
                  else:
                     self.reel_4.setStyleSheet("background:transparent;border:3px solid qradialgradient(spread:pad, cx:0, cy:1, radius:2, fx:1, fy:0.251, stop:0 rgba(241, 39, 17, 255), stop:1 rgba(245, 25, 137, 255));border-radius:35px")
               self.reel_4.setPixmap(QtGui.QPixmap("story_dp_"+str(story_count+1)+".png"))
               story_count = story_count+1
            except Exception:
                self.reel_4.setHidden(True)
                story_count = story_count+1
            try:
               self.reel_5.setHidden(False)
               story_req = requests.get(stories[story_count]['user']['profile_pic_url'])
               story_cover_download = open("story_dp_"+str(story_count+1)+".png", "wb")
               story_cover_download.write(story_req.content)
               story_cover_download.close()
               circularimg("story_dp_"+str(story_count+1)+".png")
               if stories[story_count]['latest_reel_media'] == stories[story_count]['seen']:
                  self.reel_5.setStyleSheet("background:transparent;border:3px solid rgb(77, 77, 77);border-radius:35px")
               else:
                  if stories[story_count]['has_besties_media'] == True:
                     self.reel_5.setStyleSheet("background:transparent;border:3px solid qradialgradient(spread:pad, cx:0.535, cy:0.512, radius:2, fx:0, fy:1, stop:0.0625 rgba(0, 178, 0, 255), stop:1 rgba(50, 223, 0, 255));border-radius:35px")
                  else:
                     self.reel_5.setStyleSheet("background:transparent;border:3px solid qradialgradient(spread:pad, cx:0, cy:1, radius:2, fx:1, fy:0.251, stop:0 rgba(241, 39, 17, 255), stop:1 rgba(245, 25, 137, 255));border-radius:35px")

               self.reel_5.setPixmap(QtGui.QPixmap("story_dp_"+str(story_count+1)+".png"))
               story_count = story_count+1
            except Exception:
                self.reel_5.setHidden(True)
                story_count = story_count+1
            try:
               self.reel_6.setHidden(False)
               story_req = requests.get(stories[story_count]['user']['profile_pic_url'])
               story_cover_download = open("story_dp_"+str(story_count+1)+".png", "wb")
               story_cover_download.write(story_req.content)
               story_cover_download.close()
               circularimg("story_dp_"+str(story_count+1)+".png")
               if stories[story_count]['latest_reel_media'] == stories[story_count]['seen']:
                  self.reel_6.setStyleSheet("background:transparent;border:3px solid rgb(77, 77, 77);border-radius:35px")
               else:
                  if stories[story_count]['has_besties_media'] == True:
                     self.reel_6.setStyleSheet("background:transparent;border:3px solid qradialgradient(spread:pad, cx:0.535, cy:0.512, radius:2, fx:0, fy:1, stop:0.0625 rgba(0, 178, 0, 255), stop:1 rgba(50, 223, 0, 255));border-radius:35px")
                  else:
                     self.reel_6.setStyleSheet("background:transparent;border:3px solid qradialgradient(spread:pad, cx:0, cy:1, radius:2, fx:1, fy:0.251, stop:0 rgba(241, 39, 17, 255), stop:1 rgba(245, 25, 137, 255));border-radius:35px")

               self.reel_6.setPixmap(QtGui.QPixmap("story_dp_"+str(story_count+1)+".png"))
               story_count = story_count+1  
               
            except Exception:
                self.reel_6.setHidden(True)
                story_count = story_count+1
            try:
               self.reel_7.setHidden(False)           
               story_req = requests.get(stories[story_count]['user']['profile_pic_url'])
               story_cover_download = open("story_dp_"+str(story_count+1)+".png", "wb")
               story_cover_download.write(story_req.content)
               story_cover_download.close()
               circularimg("story_dp_"+str(story_count+1)+".png")
               if stories[story_count]['latest_reel_media'] == stories[story_count]['seen']:
                  self.reel_7.setStyleSheet("background:transparent;border:3px solid rgb(77, 77, 77);border-radius:35px")
               else:
                  if stories[story_count]['has_besties_media'] == True:
                     self.reel_7.setStyleSheet("background:transparent;border:3px solid qradialgradient(spread:pad, cx:0.535, cy:0.512, radius:2, fx:0, fy:1, stop:0.0625 rgba(0, 178, 0, 255), stop:1 rgba(50, 223, 0, 255));border-radius:35px")
                  else:
                     self.reel_7.setStyleSheet("background:transparent;border:3px solid qradialgradient(spread:pad, cx:0, cy:1, radius:2, fx:1, fy:0.251, stop:0 rgba(241, 39, 17, 255), stop:1 rgba(245, 25, 137, 255));border-radius:35px")

               self.reel_7.setPixmap(QtGui.QPixmap("story_dp_"+str(story_count+1)+".png"))
               story_count = story_count+1
            except Exception:
                self.reel_7.setHidden(True)
                story_count = story_count+1
            try:
               self.reel_8.setHidden(False)
               story_req = requests.get(stories[story_count]['user']['profile_pic_url'])
               story_cover_download = open("story_dp_"+str(story_count+1)+".png", "wb")
               story_cover_download.write(story_req.content)
               story_cover_download.close()
               circularimg("story_dp_"+str(story_count+1)+".png")
               if stories[story_count]['latest_reel_media'] == stories[story_count]['seen']:
                  self.reel_8.setStyleSheet("background:transparent;border:3px solid rgb(77, 77, 77);border-radius:35px")
               else:
                  if stories[story_count]['has_besties_media'] == True:
                     self.reel_8.setStyleSheet("background:transparent;border:3px solid qradialgradient(spread:pad, cx:0.535, cy:0.512, radius:2, fx:0, fy:1, stop:0.0625 rgba(0, 178, 0, 255), stop:1 rgba(50, 223, 0, 255));border-radius:35px")
                  else:
                     self.reel_8.setStyleSheet("background:transparent;border:3px solid qradialgradient(spread:pad, cx:0, cy:1, radius:2, fx:1, fy:0.251, stop:0 rgba(241, 39, 17, 255), stop:1 rgba(245, 25, 137, 255));border-radius:35px")
               self.reel_8.setPixmap(QtGui.QPixmap("story_dp_"+str(story_count+1)+".png"))
            except Exception:
                self.reel_8.setHidden(True)
        def next_story_thread():
            global user
            global stories
            global story_count
            global story_pageno
            story_pageno = story_pageno +1
            self.reel_1.setHidden(True)
            self.reel_2.setHidden(True)
            self.reel_3.setHidden(True)
            self.reel_4.setHidden(True)
            self.reel_5.setHidden(True)
            self.reel_6.setHidden(True)
            self.reel_7.setHidden(True)
            self.reel_8.setHidden(True)
            
            story_count = story_count+1
            #stories = user.reels_tray()['tray']
            try:
               self.reel_1.setHidden(False)
               story_req = requests.get(stories[story_count]['user']['profile_pic_url'])
               story_cover_download = open("story_dp_"+str(story_count+1)+".png", "wb")
               story_cover_download.write(story_req.content)
               story_cover_download.close()
               circularimg("story_dp_"+str(story_count+1)+".png")
               if stories[story_count]['latest_reel_media'] == stories[story_count]['seen']:
                  self.reel_1.setStyleSheet("background:transparent;border:3px solid rgb(77, 77, 77);border-radius:35px")
               else:
                  if stories[story_count]['has_besties_media'] == True:
                     self.reel_1.setStyleSheet("background:transparent;border:3px solid qradialgradient(spread:pad, cx:0.535, cy:0.512, radius:2, fx:0, fy:1, stop:0.0625 rgba(0, 178, 0, 255), stop:1 rgba(50, 223, 0, 255));border-radius:35px")
                  else:
                     self.reel_1.setStyleSheet("background:transparent;border:3px solid qradialgradient(spread:pad, cx:0, cy:1, radius:2, fx:1, fy:0.251, stop:0 rgba(241, 39, 17, 255), stop:1 rgba(245, 25, 137, 255));border-radius:35px")
               self.reel_1.setPixmap(QtGui.QPixmap("story_dp_"+str(story_count+1)+".png"))
               story_count = story_count+1
            except Exception:
                self.reel_1.setHidden(True)
                story_count = story_count+1
            try:
               self.reel_2.setHidden(False)          
               story_req = requests.get(stories[story_count]['user']['profile_pic_url'])
               story_cover_download = open("story_dp_"+str(story_count+1)+".png", "wb")
               story_cover_download.write(story_req.content)
               story_cover_download.close()
               circularimg("story_dp_"+str(story_count+1)+".png")
               if stories[story_count]['latest_reel_media'] == stories[story_count]['seen']:
                  self.reel_2.setStyleSheet("background:transparent;border:3px solid rgb(77, 77, 77);border-radius:35px")
               else:
                  if stories[story_count]['has_besties_media'] == True:
                     self.reel_2.setStyleSheet("background:transparent;border:3px solid qradialgradient(spread:pad, cx:0.535, cy:0.512, radius:2, fx:0, fy:1, stop:0.0625 rgba(0, 178, 0, 255), stop:1 rgba(50, 223, 0, 255));border-radius:35px")
                  else:
                     self.reel_2.setStyleSheet("background:transparent;border:3px solid qradialgradient(spread:pad, cx:0, cy:1, radius:2, fx:1, fy:0.251, stop:0 rgba(241, 39, 17, 255), stop:1 rgba(245, 25, 137, 255));border-radius:35px")
               self.reel_2.setPixmap(QtGui.QPixmap("story_dp_"+str(story_count+1)+".png"))
               story_count = story_count+1      
            except Exception:
                self.reel_2.setHidden(True)
                story_count = story_count+1
            try:
               self.reel_3.setHidden(False)
               story_req = requests.get(stories[story_count]['user']['profile_pic_url'])
               story_cover_download = open("story_dp_"+str(story_count+1)+".png", "wb")
               story_cover_download.write(story_req.content)
               story_cover_download.close()
               circularimg("story_dp_"+str(story_count+1)+".png")
               if stories[story_count]['latest_reel_media'] == stories[story_count]['seen']:
                  self.reel_3.setStyleSheet("background:transparent;border:3px solid rgb(77, 77, 77);border-radius:35px")
               else:
                  if stories[story_count]['has_besties_media'] == True:
                     self.reel_3.setStyleSheet("background:transparent;border:3px solid qradialgradient(spread:pad, cx:0.535, cy:0.512, radius:2, fx:0, fy:1, stop:0.0625 rgba(0, 178, 0, 255), stop:1 rgba(50, 223, 0, 255));border-radius:35px")
                  else:
                     self.reel_3.setStyleSheet("background:transparent;border:3px solid qradialgradient(spread:pad, cx:0, cy:1, radius:2, fx:1, fy:0.251, stop:0 rgba(241, 39, 17, 255), stop:1 rgba(245, 25, 137, 255));border-radius:35px")
               self.reel_3.setPixmap(QtGui.QPixmap("story_dp_"+str(story_count+1)+".png"))
               story_count = story_count+1
            except Exception:
                self.reel_3.setHidden(True)
                story_count = story_count+1
            try:
               self.reel_4.setHidden(False)
               story_req = requests.get(stories[story_count]['user']['profile_pic_url'])
               story_cover_download = open("story_dp_"+str(story_count+1)+".png", "wb")
               story_cover_download.write(story_req.content)
               story_cover_download.close()
               circularimg("story_dp_"+str(story_count+1)+".png")
               if stories[story_count]['latest_reel_media'] == stories[story_count]['seen']:
                  self.reel_4.setStyleSheet("background:transparent;border:3px solid rgb(77, 77, 77);border-radius:35px")
               else:
                  if stories[story_count]['has_besties_media'] == True:
                     self.reel_4.setStyleSheet("background:transparent;border:3px solid qradialgradient(spread:pad, cx:0.535, cy:0.512, radius:2, fx:0, fy:1, stop:0.0625 rgba(0, 178, 0, 255), stop:1 rgba(50, 223, 0, 255));border-radius:35px")
                  else:
                     self.reel_4.setStyleSheet("background:transparent;border:3px solid qradialgradient(spread:pad, cx:0, cy:1, radius:2, fx:1, fy:0.251, stop:0 rgba(241, 39, 17, 255), stop:1 rgba(245, 25, 137, 255));border-radius:35px")
               self.reel_4.setPixmap(QtGui.QPixmap("story_dp_"+str(story_count+1)+".png"))
               story_count = story_count+1
            except Exception:
                self.reel_4.setHidden(True)
                story_count = story_count+1
            try:
               self.reel_5.setHidden(False)
               story_req = requests.get(stories[story_count]['user']['profile_pic_url'])
               story_cover_download = open("story_dp_"+str(story_count+1)+".png", "wb")
               story_cover_download.write(story_req.content)
               story_cover_download.close()
               circularimg("story_dp_"+str(story_count+1)+".png")
               if stories[story_count]['latest_reel_media'] == stories[story_count]['seen']:
                  self.reel_5.setStyleSheet("background:transparent;border:3px solid rgb(77, 77, 77);border-radius:35px")
               else:
                  if stories[story_count]['has_besties_media'] == True:
                     self.reel_5.setStyleSheet("background:transparent;border:3px solid qradialgradient(spread:pad, cx:0.535, cy:0.512, radius:2, fx:0, fy:1, stop:0.0625 rgba(0, 178, 0, 255), stop:1 rgba(50, 223, 0, 255));border-radius:35px")
                  else:
                     self.reel_5.setStyleSheet("background:transparent;border:3px solid qradialgradient(spread:pad, cx:0, cy:1, radius:2, fx:1, fy:0.251, stop:0 rgba(241, 39, 17, 255), stop:1 rgba(245, 25, 137, 255));border-radius:35px")

               self.reel_5.setPixmap(QtGui.QPixmap("story_dp_"+str(story_count+1)+".png"))
               story_count = story_count+1
            except Exception:
                self.reel_5.setHidden(True)
                story_count = story_count+1
            try:
               self.reel_6.setHidden(False)
               story_req = requests.get(stories[story_count]['user']['profile_pic_url'])
               story_cover_download = open("story_dp_"+str(story_count+1)+".png", "wb")
               story_cover_download.write(story_req.content)
               story_cover_download.close()
               circularimg("story_dp_"+str(story_count+1)+".png")
               if stories[story_count]['latest_reel_media'] == stories[story_count]['seen']:
                  self.reel_6.setStyleSheet("background:transparent;border:3px solid rgb(77, 77, 77);border-radius:35px")
               else:
                  if stories[story_count]['has_besties_media'] == True:
                     self.reel_6.setStyleSheet("background:transparent;border:3px solid qradialgradient(spread:pad, cx:0.535, cy:0.512, radius:2, fx:0, fy:1, stop:0.0625 rgba(0, 178, 0, 255), stop:1 rgba(50, 223, 0, 255));border-radius:35px")
                  else:
                     self.reel_6.setStyleSheet("background:transparent;border:3px solid qradialgradient(spread:pad, cx:0, cy:1, radius:2, fx:1, fy:0.251, stop:0 rgba(241, 39, 17, 255), stop:1 rgba(245, 25, 137, 255));border-radius:35px")

               self.reel_6.setPixmap(QtGui.QPixmap("story_dp_"+str(story_count+1)+".png"))
               story_count = story_count+1  
               
            except Exception:
                self.reel_6.setHidden(True)
                story_count = story_count+1
            try:
               self.reel_7.setHidden(False)           
               story_req = requests.get(stories[story_count]['user']['profile_pic_url'])
               story_cover_download = open("story_dp_"+str(story_count+1)+".png", "wb")
               story_cover_download.write(story_req.content)
               story_cover_download.close()
               circularimg("story_dp_"+str(story_count+1)+".png")
               if stories[story_count]['latest_reel_media'] == stories[story_count]['seen']:
                  self.reel_7.setStyleSheet("background:transparent;border:3px solid rgb(77, 77, 77);border-radius:35px")
               else:
                  if stories[story_count]['has_besties_media'] == True:
                     self.reel_7.setStyleSheet("background:transparent;border:3px solid qradialgradient(spread:pad, cx:0.535, cy:0.512, radius:2, fx:0, fy:1, stop:0.0625 rgba(0, 178, 0, 255), stop:1 rgba(50, 223, 0, 255));border-radius:35px")
                  else:
                     self.reel_7.setStyleSheet("background:transparent;border:3px solid qradialgradient(spread:pad, cx:0, cy:1, radius:2, fx:1, fy:0.251, stop:0 rgba(241, 39, 17, 255), stop:1 rgba(245, 25, 137, 255));border-radius:35px")

               self.reel_7.setPixmap(QtGui.QPixmap("story_dp_"+str(story_count+1)+".png"))
               story_count = story_count+1
            except Exception:
                self.reel_7.setHidden(True)
                story_count = story_count+1
            try:
               self.reel_8.setHidden(False)
               story_req = requests.get(stories[story_count]['user']['profile_pic_url'])
               story_cover_download = open("story_dp_"+str(story_count+1)+".png", "wb")
               story_cover_download.write(story_req.content)
               story_cover_download.close()
               circularimg("story_dp_"+str(story_count+1)+".png")
               if stories[story_count]['latest_reel_media'] == stories[story_count]['seen']:
                  self.reel_8.setStyleSheet("background:transparent;border:3px solid rgb(77, 77, 77);border-radius:35px")
               else:
                  if stories[story_count]['has_besties_media'] == True:
                     self.reel_8.setStyleSheet("background:transparent;border:3px solid qradialgradient(spread:pad, cx:0.535, cy:0.512, radius:2, fx:0, fy:1, stop:0.0625 rgba(0, 178, 0, 255), stop:1 rgba(50, 223, 0, 255));border-radius:35px")
                  else:
                     self.reel_8.setStyleSheet("background:transparent;border:3px solid qradialgradient(spread:pad, cx:0, cy:1, radius:2, fx:1, fy:0.251, stop:0 rgba(241, 39, 17, 255), stop:1 rgba(245, 25, 137, 255));border-radius:35px")
               self.reel_8.setPixmap(QtGui.QPixmap("story_dp_"+str(story_count+1)+".png"))
            except Exception:
                self.reel_8.setHidden(True)


        def back_story_thread():
            global user
            global stories
            global story_count
            global story_pageno
           
            if story_pageno == 1:
               pass
            else:
               story_pageno = story_pageno -1
               self.reel_1.setHidden(True)
               self.reel_2.setHidden(True)
               self.reel_3.setHidden(True)
               self.reel_4.setHidden(True)
               self.reel_5.setHidden(True)
               self.reel_6.setHidden(True)
               self.reel_7.setHidden(True)
               self.reel_8.setHidden(True)


               story_count = story_count-8
               #stories = user.reels_tray()['tray']

               try:
                  self.reel_8.setHidden(False)
                  story_req = requests.get(stories[story_count]['user']['profile_pic_url'])
                  story_cover_download = open("story_dp_"+str(story_count+1)+".png", "wb")
                  story_cover_download.write(story_req.content)
                  story_cover_download.close()
                  circularimg("story_dp_"+str(story_count+1)+".png")
                  if stories[story_count]['latest_reel_media'] == stories[story_count]['seen']:
                     self.reel_8.setStyleSheet("background:transparent;border:3px solid rgb(77, 77, 77);border-radius:35px")
                  else:
                     if stories[story_count]['has_besties_media'] == True:
                        self.reel_8.setStyleSheet("background:transparent;border:3px solid qradialgradient(spread:pad, cx:0.535, cy:0.512, radius:2, fx:0, fy:1, stop:0.0625 rgba(0, 178, 0, 255), stop:1 rgba(50, 223, 0, 255));border-radius:35px")
                     else:
                        self.reel_8.setStyleSheet("background:transparent;border:3px solid qradialgradient(spread:pad, cx:0, cy:1, radius:2, fx:1, fy:0.251, stop:0 rgba(241, 39, 17, 255), stop:1 rgba(245, 25, 137, 255));border-radius:35px")
                  self.reel_8.setPixmap(QtGui.QPixmap("story_dp_"+str(story_count+1)+".png"))
                  story_count = story_count-1
               except Exception:
                   self.reel_8.setHidden(True)
                   story_count = story_count-1
               try:
                  self.reel_7.setHidden(False)           
                  story_req = requests.get(stories[story_count]['user']['profile_pic_url'])
                  story_cover_download = open("story_dp_"+str(story_count+1)+".png", "wb")
                  story_cover_download.write(story_req.content)
                  story_cover_download.close()
                  circularimg("story_dp_"+str(story_count+1)+".png")
                  if stories[story_count]['latest_reel_media'] == stories[story_count]['seen']:
                     self.reel_7.setStyleSheet("background:transparent;border:3px solid rgb(77, 77, 77);border-radius:35px")
                  else:
                     if stories[story_count]['has_besties_media'] == True:
                        self.reel_7.setStyleSheet("background:transparent;border:3px solid qradialgradient(spread:pad, cx:0.535, cy:0.512, radius:2, fx:0, fy:1, stop:0.0625 rgba(0, 178, 0, 255), stop:1 rgba(50, 223, 0, 255));border-radius:35px")
                     else:
                        self.reel_7.setStyleSheet("background:transparent;border:3px solid qradialgradient(spread:pad, cx:0, cy:1, radius:2, fx:1, fy:0.251, stop:0 rgba(241, 39, 17, 255), stop:1 rgba(245, 25, 137, 255));border-radius:35px")

                  self.reel_7.setPixmap(QtGui.QPixmap("story_dp_"+str(story_count+1)+".png"))
                  story_count = story_count-1
               except Exception:
                   self.reel_7.setHidden(True)
                   story_count = story_count-1
               try:
                  self.reel_6.setHidden(False)
                  story_req = requests.get(stories[story_count]['user']['profile_pic_url'])
                  story_cover_download = open("story_dp_"+str(story_count+1)+".png", "wb")
                  story_cover_download.write(story_req.content)
                  story_cover_download.close()
                  circularimg("story_dp_"+str(story_count+1)+".png")
                  if stories[story_count]['latest_reel_media'] == stories[story_count]['seen']:
                     self.reel_6.setStyleSheet("background:transparent;border:3px solid rgb(77, 77, 77);border-radius:35px")
                  else:
                     if stories[story_count]['has_besties_media'] == True:
                        self.reel_6.setStyleSheet("background:transparent;border:3px solid qradialgradient(spread:pad, cx:0.535, cy:0.512, radius:2, fx:0, fy:1, stop:0.0625 rgba(0, 178, 0, 255), stop:1 rgba(50, 223, 0, 255));border-radius:35px")
                     else:
                        self.reel_6.setStyleSheet("background:transparent;border:3px solid qradialgradient(spread:pad, cx:0, cy:1, radius:2, fx:1, fy:0.251, stop:0 rgba(241, 39, 17, 255), stop:1 rgba(245, 25, 137, 255));border-radius:35px")

                  self.reel_6.setPixmap(QtGui.QPixmap("story_dp_"+str(story_count+1)+".png"))
                  story_count = story_count-1  
                  
               except Exception:
                   self.reel_6.setHidden(True)
                   story_count = story_count-1
               try:
                  self.reel_5.setHidden(False)
                  story_req = requests.get(stories[story_count]['user']['profile_pic_url'])
                  story_cover_download = open("story_dp_"+str(story_count+1)+".png", "wb")
                  story_cover_download.write(story_req.content)
                  story_cover_download.close()
                  circularimg("story_dp_"+str(story_count+1)+".png")
                  if stories[story_count]['latest_reel_media'] == stories[story_count]['seen']:
                     self.reel_5.setStyleSheet("background:transparent;border:3px solid rgb(77, 77, 77);border-radius:35px")
                  else:
                     if stories[story_count]['has_besties_media'] == True:
                        self.reel_5.setStyleSheet("background:transparent;border:3px solid qradialgradient(spread:pad, cx:0.535, cy:0.512, radius:2, fx:0, fy:1, stop:0.0625 rgba(0, 178, 0, 255), stop:1 rgba(50, 223, 0, 255));border-radius:35px")
                     else:
                        self.reel_5.setStyleSheet("background:transparent;border:3px solid qradialgradient(spread:pad, cx:0, cy:1, radius:2, fx:1, fy:0.251, stop:0 rgba(241, 39, 17, 255), stop:1 rgba(245, 25, 137, 255));border-radius:35px")

                  self.reel_5.setPixmap(QtGui.QPixmap("story_dp_"+str(story_count+1)+".png"))
                  story_count = story_count-1
               except Exception:
                   self.reel_5.setHidden(True)
                   story_count = story_count-1
               try:
                  self.reel_4.setHidden(False)
                  story_req = requests.get(stories[story_count]['user']['profile_pic_url'])
                  story_cover_download = open("story_dp_"+str(story_count+1)+".png", "wb")
                  story_cover_download.write(story_req.content)
                  story_cover_download.close()
                  circularimg("story_dp_"+str(story_count+1)+".png")
                  if stories[story_count]['latest_reel_media'] == stories[story_count]['seen']:
                     self.reel_4.setStyleSheet("background:transparent;border:3px solid rgb(77, 77, 77);border-radius:35px")
                  else:
                     if stories[story_count]['has_besties_media'] == True:
                        self.reel_4.setStyleSheet("background:transparent;border:3px solid qradialgradient(spread:pad, cx:0.535, cy:0.512, radius:2, fx:0, fy:1, stop:0.0625 rgba(0, 178, 0, 255), stop:1 rgba(50, 223, 0, 255));border-radius:35px")
                     else:
                        self.reel_4.setStyleSheet("background:transparent;border:3px solid qradialgradient(spread:pad, cx:0, cy:1, radius:2, fx:1, fy:0.251, stop:0 rgba(241, 39, 17, 255), stop:1 rgba(245, 25, 137, 255));border-radius:35px")
                  self.reel_4.setPixmap(QtGui.QPixmap("story_dp_"+str(story_count+1)+".png"))
                  story_count = story_count-1
               except Exception:
                   self.reel_4.setHidden(True)
                   story_count = story_count-1

               try:
                  self.reel_3.setHidden(False)
                  story_req = requests.get(stories[story_count]['user']['profile_pic_url'])
                  story_cover_download = open("story_dp_"+str(story_count+1)+".png", "wb")
                  story_cover_download.write(story_req.content)
                  story_cover_download.close()
                  circularimg("story_dp_"+str(story_count+1)+".png")
                  if stories[story_count]['latest_reel_media'] == stories[story_count]['seen']:
                     self.reel_3.setStyleSheet("background:transparent;border:3px solid rgb(77, 77, 77);border-radius:35px")
                  else:
                     if stories[story_count]['has_besties_media'] == True:
                        self.reel_3.setStyleSheet("background:transparent;border:3px solid qradialgradient(spread:pad, cx:0.535, cy:0.512, radius:2, fx:0, fy:1, stop:0.0625 rgba(0, 178, 0, 255), stop:1 rgba(50, 223, 0, 255));border-radius:35px")
                     else:
                        self.reel_3.setStyleSheet("background:transparent;border:3px solid qradialgradient(spread:pad, cx:0, cy:1, radius:2, fx:1, fy:0.251, stop:0 rgba(241, 39, 17, 255), stop:1 rgba(245, 25, 137, 255));border-radius:35px")
                  self.reel_3.setPixmap(QtGui.QPixmap("story_dp_"+str(story_count+1)+".png"))
                  story_count = story_count-1
               except Exception:
                   self.reel_3.setHidden(True)
                   story_count = story_count-1
               try:
                  self.reel_2.setHidden(False)          
                  story_req = requests.get(stories[story_count]['user']['profile_pic_url'])
                  story_cover_download = open("story_dp_"+str(story_count+1)+".png", "wb")
                  story_cover_download.write(story_req.content)
                  story_cover_download.close()
                  circularimg("story_dp_"+str(story_count+1)+".png")
                  if stories[story_count]['latest_reel_media'] == stories[story_count]['seen']:
                     self.reel_2.setStyleSheet("background:transparent;border:3px solid rgb(77, 77, 77);border-radius:35px")
                  else:
                     if stories[story_count]['has_besties_media'] == True:
                        self.reel_2.setStyleSheet("background:transparent;border:3px solid qradialgradient(spread:pad, cx:0.535, cy:0.512, radius:2, fx:0, fy:1, stop:0.0625 rgba(0, 178, 0, 255), stop:1 rgba(50, 223, 0, 255));border-radius:35px")
                     else:
                        self.reel_2.setStyleSheet("background:transparent;border:3px solid qradialgradient(spread:pad, cx:0, cy:1, radius:2, fx:1, fy:0.251, stop:0 rgba(241, 39, 17, 255), stop:1 rgba(245, 25, 137, 255));border-radius:35px")
                  self.reel_2.setPixmap(QtGui.QPixmap("story_dp_"+str(story_count+1)+".png"))
                  story_count = story_count-1      
               except Exception:
                   self.reel_2.setHidden(True)
                   story_count = story_count-1
               try:
                  self.reel_1.setHidden(False)
                  story_req = requests.get(stories[story_count]['user']['profile_pic_url'])
                  story_cover_download = open("story_dp_"+str(story_count+1)+".png", "wb")
                  story_cover_download.write(story_req.content)
                  story_cover_download.close()
                  circularimg("story_dp_"+str(story_count+1)+".png")
                  if stories[story_count]['latest_reel_media'] == stories[story_count]['seen']:
                     self.reel_1.setStyleSheet("background:transparent;border:3px solid rgb(77, 77, 77);border-radius:35px")
                  else:
                     if stories[story_count]['has_besties_media'] == True:
                        self.reel_1.setStyleSheet("background:transparent;border:3px solid qradialgradient(spread:pad, cx:0.535, cy:0.512, radius:2, fx:0, fy:1, stop:0.0625 rgba(0, 178, 0, 255), stop:1 rgba(50, 223, 0, 255));border-radius:35px")
                     else:
                        self.reel_1.setStyleSheet("background:transparent;border:3px solid qradialgradient(spread:pad, cx:0, cy:1, radius:2, fx:1, fy:0.251, stop:0 rgba(241, 39, 17, 255), stop:1 rgba(245, 25, 137, 255));border-radius:35px")
                  self.reel_1.setPixmap(QtGui.QPixmap("story_dp_"+str(story_count+1)+".png"))
                  story_count = story_count+7

               except Exception:
                   self.reel_1.setHidden(True)
                   story_count = story_count+7


        def next_story():
            thread11= threading.Thread(target = next_story_thread)
            thread11.start()
        def back_story():
            thread11= threading.Thread(target = back_story_thread)
            thread11.start()          
#starting application
import resource
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
