
import unittest


class MyTestResult(unittest.TestResult):
    def startTest(self, test):
        super().startTest(test)
        print(f"Starting test: {test}")

    def addSuccess(self, test):
        super().addSuccess(test)
        print(f"Test passed: {test}")

    def addFailure(self, test, err):
        super().addFailure(test, err)
        print(f"Test failed: {test}")


class MyTestCase(unittest.TestCase):
    def test_example(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
    runner = unittest.TextTestRunner(resultclass=MyTestResult)
    runner.run(suite)
