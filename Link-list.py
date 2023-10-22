class sill:
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next
    def __str__(self):
        return(f"item is {self.item} next is {self.next}")

sl1=sill(20,20)

print(sl1)
