from typing import List


class ShoppingCart:
    def __init__(self, max_size: int) -> None:  #The -> operator in Python is part of function annotations — it tells you the expected return type of a function. #self. something vanya instance variable ho
        self.items: List[str] = []
        self.max_size = max_size
        
    def add(self, item: str):
        if self.size() == self.max_size :
            raise OverflowError("cannot add more items")
        self.items.append(item)
        
    def size(self) -> int:
        return len(self.items)
    
    def get_items(self) -> List[str]:
        return self.items
    
    def get_total_price(self, price_map):
        total_price = 0
        for item in self.items:
            total_price += price_map.get(item)
        return total_price