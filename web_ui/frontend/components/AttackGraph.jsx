import React, { useState } from "react";
import UploadPage from "./pages/UploadPage";
import NetworkGraph from "./components/NetworkGraph";
import RiskPanel from "./components/RiskPanel";
import AttackGraph from "./components/AttackGraph";

export default function App() {
  const [analysisResult, setAnalysisResult] = useState(null);

  return (
    <div className="p-6 space-y-8">
      <UploadPage onResult={setAnalysisResult} />

      {analysisResult && (
        <>
          <NetworkGraph
            nodes={analysisResult.nodes}
            edges={analysisResult.edges}
            vulnerableNodes={analysisResult.vulnerable_nodes}
          />
          <AttackGraph
            criticalPaths={analysisResult.critical_paths}
          />
          <RiskPanel riskReport={analysisResult.risk_report} />
        </>
      )}
    </div>
  );
}
