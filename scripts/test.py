"""
Test Script
"""

from utils import config  # pylint: disable=unused-import

from pysolidworks.services.solidworks import SolidWorksService


def main():
    """Test"""
    solidworks_service = SolidWorksService()
    solidworks_service.test()


if __name__ == "__main__":
    main()
