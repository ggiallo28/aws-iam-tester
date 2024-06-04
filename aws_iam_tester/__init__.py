from importlib.metadata import version, PackageNotFoundError
from aws_iam_tester.lib import AwsIamTester

try:
    __version__ = version(__name__)
except PackageNotFoundError:
    __version__ = "unknown"
