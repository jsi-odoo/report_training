from odoo import _, api, models


class ReportPartnerLedger(models.AbstractModel):
    _inherit = "account.partner.ledger"

    @api.model
    def _get_query_amls(self, options, expanded_partner=None, offset=None, limit=None):
        query, where_params = super()._get_query_amls(options, expanded_partner, offset, limit)
        query = query.replace('AS partner_name,', 'AS partner_name, account_move_line__move_id.payment_reference    AS move_payment_ref,')
        return query, where_params

    def _get_columns_name(self, options):
        columns = super(ReportPartnerLedger, self)._get_columns_name(options)
        columns.append({'name': _('Payment Reference')})
        return columns

    @api.model
    def _get_report_line_move_line(self, options, partner, aml, cumulated_init_balance, cumulated_balance):
        res = super(ReportPartnerLedger, self)._get_report_line_move_line(options, partner, aml, cumulated_init_balance, cumulated_balance)
        res['columns'].append({'name': aml['move_payment_ref']})
        return res
