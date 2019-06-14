from plumbum import cli

class MergeSort(cli.Application):

    _list = [8, 100, 99, 5, 15, 99, 85, 15, 25, 5, 99, 97, 10, 35, 36]

    def main(self):
        if list is None or len(self._list) is 0:
            print("List should have at least one element")
            return 1
        else:
            sorted_list = self.sort(self._list)
            print(sorted_list)

    def sort(self, mylist):
        length = len(mylist)

        # Base case
        if length is 1:
            return mylist

        # Divide step
        if length is 2:
            first_half = [mylist[0]]
            second_half = [mylist[1]]
        else:
            half = int(length/2)
            first_half = self.sort(mylist[0:half])
            second_half = self.sort(mylist[half:])

        # Conquer!
        f=0 # counter for first array
        s=0 # counter for second array

        sorted_list = []
        while len(first_half) is not 0 \
                and len(second_half) is not 0:
            if first_half[0] <= second_half[0]:
                sorted_list.append(first_half[0])
                first_half.remove(first_half[0])
            else:
                sorted_list.append(second_half[0])
                second_half.remove(second_half[0])

        # Need this last part, at some point one half will be exhausted.  Since we're sorted, simply add the rest.
        if len(first_half) is 0:
            sorted_list.extend(second_half)
        else:
            sorted_list.extend(first_half)

        return sorted_list