# -*- coding: utf-8 -*-
"""Definition of the MJ content type
"""

from zope.interface import implements

from AccessControl import ClassSecurityInfo

from Products.Archetypes import atapi
from Products.Archetypes.utils import DisplayList
from Products.ATContentTypes.content.event import ATEventSchema
from Products.ATContentTypes.interfaces import IATEvent
from Products.ATContentTypes.interfaces import IATFolder
from Products.ATContentTypes.content.folder import ATFolder
from Products.ATContentTypes.content import schemata
from Products.ATContentTypes.lib.calendarsupport import CalendarSupportMixin
from Products.CMFCore.utils import getToolByName

# -*- Message Factory Imported Here -*-
from mj.agenda import agendaMessageFactory as _

from mj.agenda.interfaces.interfaces import IMJEvento
from mj.agenda.config import PROJECTNAME


MJEventoSchema = ATFolder.schema.copy() + ATEventSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-
    atapi.StringField(
        name='event_categoria',
        required=False,
        searchable=True,
        schemata='categorization',
        widget=atapi.SelectionWidget(
            label=_(u"Categoria do evento"),
            description=_(u"Selecione a categoria do evento"),
            format='select',),
        vocabulary='getCategoria',
    ),

))


schemata.finalizeATCTSchema(MJEventoSchema, moveDiscussion=False)


class MJEvento(ATFolder, CalendarSupportMixin):
    """
    """

    implements(IMJEvento, IATFolder, IATEvent)

    meta_type = "MJEvento"
    portal_type = 'MJEvento'
    schema = MJEventoSchema

    security = ClassSecurityInfo()

    def getCategoria(self):
        catalog = getToolByName(self, 'portal_catalog')
        categorias = catalog(portal_type='SimpleVocabularyTerm',
                             sort_on='id',
                             review_state='published')
        listCategorias = DisplayList()
        if categorias:
            listCategorias.add('', '')
            for i in categorias:
                categoria = i.Title
                id = i.id
                #cor = i.cor_categoria
                #listCategorias.add(cor, categoria)
                listCategorias.add(id, categoria)
        return listCategorias


atapi.registerType(MJEvento, PROJECTNAME)
