import React, { useRef, useEffect } from "react";
import ForceGraph2D from "react-force-graph-2d";

export default function NetworkGraph({ nodes, edges, vulnerableNodes = [], compromisedNodes = [] }) {
  const fgRef = useRef();

  const getNodeColor = (nodeId) => {
    if (compromisedNodes.includes(nodeId)) return "black";
    if (vulnerableNodes.includes(nodeId)) return "red";
    return "green";
  };

  useEffect(() => {
    if (fgRef.current) {
      fgRef.current.zoomToFit(500);
    }
  }, [nodes, edges]);

  return (
    <div className="border p-4 rounded shadow bg-white">
      <h3 className="text-lg font-semibold mb-2">Граф сети</h3>
      <div style={{ height: "500px" }}>
        <ForceGraph2D
          ref={fgRef}
          graphData={{
            nodes: nodes.map((n) => ({ id: n.id, name: n.label })),
            links: edges.map((e) => ({
              source: e.source,
              target: e.target,
            })),
          }}
          nodeLabel="name"
          nodeAutoColorBy="id"
          nodeCanvasObject={(node, ctx, globalScale) => {
            const label = node.name;
            const fontSize = 12 / globalScale;
            ctx.fillStyle = getNodeColor(node.id);
            ctx.beginPath();
            ctx.arc(node.x, node.y, 8, 0, 2 * Math.PI, false);
            ctx.fill();

            ctx.font = `${fontSize}px Sans-Serif`;
            ctx.fillStyle = "black";
            ctx.textAlign = "center";
            ctx.fillText(label, node.x, node.y + 12);
          }}
        />
      </div>
    </div>
  );
}
