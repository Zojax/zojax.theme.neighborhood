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

_ = MessageFactory('zojax.theme.inove')


class ILayer(interface.Interface):
    """ inove layer """


class INoveSkin(ILayer, ILayoutFormLayer):
    """ iNove skin """


class IPageHeaders(IPageElement):
    """ page headers """
