from __future__ import unicode_literals
import frappe
import frappe.defaults
from frappe.utils import nowdate, cstr, flt, cint, now ,getdate
from frappe import throw, _
from frappe.utils import formatdate, get_number_format_info
import requests
import json
import datetime

@frappe.whitelist()
def notify_delete(doc, event):
	check_doctype = ['example_doc']
	try:
		doc = doc.as_dict()
		del_data = doc.data.strip()
		recipients = "team@company.com"
		subject = "[Notification] Deleted document"
		msg = """
General info:

Deleted by: {user}
Date: {now}
Type of document: {doctype}
Doc. Name: {doc_name}

Document info:

{all_info}

""".format(user=doc.owner, now=now(), doctype=doc.deleted_doctype, doc_name=doc.deleted_name, all_info=del_data)
		frappe.sendmail(recipients=recipients, subject=subject,message=msg, now=True)

	except Exception as e:
		print(e)
		pass