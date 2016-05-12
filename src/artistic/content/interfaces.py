# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from artistic.content import _
from zope import schema
from plone.app.textfield import RichText
from plone.namedfile.field import NamedBlobImage
from plone.directives import form, dexterity
from zope.interface import Interface
from z3c.form.browser.checkbox import CheckBoxFieldWidget
from collective import dexteritytextindexer
from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from plone.formwidget.autocomplete import AutocompleteFieldWidget
from z3c.relationfield.schema import RelationList, RelationChoice
from zope.interface import Invalid

from config import HR_CLASSFICATION
from config import CITY
from config import CITY_WITHOUT_ALL
from config import SERVICE_LEVEL
from config import EXPERTISE
from config import PUBLIC_OR_PRIVATE
from config import ART_CLASSFICATION
from config import DEVICE_CLASSFICATION
from config import SETTABLE_YEARS


class IArtisticContentLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


def checkImage1_1(image):
    """Check Image width:height is 2:1
    """
    # 暫時先不對子計畫logo做檢查
    return True
    imageSize = image.getImageSize()
    if imageSize[0] == 2 * imageSize[1]:
        return True
    raise Invalid(_(u"Wrong! width:height must be 2:1."))


def checkCoverImage(image):
    """Check Image height:width is 1:1.8
    """
    imageSize = image.getImageSize()
    if imageSize[0] == 720 and imageSize[1] == 300:
        return True
    raise Invalid(_(u"Wrong! Image Size must be 720X300(W:H)"))


class ISubProject(Interface):

    dexteritytextindexer.searchable('title')
    title = schema.TextLine(
        title=_(u"Project Title"),
        required=True,
    )

    dexteritytextindexer.searchable('description')
    description = schema.Text(
        title=_(u"Description"),
        required=False,
    )

    image = NamedBlobImage(
        title=_(u"Sub Project Image"),
        description=_(u"width:height must be 1:1"),
        constraint=checkImage1_1,
        required=True,
    )

    url = schema.URI(
        title=_(u"Sub Project Website URL."),
        description=_(u"Must be include http:// or https://"),
        required=True,
    )


class ICover(Interface):

    title = schema.TextLine(
        title=_(u"Title"),
        required=True,
    )

    description = schema.Text(
        title=_(u"Description"),
        required=False,
    )

    slider1 = NamedBlobImage(
        title=_(u"Cover Slider 1"),
        description=_(u"Image Size must be 720X300(W:H)"),
        constraint=checkCoverImage,
        required=True,
    )

    slogan1 = schema.TextLine(
        title=_(u"Cover Slogan 1"),
        required=True,
    )

    url_1 = schema.URI(
        title=_(u"Url For Slider 1"),
        description=_(u"Must be include http:// or https://"),
        required=False,
    )

    slider2 = NamedBlobImage(
        title=_(u"Cover Slider 2"),
        description=_(u"Image Size must be 720X300(W:H)"),
        constraint=checkCoverImage,
        required=False,
    )

    slogan2 = schema.TextLine(
        title=_(u"Cover Slogan 2"),
        required=False,
    )

    url_2 = schema.URI(
        title=_(u"Url For Slider 2"),
        description=_(u"Must be include http:// or https://"),
        required=False,
    )

    slider3 = NamedBlobImage(
        title=_(u"Cover Slider 3"),
        description=_(u"Image Size must be 720X300(W:H)"),
        constraint=checkCoverImage,
        required=False,
    )

    slogan3 = schema.TextLine(
        title=_(u"Cover Slogan 3"),
        required=False,
    )

    url_3 = schema.URI(
        title=_(u"Url For Slider 3"),
        description=_(u"Must be include http:// or https://"),
        required=False,
    )

    slider4 = NamedBlobImage(
        title=_(u"Cover Slider 4"),
        description=_(u"Image Size must be 720X300(W:H)"),
        constraint=checkCoverImage,
        required=False,
    )

    slogan4 = schema.TextLine(
        title=_(u"Cover Slogan 4"),
        required=False,
    )

    url_4 = schema.URI(
        title=_(u"Url For Slider 4"),
        description=_(u"Must be include http:// or https://"),
        required=False,
    )

    slider5 = NamedBlobImage(
        title=_(u"Cover Slider 5"),
        description=_(u"Image Size must be 720X300(W:H)"),
        constraint=checkCoverImage,
        required=False,
    )

    slogan5 = schema.TextLine(
        title=_(u"Cover Slogan 5"),
        required=False,
    )

    url_5 = schema.URI(
        title=_(u"Url For Slider 5"),
        description=_(u"Must be include http:// or https://"),
        required=False,
    )


class IDeviceBudget(Interface):

    title = schema.TextLine(
        title=_(u"Device Name"),
        required=True,
    )

    years = schema.Choice(
        title=_(u"Years"),
        vocabulary=SETTABLE_YEARS,
        required=True,
    )

    deviceClassfication = schema.Choice(
        title=_(u"Device Classfication"),
        vocabulary=DEVICE_CLASSFICATION,
        required=True,
    )

    budget = schema.Int(
        title=_(u"Budget"),
        required=True,
    )


