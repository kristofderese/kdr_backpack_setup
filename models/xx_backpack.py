from odoo import fields, models, api


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
    xx_setup_weight = fields.Float(
        string="Total Weight",
        compute='_compute_setup_weight',
        store=True)
    xx_setup_weight_uom = fields.Many2one(
        'uom.uom',
        string="Weight Unit",
        domain="[('category_id.name', '=', 'Weight')]",
        default=lambda self: self.env.ref('uom.product_uom_kgm', raise_if_not_found=False)
    )

    #Backpack fields
    xx_pack_brand = fields.Many2one('backpack.brand', string="Backpack Brand", copy=False)
    xx_pack_model = fields.Many2one('backpack.model', string="Backpack Model", copy=False, domain="[('xx_backpack_brand_id', '=', xx_pack_brand)]")
    xx_pack_weight = fields.Float(string="Backpack Weight", default=0)
    xx_setup_image = fields.Image(
        related='xx_pack_model.image_1920',
        string="Image",
        readonly=True,
        store=False)

    # Lines and line based computes
    xx_backpack_lines = fields.One2many(
        comodel_name='backpack.item',
        inverse_name='xx_backpack_order_id',
        string="Backpack Items",
        copy=True, auto_join=True)

    @api.depends('xx_backpack_lines.xx_item_weight', 'xx_backpack_lines.xx_item_weight_uom',
                 'xx_backpack_lines.xx_item_qty', 'xx_setup_weight_uom', 'xx_pack_weight',
                 'xx_pack_model.xx_model_weight', 'xx_pack_model.xx_model_weight_uom')
    def _compute_setup_weight(self):
        for record in self:
            total_weight = 0.0
            target_uom = record.xx_setup_weight_uom

            if not target_uom:
                record.xx_setup_weight = 0.0
                continue

            # Add backpack weight (use xx_pack_weight field, not model weight)
            if record.xx_pack_weight:
                # Assuming xx_pack_weight is in the same UoM as xx_setup_weight_uom
                # You might need UoM conversion here too if they can be different
                total_weight += record.xx_pack_weight

            # Add items weight
            for line in record.xx_backpack_lines:
                if line.xx_item_weight and line.xx_item_weight_uom:
                    item_total_weight = line.xx_item_weight * (line.xx_item_qty or 1)
                    source_uom = line.xx_item_weight_uom

                    if source_uom.category_id == target_uom.category_id:
                        converted_weight = source_uom._compute_quantity(
                            item_total_weight, target_uom, round=False)
                        total_weight += converted_weight

            record.xx_setup_weight = total_weight

    @api.onchange('xx_setup_weight_uom')
    def _onchange_setup_weight_uom(self):
        # Trigger recomputation when UoM changes
        self._compute_setup_weight()

    @api.onchange('xx_pack_model')
    def _onchange_pack_weight(self):
        if self.xx_pack_model and self.xx_pack_model.xx_model_weight:
            self.xx_pack_weight = self.xx_pack_model.xx_model_weight
        else:
            self.xx_pack_weight = 0.0