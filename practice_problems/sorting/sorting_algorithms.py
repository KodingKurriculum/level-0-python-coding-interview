#!/usr/bin/env python
from plumbum import cli
from merge_sort import MergeSort
from heap_sort import HeapSort
from bubble_sort import BubbleSort

class SortingAlgorithms(cli.Application):

    def main(self, *args):
        if args:
            print("Unknown command {0!r}".format(args[0]))
            return 1   # error exit code
        if not self.nested_command:           # will be ``None`` if no sub-command follows
            print("No command given")
            return 1   # error exit code

if __name__ == '__main__':
    SortingAlgorithms.subcommand("bubble", BubbleSort)
    SortingAlgorithms.subcommand("heap", HeapSort)
    SortingAlgorithms.subcommand("merge", MergeSort)

    SortingAlgorithms.run()
