#!/usr/bin/env python
# -*- coding: latin-1 -*-
# (--> encoding for umlauts...)

# python -m pip install --upgrade pip wheel setuptools
# python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew
# python -m pip install kivy

# music from: https://freepd.com/music/?C=S;O=A	(license: CC0)


from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.core.audio import SoundLoader

class Musik(Widget):
		
	def play_working(self,):
		player = SoundLoader.load('Awkward Apocalyptic Pickup.mp3')
		player.play()

	def play_stall(self,):
		player = SoundLoader.load('Apex.mp3')
		player.play()
		
		
class MusikApp(App):	## loads musik.kv

	def build(self):
		g = GridLayout(cols = 1)
		g.add_widget(Button(text = "Apex (stalls)", on_release = Musik.play_stall))
		g.add_widget(Button(text = "Awkward (works)", on_release = Musik.play_working))
		return g
	
if __name__ == '__main__':
	MusikApp().run()