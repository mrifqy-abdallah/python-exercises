class Clock:
    def __init__(self, hour: int, minute: int):
        self.total_minutes = (hour * 60 + minute) % 1440  # 1440 is 60x24
        self.hour = str(self.total_minutes // 60)
        self.minute = str(self.total_minutes % 60)

    def __repr__(self):
        hour = self.hour.zfill(2)
        minute = self.minute.zfill(2)
        return f"{hour}:{minute}"

    def __eq__(self, other):
        return self.total_minutes == other.total_minutes

    def __add__(self, minutes):
        return Clock(0, self.total_minutes + minutes)

    def __sub__(self, minutes):
        return Clock(0, self.total_minutes - minutes)
