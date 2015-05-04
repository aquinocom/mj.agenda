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
import datetime
from zope.i18nmessageid import MessageFactory
from zope.component import queryUtility
from zope.i18n.interfaces import ITranslationDomain
from mj.agenda import agendaMessageFactory as _
#Libs imports


# mj.agenda imports
from mj.agenda.interfaces.interfaces import IMJEvento



class ListEventosView(BrowserView):
    """ view 
    """

    @memoize
    def getEventos(self):
        """
        """
        catalog = getToolByName(self, 'portal_catalog')
        path_eventos = '/'.join(self.context.getPhysicalPath())
        eventos = catalog(object_provides=IMJEvento.__identifier__,
                           path=path_eventos,
                           sort_on='start',)
        return eventos

    def getDate(self):
        lt = getToolByName(self, 'portal_languages')
        idioma = lt.getDefaultLanguage()

        if idioma == 'pt-br':
            idioma = 'pt_BR'

        data = datetime.datetime.today()

        translation = getToolByName(self.context, 'translation_service')
        PLMF = MessageFactory('plonelocales')
        util = queryUtility(ITranslationDomain, 'plonelocales')

        weekdayName = PLMF(translation.day_msgid(data.isoweekday()))
        weekday = util.translate(weekdayName, target_language=idioma)

        monthName = PLMF(translation.month_msgid(data.month))
        month = util.translate(monthName, target_language=idioma)

        return weekday + ', ' + str(data.day) + ' de ' +  month + ' de ' + str(data.year)

