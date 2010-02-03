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
from zope.component import queryMultiAdapter
from zope.contentprovider.interfaces import IContentProvider

from zojax.extensions.interfaces import IExtensible

from zojax.cache.view import cache
from zojax.cache.keys import ContextModified
from zojax.cache.timekey import TimeKey, each15minutes

from interfaces import IPortletable


class PortalHeader(object):
    
    headerContext = None

    def update(self):
        context = self.context
        request = self.request

        while context is not None and (not IPortletable.providedBy(context)):
            context = context.__parent__
        self.headerContext = context
        self.hasAdvTop = queryMultiAdapter((context, request, self), IContentProvider, name='columns.advtop')
        if self.hasAdvTop is not None:
            self.hasAdvTop = elf.hasAdvTop.updateAndRender()