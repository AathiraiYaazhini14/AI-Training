from abc import ABC, abstractmethod

class StoragePlan(ABC):
    @abstractmethod
    def allow_upload(self, file_size):
        pass


class FreeStorage(StoragePlan):
    def allow_upload(self, file_size):
        return file_size <= 100


class PaidStorage(StoragePlan):
    def allow_upload(self, file_size):
        return file_size <= 1000


if __name__ == "__main__":
    plans = [FreeStorage(), PaidStorage()]
    for plan in plans:
        print(plan.allow_upload(150))
