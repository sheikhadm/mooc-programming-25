# Write your solution here:
class Clock() :
    def __init__ (self,h = 0,minutes = 0,seconds = 0):
        self.h = h
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return f'{self.h:02}:{self.minutes:02}:{self.seconds:02}'

    def tick(self):
        self.seconds += 1
        
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1

       
        if self.minutes == 60:
            self.minutes = 0
            self.h += 1

        if self.h == 24:
            self.h = 0
            self.minutes = 0
            self.seconds = 0
    
    def set(self, h = 0,minutes = 0,seconds = 0) :
        self.h = h
        self.minutes = minutes
        self.seconds = seconds

        
if __name__ == "__main__":
    clock = Clock(23, 59, 55)
    print(clock)
    clock.tick()
    print(clock)

