from plumbum import cli

class BubbleSort(cli.Application):

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
        if length is 1:
            return mylist

        swapped = False
        # Walk down the length backwards, for optimization
        for x in range(length-1, 0, -1):
            # An optimization where the list we're searching is less and less
            for y in range(x):
                if mylist[y] > mylist[y+1]:
                    # Swap the neighboring values - largest always "bubbles" up to end
                    mylist[y], mylist[y+1] = mylist[y+1], mylist[y]

        return mylist