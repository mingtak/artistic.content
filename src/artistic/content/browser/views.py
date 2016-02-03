from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
#from zope.component import getMultiAdapter
from plone import api

#from Acquisition import aq_inner
#from zope.component import getUtility
#from zope.intid.interfaces import IIntIds
#from zope.security import checkPermission
#from zc.relation.interfaces import ICatalog


class HrdbSearchView(BrowserView):
    """ hrdb search view """


class HrdbResultView(BrowserView):
    """ hrdb result view """


class GetPortalType(BrowserView):

    def __call__(self):
        context = self.context
        return context.Type()


class GetPortalId(BrowserView):

    def __call__(self):
        portal = api.portal.get()
        return portal.getId()


class FolderNewsAndEvent(BrowserView):
    """ Folder News And Event View
    """


class ArtFolderView(BrowserView):
    """ Art Folder View
    """


class ArtFolderListingView(BrowserView):
    """ Art Folder Listing View
    """


class CoverView(BrowserView):
    """ Cover View (default)
    """


class SchoolInfoView(BrowserView):
    """ School Info View (default)
    """


class Is_Anonymous(BrowserView):

    def __call__(self):
        return api.user.is_anonymous()
