# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from artistic.content.testing import ARTISTIC_CONTENT_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that artistic.content is properly installed."""

    layer = ARTISTIC_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if artistic.content is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('artistic.content'))

    def test_browserlayer(self):
        """Test that IArtisticContentLayer is registered."""
        from artistic.content.interfaces import IArtisticContentLayer
        from plone.browserlayer import utils
        self.assertIn(IArtisticContentLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = ARTISTIC_CONTENT_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['artistic.content'])

    def test_product_uninstalled(self):
        """Test if artistic.content is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled('artistic.content'))

    def test_browserlayer_removed(self):
        """Test that IArtisticContentLayer is removed."""
        from artistic.content.interfaces import IArtisticContentLayer
        from plone.browserlayer import utils
        self.assertNotIn(IArtisticContentLayer, utils.registered_layers())
