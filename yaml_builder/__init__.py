import argparse
import yaml

from .loader import ComposeLoader


def main():
    """Builds a yaml file"""
    parser = argparse.ArgumentParser(description='Compose a yaml file.')
    parser.add_argument(
        'root',
        type=argparse.FileType('r'),
        help='The root yaml file to compose.'
    )

    args = parser.parse_args()

    result = yaml.load(args.root, Loader=ComposeLoader)

    print(yaml.dump(result))
