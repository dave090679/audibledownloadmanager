import appModuleHandler
import controlTypes
from NVDAObjects.UIA import UIA, ListItem
class audiblegroup(UIA):
	def _get_name(self):
		return self.firstChild.name
class audiblelistitem(ListItem):
	def _get_name(self):
		return self.firstChild.name

class AppModule(appModuleHandler.AppModule):
	def chooseNVDAObjectOverlayClasses(self, obj, clslist):
		if obj.role == controlTypes.ROLE_GROUPING:
			clslist.insert(0,audiblegroup)
		elif obj.role == controlTypes.ROLE_LISTITEM and obj.name == "":
			clslist.insert(0,audiblelistitem)
