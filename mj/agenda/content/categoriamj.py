# -*- coding: utf-8 -*-
"""Definition of the MJ content type
"""

from zope.interface import implements
from AccessControl import ClassSecurityInfo
from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content.base import ATCTContent
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-
from mj.agenda import agendaMessageFactory as _

from mj.agenda.interfaces.interfaces import IMJCategoria
from mj.agenda.config import PROJECTNAME

MJCategoriaSchema = ATCTContent.schema.copy() + atapi.Schema((
    atapi.StringField(
        name='cor_categoria',
        required=False,
        searchable=True,
        default='#DFDFDF',
        widget=atapi.StringWidget(
            label=_(u"Cor da categoria"),
            description=_(u"Hexadecimal da cor"),
            size=7,)
    ),
))

MJCategoriaSchema['description'].widget.visible['edit'] = 'invisible'
schemata.finalizeATCTSchema(MJCategoriaSchema, moveDiscussion=False)


class MJCategoria(base.ATCTContent):
    """
    """
    #security = ClassSecurityInfo()
    implements(IMJCategoria)

    meta_type = "MJCategoria"
    portal_type = 'MJCategoria'
    schema = MJCategoriaSchema

    security = ClassSecurityInfo()

atapi.registerType(MJCategoria, PROJECTNAME)
