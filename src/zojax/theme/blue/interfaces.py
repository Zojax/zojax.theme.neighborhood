##############################################################################
#
# Copyright (c) 2008 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""

$Id$
"""
from zope import interface
from zope.i18nmessageid import MessageFactory
from zojax.pageelement.interfaces import IPageElement
from zojax.layoutform.interfaces import ILayoutFormLayer

from zojax.theme.default.interfaces import ICommonSkinLayer

_ = MessageFactory('zojax.theme.blue')


class ISkinLayer(interface.Interface):
    """ blue layer """


class IBlueSkin(ISkinLayer, ICommonSkinLayer):
    """ Blue skin """


class IPageHeaders(IPageElement):
    """ page headers """
