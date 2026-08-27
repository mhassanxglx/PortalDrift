# test_portaldrift.py
"""
Tests for PortalDrift module.
"""

import unittest
from portaldrift import PortalDrift

class TestPortalDrift(unittest.TestCase):
    """Test cases for PortalDrift class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PortalDrift()
        self.assertIsInstance(instance, PortalDrift)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PortalDrift()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
