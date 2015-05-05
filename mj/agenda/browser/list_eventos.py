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


# mj.agenda imports
from mj.agenda.interfaces.interfaces import IMJEvento


class ListEventosView(BrowserView):
    """ view 
    """

    @memoize
    def getRangeDate(self):
        data = self.request.get('date', None)
        try:
            #start_date = DateTime(date + ' 00:00:00')
            #end_date = DateTime(date + ' 23:59:59')
            start_date = DateTime(data + ' 00:00:00 UTC')
            end_date = DateTime(data + ' 23:59:59 UTC')
            return (start_date, end_date)
        except:
            #start_date = DateTime(DateTime().Date() + ' 00:00:00')
            #end_date = DateTime(DateTime().Date() + ' 23:59:59')
            start_date = DateTime(DateTime().Date() + ' 00:00:00 UTC')
            end_date = DateTime(DateTime().Date() + ' 23:59:59 UTC')
            return (start_date, end_date)

    @memoize
    def getEventos(self):
        """
        """
        range_date = self.getRangeDate()
        catalog = getToolByName(self, 'portal_catalog')
        path_eventos = '/'.join(self.context.getPhysicalPath())
        eventos = catalog(object_provides=IMJEvento.__identifier__,
                          start={'query': range_date, 'range': 'min:max'},
                          path=path_eventos,
                          sort_on='start',)
        return eventos

    def getDate(self):
        lt = getToolByName(self, 'portal_languages')
        idioma = lt.getDefaultLanguage()

        if idioma == 'pt-br':
            idioma = 'pt_BR'

        data = self.request.get('date', None)
        try:
            data = data.split('/')
            data = [int(i) for i in data]
            data = date(data[0], data[1], data[2])
        except:
            data = datetime.today()

        translation = getToolByName(self.context, 'translation_service')
        PLMF = MessageFactory('plonelocales')
        util = queryUtility(ITranslationDomain, 'plonelocales')

        isoweekday = data.isoweekday()
        if isoweekday == 7:
            isoweekday = 0

        weekdayName = PLMF(translation.day_msgid(isoweekday))
        weekday = util.translate(weekdayName, target_language=idioma)

        monthName = PLMF(translation.month_msgid(data.month))
        month = util.translate(monthName, target_language=idioma)

        return weekday + ', ' + str(data.day) + ' de ' +  month + ' de ' + str(data.year)

