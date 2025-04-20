import json
import random
import uuid
from typing import List, Dict

# Типы устройств
DEVICE_TYPES = [
    "Workstation", "Laptop", "Printer", "Server", "Switch", "Router", "Firewall"
]

# Типы сервисов и возможные уязвимости
SERVICES = {
    "HTTP": ["CVE-2021-41773", "CVE-2019-8942"],
    "FTP": ["CVE-2021-22945", "CVE-2015-3306"],
    "SMB": ["CVE-2017-0144", "CVE-2020-0796"],
    "SSH": ["CVE-2018-15473"],
    "RDP": ["CVE-2019-0708"],
    "MySQL": ["CVE-2012-2122"],
    "PostgreSQL": ["CVE-2022-1552"],
    "SNMP": ["CVE-2017-6736"]
}

# Простые рекомендации по закрытию уязвимостей
REMEDIATIONS = {
    "CVE-2021-41773": "Обновите Apache до последней версии.",
    "CVE-2019-8942": "Отключите обработку PUT-запросов.",
    "CVE-2021-22945": "Ограничьте доступ к FTP только по VPN.",
    "CVE-2015-3306": "Используйте SFTP вместо FTP.",
    "CVE-2017-0144": "Установите патч EternalBlue.",
    "CVE-2020-0796": "Отключите SMBv3 или обновите систему.",
    "CVE-2018-15473": "Обновите SSH-сервер и включите fail2ban.",
    "CVE-2019-0708": "Отключите RDP или включите сетевую аутентификацию.",
    "CVE-2012-2122": "Отключите root-доступ к базе данных.",
    "CVE-2022-1552": "Обновите PostgreSQL до последней версии.",
    "CVE-2017-6736": "Отключите SNMPv1 и v2c, используйте SNMPv3."
}

def generate_device_name(index: int, device_type: str) -> str:
    return f"{device_type}-{index:02d}"

def generate_topology(num_devices: int = 80) -> Dict:
    devices = []
    connections = []
    
    for i in range(num_devices):
        device_type = random.choice(DEVICE_TYPES)
        device_name = generate_device_name(i, device_type)
        services = random.sample(list(SERVICES.keys()), k=random.randint(1, 3))

        device_services = []
        for service in services:
            vulns = SERVICES[service]
            vuln = random.choice(vulns)
            remediation = REMEDIATIONS[vuln]
            device_services.append({
                "name": service,
                "vulnerability": vuln,
                "remediation": remediation
            })

        devices.append({
            "id": str(uuid.uuid4()),
            "name": device_name,
            "type": device_type,
            "services": device_services
        })

    # Случайные соединения между устройствами (гарантировать связность графа)
    for i in range(1, num_devices):
        src = random.randint(0, i - 1)
        dst = i
        connections.append({
            "from": devices[src]["id"],
            "to": devices[dst]["id"]
        })

        # Добавить дополнительные случайные связи
        if random.random() < 0.3:
            extra_src = random.randint(0, num_devices - 1)
            extra_dst = random.randint(0, num_devices - 1)
            if extra_src != extra_dst:
                connections.append({
                    "from": devices[extra_src]["id"],
                    "to": devices[extra_dst]["id"]
                })

    return {
        "devices": devices,
        "connections": connections
    }

def save_topology(filename: str, topology: Dict):
    with open(filename, 'w') as f:
        json.dump(topology, f, indent=2)

if __name__ == "__main__":
    topology = generate_topology(num_devices=80)
    save_topology("data/generated_topologies/sample_topology.json", topology)
    print("✔ Сетевая топология сгенерирована и сохранена.")
