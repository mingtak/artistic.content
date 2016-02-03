# -*- coding: utf-8 -*-
# from Products.CMFPlone.utils import safe_unicode
from plone import api


def updatePassword(event):
    """ """
    portal = api.portal.get()
    request = portal.REQUEST
    try:
        if request.form.has_key('form.widgets.member_password'):
            user = api.user.get(username=event.context.member.getId())
            newPassword = request.form['form.widgets.member_password']
            user.setSecurityProfile(password=newPassword)
    except:pass


def setPassword(event):
    """ """
    portal = api.portal.get()
    request = portal.REQUEST
    try:
        if request.form.has_key('form.widgets.member_password'):
            user = api.user.get(username=event.object.getId())
            newPassword = request.form['form.widgets.member_password']
            user.setSecurityProfile(password=newPassword)
    except:pass


def moveContentToTop(item, event):
    """ Moves Item to the top of its folder """
    folder = item.getParentNode()
    if hasattr(folder, 'moveObjectsToTop'):
        folder.moveObjectsToTop(item.id)

