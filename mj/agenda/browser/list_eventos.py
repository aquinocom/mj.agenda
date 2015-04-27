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
     	return DateTime().strftime('%A, %d de %B de %Y')
