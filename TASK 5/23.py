from abc import ABC, abstractmethod

class Attendance(ABC):
    @abstractmethod
    def record_attendance(self):
        pass


class ManualAttendance(Attendance):
    def record_attendance(self):
        return "Attendance recorded manually"


class RFIDAttendance(Attendance):
    def record_attendance(self):
        return "Attendance recorded via RFID"


if __name__ == "__main__":
    methods = [ManualAttendance(), RFIDAttendance()]
    for method in methods:
        print(method.record_attendance())
