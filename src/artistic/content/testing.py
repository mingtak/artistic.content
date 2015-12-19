# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import artistic.content


class ArtisticContentLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=artistic.content)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'artistic.content:default')


ARTISTIC_CONTENT_FIXTURE = ArtisticContentLayer()


ARTISTIC_CONTENT_INTEGRATION_TESTING = IntegrationTesting(
    bases=(ARTISTIC_CONTENT_FIXTURE,),
    name='ArtisticContentLayer:IntegrationTesting'
)


ARTISTIC_CONTENT_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(ARTISTIC_CONTENT_FIXTURE,),
    name='ArtisticContentLayer:FunctionalTesting'
)


ARTISTIC_CONTENT_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        ARTISTIC_CONTENT_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='ArtisticContentLayer:AcceptanceTesting'
)
