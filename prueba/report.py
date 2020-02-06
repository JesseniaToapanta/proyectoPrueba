from openerp import api, models

class ReportSession(models.AbstractModel):
    _name = "report.prueba.report_session"

    @api.multi
#    def render_html(self, data=None):
    def render_html(self, docids, data=None):
        report_obj = self.env["report"]
        report = report_obj._get_report_from_name("prueba.report_session")
        docargs = {
#           "doc_ids": self._ids,
           "doc_ids": docids,
           "doc_model": report.session,
#           "docs": self,
           "docs": self.env['prueba.session'].browse(docids),
           "other_variable": 'other_value'
        }
#       return report_obj.render("session.report_session", docargs)
        return report_obj.render("prueba.report_session_view", docargs)
