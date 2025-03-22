import pytest
import os
import sys

def run_tests():
    """Run all tests and report results."""
    print("Running all tests...")
    
    # Run tests in verbose mode
    result = pytest.main(["-v"])
    
    if result == 0:
        print("\nAll tests passed successfully!")
    else:
        print("\nSome tests failed. Please check the output above.")
    
    return result

if __name__ == "__main__":
    # Add the src directory to the Python path
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
    
    # Run tests
    run_tests()