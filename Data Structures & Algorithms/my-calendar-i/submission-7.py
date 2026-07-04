class MyCalendar:
    
    def __init__(self):
        self.bookings = []
        

    def book(self, startTime: int, endTime: int) -> bool:
        interval = [startTime,endTime]
        for booking in self.bookings:
            a,b = booking
            if (
                a <= startTime < b
                or a < endTime <= b
                or startTime <= a < endTime
                or startTime < b <= endTime
            ) :
                return False
        self.bookings.append(interval)

        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)