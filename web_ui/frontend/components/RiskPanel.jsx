import React from "react";

export default function RiskPanel({ riskReport }) {
  return (
    <div className="p-4 bg-white shadow rounded">
      <h2 className="text-xl font-bold mb-4">Оценка рисков</h2>
      <table className="w-full text-left border-collapse">
        <thead>
          <tr>
            <th className="border-b p-2">Устройство</th>
            <th className="border-b p-2">Риск</th>
            <th className="border-b p-2">Уязвимости</th>
          </tr>
        </thead>
        <tbody>
          {riskReport.map((entry, idx) => (
            <tr key={idx} className="border-t hover:bg-gray-50">
              <td className="p-2 font-medium">{entry.device}</td>
              <td className="p-2">{entry.risk_score}</td>
              <td className="p-2">
                <ul className="list-disc ml-4">
                  {entry.vulnerabilities.map((s, i) => (
                    <li key={i}>{s.vulnerability} — {s.remediation}</li>
                  ))}
                </ul>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}
