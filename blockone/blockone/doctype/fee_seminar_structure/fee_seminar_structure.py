# Copyright (c) 2022, Rowad ERP Team and contributors
# For license information, please see license.txt

# import frappe

import frappe
from frappe.model.document import Document
from frappe.model.mapper import get_mapped_doc

class FeeSeminarStructure(Document):
	def validate(self):
		self.calculate_total()

	def calculate_total(self):
		"""Calculates total amount."""
		self.total_amount = 0
		for d in self.components:
			self.total_amount += d.amount


# @frappe.whitelist()
# def make_fee_schedule(source_name, target_doc=None):
# 	return get_mapped_doc("Fee Seminar Structure", source_name, {
# 		"Fee Seminar Structure": {
# 			"doctype": "Fee Schedule", "validation": { "docstatus": ["=", 1],
# 			}
# 		},
#         	"Seminar Fee Component": {
# 			"doctype": "Fee Component"
# 		}
# 	}, target_doc)

