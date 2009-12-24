##############################################################################
#
# Copyright (c) 2009 Zope Foundation and Contributors.
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
from zope.component import \
    getAdapters, getMultiAdapter, queryMultiAdapter
from zope.app.component.hooks import getSite
from zope.traversing.browser import absoluteURL
from z3c.breadcrumb.interfaces import IBreadcrumb
from zojax.layout.interfaces import ILayout
from zojax.content.draft.interfaces import IDraftedContent
from zojax.content.space.interfaces import \
    IContentSpace, IWorkspace, IWorkspaceFactory


class PortalHeader(object):

    def update(self):
        super(PortalHeader, self).update()

        wsname = u''
        ws = None

        if ILayout.providedBy(self.view):
            space = self.view.maincontext
        else:
            space = self.view

        while not IContentSpace.providedBy(space) \
                or IDraftedContent.providedBy(space):
            if IWorkspace.providedBy(space):
                ws = space
                wsname = space.__name__
            space = space.__parent__

        self.space = space
        self.workspace = ws

        request = self.request
        url = absoluteURL(space, request)

        selected = False
        workspaces = []
        for name, factory in getAdapters((space,), IWorkspaceFactory):
            if name not in space.enabledWorkspaces:
                continue
            if not space.isEnabled(factory):
                continue

            if name == wsname:
                selected = True

            workspaces.append(
                (factory.weight, factory.title,
                 {'name': name,
                  'url': '%s/%s/'%(url, name),
                  'title': factory.title,
                  'description': factory.description,
                  'selected': name == wsname,
                  'icon': queryMultiAdapter((factory, request), name='zmi_icon'),
                  }))

        if not selected:
            self.siteSelected = True
        else:
            self.siteSelected = False

        self.siteUrl = '%s/'%absoluteURL(getSite(), request)

        workspaces.sort()
        self.workspaces = [info for _w, _t, info in workspaces]

        self.portal_title = getMultiAdapter((getSite(), request), IBreadcrumb).name
