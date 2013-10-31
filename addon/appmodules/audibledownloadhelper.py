#appModules/audibledownloadhelper.py
#A part of NonVisual Desktop Access (NVDA)
#Copyright (C) 2006-2012 NVDA Contributors
#This file is covered by the GNU General Public License.
#See the file COPYING for more details.
import appModuleHandler
import api
import controlTypes
from NVDAObjects.IAccessible import IAccessible
class audibledownloadmanagerlistitem(IAccessible):
	def _get_name(self):
		if self.displayText:
			return(self.displayText)
class AppModule(appModuleHandler.AppModule):
	def chooseNVDAObjectOverlayClasses(self, obj, clsList):
		if obj.role == controlTypes.ROLE_LISTITEM:
			clsList.insert(0,audibledownloadmanagerlistitem)
