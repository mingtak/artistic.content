from plone.app.portlets.portlets import base
from plone.memoize.compress import xhtml_compress
from plone.memoize.instance import memoize
from plone.portlets.interfaces import IPortletDataProvider
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zope import schema
from zope.interface import implements
from artistic.content import _


class ISchoolSearch(IPortletDataProvider):

    text = schema.TextLine(
        title=_(u"Text"),
        required=True,
        )


class Assignment(base.Assignment):
    implements(ISchoolSearch)

    def __init__(self, text=''):
        self.text = text

    @property
    def title(self):
        return _(u"SchoolSearch")


class Renderer(base.Renderer):

    _template = ViewPageTemplateFile('school_search.pt')

    def __init__(self, *args):
        base.Renderer.__init__(self, *args)

    def render(self):
        return xhtml_compress(self._template())


class AddForm(base.AddForm):
    schema = ISchoolSearch
    label = _(u"Add School Search Portlet")
    description = _(u"This portlet rendering School Search.")

    def create(self, data):
        return Assignment(
            text=data.get('text', ''),
            )


class EditForm(base.EditForm):
    schema = ISchoolSearch
    label = _(u"Edit School Search Portlet")
    description = _(u"This portlet rendering SchoolSearch.")


