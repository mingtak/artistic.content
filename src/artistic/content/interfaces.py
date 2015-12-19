# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from artistic.content import _
from zope import schema
from plone.directives import form
from zope.interface import Interface
from z3c.form.browser.checkbox import CheckBoxFieldWidget
from config import  HR_CLASSFICATION, CITY, SERVICE_LEVEL, EXPERTISE
from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class IArtisticContentLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IHrDb(Interface):

    form.fieldset('Basic',
            label=_(u"Basic"),
            fields=['title', 'artisticOrg', 'serviceOrg', 'email'],
        )

    title = schema.TextLine(
        title=_(u"Name"),
        required=True,
    )

    artisticOrg = schema.TextLine(
        title=_(u"Artistic Organization"),
        required=False,
    )

    serviceOrg = schema.TextLine(
        title=_(u"Service Organization"),
        required=False,
    )

    email = schema.TextLine(
        title=_(u"Email Address"),
        required=False,
    )

    form.fieldset('category',
            label=_(u"Category information"),
            fields=['classfication', 'serviceLevel', 'expertise'],
        )

#    form.widget(classfication=CheckBoxFieldWidget)
    classfication = schema.Choice(
        title=_(u"HR Classfication"),
        vocabulary=HR_CLASSFICATION,
        required=True,
    )

    form.widget(serviceLevel=CheckBoxFieldWidget)
    serviceLevel = schema.List(
        title=_(u"Service Level"),
        value_type=schema.Choice(
            vocabulary=SERVICE_LEVEL),
        required=False,
        default=None,
    )

    form.widget(expertise=CheckBoxFieldWidget)
    expertise = schema.List(
        title=_(u"Experitse"),
        value_type=schema.Choice(
            vocabulary=EXPERTISE),
        required=False,
    )

    form.fieldset('cities',
            label=_(u"Service Cities"),
            fields=['city'],
        )

    form.widget(city=CheckBoxFieldWidget)
    city = schema.List(
        title=_(u"City"),
        value_type=schema.Choice(
            vocabulary=CITY),
        default=[u"All Cities"],
        required=True,
    )

