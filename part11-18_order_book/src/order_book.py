# Write your solution here:
class Task:
    id = 0
    def __init__(self,description,name,load):
        self.description = description
        self.programmer = name
        self.workload = load
        self.finished = False
        Task.id += 1
        self.id = Task.id
    
    def __str__(self):
        return f'{self.id}: {self.description} ({self.workload} hours), programmer {self.programmer} {'FINISHED' if self.finished else 'NOT FINISHED'}'
    
    def is_finished(self):
        return self.finished
    
    def mark_finished(self):
        self.finished = True
    
class OrderBook:
    def __init__(self):
        self.orders = []
    
    def add_order(self,description,name,load):
        new_order = Task(description,name,load)
        self.orders.append(new_order)
    
    def all_orders(self):
        return self.orders
    
    def programmers(self):
        return list(set([x.programmer for x in self.orders]))

    def mark_finished(self,id:int):
        c = False
        for x in self.orders:
            if x.id == id:
                c = True
                x.mark_finished()
        if c == False: raise ValueError('invalid ID')
    
    def finished_orders(self):
        return [x for x in self.orders if x.is_finished() == True]
    def unfinished_orders(self):
        return [x for x in self.orders if x.is_finished() == False]

    def status_of_programmer(self,programmer:str):
        finished_task = 0
        unfinished_task = 0
        finished_workload = 0
        unfinished_workload = 0
        c = True
        for x in self.orders:
            if x.programmer == programmer:
                c = False
                if x.is_finished() == True:
                    finished_task += 1
                    finished_workload += x.workload
                elif x.is_finished() == False:
                    unfinished_task += 1
                    unfinished_workload += x.workload
        if c:
            raise ValueError('invalid name')
        return (finished_task,unfinished_task,finished_workload,unfinished_workload)
            

if __name__ == "__main__":
    orders = OrderBook()
    orders.add_order("program webstore", "Adele", 10)
    orders.add_order("program mobile app for workload accounting", "Adele", 25)
    orders.add_order("program app for practising mathematics", "Adele", 100)
    orders.add_order("program the next facebook", "Eric", 1000)

    orders.mark_finished(1)
    orders.mark_finished(2)
    t = OrderBook()
    t.add_order("program webstore", "Andy", 10)

    status = orders.status_of_programmer("Adele")
    print(status)