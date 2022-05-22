# Copyright (c) 2022, Rowad ERP Team and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Seminars(Document):
	pass

@frappe.whitelist()
def get_project_template_task(project_template):
		return frappe.get_all("Project Template Task",
			fields=["task", "subject", "docstatus"], filters={"parent":project_template}, order_by= "idx")
