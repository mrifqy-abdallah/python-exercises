class Clock:
    def __init__(self, hour: int, minute: int):
        self.total_minutes = (hour * 60 + minute) % 1440  # 1440 is 60x24
        self.hour = str(self.total_minutes // 60)
        self.minute = str(self.total_minutes % 60)

    def __repr__(self):
        hour = self.hour if len(self.hour) == 2 else f"0{self.hour}"
        minute = self.minute if len(self.minute) == 2 else f"0{self.minute}"
        return f"{hour}:{minute}"

    def __eq__(self, other):
        return self.total_minutes == other.total_minutes

    def __add__(self, minutes):
        return Clock(0, self.total_minutes + minutes)

    def __sub__(self, minutes):
        return Clock(0, self.total_minutes - minutes)
