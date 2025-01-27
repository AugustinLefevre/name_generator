import unittest
import os

def discover_and_run_tests():
    test_dir = os.path.join(os.path.dirname(__file__), 'tests')
    test_suite = unittest.defaultTestLoader.discover(test_dir, pattern="*.py")
    test_runner = unittest.TextTestRunner(verbosity=2)
    test_runner.run(test_suite)

if __name__ == "__main__":
    discover_and_run_tests()
