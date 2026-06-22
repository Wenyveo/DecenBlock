# test_decenblock.py
"""
Tests for DecenBlock module.
"""

import unittest
from decenblock import DecenBlock

class TestDecenBlock(unittest.TestCase):
    """Test cases for DecenBlock class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DecenBlock()
        self.assertIsInstance(instance, DecenBlock)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DecenBlock()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
