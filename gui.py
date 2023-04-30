# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HomeGuiVersion4_emptiedKATFVj.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class Record:
    def __init__(self, name, picture_path, likes, listennings):
        self.name = name
        self.picture_path = picture_path
        self.likes = likes
        self.listennings = listennings


SEND_FOR_SONGS = lambda name: f'GET /music/{name}/{name}.m3u8 HTTP/1.1'
SIGN_UP = 'UserProcessor/SignUp?username={}&password={}&email={}@'
SIGN_IN = 'UserProcessor/SignIn?username={}&password={}@'
SIGN_IN_LABEL = 'Please enter your username and password.'
SIGN_UP_LABEL = 'Please enter your username, password and email.'
SIGN_IN_LABEL_AFTER_FAIL = 'Wrong username or password. Please enter credentials again.'
SIGN_UP_LABEL_AFTER_FAIL = 'User already exists. Please try another email or username.'
PROFILE_PIC_PATH = ''
SONG_RECOMMENDATION_COUNT = 8
SONG_RECOMMENDATION_PROMPT = '^Song_Recommendations'
ALBUM_RECOMMENDATIONS_PROMPT = '^Album_Recommendations'
SEARCH = lambda prompt: f'Search?prompt={prompt}@'
FETCH_RECORD = lambda record: f'Fetch/{record}@'
SEARCH_RESPONSE_PREFIX = 'Searched'
FETCH_RECORD_RESPONSE_PREFIX = 'Fetched'
RECORD_PIC_PATH = lambda identifier: f"record_pictures/{identifier}"
HOME_RECOMMENDATION_IDENTIFIER = lambda n: f"home_pic#{n}.jpg"

