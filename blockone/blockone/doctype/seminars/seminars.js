// Copyright (c) 2022, Rowad ERP Team and contributors
// For license information, please see license.txt

frappe.ui.form.on('Seminars', {
		project_template: function(frm) {
		if (frm.doc.project_template) {
			frappe.call({
				method: 'blockone.api.get_project_template_tasks',
				args: {
					project_template: frm.doc.project_template
				},
				callback: function(r) {
					if (r.message) {
						frappe.model.clear_table(frm.doc, 'tasks');
						$.each(r.message, function(i, d) {
							var row = frm.add_child('tasks');
							row.task = d.task;
							row.subject = d.subject;
							row.is_group = d.is_group;
							row.parent_task = d.parent_task;
						});
						frm.refresh_field('tasks');
					}
				}
			});
		}
	},
});

