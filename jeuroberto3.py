#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 14:43:37 2016

@author: georgesarsouze
"""
from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.behaviors import DragBehavior
from kivy.uix.scatter import Scatter


class Cache1(RelativeLayout):
    def on_touch_move(self,touch):
        tx,ty=touch.pos
        sx,sy=self.pos
        if sx<=tx<=sx+self.width and sy<=ty<=sy+self.width:
            print "dedans"
        return super(Cache1,self).on_touch_move(touch)
    pass
class Cache2(RelativeLayout):
    pass
class Cache3(RelativeLayout):
    pass
class Cache4(RelativeLayout):
    pass

class Interface(AnchorLayout):
    pass
    
class EspaceJeu(RelativeLayout):
    pass
class EspaceOutils(BoxLayout):
    pass

class JeuRoberto2App(App):
    def build(self):
        return Interface()
        
JeuRoberto2App().run()
