#!/usr/bin/env python
from plumbum import cli
from max_overlapping_intervals import MaxOverlappingIntervals

class InterviewProblems(cli.Application):

    def main(self, *args):
        if args:
            print("Unknown command {0!r}".format(args[0]))
            return 1   # error exit code
        if not self.nested_command:           # will be ``None`` if no sub-command follows
            print("No command given")
            return 1   # error exit code


if __name__ == '__main__':
    InterviewProblems.subcommand("intervals", MaxOverlappingIntervals)
    InterviewProblems.run()
