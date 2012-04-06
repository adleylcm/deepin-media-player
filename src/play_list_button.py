#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2012 Deepin, Inc.
#               2012 Hailong Qiu
#
# Author:     Hailong Qiu <356752238@qq.com>
# Maintainer: Hailong Qiu <356752238@qq.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


from dtk.ui.frame import *

from utils import *
from ImageButton import *

class PlayListButton(object):
    def __init__(self):
        self.show_play_list_bool = True
        self.hframe = HorizontalFrame(padding = 14)
        self.button = ImageButton(app_theme.get_pixbuf("big_button_background.png"),
                                  app_theme.get_pixbuf("play_list_button.png"))
        self.button.connect("clicked", self.show_play_list)
        self.hframe.add(self.button)
        
    def show_play_list(self, widget):    
        if self.show_play_list_bool:
            media_player["playlist"].hide_playlist()    
        else:    
            media_player["playlist"].show_playlist()
            
        self.show_play_list_bool = not self.show_play_list_bool    
        print self.show_play_list_bool