PRODUCE_SONG_PATH = lambda name: f"music/{name}/{name}.m3u8"


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, send_queue, login_finished_event, login_approved, expect_m3u8_and_url, scrollbar_playing_event, player_playing_event, player_fetching_event, scrollbar_paused_event, gui_msg_queue):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(941, 582)
        self.gui_msg_queue = gui_msg_queue
        self.scrollbar_paused_event = scrollbar_paused_event
        self.player_fetching_event = player_fetching_event  # change time in a song
        self.scrollbar_playing_event = scrollbar_playing_event
        self.player_playing_event = player_playing_event
        self.expect_m3u8_and_url = expect_m3u8_and_url
        self.login_finished_event = login_finished_event
        self.login_approved = login_approved
        self.send_queue = send_queue
        self.homepage_songs = []
        self.playlist_songs = []
        self.search_songs = []
        self.profile_songs = []
        self.serial = 0
        self.username = None
        self.sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        self.sizePolicy.setHorizontalStretch(0)
        self.sizePolicy.setVerticalStretch(0)
        self.sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(self.sizePolicy)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.MainStackWidget = QStackedWidget(self.centralwidget)
        self.MainStackWidget.setObjectName(u"MainStackWidget")
        self.AfterSignInPage = QWidget()
        self.AfterSignInPage.setObjectName(u"AfterSignInPage")
        self.horizontalLayout_20 = QHBoxLayout(self.AfterSignInPage)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetMinimumSize)
        self.left_side_profile_pic_label = QLabel(self.AfterSignInPage)
        self.left_side_profile_pic_label.setObjectName(u"left_side_profile_pic_label")
        self.sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.sizePolicy1.setHorizontalStretch(1)
        self.sizePolicy1.setVerticalStretch(0)
        self.sizePolicy1.setHeightForWidth(self.left_side_profile_pic_label.sizePolicy().hasHeightForWidth())
        self.left_side_profile_pic_label.setSizePolicy(self.sizePolicy1)
        self.left_side_profile_pic_label.setMinimumSize(QSize(63, 0))
        self.left_side_profile_pic_label.setMaximumSize(QSize(63, 50))
        self.left_side_profile_pic_label.setBaseSize(QSize(50, 50))
        self.left_side_profile_pic_label.setPixmap(QPixmap(u"../../Users/\u05d9\u05d4\u05d5\u05e0\u05ea\u05df \u05d0\u05dc\u05e4\u05e1\u05d9/Downloads/146-1468479_my-profile-icon-blank-profile-picture-circle-hd.png"))
        self.left_side_profile_pic_label.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.left_side_profile_pic_label)

        self.left_side_username_label = QLabel(self.AfterSignInPage)
        self.left_side_username_label.setObjectName(u"left_side_username_label")
        self.sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.sizePolicy2.setHorizontalStretch(0)
        self.sizePolicy2.setVerticalStretch(0)
        self.sizePolicy2.setHeightForWidth(self.left_side_username_label.sizePolicy().hasHeightForWidth())
        self.left_side_username_label.setSizePolicy(self.sizePolicy2)
        self.left_side_username_label.setMinimumSize(QSize(150, 60))
        self.left_side_username_label.setBaseSize(QSize(50, 50))

        self.horizontalLayout_2.addWidget(self.left_side_username_label)

        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.home_button = QPushButton(self.AfterSignInPage)
        self.home_button.setObjectName(u"home_button")

        self.verticalLayout_3.addWidget(self.home_button)

        self.profile_button = QPushButton(self.AfterSignInPage)
        self.profile_button.setObjectName(u"profile_button")

        self.verticalLayout_3.addWidget(self.profile_button)

        self.log_out_button = QPushButton(self.AfterSignInPage)
        self.log_out_button.setObjectName(u"log_out_button")

        self.verticalLayout_3.addWidget(self.log_out_button)

        self.frame = QFrame(self.AfterSignInPage)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_3.addWidget(self.frame)

        self.verticalLayout_3.setStretch(2, 1)
        self.verticalLayout_3.setStretch(3, 1)
        self.verticalLayout_3.setStretch(4, 1)

        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SetFixedSize)
        self.SearchBar = QTextBrowser(self.AfterSignInPage)
        self.SearchBar.setObjectName(u"SearchBar")
        self.sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.sizePolicy3.setHorizontalStretch(0)
        self.sizePolicy3.setVerticalStretch(1)
        self.sizePolicy3.setHeightForWidth(self.SearchBar.sizePolicy().hasHeightForWidth())
        self.SearchBar.setSizePolicy(self.sizePolicy3)
        self.SearchBar.setMinimumSize(QSize(277, 30))
        self.SearchBar.setMaximumSize(QSize(16777215, 30))
        self.SearchBar.setLineWrapMode(QTextEdit.NoWrap)
        self.SearchBar.setLineWrapColumnOrWidth(0)
        self.SearchBar.setReadOnly(False)
        self.SearchBar.setOverwriteMode(False)
        self.SearchBar.setTabStopDistance(10.000000000000000)
        self.SearchBar.setAcceptRichText(True)

        self.horizontalLayout_4.addWidget(self.SearchBar)

        self.SearchBarButton = QPushButton(self.AfterSignInPage)
        self.SearchBarButton.setObjectName(u"SearchBarButton")
        self.SearchBarButton.setMinimumSize(QSize(0, 10))
        self.SearchBarButton.setAutoDefault(False)

        self.horizontalLayout_4.addWidget(self.SearchBarButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.HomePageRightStackeddWidget = QStackedWidget(self.AfterSignInPage)
        self.HomePageRightStackeddWidget.setObjectName(u"HomePageRightStackeddWidget")
        self.HomeRightSide = QWidget()
        self.HomeRightSide.setObjectName(u"HomeRightSide")
        self.horizontalLayout_21 = QHBoxLayout(self.HomeRightSide)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.scrollArea_3 = QScrollArea(self.HomeRightSide)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, 0, 635, 368))
        self.horizontalLayout_9 = QHBoxLayout(self.scrollAreaWidgetContents_5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_2 = QFrame(self.scrollAreaWidgetContents_5)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setSizeConstraint(QLayout.SetMinimumSize)
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_6.addWidget(self.label_4)

        self.homepage_albums_scroll = QScrollArea(self.frame_2)
        self.homepage_albums_scroll.setObjectName(u"homepage_albums_scroll")
        self.sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.sizePolicy4.setHorizontalStretch(0)
        self.sizePolicy4.setVerticalStretch(0)
        self.sizePolicy4.setHeightForWidth(self.homepage_albums_scroll.sizePolicy().hasHeightForWidth())
        self.homepage_albums_scroll.setSizePolicy(self.sizePolicy4)
        self.homepage_albums_scroll.setMinimumSize(QSize(0, 140))
        self.homepage_albums_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.homepage_albums_scroll.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 595, 121))
        self.horizontalLayout_6 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.homepage_album = QVBoxLayout()
        self.homepage_album.setObjectName(u"homepage_album")
        self.homepage_album.setSizeConstraint(QLayout.SetMinimumSize)
        self.pushButton_8 = QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.sizePolicy2.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(self.sizePolicy2)
        self.pushButton_8.setMinimumSize(QSize(70, 70))
        self.pushButton_8.setMaximumSize(QSize(70, 70))
        icon = QIcon()
        icon.addFile(u"../../Users/\u05d9\u05d4\u05d5\u05e0\u05ea\u05df \u05d0\u05dc\u05e4\u05e1\u05d9/Downloads/264x264.jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon)
        self.pushButton_8.setIconSize(QSize(80, 80))

        self.homepage_album.addWidget(self.pushButton_8)

        self.label_23 = QLabel(self.scrollAreaWidgetContents)
        self.label_23.setObjectName(u"label_23")
        self.sizePolicy2.setHeightForWidth(self.label_23.sizePolicy().hasHeightForWidth())
        self.label_23.setSizePolicy(self.sizePolicy2)

        self.homepage_album.addWidget(self.label_23)


        self.horizontalLayout_6.addLayout(self.homepage_album)

        self.homepage_albums_scroll.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_6.addWidget(self.homepage_albums_scroll)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_6.addWidget(self.label_5)

        self.homepage_songs_scroll = QScrollArea(self.frame_2)
        self.homepage_songs_scroll.setObjectName(u"homepage_songs_scroll")
        self.sizePolicy4.setHeightForWidth(self.homepage_songs_scroll.sizePolicy().hasHeightForWidth())
        self.homepage_songs_scroll.setSizePolicy(self.sizePolicy4)
        self.homepage_songs_scroll.setMinimumSize(QSize(0, 140))
        self.homepage_songs_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.homepage_songs_scroll.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.homepage_songs_scroll.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 595, 121))
        self.horizontalLayout_5 = QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")

        self.homepage_songs_scroll.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_6.addWidget(self.homepage_songs_scroll)

        self.verticalLayout_6.setStretch(3, 1)

        self.horizontalLayout_9.addWidget(self.frame_2)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_5)

        self.horizontalLayout_21.addWidget(self.scrollArea_3)

        self.HomePageRightStackeddWidget.addWidget(self.HomeRightSide)
        self.SearchRightSide = QWidget()
        self.SearchRightSide.setObjectName(u"SearchRightSide")
        self.horizontalLayout_22 = QHBoxLayout(self.SearchRightSide)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.search_scroll = QScrollArea(self.SearchRightSide)
        self.search_scroll.setObjectName(u"search_scroll")
        self.search_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.search_scroll.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 635, 313))
        self.horizontalLayout_23 = QHBoxLayout(self.scrollAreaWidgetContents_3)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.search_song = QHBoxLayout()
        self.search_song.setObjectName(u"search_song")
        self.pushButton_29 = QPushButton(self.scrollAreaWidgetContents_3)
        self.pushButton_29.setObjectName(u"pushButton_29")
        self.sizePolicy2.setHeightForWidth(self.pushButton_29.sizePolicy().hasHeightForWidth())
        self.pushButton_29.setSizePolicy(self.sizePolicy2)
        self.pushButton_29.setMinimumSize(QSize(70, 70))
        self.pushButton_29.setMaximumSize(QSize(70, 70))
        self.pushButton_29.setIcon(icon)
        self.pushButton_29.setIconSize(QSize(80, 80))

        self.search_song.addWidget(self.pushButton_29)

        self.song1 = QLabel(self.scrollAreaWidgetContents_3)
        self.song1.setObjectName(u"song1")

        self.search_song.addWidget(self.song1)


        self.verticalLayout_30.addLayout(self.search_song)


        self.horizontalLayout_23.addLayout(self.verticalLayout_30)

        self.search_scroll.setWidget(self.scrollAreaWidgetContents_3)

        self.horizontalLayout_22.addWidget(self.search_scroll)

        self.HomePageRightStackeddWidget.addWidget(self.SearchRightSide)
        self.InsidePlaylistRightSide = QWidget()
        self.InsidePlaylistRightSide.setObjectName(u"InsidePlaylistRightSide")
        self.horizontalLayout_24 = QHBoxLayout(self.InsidePlaylistRightSide)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.InsidePlaylistMainVerticalLayout = QVBoxLayout()
        self.InsidePlaylistMainVerticalLayout.setObjectName(u"InsidePlaylistMainVerticalLayout")
        self.playlist_pics_and_titles_layout = QHBoxLayout()
        self.playlist_pics_and_titles_layout.setObjectName(u"playlist_pics_and_titles_layout")
        self.playlist_picture_label = QLabel(self.InsidePlaylistRightSide)
        self.playlist_picture_label.setObjectName(u"playlist_picture_label")
        self.sizePolicy2.setHeightForWidth(self.playlist_picture_label.sizePolicy().hasHeightForWidth())
        self.playlist_picture_label.setSizePolicy(self.sizePolicy2)
        self.playlist_picture_label.setMinimumSize(QSize(80, 80))
        self.playlist_picture_label.setMaximumSize(QSize(80, 80))
        self.playlist_picture_label.setPixmap(QPixmap(u"../../Users/\u05d9\u05d4\u05d5\u05e0\u05ea\u05df \u05d0\u05dc\u05e4\u05e1\u05d9/Downloads/264x264.jpg"))
        self.playlist_picture_label.setScaledContents(True)

        self.playlist_pics_and_titles_layout.addWidget(self.playlist_picture_label)

        self.playlist_title_label = QLabel(self.InsidePlaylistRightSide)
        self.playlist_title_label.setObjectName(u"playlist_title_label")

        self.playlist_pics_and_titles_layout.addWidget(self.playlist_title_label, 0, Qt.AlignVCenter)


        self.InsidePlaylistMainVerticalLayout.addLayout(self.playlist_pics_and_titles_layout)

        self.playlist_scroll = QScrollArea(self.InsidePlaylistRightSide)
        self.playlist_scroll.setObjectName(u"playlist_scroll")
        self.playlist_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.playlist_scroll.setWidgetResizable(True)
        self.scrollAreaWidgetContents_4 = QWidget()
        self.scrollAreaWidgetContents_4.setObjectName(u"scrollAreaWidgetContents_4")
        self.scrollAreaWidgetContents_4.setGeometry(QRect(0, 0, 633, 223))
        self.horizontalLayout_28 = QHBoxLayout(self.scrollAreaWidgetContents_4)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.playlist_song = QHBoxLayout()
        self.playlist_song.setObjectName(u"playlist_song")
        self.pushButton = QPushButton(self.scrollAreaWidgetContents_4)
        self.pushButton.setObjectName(u"pushButton")
        self.sizePolicy2.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(self.sizePolicy2)
        self.pushButton.setMinimumSize(QSize(70, 70))
        self.pushButton.setMaximumSize(QSize(70, 70))
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(80, 80))

        self.playlist_song.addWidget(self.pushButton)

        self.label_9 = QLabel(self.scrollAreaWidgetContents_4)
        self.label_9.setObjectName(u"label_9")

        self.playlist_song.addWidget(self.label_9)


        self.verticalLayout_28.addLayout(self.playlist_song)


        self.horizontalLayout_28.addLayout(self.verticalLayout_28)

        self.playlist_scroll.setWidget(self.scrollAreaWidgetContents_4)

        self.InsidePlaylistMainVerticalLayout.addWidget(self.playlist_scroll)


        self.horizontalLayout_24.addLayout(self.InsidePlaylistMainVerticalLayout)

        self.HomePageRightStackeddWidget.addWidget(self.InsidePlaylistRightSide)
        self.ProfilePage = QWidget()
        self.ProfilePage.setObjectName(u"page_5")
        self.horizontalLayout_25 = QHBoxLayout(self.ProfilePage)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.profile_my_profile_label = QLabel(self.ProfilePage)
        self.profile_my_profile_label.setObjectName(u"profile_my_profile_label")
        self.sizePolicy2.setHeightForWidth(self.profile_my_profile_label.sizePolicy().hasHeightForWidth())
        self.profile_my_profile_label.setSizePolicy(self.sizePolicy2)

        self.verticalLayout_4.addWidget(self.profile_my_profile_label)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.profile_picture_label = QLabel(self.ProfilePage)
        self.profile_picture_label.setObjectName(u"profile_picture_label")
        self.sizePolicy2.setHeightForWidth(self.profile_picture_label.sizePolicy().hasHeightForWidth())
        self.profile_picture_label.setSizePolicy(self.sizePolicy2)
        self.profile_picture_label.setMinimumSize(QSize(100, 100))
        self.profile_picture_label.setMaximumSize(QSize(100, 100))
        self.profile_picture_label.setPixmap(QPixmap(u"../../Users/\u05d9\u05d4\u05d5\u05e0\u05ea\u05df \u05d0\u05dc\u05e4\u05e1\u05d9/Downloads/146-1468479_my-profile-icon-blank-profile-picture-circle-hd.png"))
        self.profile_picture_label.setScaledContents(True)

        self.horizontalLayout_27.addWidget(self.profile_picture_label)

        self.profile_username_label = QLabel(self.ProfilePage)
        self.profile_username_label.setObjectName(u"profile_username_label")
        self.sizePolicy2.setHeightForWidth(self.profile_username_label.sizePolicy().hasHeightForWidth())
        self.profile_username_label.setSizePolicy(self.sizePolicy2)
        self.profile_username_label.setMinimumSize(QSize(500, 100))
        self.profile_username_label.setMaximumSize(QSize(16777215, 100))

        self.horizontalLayout_27.addWidget(self.profile_username_label)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_5)


        self.verticalLayout_4.addLayout(self.horizontalLayout_27)

        self.label_8 = QLabel(self.ProfilePage)
        self.label_8.setObjectName(u"label_8")
        self.sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        self.sizePolicy5.setHorizontalStretch(0)
        self.sizePolicy5.setVerticalStretch(0)
        self.sizePolicy5.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(self.sizePolicy5)

        self.verticalLayout_4.addWidget(self.label_8)

        self.profile_albums_scroll = QScrollArea(self.ProfilePage)
        self.profile_albums_scroll.setObjectName(u"profile_albums_scroll")
        self.profile_albums_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.profile_albums_scroll.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 633, 159))
        self.horizontalLayout_26 = QHBoxLayout(self.scrollAreaWidgetContents_7)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.scrollArea_4 = QScrollArea(self.scrollAreaWidgetContents_7)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 613, 139))
        self.horizontalLayout_41 = QHBoxLayout(self.scrollAreaWidgetContents_6)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.profile_song = QHBoxLayout()
        self.profile_song.setObjectName(u"profile_song")
        self.pushButton_7 = QPushButton(self.scrollAreaWidgetContents_6)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.sizePolicy2.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(self.sizePolicy2)
        self.pushButton_7.setMinimumSize(QSize(70, 70))
        self.pushButton_7.setMaximumSize(QSize(70, 70))
        self.pushButton_7.setIcon(icon)
        self.pushButton_7.setIconSize(QSize(80, 80))

        self.profile_song.addWidget(self.pushButton_7)

        self.label_33 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_33.setObjectName(u"label_33")

        self.profile_song.addWidget(self.label_33)


        self.verticalLayout_29.addLayout(self.profile_song)


        self.horizontalLayout_41.addLayout(self.verticalLayout_29)

        self.scrollArea_4.setWidget(self.scrollAreaWidgetContents_6)

        self.horizontalLayout_26.addWidget(self.scrollArea_4)

        self.profile_albums_scroll.setWidget(self.scrollAreaWidgetContents_7)

        self.verticalLayout_4.addWidget(self.profile_albums_scroll)


        self.horizontalLayout_25.addLayout(self.verticalLayout_4)

        self.HomePageRightStackeddWidget.addWidget(self.ProfilePage)

        self.verticalLayout_2.addWidget(self.HomePageRightStackeddWidget)

        self.create_player()

        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")

        self.verticalLayout_2.addLayout(self.verticalLayout_27)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalLayout.setStretch(1, 1)

        self.horizontalLayout_20.addLayout(self.horizontalLayout)

        self.MainStackWidget.addWidget(self.AfterSignInPage)
        self.SignInOrUpPage = QWidget()
        self.SignInOrUpPage.setObjectName(u"SignInOrUpPage")
        self.horizontalLayout_10 = QHBoxLayout(self.SignInOrUpPage)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.SignInOrLogInStackedWidget = QStackedWidget(self.SignInOrUpPage)
        self.SignInOrLogInStackedWidget.setObjectName(u"SignInOrLogInStackedWidget")
        self.SignIn = QWidget()
        self.SignIn.setObjectName(u"SignIn")
        self.horizontalLayout_11 = QHBoxLayout(self.SignIn)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.frame_3 = QFrame(self.SignIn)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_25.addItem(self.verticalSpacer_2)

        self.sign_in_label = QLabel(self.frame_3)
        self.sign_in_label.setObjectName(u"sign_in_label")

        self.verticalLayout_25.addWidget(self.sign_in_label)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.username_for_sign_in = QLineEdit(self.frame_3)
        self.username_for_sign_in.setObjectName(u"username_for_sign_in")
        self.sizePolicy2.setHeightForWidth(self.username_for_sign_in.sizePolicy().hasHeightForWidth())
        self.username_for_sign_in.setSizePolicy(self.sizePolicy2)
        self.username_for_sign_in.setMaximumSize(QSize(16777215, 30))
        self.username_for_sign_in.setReadOnly(False)

        self.horizontalLayout_15.addWidget(self.username_for_sign_in)


        self.verticalLayout_25.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.password_for_sign_in = QLineEdit(self.frame_3)
        self.password_for_sign_in.setObjectName(u"password_for_sign_in")
        self.sizePolicy2.setHeightForWidth(self.password_for_sign_in.sizePolicy().hasHeightForWidth())
        self.password_for_sign_in.setSizePolicy(self.sizePolicy2)
        self.password_for_sign_in.setMaximumSize(QSize(16777215, 30))
        self.password_for_sign_in.setReadOnly(False)

        self.horizontalLayout_14.addWidget(self.password_for_sign_in)


        self.verticalLayout_25.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.SwitchToSignUpButton = QPushButton(self.frame_3)
        self.SwitchToSignUpButton.setObjectName(u"SwitchToSignUpButton")

        self.horizontalLayout_16.addWidget(self.SwitchToSignUpButton)

        self.SignInButton = QPushButton(self.frame_3)
        self.SignInButton.setObjectName(u"SignInButton")

        self.horizontalLayout_16.addWidget(self.SignInButton)


        self.verticalLayout_25.addLayout(self.horizontalLayout_16)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_25.addItem(self.verticalSpacer)


        self.horizontalLayout_13.addLayout(self.verticalLayout_25)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_2)


        self.verticalLayout_24.addLayout(self.horizontalLayout_13)


        self.horizontalLayout_12.addLayout(self.verticalLayout_24)


        self.horizontalLayout_11.addWidget(self.frame_3)

        self.SignInOrLogInStackedWidget.addWidget(self.SignIn)
        self.SignUp = QWidget()
        self.SignUp.setObjectName(u"SignUp")
        self.horizontalLayout_18 = QHBoxLayout(self.SignUp)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_3)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacer_4)

        self.sign_up_label = QLabel(self.SignUp)
        self.sign_up_label.setObjectName(u"sign_up_label")

        self.verticalLayout_26.addWidget(self.sign_up_label, 0, Qt.AlignHCenter)

        self.email_for_sign_up = QLineEdit(self.SignUp)
        self.email_for_sign_up.setObjectName(u"email_for_sign_up")
        self.sizePolicy2.setHeightForWidth(self.email_for_sign_up.sizePolicy().hasHeightForWidth())
        self.email_for_sign_up.setSizePolicy(self.sizePolicy2)
        self.email_for_sign_up.setMaximumSize(QSize(16777215, 30))
        self.email_for_sign_up.setReadOnly(False)

        self.verticalLayout_26.addWidget(self.email_for_sign_up, 0, Qt.AlignHCenter)

        self.username_for_sign_up = QLineEdit(self.SignUp)
        self.username_for_sign_up.setObjectName(u"username_for_sign_up")
        self.sizePolicy2.setHeightForWidth(self.username_for_sign_up.sizePolicy().hasHeightForWidth())
        self.username_for_sign_up.setSizePolicy(self.sizePolicy2)
        self.username_for_sign_up.setMaximumSize(QSize(16777215, 30))
        self.username_for_sign_up.setReadOnly(False)

        self.verticalLayout_26.addWidget(self.username_for_sign_up, 0, Qt.AlignHCenter)

        self.password_for_sign_up = QLineEdit(self.SignUp)
        self.password_for_sign_up.setObjectName(u"password_for_sign_up")
        self.sizePolicy2.setHeightForWidth(self.password_for_sign_up.sizePolicy().hasHeightForWidth())
        self.password_for_sign_up.setSizePolicy(self.sizePolicy2)
        self.password_for_sign_up.setMaximumSize(QSize(16777215, 30))
        self.password_for_sign_up.setReadOnly(False)

        self.verticalLayout_26.addWidget(self.password_for_sign_up, 0, Qt.AlignHCenter)

        self.password_confiem_for_sign_up = QLineEdit(self.SignUp)
        self.password_confiem_for_sign_up.setObjectName(u"password_confiem_for_sign_up")
        self.sizePolicy2.setHeightForWidth(self.password_confiem_for_sign_up.sizePolicy().hasHeightForWidth())
        self.password_confiem_for_sign_up.setSizePolicy(self.sizePolicy2)
        self.password_confiem_for_sign_up.setMaximumSize(QSize(16777215, 30))
        self.password_confiem_for_sign_up.setReadOnly(False)

        self.verticalLayout_26.addWidget(self.password_confiem_for_sign_up, 0, Qt.AlignHCenter)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.SwitchToSignInButton = QPushButton(self.SignUp)
        self.SwitchToSignInButton.setObjectName(u"SwitchToSignInButton")

        self.horizontalLayout_19.addWidget(self.SwitchToSignInButton)

        self.SignUpButton = QPushButton(self.SignUp)
        self.SignUpButton.setObjectName(u"SignUpButton")
        self.SignUpButton.setAutoDefault(False)

        self.horizontalLayout_19.addWidget(self.SignUpButton)


        self.verticalLayout_26.addLayout(self.horizontalLayout_19)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacer_3)


        self.horizontalLayout_17.addLayout(self.verticalLayout_26)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_4)


        self.horizontalLayout_18.addLayout(self.horizontalLayout_17)

        self.SignInOrLogInStackedWidget.addWidget(self.SignUp)

        self.horizontalLayout_10.addWidget(self.SignInOrLogInStackedWidget)

        self.MainStackWidget.addWidget(self.SignInOrUpPage)

        self.verticalLayout.addWidget(self.MainStackWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 941, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.MainStackWidget.setCurrentIndex(0)
        self.HomePageRightStackeddWidget.setCurrentIndex(2)
        self.SignInOrLogInStackedWidget.setCurrentIndex(0)
        self.SignUpButton.setDefault(False)



        #self.mytest = self.add_record_to_homepage("longSoundExample", "TheGreatestHits.jpg", 15, 50)



        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.left_side_profile_pic_label.setText("")
        self.left_side_username_label.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.home_button.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.profile_button.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.log_out_button.setText(QCoreApplication.translate("MainWindow", u"Log Out", None))
        self.SearchBar.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search your favorites", None))
        self.SearchBarButton.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Albums", None))
        self.pushButton_8.setText("")
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Greatest Hits", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Songs", None))
        self.pushButton_29.setText("")
        self.song1.setText(QCoreApplication.translate("MainWindow", u"Song1", None))
        self.playlist_picture_label.setText("")
        self.playlist_title_label.setText(QCoreApplication.translate("MainWindow", u"Playlist Title", None))
        self.pushButton.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Song1", None))
        self.profile_my_profile_label.setText(QCoreApplication.translate("MainWindow", u"My Profile:", None))
        self.profile_picture_label.setText("")
        self.profile_username_label.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"My Playlists:", None))
        self.pushButton_7.setText("")
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Song1", None))
        self.player_picture.setText("")
        self.player_track_name.setText(QCoreApplication.translate("MainWindow", u"Playing: ...", None))
        self.player_track_likes.setText(QCoreApplication.translate("MainWindow", u"Likes:               ", None))
        self.player_track_listenings.setText(QCoreApplication.translate("MainWindow", u"Listenings:           ", None))
        self.PrevTrack.setText(QCoreApplication.translate("MainWindow", u"Previous", None))
        self.PausePlay.setText(QCoreApplication.translate("MainWindow", u"Pause/Play", None))
        self.NextTrack.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.LikeCurrentTrack.setText(QCoreApplication.translate("MainWindow", u"Like", None))
        self.sign_in_label.setText(QCoreApplication.translate("MainWindow", u"Please enter your username and password:", None))
        self.username_for_sign_in.setPlaceholderText(QCoreApplication.translate("MainWindow", u"MyUsername", None))
        self.password_for_sign_in.setPlaceholderText(QCoreApplication.translate("MainWindow", u"SecretPassword", None))
        self.SwitchToSignUpButton.setText(QCoreApplication.translate("MainWindow", u"Don't have an account yet?", None))
        self.SignInButton.setText(QCoreApplication.translate("MainWindow", u"Sign In", None))
        self.sign_up_label.setText(QCoreApplication.translate("MainWindow", u"Please enter a username, password and email adress\n"
"to create your account: ", None))
        self.email_for_sign_up.setPlaceholderText(QCoreApplication.translate("MainWindow", u"hello@gmail.com", None))
        self.username_for_sign_up.setPlaceholderText(QCoreApplication.translate("MainWindow", u"MyUsername", None))
        self.password_for_sign_up.setPlaceholderText(QCoreApplication.translate("MainWindow", u"SecretPassword", None))
        self.password_confiem_for_sign_up.setPlaceholderText(QCoreApplication.translate("MainWindow", u"ConfirmPassword", None))
        self.SwitchToSignInButton.setText(QCoreApplication.translate("MainWindow", u"Already have an account?", None))
        self.SignUpButton.setText(QCoreApplication.translate("MainWindow", u"Create Account", None))
        self.SignInButton.clicked.connect(self.sign_in)
        self.SwitchToSignUpButton.clicked.connect(self.switch_to_sign_up)

        # linking buttons in sign up window to functions
        self.SignUpButton.clicked.connect(self.sign_up)
        self.SwitchToSignInButton.clicked.connect(self.switch_to_sign_in)

        # linking left of main screen buttons to functions
        self.home_button.clicked.connect(self.go_to_home)
        self.profile_button.clicked.connect(self.go_to_profile)
        self.SearchBarButton.clicked.connect(self.go_to_search)
        self.pushButton_8.clicked.connect(self.go_to_playlist)
        self.log_out_button.clicked.connect(self.log_out)

        self.recommendation_songs = self.search(SONG_RECOMMENDATION_PROMPT)
        #self.recommenation_albums = self.search(SEARCH(ALBUM_RECOMMENDATIONS_PROMPT))
        self.widgets = []
        for song in self.recommendation_songs:
            self.widgets.append(self.add_record_to_homepage(song, self.horizontalLayout_5))
        #for album in self.recommenation_albums:
        #    self.widgets.append(self.add_record_to_homepage(album, self.homepage_album))




    # retranslateUi


    def search(self, prompt):
        self.send_queue.put(SEARCH(prompt))
        record_names = self.process_search_response(self.gui_msg_queue.get().decode())
        records_left = len(record_names)
        records = [None for i in range(len(record_names))]
        while records_left > 0:
            curr_msg = self.gui_msg_queue.get()
            curr_record = self.process_fetch_response(curr_msg, records_left)
            records[record_names.index(curr_record.name)] = curr_record
            records_left -= 1
        return records

    def process_search_response(self, msg):
        record_names = [record.split('\r\n')[1] for record in msg.split('#')[1:]]
        for record in record_names:
            self.send_queue.put(FETCH_RECORD(record))
        return record_names


    def process_fetch_response(self, msg, serial):
        split_msg = b''.join(msg.split(b'/')[2:]).split(b'&')
        first_three_fields = split_msg[:3]
        name, likes, listennings = [field.split(b'=')[1] for field in first_three_fields]
        picture_data = msg[msg.find(b'&picture=') + len(b'&picture='):]
        picture_path = RECORD_PIC_PATH(HOME_RECOMMENDATION_IDENTIFIER(serial))
        with open(picture_path, 'wb') as pic:
            pic.write(picture_data)
        return Record(name.decode(), picture_path, int(likes.decode()), int(listennings.decode()))


    def pause_or_play(self):
        self.scrollbar_playing_event.pause_or_play()
        self.player_playing_event.set()


    def change_time(self):
        val = self.scrollbar_val
        track_length, curr_time = self.scrollbar_playing_event.info
        self.scrollbar_playing_event.set((track_length, val / 1000 * track_length))
        track_length, curr_time, is_new_song = self.player_fetching_event.info
        self.player_fetching_event.set((track_length, val / 1000 * track_length, False))


    def holding_slider(self, val):
        self.scrollbar_val = val
        if not self.scrollbar_paused_event.isSet():
            self.scrollbar_playing_event.pause_or_play()


    def create_player(self):
        #main horizontal layout
        self.CurrentTrackMainHorizontalLayout = QHBoxLayout()
        self.CurrentTrackMainHorizontalLayout.setObjectName(u"CurrentTrackMainHorizontalLayout")

        #picture
        self.player_picture = QLabel(self.AfterSignInPage)
        self.player_picture.setObjectName(u"player_picture")
        self.sizePolicy2.setHeightForWidth(self.player_picture.sizePolicy().hasHeightForWidth())
        self.player_picture.setSizePolicy(self.sizePolicy2)
        self.player_picture.setMinimumSize(QSize(110, 112))
        self.player_picture.setMaximumSize(QSize(110, 112))
        self.player_picture.setPixmap(QPixmap(
            u"../../Users/\u05d9\u05d4\u05d5\u05e0\u05ea\u05df \u05d0\u05dc\u05e4\u05e1\u05d9/Downloads/264x264.jpg"))
        self.player_picture.setScaledContents(True)

        self.CurrentTrackMainHorizontalLayout.addWidget(self.player_picture)

        #right vertical layout
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.player_track_name = QLabel(self.AfterSignInPage)
        self.player_track_name.setObjectName(u"player_track_name")

        self.horizontalLayout_7.addWidget(self.player_track_name)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.player_track_likes = QLabel(self.AfterSignInPage)
        self.player_track_likes.setObjectName(u"player_track_likes")
        self.sizePolicy6 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        self.sizePolicy6.setHorizontalStretch(0)
        self.sizePolicy6.setVerticalStretch(0)
        self.sizePolicy6.setHeightForWidth(self.player_track_likes.sizePolicy().hasHeightForWidth())
        self.player_track_likes.setSizePolicy(self.sizePolicy6)

        self.verticalLayout_23.addWidget(self.player_track_likes)

        self.player_track_listenings = QLabel(self.AfterSignInPage)
        self.player_track_listenings.setObjectName(u"player_track_listenings")
        self.sizePolicy6.setHeightForWidth(self.player_track_listenings.sizePolicy().hasHeightForWidth())
        self.player_track_listenings.setSizePolicy(self.sizePolicy6)

        self.verticalLayout_23.addWidget(self.player_track_listenings)

        self.horizontalLayout_7.addLayout(self.verticalLayout_23)

        self.verticalLayout_5.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")

        self.verticalLayout_5.addLayout(self.horizontalLayout_8)


        #player_scrollbar
        self.player_scrollbar = QSlider(self.AfterSignInPage)
        self.player_scrollbar.setObjectName(u"player_scrollbar")
        self.player_scrollbar.setOrientation(Qt.Horizontal)
        self.player_scrollbar.setRange(0, 1000)
        self.player_scrollbar.sliderMoved.connect(self.holding_slider)
        self.player_scrollbar.sliderReleased.connect(self.change_time)

        self.verticalLayout_5.addWidget(self.player_scrollbar)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.PrevTrack = QPushButton(self.AfterSignInPage)
        self.PrevTrack.setObjectName(u"PrevTrack")

        self.horizontalLayout_3.addWidget(self.PrevTrack)

        self.PausePlay = QPushButton(self.AfterSignInPage)
        self.PausePlay.setObjectName(u"PausePlay")
        self.PausePlay.clicked.connect(self.pause_or_play)

        self.horizontalLayout_3.addWidget(self.PausePlay)

        self.NextTrack = QPushButton(self.AfterSignInPage)
        self.NextTrack.setObjectName(u"NextTrack")

        self.horizontalLayout_3.addWidget(self.NextTrack)

        self.LikeCurrentTrack = QPushButton(self.AfterSignInPage)
        self.LikeCurrentTrack.setObjectName(u"LikeCurrentTrack")
        self.sizePolicy2.setHeightForWidth(self.LikeCurrentTrack.sizePolicy().hasHeightForWidth())
        self.LikeCurrentTrack.setSizePolicy(self.sizePolicy2)
        self.LikeCurrentTrack.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_3.addWidget(self.LikeCurrentTrack)

        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.CurrentTrackMainHorizontalLayout.addLayout(self.verticalLayout_5)

        self.verticalLayout_2.addLayout(self.CurrentTrackMainHorizontalLayout)

    def go_to_page(self, n, m):
        '''
        (1,1) - Sign Up
        (1, 2) - Sign In
        (2, 1) - Homepage
        (2, 2) - Search Page
        (2, 3) - Profile Page
        (2, 4) - Playlist Page
        :param n:
        :param m:
        :return:
        '''
        if n == 1:
            self.MainStackWidget.setCurrentWidget(self.SignInOrUpPage)
            self.SignInOrLogInStackedWidget.setCurrentWidget(self.SignUp) if m == 1 else self.SignInOrLogInStackedWidget.setCurrentWidget(self.SignIn)
        else:
            self.MainStackWidget.setCurrentWidget(self.SignInOrUpPage)
            if m == 1:
                right_side = self.HomeRightSide
            elif m == 2:
                right_side = self.SearchRightSide
            elif m == 3:
                right_side = self.ProfilePage
            else:
                right_side = self.InsidePlaylistRightSide
            self.HomePageRightStackeddWidget.setCurrentWidget(right_side)


    def add_album_to_homepage(self):
        pass


    def request_song(self, song):
        self.expect_m3u8_and_url[0], self.expect_m3u8_and_url[1] = True, PRODUCE_SONG_PATH(song.name)
        self.send_queue.put(SEND_FOR_SONGS(song.name))
        self.player_fetching_event.set((None, 0, True))
        pixmap = QPixmap(song.picture_path)
        self.player_picture.setPixmap(pixmap)
        self.player_track_name.setText(song.name)
        self.player_track_likes.setText('likes: ' + str(song.likes))
        self.player_track_listenings.setText('listennings: ' + str(song.listennings))


    def add_record_to_homepage(self, record, main_layout):
        name, picture_path, likes, listennings = record.name, record.picture_path, record.likes, record.listennings
        layout = QVBoxLayout()
        layout.setObjectName(str.format(u"homepage_song_ser_{}", self.serial))

        #preparing button
        button = QPushButton(self.scrollAreaWidgetContents_2)
        button.setObjectName(name)
        self.sizePolicy2.setHeightForWidth(button.sizePolicy().hasHeightForWidth())
        button.setSizePolicy(self.sizePolicy2)
        button.setMinimumSize(QSize(70, 70))
        button.setMaximumSize(QSize(70, 70))
        button.clicked.connect(lambda: self.request_song(record))

        #song picture
        icon = QIcon()
        icon.addFile(picture_path)
        button.setIcon(icon)
        button.setIconSize(QSize(80, 80))
        button.setText("")

        layout.addWidget(button)

        #preparing label
        label = QLabel(self.scrollAreaWidgetContents_2)
        label.setObjectName(u"label")
        self.sizePolicy2.setHeightForWidth(label.sizePolicy().hasHeightForWidth())
        label.setSizePolicy(self.sizePolicy2)
        label.setText(QCoreApplication.translate("MainWindow", name, None))

        layout.addWidget(label)

        main_layout.addLayout(layout)

        widgets = [layout, button, label]

        return widgets


    def clear_homepage(self):
        pass


    def set_playlist_songs(self):
        pass


    def sign_in(self):
        self.send_queue.put(str.format(SIGN_IN, self.username_for_sign_in.text(), self.password_for_sign_in.text()))
        successful = self.log_in(self.username_for_sign_in.text())
        self.username_for_sign_in.clear()
        self.password_for_sign_in.clear()
        if not successful:
            self.sign_in_label.setText(SIGN_IN_LABEL_AFTER_FAIL)

    def sign_up(self):
        self.send_queue.put(str.format(SIGN_UP, self.username_for_sign_up.text(), self.password_for_sign_up.text(), self.email_for_sign_up.text()))
        successful = self.log_in(self.username_for_sign_up.text())
        self.username_for_sign_up.clear()
        self.password_for_sign_up.clear()
        self.password_confiem_for_sign_up.clear()
        self.email_for_sign_up.clear()
        if not successful:
            self.sign_up_label.setText(SIGN_UP_LABEL_AFTER_FAIL)


    def log_in(self, username):
        self.login_finished_event.clear()
        self.login_finished_event.wait()
        if self.login_approved[0]:
            self.main_go_to(self.AfterSignInPage)
            self.HomePageRightStackeddWidget.setCurrentWidget(self.HomeRightSide)
            self.left_side_username_label.setText(username)
        return self.login_approved[0]


    def switch_to_sign_in(self):
        self.SignInOrLogInStackedWidget.setCurrentWidget(self.SignIn)

    def switch_to_sign_up(self):
        self.SignInOrLogInStackedWidget.setCurrentWidget(self.SignUp)

    def go_to_home(self):
        self.HomePageRightStackeddWidget.setCurrentWidget(self.HomeRightSide)

    def go_to_search(self):
        self.HomePageRightStackeddWidget.setCurrentWidget(self.SearchRightSide)

    def go_to_playlist(self):
        self.HomePageRightStackeddWidget.setCurrentWidget(self.InsidePlaylistRightSide)

    def go_to_profile(self):
        self.HomePageRightStackeddWidget.setCurrentWidget(self.ProfilePage)

    def log_out(self):
        self.MainStackWidget.setCurrentWidget(self.SignInOrUpPage)


    def main_go_to(self, page):
        self.MainStackWidget.setCurrentWidget(page)


    def set_scrollbar_value(self, val):
        self.player_scrollbar.setValue(1000 * val)


    def start(self, send_queue, login_finished_event, login_approved, expect_m3u8_and_url, scrollbar_playing_event, player_playing_event, player_fetching_event, scrollbar_paused_event, gui_msg_queue):
        self.app = QApplication(sys.argv)
        self.MainWindow = QMainWindow()
        self.setupUi(self.MainWindow, send_queue, login_finished_event, login_approved, expect_m3u8_and_url, scrollbar_playing_event, player_playing_event, player_fetching_event, scrollbar_paused_event, gui_msg_queue)
        self.go_to_page(1, 2)
        self.MainWindow.show()
        sys.exit(self.app.exec())
