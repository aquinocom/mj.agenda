# -*- coding: utf-8 -*-
from StringIO import StringIO
from time import localtime

from plone.memoize import ram
from plone.memoize.compress import xhtml_compress
from plone.portlets.interfaces import IPortletDataProvider

from zope.i18nmessageid import MessageFactory
from zope.interface import implements
from zope.component import getMultiAdapter

from Acquisition import aq_inner
from DateTime import DateTime
from Products.CMFCore.utils import getToolByName
from Products.CMFPlone.utils import safe_unicode
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.PythonScripts.standard import url_quote_plus

from plone.app.portlets import PloneMessageFactory as _
from plone.app.portlets import cache
from plone.app.portlets.portlets import base

from plone.app.portlets.portlets.calendar import ICalendarPortlet
from plone.app.portlets.portlets.calendar import Assignment
from plone.app.portlets.portlets.calendar import Renderer
from plone.app.portlets.portlets.calendar import AddForm

PLMF = MessageFactory('plonelocales')


class ICalendarPortlet(ICalendarPortlet):
    """A portlet displaying a calendar
    """
    pass


class Assignment(Assignment):
    implements(ICalendarPortlet)

    title = _(u'Calendário Agenda')


class Renderer(Renderer):

    _template = ViewPageTemplateFile('calendar.pt')


class AddForm(AddForm):

    def create(self):
        return Assignment()
