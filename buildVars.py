# -*- coding: UTF-8 -*-

# Build customizations
# Change this file instead of sconstruct or manifest files, whenever possible.

# Full getext (please don't change)
_ = lambda x : x

# Add-on information variables
addon_info = {
	# for previously unpublished addons, please follow the community guidelines at:
	# https://bitbucket.org/nvdaaddonteam/todo/raw/master/guideLines.txt
	# add-on Name, internal for nvda
	"addon-name" : "audibledownloadmanager",
	# Add-on summary, usually the user visible name of the addon.
	# Translators: Summary for this add-on to be shown on installation and add-on information.
	"addon-summary" : _("audible download manager"),
	# Add-on description
	# Translators: Long description to be shown for this add-on on add-on information from add-ons manager
	"addon-description" : _("""this add-on improves the accessibility of the audible download manager.
Instead of displaying the full paths of the .adh files in the downloads list, meta infos are displayed (such as the download status)."""),
	# version
	"addon-version" : "1.1",
	# Author(s)
	"addon-author" : u"David Parduhn <xkill85@gmx.net>",
	# URL for the add-on documentation support
	"addon-url" : None,
	"lastTestedNVDAVersion": "2019.3.0"
}


import os.path

# Define the python files that are the sources of your add-on.
# You can use glob expressions here, they will be expanded.
pythonSources = []

# Files that contain strings for translation. Usually your python sources
i18nSources = pythonSources + ["buildVars.py", "docHandler.py"]

# Files that will be ignored when building the nvda-addon file
# Paths are relative to the addon directory, not to the root directory of your addon sources.
excludedFiles = []
