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
from zope.component import getMultiAdapter
from zope.traversing.browser import absoluteURL
from zope.app.component.hooks import getSite
from zope.app.component.interfaces import ISite
from z3c.breadcrumb.interfaces import IBreadcrumb


class LayoutPage(object):

    notRoot = False

    def update(self):
        context = self.context
        request = self.request

        self.portal_url = '%s/'%absoluteURL(context, request)

        self.context_title = getMultiAdapter(
            (self.maincontext, self.request), IBreadcrumb).name

        if not ISite.providedBy(self.maincontext):
            self.notRoot = True
            self.portal_title = getMultiAdapter(
                (getSite(), self.request), IBreadcrumb).name

        self.url = '%s/'%request.URL
        self.base_url = '%s/'%request.URL[-1]
