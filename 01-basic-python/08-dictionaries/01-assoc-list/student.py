class AssocList:
    def __init__(self):
        self.__items = []

    def __setitem__(self, key, value):
        if [key, value] not in self.__items:
            self.__items.append([key, value])
        else:
            ...
            
    def __getitem__(self, key):
        for i in range(len(self.__items)):
            if self.__items[i][0] == key:
                
        
# assoc_list = AssocList()
# assoc_list["Cat"] = "Chat"
# print(assoc_list)
