import json
from typing import Dict, List

class NetworkLoader:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.devices = []
        self.connections = []

    def load(self):
        with open(self.filepath, 'r') as f:
            data = json.load(f)
        self.devices = data.get("devices", [])
        self.connections = data.get("connections", [])

    def get_devices(self) -> List[Dict]:
        return self.devices

    def get_connections(self) -> List[Dict]:
        return self.connections

    def get_device_map(self) -> Dict[str, Dict]:
        return {device['id']: device for device in self.devices}
