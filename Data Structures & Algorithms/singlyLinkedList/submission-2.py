class LinkedList:
    
    def __init__(self):
        self.list = None
    
    def get(self, index: int) -> int:
        curr = self.list
        i = 0
        while(curr is not None):
            if (i == index):
                return curr[0]
            curr = curr[1]
            i += 1
        return -1

    def insertHead(self, val: int) -> None:
        head_arr = [val, self.list]
        self.list = head_arr

    def insertTail(self, val: int) -> None:
        tail_arr = [val, None]
        if self.list == None:
            self.list = tail_arr
        else:
            curr = self.list
            while curr[1] is not None:
                curr = curr[1]
            curr[1] = tail_arr


    def remove(self, index: int) -> bool:
        if self.list is None:
            return False
        if index == 0:
            self.list = self.list[1]
            return True
        
        curr = self.list
        i = 1
        while curr is not None and curr[1] is not None:
            if i == index:
                curr[1] = curr[1][1]
                return True
            curr = curr[1]
            i += 1
        return False

    def getValues(self) -> List[int]:
        values = []
        curr = self.list
        while curr is not None:
            values.append(curr[0])
            curr = curr[1]
        return values
