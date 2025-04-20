from typing import List, Dict

class RiskEvaluator:
    def __init__(self, devices: List[Dict]):
        self.devices = devices

    def evaluate(self) -> List[Dict]:
        risk_report = []
        for device in self.devices:
            risk_score = 0
            for service in device.get("services", []):
                vuln = service.get("vulnerability")
                if vuln:
                    # Простая эвристика: оценка по известности CVE и наличию рекомендации
                    risk_score += 3
                    if service.get("remediation"):
                        risk_score += 2
            if risk_score > 0:
                risk_report.append({
                    "device": device["name"],
                    "risk_score": risk_score,
                    "vulnerabilities": device["services"]
                })
        return sorted(risk_report, key=lambda x: x["risk_score"], reverse=True)

if __name__ == "__main__":
    from loader import NetworkLoader

    loader = NetworkLoader("data/generated_topologies/sample_topology.json")
    loader.load()
    evaluator = RiskEvaluator(loader.get_devices())
    report = evaluator.evaluate()

    for entry in report:
        print(f"{entry['device']} — Risk: {entry['risk_score']}")
