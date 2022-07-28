{
    'name': 'Report Customization Training',
    'version': '15.0.1.0',
    'description': u"""
        Sample module for
            - Inheriting Invoice report to add new fields
            - Creating new invoice report
            - Inheriting Financial report
""",
    'author': 'odoo-hk',
    'depends': [
        'account',
        "account_reports",
    ],
    'data': [

    # PDF REPORT
        # Invoice report inherited file
        'pdf_reports/report_invoice.xml',

        # New invoice report
        'pdf_reports/report_invoice_custom.xml',

        # New report action
        'pdf_reports/ir_actions_report.xml',


    # FINANCIAL REPORT
        "financial_reports/partner_ledger_report.xml",
    ],
    'application': False,
    'license': 'OPL-1',
}
