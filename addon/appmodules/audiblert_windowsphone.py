import appModuleHandler
import controlTypes
from NVDAObjects.UIA import UIA, ListItem
import mouseHandler
import winUser

class audibleunlabeledcontrol (UIA):
	def _get_name(self):
		return self.firstChild.name
class audiblelistitem(ListItem):
	__gestures = {
		"kb:enter": "linksklick",
		"kb:numpadEnter": "linksklick",
		"kb:shift+f10": "rechtsklick",
		"kb:applications": "rechtsklick"
	}
	def script_linksklick(self, gesture):
		x = self.location.center.x
		y = self.location.center.y
		winUser.setCursorPos(x,y)
		mouseHandler.executeMouseMoveEvent(x,y)
		mouseHandler.executeMouseEvent(winUser.MOUSEEVENTF_LEFTDOWN,0,0)
		mouseHandler.executeMouseEvent(winUser.MOUSEEVENTF_LEFTUP,0,0)

	def script_rechtsklick(self, gesture):
		x = self.location.center.x
		y = self.location.center.y
		winUser.setCursorPos(x,y)
		mouseHandler.executeMouseMoveEvent(x,y)
		mouseHandler.executeMouseEvent(winUser.MOUSEEVENTF_RIGHTDOWN,0,0)
		mouseHandler.executeMouseEvent(winUser.MOUSEEVENTF_RIGHTUP,0,0)


	def _get_name(self):
		l = list()
		for x in self.children:
			s = x.name
			if s != "" and x.role == controlTypes.ROLE_STATICTEXT:
				l.append(s)
		return '; '.join(l)

class AppModule(appModuleHandler.AppModule):
	def chooseNVDAObjectOverlayClasses(self, obj, clslist):
		if obj.role == controlTypes.ROLE_GROUPING:
			clslist.insert(0,audibleunlabeledcontrol)
		elif obj.role == controlTypes.ROLE_BUTTON and obj.name == "":
			clslist.insert(0,audibleunlabeledcontrol)
		elif obj.role == controlTypes.ROLE_LISTITEM:
			clslist.insert(0,audiblelistitem)
