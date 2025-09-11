from odoo import fields, models

class Backpack(models.Model):
    _name = "backpack.backpack"
    _description = "Information about backpack"
    _rec_name = "xx_setup_name"

    #Backpack setup fields
    xx_setup_name = fields.Char(string="Backpack Setup Name", required=True)
    xx_backpack_owner = fields.Many2one(
        comodel_name="res.partner",
        string="Backpack Owner",
        index=True)
    #xx_pack_is_packed = fields.Boolean(string="Packed?", default=False)
    xx_period_used_from = fields.Datetime(string="Start of trip", copy=False)
    xx_period_used_till = fields.Datetime(string="End of trip", copy=False)
    #xx_setup_weight = xx_pack_weight + sum of xx_backpack_lines
    #xx_setup_content_weight = sum of xx_backpack_lines

    #Backpack fields
    xx_pack_brand = fields.Many2one('backpack.brand', string="Backpack Brand", copy=False)
    xx_pack_model = fields.Many2one('backpack.model', string="Backpack Model", copy=False, domain="[('xx_backpack_brand_id', '=', xx_pack_brand)]")
    #xx_model_image = fields.Image(
     #   related='xx_pack_model.xx_image_1920',
      #  string="Image",
     #   readonly=True)

    # Lines and line based computes
    xx_backpack_lines = fields.One2many(
        comodel_name='backpack.item',
        inverse_name='xx_backpack_order_id',
        string="Backpack Items",
        copy=True, auto_join=True)

