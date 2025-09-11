from odoo import fields, models

class BackpackBrand(models.Model):
    _name = "backpack.brand"
    _description = "Backpack Brand"
    _rec_name = "xx_brand_name"

    xx_brand_name = fields.Char(string="Backpack Brand Name", required=True)
