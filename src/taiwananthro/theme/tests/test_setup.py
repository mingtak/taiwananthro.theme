# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from taiwananthro.theme.testing import TAIWANANTHRO_THEME_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that taiwananthro.theme is properly installed."""

    layer = TAIWANANTHRO_THEME_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if taiwananthro.theme is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'taiwananthro.theme'))

    def test_browserlayer(self):
        """Test that ITaiwananthroThemeLayer is registered."""
        from taiwananthro.theme.interfaces import (
            ITaiwananthroThemeLayer)
        from plone.browserlayer import utils
        self.assertIn(ITaiwananthroThemeLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = TAIWANANTHRO_THEME_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['taiwananthro.theme'])

    def test_product_uninstalled(self):
        """Test if taiwananthro.theme is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'taiwananthro.theme'))

    def test_browserlayer_removed(self):
        """Test that ITaiwananthroThemeLayer is removed."""
        from taiwananthro.theme.interfaces import \
            ITaiwananthroThemeLayer
        from plone.browserlayer import utils
        self.assertNotIn(ITaiwananthroThemeLayer, utils.registered_layers())
