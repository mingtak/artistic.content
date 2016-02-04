# -*- coding: utf-8 -*-
from plone.indexer.decorator import indexer
from artistic.content import interfaces
from zope.interface import Interface


@indexer(Interface)
def classfication_indexer(obj):
    return obj.classfication

@indexer(Interface)
def serviceLevel_indexer(obj):
    return obj.serviceLevel

@indexer(Interface)
def expertise_indexer(obj):
    return obj.expertise

#@indexer(Interface)
#def city_indexer(obj):
#    return obj.city

@indexer(Interface)
def hrid_indexer(obj):
    return obj.hrid

@indexer(Interface)
def url_indexer(obj):
    return obj.url

@indexer(Interface)
def years_indexer(obj):
    return obj.years

@indexer(Interface)
def whoCanEditor_indexer(obj):
    return obj.whoCanEditor

@indexer(Interface)
def city_indexer(obj):
    return obj.city

@indexer(Interface)
def artClassfication_indexer(obj):
    return obj.artClassfication
