import os
import argparse
import sys

from coala_json.reporters.JunitReporter import JunitReporter


def get_path(filepath):
    return os.path.join(os.getcwd(), filepath)


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--junit', const=True, action='store_const',
                        help='mode in which coala will produce a JUnit report')
    parser.add_argument('-f', '--input', help='path of the json input file')
    parser.add_argument('-o', '--output', default='test_report.xml',
                        help='path of output report file')
    return parser


def main(arg):
    """
    main function to produce report
    :param arg: use to specify explicit args when running pytest
    :return: None
    """
    parser = create_parser()
    args = parser.parse_args(arg)
    produce_report(parser, args)


def produce_report(parser, args):
    if args.junit and args.input:
        with open(get_path(args.input)) as input_file:
            j = JunitReporter(input_file)
            output = j.to_output()
        with open(args.output, 'w+') as report:
            report.write(output)
    if not args.junit:
        parser.error("Please specify an output mode")
    if not args.input:
        parser.error("Please specify a 'coala-json' input file")


def main_call():
    if __name__ == '__main__':
        sys.exit(main(arg=None))


main_call()
