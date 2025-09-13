import logging
from odoo import models, fields, api

_logger = logging.getLogger(__name__)

class BackpackModel(models.Model):
    _name = "backpack.model"
    _description = "Backpack Model"
    _rec_name = "xx_model_name"

    def write(self, vals):
        _logger.info("BEFORE WRITE - image_1920: %s", bool(self.image_1920))
        _logger.info("WRITE VALS: %s", vals.keys())
        result = super().write(vals)
        _logger.info("AFTER WRITE - image_1920: %s", bool(self.image_1920))
        return result

    image_1920 = fields.Image(string="Image", max_width=1920, max_height=1920)
    image_1024 = fields.Image("Image 1024", related="image_1920", max_width=1024, max_height=1024)
    image_512 = fields.Image("Image 512", related="image_1920", max_width=512, max_height=512)
    image_256 = fields.Image("Image 256", related="image_1920", max_width=256, max_height=256)
    image_128 = fields.Image("Image 128", related="image_1920", max_width=128, max_height=128)

    xx_model_name = fields.Char(string="Model", required=True)
    xx_backpack_brand_id = fields.Many2one(
        comodel_name='backpack.brand',
        string='Brand',
        required=True,
        ondelete='cascade',
        index=True,
        copy=False)


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

