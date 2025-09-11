from odoo import fields, models

class BackpackItem(models.Model):
    _name = "backpack.item"
    _description = "Backpack Item"
    _rec_name = "xx_backpack_product_id"

    xx_backpack_order_id = fields.Many2one(
        comodel_name='backpack.backpack',
        string='Backpack Setup',
        required=True,
        ondelete='cascade',
        index=True,
        copy=False)
    sequence = fields.Integer(string="Sequence", default=10)
    xx_backpack_product_id = fields.Many2one("product.product", string="Item")
    xx_item_description = fields.Char(string="Description")
    xx_item_qty = fields.Integer(string="Qty", default=0)
    xx_item_weight = fields.Float(string="Weight", default=0)
    xx_item_weight_uom = fields.Many2one(
        'uom.uom',
        string="Weight Unit",
        domain="[('category_id.name', '=', 'Weight')]",
        default=lambda self: self.env.ref('uom.product_uom_kgm', raise_if_not_found=False)
    )
    #xx_item_description =
    #xx_item_total_weight =
    #xx_item_cost =
    #xx_is_item_packed = fields.Boolean
    #xx_is_item_used = fields.Boolean
    #xx_item_cat =

