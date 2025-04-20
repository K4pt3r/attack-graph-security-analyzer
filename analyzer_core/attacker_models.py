from enum import Enum

class AttackerType(Enum):
    EXTERNAL = "external"
    INTERNAL = "internal"

class AttackerModel:
    def __init__(self, attacker_type: AttackerType, initial_access: list):
        self.attacker_type = attacker_type
        self.initial_access = initial_access  # Список ID узлов, с которых может начаться атака

    def describe(self):
        if self.attacker_type == AttackerType.EXTERNAL:
            return f"Внешний атакующий. Доступ только к публичным сервисам: {self.initial_access}"
        elif self.attacker_type == AttackerType.INTERNAL:
            return f"Внутренний атакующий. Имеет доступ к: {self.initial_access}"
        return "Неизвестная модель атакующего."

if __name__ == "__main__":
    external = AttackerModel(AttackerType.EXTERNAL, ["Firewall-00", "Server-01"])
    internal = AttackerModel(AttackerType.INTERNAL, ["Workstation-03", "Laptop-15"])
    print(external.describe())
    print(internal.describe())
