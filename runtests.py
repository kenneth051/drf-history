from settings import *
django.setup()

from django_nose import NoseTestSuiteRunner

def run_tests(*test_args):
    if not test_args:
        test_args = ["tests"]

    test_runner = NoseTestSuiteRunner(verbosity=1)
    failures = test_runner.run_tests(test_args)
    if failures:
        sys.exit(failures)


if __name__ == "__main__":
    run_tests(*sys.argv[1:])
