from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
#from zope.component import getMultiAdapter
from plone import api

#from Acquisition import aq_inner
#from zope.component import getUtility
#from zope.intid.interfaces import IIntIds
#from zope.security import checkPermission
#from zc.relation.interfaces import ICatalog


class Go_To_School_Term(BrowserView):
    """ Go_To_School_Term """

    def __call__(self):
        request = self.request
        response = request.response
        user = api.user.get_current()
        userId = user.getProperty('id')
        userPassword = user.getProperty('member_password')
        response.redirect('http://140.122.118.108/login_ex.php?username=%s&pwd=%s' % (userId, userPassword))
        return


class Go_To_Old_Admin(BrowserView):
    """ Go_To_Old_Admin """

    def __call__(self):
        request = self.request
        response = request.response
        user = api.user.get_current()
        userId = user.getProperty('id')
        userPassword = user.getProperty('member_password')
#        response.redirect('http://140.122.118.108/admin')
        response.redirect('http://140.122.118.108/admin/login_ex.php?username=%s&pwd=%s' % (userId, userPassword))
        return


class SchoolListingView(BrowserView):
    """ School listing view """


class SubprojectFolderView(BrowserView):
    """ subproject folder view """


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


class AlbumView(BrowserView):
    """ Album View (default)
    """

class Is_Anonymous(BrowserView):

    def __call__(self):
        return api.user.is_anonymous()


"""
class TEST(BrowserView):

    def __call__(self):
        context = self.context
        catalog = context.portal_catalog
        brain = catalog(Type='HrDb')
        for item in brain:
            itemObj = item.getObject()
            itemObj.reindexObject()
"""