class ISchoolInfo(Interface):

    form.fieldset('Basic',
            label=_(u"Basic"),
            fields=['title',
                    'description',
                    'whoCanEditor',
                    'city',
                    'category_1',
                    'category_2'],
    )

    dexteritytextindexer.searchable('title')
    title = schema.TextLine(
        title=_(u"School Name"),
        required=True,
    )

    dexteritytextindexer.searchable('description')
    description = schema.Text(
        title=_(u"School short description"),
        required=True,
    )

    dexterity.write_permission(whoCanEditor='cmf.ManagePortal')
    whoCanEditor = schema.Choice(
        title=_(u"Assign Editor"),
        vocabulary=u"plone.principalsource.Users",
        required=True,
    )

    city = schema.Choice(
        title=_(u"City"),
        vocabulary=CITY_WITHOUT_ALL,
        required=True,
    )

    # 學校級別(國小 / 國中 / 高中)
    category_1 = schema.Choice(
        title=_(u"School Level"),
        vocabulary=SERVICE_LEVEL,
        required=True,
    )

    # 公私立
    category_2 = schema.Choice(
        title=_(u"Public or Private School"),
        vocabulary=PUBLIC_OR_PRIVATE,
        required=True,
    )

    form.fieldset('School Information',
            label=_(u"School Information"),
            fields=['artClassfication',
                    'schoolPhone',
                    'schoolFax',
                    'schoolAddress',
                    'schoolDist',
                    'schoolUrl',
                    'principalName',
                    'principalExt',
                    'manager_1',
                    'manager_1_ext',
                    'manager_2',
                    'manager_2_ext',
                    'manager_3',
                    'manager_3_ext',
                    'manager_4',
                    'manager_4_ext',],
    )

    # 藝才類別
    artClassfication = schema.Choice(
        title=_(u"Art Classfication"),
        vocabulary=ART_CLASSFICATION,
        required=True,
    )

    schoolPhone = schema.TextLine(
        title=_(u"School Phone Number"),
        required=False,
    )

    schoolFax = schema.TextLine(
        title=_(u"School Fax Number"),
        required=False,
    )

    schoolAddress = schema.TextLine(
        title=_(u"School Address"),
        required=False,
    )

    # 學校學區
    schoolDist = schema.TextLine(
        title=_(u"School District"),
        required=False,
    )

    schoolUrl = schema.URI(
        title=_(u"School URL"),
        description=_(u"Must include http:// or https://"),
        required=False,
    )

    principalName = schema.TextLine(
        title=_(u"Principal Name"),
        required=False,
    )

    principalExt = schema.TextLine(
        title=_(u"Principal Extension"),
        required=False,
    )

    manager_1 = schema.TextLine(
        title=_(u"Manager 1's Name"),
        required=False,
    )

    manager_1_ext = schema.TextLine(
        title=_(u"Manager 1's Extension"),
        required=False,
    )

    manager_2 = schema.TextLine(
        title=_(u"Manager 2's Name"),
        required=False,
    )

    manager_2_ext = schema.TextLine(
        title=_(u"Manager 2's Extension"),
        required=False,
    )
    manager_3 = schema.TextLine(
        title=_(u"Manager 3's Name"),
        required=False,
    )

    manager_3_ext = schema.TextLine(
        title=_(u"Manager 3's Extension"),
        required=False,
    )

    manager_4 = schema.TextLine(
        title=_(u"Manager 4's Name"),
        required=False,
    )

    manager_4_ext = schema.TextLine(
        title=_(u"Manager 4's Extension"),
        required=False,
    )

    form.fieldset('Classes Introduction',
            label=_(u"Classes Introduction"),
            fields=['text',
                    'imgFolderId',
                    'relatedImages',
                    'image_1',
                    'image_2',
                    'image_3',],
        )

    dexteritytextindexer.searchable('text')
    text = RichText(
        title=_(u"Introduction"),
        required=False,
    )

    dexterity.write_permission(imgFolderId='cmf.ManagePortal')
    dexterity.read_permission(imgFolderId='cmf.ManagePortal')
    imgFolderId = schema.TextLine(
        title=_(u"Old Image Folder id"),
        required=False,
    )

    dexterity.write_permission(relatedImages='cmf.ManagePortal')
    dexterity.read_permission(relatedImages='cmf.ManagePortal')
    relatedImages = RelationList(
        title=_(u"Related Images"),
        value_type=RelationChoice(
            title=_(u"Related Image"),
            vocabulary="plone.app.vocabularies.Catalog",
            required=False,
        )
    )

    image_1 = NamedBlobImage(
        title=_(u"Please upload an image"),
        description=_('Recommend that all use the same size photo'),
        required=False,
    )

    image_2 = NamedBlobImage(
        title=_(u"Please upload an image"),
        description=_('Recommend that all use the same size photo'),
        required=False,
    )

    image_3 = NamedBlobImage(
        title=_(u"Please upload an image"),
        description=_('Recommend that all use the same size photo'),
        required=False,
    )


class IHrDb(Interface):

    form.fieldset('Basic',
            label=_(u"Basic"),
            fields=['hrid', 'title', 'artisticOrg', 'serviceOrg', 'email'],
        )

    dexterity.write_permission(hrid='cmf.ManagePortal')
    dexterity.read_permission(hrid='cmf.ManagePortal')
    hrid = schema.Int(
        title=_(u"HR id"),
        required=False,
    )

    dexteritytextindexer.searchable('title')
    title = schema.TextLine(
        title=_(u"Name"),
        required=True,
    )

    artisticOrg = schema.TextLine(
        title=_(u"Artistic Organization"),
        required=False,
    )

    # 服務單位(校名)
    dexteritytextindexer.searchable('serviceOrg')
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
        required=True,
    )


class IAlbum(Interface):

    title = schema.TextLine(
        title=_(u"Title"),
        required=True,
    )

    description = schema.Text(
        title=_(u"Description"),
        required=False,
    )

