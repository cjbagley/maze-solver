from unittest import TestCase
from components.window import Window

class TestWindow(TestCase):
    def test_window_construction(self):
        try:
            win = Window(800, 800)
        except:
            self.fail("Window could not be constructed")
        
        self.assertIsInstance(win, Window)