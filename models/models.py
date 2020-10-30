from odoo import models, fields, api


class kingdoms(models.Model):
    _name = 'kingdoms.kingdoms'
    _description = 'REINOS'

    name = fields.Char()
    population = fields.Integer()
    gold = fields.Float(default=100.0)
    photo = fields.Image(max_width=200)
    kings = fields.Many2one('kingdoms.kings', ondelete='cascade')
    heros = fields.One2many('kingdoms.heros', 'kingdoms')


class kings(models.Model):
    _name = "kingdoms.kings"
    _description = 'REYES'

    name = fields.Char()
    race = fields.Selection([('1', 'Hombre'), ('2', 'Elf'), ('3', 'Enano'), ('4', 'Orc'), ('5', 'Dark Elf'), ('6',
                                                                                                              "Devil")])
    sex = fields.Selection([('1', 'M'), ('2', 'F')])
    level = fields.Integer()
    kingdoms = fields.One2many('kingdoms.kingdoms', 'kings')
    group_killers = fields.One2many('kingdoms.killers', 'kings')

class dungeons(models.Model):
    _name = "kingdoms.dungeons"
    _description = "MAZMORRAS"

    name = fields.Char()
    killers = fields.One2many('kingdoms.killers', 'dungeons')


class killers(models.Model):
    _name = "kingdoms.killers"
    _description = "ASESINOS"

    name = fields.Char()
    years = fields.Char()
    weapon = fields.Char()
    drug = fields.Integer()
    #hate = fields.Selection([('1','Strongh'('2',''))])
    dungeons = fields.Many2one('kingdoms.dungeons', 'killers')
    kings = fields.Many2one('kingdoms.kings', 'killers')

class heros(models.Model):
    _name = "kingdoms.heros"
    _description = "HEROES"

    name = fields.Char()
    years = fields.Char()
    level = fields.Integer()
    energy = fields.Integer()
    weapon_type = fields.Selection([('0','Knife'),('1','Sword')])
    luck = fields.Integer()
    kingdoms = fields.Many2one('kingdoms.kingdoms', 'heros')



