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
from zope.app.component.hooks import getSite
from zope.traversing.browser import absoluteURL
from zope.app.container.interfaces import IReadContainer


class PageHeaders(object):

    faviconUrl = None
    names = ('favicon.ico', 'favicon.gif', 'favicon.png')

    def update(self):
        site = getSite()
        self.siteURL = '%s/'%absoluteURL(site, self.request)

        if IReadContainer.providedBy(site):
            for name in self.names:
                if name in site:
                    self.faviconUrl = '%s%s'%(self.siteURL, name)
                    break
