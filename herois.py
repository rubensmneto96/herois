# -*- coding: utf-8 -*-

from OFS import SimpleItem
from Products.PageTemplates.PageTemplateFile import PageTemplateFile


class Herois(SimpleItem.SimpleItem):
    """Classe Heroi com suas configuracoes"""
    
    meta_type = "cadastro de Herois"
    
    manage_options = (
        {'label': 'View', 'action': 'index_html',},
        {'label': 'Properties', 'action': 'manage_editHerois',},
    )
    
    # Paginas
    index = PageTemplateFile('Main/index_html', globals())
    manage_editHerois = PageTemplateFile('Cadastro/edit', globals())
    manage_deleteHerois = PageTemplateFile('Cadastro/delete', globals())
    delSuccess = PageTemplateFile('Cadastro/deleteSuccess', globals())
    
    # Macros
    nav = PageTemplateFile('templates/nav', globals())
    foot = PageTemplateFile('templates/foot', globals())
    
    # CSS e Bootstrap
    style = PageTemplateFile('css/style.css', globals())
    
    
    
    def __init__(self, id, nome, idade, poder):
        """Inicializa Heroi"""
        self.id = id
        self.nome = nome
        self.idade = idade
        self.poder = poder 
    
    def index_html(self):
        """Redireciona para pagina index_html com informacoes do heroi"""
        return self.index()
    
    def manage_editAction(self, nome, idade, poder, RESPONSE=None):
        """Edita dados do Heroi"""
        self.nome = nome
        self.idade = idade
        self.poder = poder
        self._p_changed = 1
        RESPONSE.redirect('manage_editHerois')
        
    def manage_deleteAction(self, id='ID heroi', nome='Nome heroi', idade='Idade heroi', poder='Poder heroi'):
        """Deleta Herois"""
        self.id = id
        self.nome = nome
        self.idade = idade
        self.poder = poder
        page = PageTemplateFile
        del page, id, nome, idade, poder
        return self.delSuccess()


def manage_addHerois(self, id='ID heroi', nome="Nome heroi", idade="Idade heroi", poder="Poder heroi", RESPONSE=None):
    """Adiciona Herois em uma pasta"""
    self._setObject(id, Herois(id, nome, idade, poder))
    RESPONSE.redirect(id + '/index_html')
    
def cad(self):
    """Redireciona para cadastro de heroi"""
    return self.manage_addHeroisForm()


def delete(self):
    """Redireciona para pagina para deletar heroi"""
    return self.manage_deleteHerois()


manage_addHeroisForm = PageTemplateFile('Cadastro/cad', globals())


nav = PageTemplateFile('templates/nav', globals())
foot = PageTemplateFile('templates/foot', globals())