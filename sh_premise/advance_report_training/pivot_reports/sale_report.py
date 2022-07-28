from odoo import fields, models


class SaleReport(models.Model):
    _inherit = "sale.report"

    partner_state_id = fields.Many2one('res.country.state', 'Customer State', readonly=True)

    def _query(self, with_clause='', fields={}, groupby='', from_clause=''):
        fields['partner_state_id'] = ', partner.state_id as partner_state_id'
        groupby += ', partner_state_id'
        return super(SaleReport, self)._query(with_clause, fields, groupby, from_clause)
