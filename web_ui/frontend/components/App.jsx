import React, { useState } from "react";
import UploadPage from "./pages/UploadPage";
import NetworkGraph from "./components/NetworkGraph";
import RiskPanel from "./components/RiskPanel";
import AttackSimulationPanel from "./components/AttackSimulationPanel";

export default function App() {
  const [analysisResult, setAnalysisResult] = useState(null);
  const [uploadedFile, setUploadedFile] = useState(null);
  const [simulationResult, setSimulationResult] = useState([]);

  return (
    <div className="p-6 space-y-8">
      <UploadPage
        onResult={setAnalysisResult}
        onFileSelected={setUploadedFile}
      />

      {analysisResult && (
        <>
          <NetworkGraph
            nodes={analysisResult.nodes}
            edges={analysisResult.edges}
            vulnerableNodes={analysisResult.vulnerable_nodes}
            compromisedNodes={simulationResult}
          />
          <RiskPanel riskReport={analysisResult.risk_report} />
          <AttackSimulationPanel
            file={uploadedFile}
            onResult={setSimulationResult}
          />
        </>
      )}
    </div>
  );
}
