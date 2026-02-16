from abc import ABC, abstractmethod

class UpdateStrategy(ABC):
    @abstractmethod
    def apply_update(self):
        pass


class AutomaticUpdate(UpdateStrategy):
    def apply_update(self):
        return "Update applied automatically"


class ManualUpdate(UpdateStrategy):
    def apply_update(self):
        return "User approval required"


if __name__ == "__main__":
    updates = [AutomaticUpdate(), ManualUpdate()]
    for u in updates:
        print(u.apply_update())
