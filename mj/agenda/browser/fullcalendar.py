# -*- coding: utf-8 -*-

# Zope3 imports
from zope.component import getUtility
from Acquisition import aq_inner

# Product imports
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.CMFCore.utils import getToolByName

#Plone imports
from plone.memoize.instance import memoize
from plone.registry.interfaces import IRegistry
from DateTime import DateTime
from datetime import datetime, date, time
from zope.i18nmessageid import MessageFactory
from zope.component import queryUtility
from zope.i18n.interfaces import ITranslationDomain
from mj.agenda import agendaMessageFactory as _
#Libs imports
import simplejson as json
from zope.component import getMultiAdapter
# mj.agenda imports
from mj.agenda.interfaces.interfaces import IMJEvento


class FullCalendarView(BrowserView):
    """ view 
    """


class JSONFullCalendarView(BrowserView):
    """ view 
    """
    @memoize
    def __call__(self):
        self.request.response.setHeader('Content-Type', 'application/json; charset=utf-8')
        catalog = getToolByName(self, 'portal_catalog')
        path_eventos = '/'.join(self.context.getPhysicalPath())
        eventos = catalog(object_provides=IMJEvento.__identifier__,
                          path=path_eventos,
                          sort_on='start',)
        result = []
        if eventos:
            for i in eventos:
                titulo = i.Title
                start = i.start.strftime('%Y-%m-%dT%H:%M:%S')
                end = i.end.strftime('%Y-%m-%dT%H:%M:%S')
                tipo_evento = i.event_categoria
                url = i.getURL()
                if tipo_evento:
                    categorias = catalog(portal_type='SimpleVocabularyTerm', id=tipo_evento,)
                    if categorias:
                        categoria = categorias[0]
                        color = '#' + categoria.cor_categoria
                        result.append({'title': titulo, 'start': start, 'end': end, 'color': color, 'url': url})
                else:
                    result.append({'title': titulo, 'start': start, 'end': end, 'url': url})
        return json.dumps(result)
