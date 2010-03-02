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
from zope import interface, component
from zope.security.interfaces import IPrincipal
from zope.traversing.browser import absoluteURL
from zope.app.component.hooks import getSite

from zojax.statusmessage.interfaces import IStatusMessage
from zojax.authentication.interfaces import _, ISuccessLoginAction
from zojax.authentication.browser import defaultlogin


class LoginAction(defaultlogin.LoginAction):

    def update(self):
        super(LoginAction, self).update()
        self.loginURL = u'%s/modallogin.html'%absoluteURL(getSite(), self.request)
