from unittest import TestCase
from stack import Stack

class TestStack(TestCase):
    """Test cases for Stack"""

    def setUp(self):
        """Setup before each test"""
        self.stack = Stack()

    def tearDown(self):
        """Tear down after each test"""
        self.stack = None

    def test_push(self):
        """Test pushing an item into the stack"""
        self.stack.push(42)
        self.assertEqual(42,self.stack.peek())

    def test_pop(self):
        """Test popping an item of off the stack"""
        self.stack.push(42)
        self.assertEqual(42,self.stack.peek())
        self.assertEqual(42,self.stack.pop())
        self.assertEqual(True,self.stack.is_empty())

    def test_peek(self):
        """Test peeking at the top the stack"""
        self.stack.push(42)
        self.stack.push(44)
        self.assertEqual(44,self.stack.peek())
        self.assertEqual(44,self.stack.pop())
        self.assertEqual(42,self.stack.peek())
        self.assertEqual(42,self.stack.pop())
        self.assertEqual(True,self.stack.is_empty())

    def test_is_empty(self):
        """Test if the stack is empty"""
        self.assertEqual(True,self.stack.is_empty())
