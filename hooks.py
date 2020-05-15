# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "Notify Delete"
app_title = "Notify Delete"
app_publisher = "Marcos Vinicius Fernandes Machado"
app_description = "Monitor deleted documents"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = ""
app_license = "MIT"

## insert code below in your hook.py file ##
doc_events = {
	"Deleted Document": {
		"autoname": "notify.main.notify_delete"
	}
}