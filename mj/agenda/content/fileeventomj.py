# -*- coding: utf-8 -*-
"""Definition of the MJ content type
"""

from zope.interface import implements

from AccessControl import ClassSecurityInfo

from Products.Archetypes import atapi
from Products.ATContentTypes.content import schemata
from plone.app.blob.content import ATBlob
from plone.app.blob.interfaces import IATBlobFile
from Products.ATContentTypes.interfaces import IATFile, IFileContent
# -*- Message Factory Imported Here -*-
from mj.agenda import agendaMessageFactory as _
from mj.agenda.interfaces.interfaces import IMJFileEvento
from mj.agenda.config import PROJECTNAME


MJFileEventoSchema = ATBlob.schema.copy()

schemata.finalizeATCTSchema(MJFileEventoSchema, moveDiscussion=False)


class MJFileEvento(ATBlob):
    """
    """

    implements(IMJFileEvento, IATBlobFile, IATFile, IFileContent)

    meta_type = "MJFileEvento"
    portal_type = 'MJFileEvento'
    schema = MJFileEventoSchema

    security = ClassSecurityInfo()


atapi.registerType(MJFileEvento, PROJECTNAME)

