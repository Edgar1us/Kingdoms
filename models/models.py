from odoo import models, fields, api


class kingdoms(models.Model):
    _name = 'kingdoms.kingdoms'
    _description = 'KINGDOMS'

    name = fields.Char()
    population = fields.Integer()
    gold = fields.Float(default=100.0)
    photo = fields.Image(max_width=200)
    technology = fields.Selection([('1', 'Hard'), ('2', 'Soft')])
    contamination = fields.Integer()
    temperature = fields.Integer()
    level = fields.Integer()
    material = fields.Float(default=0)
    kings = fields.Many2one('kingdoms.kings', ondelete='cascade')
    heros = fields.One2many('kingdoms.heros', 'kingdoms')


class kings(models.Model):
    _name = "kingdoms.kings"
    _description = 'KINGS'

    name = fields.Char()
    race = fields.Selection([('1', 'Man'), ('2', 'Elf'), ('3', 'Dwarf'), ('4', 'Orc'), ('5', 'Dark Elf'), ('6', 'Demon')])
    sex = fields.Selection([('1', 'M'), ('2', 'F')])
    age = fields.Integer()
    level = fields.Integer()
    kingdoms = fields.One2many('kingdoms.kingdoms', 'kings')
    group_killers = fields.One2many('kingdoms.killers', 'kings')


class book(models.Model):
    _name = 'book.kingdoms'
    _description = 'Holy books'

    name = fields.Char()
    serial = fields.Integer()
    price = fields.Float()
    registered = fields.Date()
    date = fields.Datetime()
    photo = fields.Image(max_width=200)
    edition = fields.Selection([('1', 'Standard'), ('2', 'Premium')])
    kings = fields.Many2one('books.kings', ondelete='cascade')
    group = fields.Many2many(comodel_name='books.kings',
                             relation='books_kings_group',
                             column1='books_id', column2='kings_id')


    @api.onchange()
    def _onchage_book(self):
        self.serial = self.serial * 5 * 1.5
        if self.serial < 0:
            return {
                'warning': {
                    'title': "Error, book",
                    'message': "This book can't be assigned"
                },
            }
        if self.serial > 0:
            return {
                'domain': {
                    {'kings': [('partner_id', '=', book.serial)]}
                }
            }


class dungeons(models.Model):
    _name = "kingdoms.dungeons"
    _description = "DUNGEONS"

    name = fields.Char()
    security_level = fields.Selection([('1', 'low'), ('2', 'Medium'), ('3', 'high')])


    killers = fields.One2many('kingdoms.killers', 'dungeons')

class points(models.Model):
    _name = 'kingdoms.points'

    date = fields.Datetime()
    points = fields.Integer()

    @api.model
    def update_points(self):
        global date

        points = self.env['kingdoms.points'].search([])
        if __name__ == '__main__':
            date = self.env['kingdoms.points']
        points._calculate_points()
        date._calculate_time()

class killers(models.Model):
    _name = "kingdoms.killers"
    _description = "KILLERS"

    name = fields.Char()
    years = fields.Char()
    weapon = fields.Char()
    drug = fields.Integer()
    weapon_type = fields.Selection([('0', 'Knife'), ('1', 'Sword'), ('2', 'Air'), ('3', 'Drill'), ('4', 'Bazooka'), ('5', 'Gun'), ('6', 'Hammer')])
    dungeons = fields.Many2one('kingdoms.dungeons', 'killers')
    kings = fields.Many2one('kingdoms.kings', 'killers')

class heros(models.Model):
    _name = "kingdoms.heros"
    _description = "HERO'S"

    name = fields.Char()
    years = fields.Char()
    level = fields.Integer()
    energy = fields.Integer()
    power = fields.Char()
    luck = fields.Integer()
    kingdoms = fields.Many2one('kingdoms.kingdoms', 'heros')



