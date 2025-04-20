import React, { useState } from "react";

export default function AttackSimulationPanel({ file, onResult }) {
  const [attackerType, setAttackerType] = useState("external");

  const handleSimulate = async () => {
    if (!file) return;
    const formData = new FormData();
    formData.append("file", file);
    formData.append("attacker_type", attackerType);

    const res = await fetch("http://localhost:8000/simulate-attack/", {
      method: "POST",
      body: formData,
    });

    const data = await res.json();
    onResult(data.compromised_nodes);
  };

  return (
    <div className="space-y-2">
      <h3 className="text-lg font-semibold">Симуляция атаки</h3>

      <div>
        <label className="mr-4">
          <input
            type="radio"
            name="attacker"
            value="external"
            checked={attackerType === "external"}
            onChange={() => setAttackerType("external")}
          />
          Внешний атакующий
        </label>
        <label className="ml-4">
          <input
            type="radio"
            name="attacker"
            value="internal"
            checked={attackerType === "internal"}
            onChange={() => setAttackerType("internal")}
          />
          Внутренний атакующий
        </label>
      </div>

      <button
        onClick={handleSimulate}
        className="px-4 py-2 bg-blue-600 text-white rounded"
      >
        Запустить симуляцию
      </button>
    </div>
  );
}
