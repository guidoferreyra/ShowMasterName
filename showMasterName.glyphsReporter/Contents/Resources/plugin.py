# encoding: utf-8

###########################################################################################################
#
#
#	Reporter Plugin
#
#	Read the docs:
#	https://github.com/schriftgestalt/GlyphsSDK/tree/master/Python%20Templates/Reporter
#
#
###########################################################################################################


from __future__ import division, print_function, unicode_literals
import objc
from GlyphsApp import *
from GlyphsApp.plugins import *

class showMasterName(ReporterPlugin):

	@objc.python_method
	def settings(self):
		self.menuName = Glyphs.localize({
			'en': 'Master Name',
		})

	@objc.python_method
	def foregroundInViewCoords(self):
		font = Glyphs.font
		currentTab = font.currentTab
		# masterID = layer.associatedMasterId
		thisMaster = font.selectedFontMaster
		fontSize = 20

		masterValues = []
		masterValues.append(thisMaster.name)
		for i, value in enumerate(thisMaster.axes):
			masterValues.append("%s: %d" % (font.axes[i].axisTag, value))
		
		x = currentTab.viewPort.origin.x + 10
		y = currentTab.viewPort.origin.y + font.currentTab.viewPort.size.height - (fontSize*1.4) * ( len(masterValues))
		
		text = "\n".join(masterValues)
		pos = NSPoint(x, y)
		
		self.drawTextAtPoint(text, pos, fontSize * currentTab.scale)
	

	@objc.python_method
	def __file__(self):
		"""Please leave this method unchanged"""
		return __file__
