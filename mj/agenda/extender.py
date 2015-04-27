# -*- coding: utf-8 -*-
from Products.Archetypes.public import StringField
from Products.Archetypes.public import StringWidget
from archetypes.schemaextender.field import ExtensionField
from archetypes.schemaextender.interfaces import ISchemaExtender
from zope.interface import implements
from mj.agenda import agendaMessageFactory as _


class MJStringField(ExtensionField, StringField):
    """ Um campo string simples """


class VocabularioExtender(object):
    implements(ISchemaExtender)

    fields = [
        MJStringField("corCategoria",
                      required=True,
                      searchable=False,
                      widget=StringWidget(label=_(u"Cor da etiqueta"),
                                          helper_js=('++resource++color.js',),),
                      ),
        ]

    def __init__(self, context):
        self.context = context

    def getFields(self):
        portal_type = getattr(self.context, 'portal_type', None)
        if portal_type == 'TreeVocabularyTerm':
            return self.fields
        else:
            return []
