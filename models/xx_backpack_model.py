from odoo import fields, models

class BackpackModel(models.Model):
    _name = "backpack.model"
    _description = "Backpack Model"
    _rec_name = "xx_model_name"


    xx_model_name = fields.Char(string="Model", required=True)
    xx_backpack_brand_id = fields.Many2one(
        comodel_name='backpack.brand',
        string='Brand',
        required=True,
        ondelete='cascade',
        index=True,
        copy=False)

    #xx_image_1920 = fields.Image(string="Image")
    xx_model_weight = fields.Float(string="Pack Weight", digits=(10, 2))
    xx_model_weight_uom = fields.Many2one(
        'uom.uom',
        string="Weight Unit",
        domain="[('category_id.name', '=', 'Weight')]",
        default=lambda self: self.env.ref('uom.product_uom_kgm', raise_if_not_found=False)
    )

    xx_model_volume = fields.Float(string="Pack Volume",  digits=(10, 2))
    xx_model_volume_uom = fields.Many2one(
        'uom.uom',
        string='Volume Unit',
        domain="[('category_id.name', '=', 'Volume')]",
        default=lambda self: self.env.ref('uom.product_uom_litre', raise_if_not_found=False)
    )

