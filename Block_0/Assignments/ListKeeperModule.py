class ListKeeper:
    def __init__(self):
        self.keeperdict = {
        'names': ['example'],
        'lists': [[1,2,3,4,5]]}
    def show(self):   
        print(self.keeperdict["names"])
        print(self.keeperdict["lists"])  
    def add(self,new_name,new_list):
        self.keeperdict["names"].append(new_name) 
        self.keeperdict["lists"].append(new_list)
    def delet(self,del_name):
        index = self.keeperdict["names"].index(del_name)
        self.keeperdict["names"].pop(index)      
        self.keeperdict["lists"].pop(index)
    def sort(self,sort_name):
        index= self.keeperdict["names"].index(sort_name)
        self.keeperdict["lists"][index].sort()
        return self.keeperdict["lists"][index]
        
        