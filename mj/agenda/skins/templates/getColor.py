## Script (Python) "getReferencias"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##title=Lista as Referencias
##parameters=id

from Products.CMFPlone.utils import getToolByName
catalog = getToolByName(context, 'portal_catalog')
categorias = catalog(portal_type='SimpleVocabularyTerm',
                     id=id,)
if categorias:
    cor = '#' + categorias[0].cor_categoria
    return cor
else:
    return 'transparent'
