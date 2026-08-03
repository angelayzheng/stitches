import React, { useEffect, useState } from 'react';
import ForceGraph3D from 'react-force-graph-3d';
import type { GraphData, GraphNode } from '../types/graph';

export const Graph3D: React.FC = () => {
  const [data, setData] = useState<GraphData>({ nodes: [], links: [] });
  const [selectedNode, setSelectedNode] = useState<GraphNode | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    fetch('http://localhost:8000/api/graph')
      .then((res) => {
        if (!res.ok) {
          throw new Error(`HTTP error! Status: ${res.status}`);
        }
        return res.json();
      })
      .then((graphData: GraphData) => {
        setData(graphData);
        setLoading(false);
      })
      .catch((err) => {
        console.error('Failed to fetch graph data:', err);
        setError('Failed to load graph from FastAPI backend.');
        setLoading(false);
      });
  }, []);

  return (
    <div className="relative w-screen h-screen bg-slate-950 overflow-hidden">
      {/* Loading & Error States */}
      {loading && (
        <div className="absolute inset-0 flex items-center justify-center text-slate-400 text-sm z-20">
          Loading 3D Graph...
        </div>
      )}

      {error && (
        <div className="absolute top-4 left-4 p-4 bg-red-900/80 text-white rounded-xl border border-red-700 z-20">
          {error}
        </div>
      )}

      {/* 3D Force Graph Visualizer */}
      {!loading && !error && (
        <ForceGraph3D
          graphData={data}
          nodeLabel="name"
          nodeColor={(node: any) => node.color || '#3b82f6'}
          nodeVal={(node: any) => node.val || 1}
          onNodeClick={(node: any) => setSelectedNode(node)}
          cooldownTicks={100}
        />
      )}

      {/* Tailwind CSS Overlay HUD (Active when a node is clicked) */}
      {selectedNode && (
        <div className="absolute top-4 left-4 p-4 bg-slate-900/90 text-white rounded-xl shadow-xl border border-slate-700 max-w-sm backdrop-blur-md z-10 transition-all">
          <div className="flex items-center justify-between gap-4">
            <h3 className="text-lg font-bold text-blue-400">{selectedNode.name}</h3>
            <button
              onClick={() => setSelectedNode(null)}
              className="text-slate-400 hover:text-white text-xs px-2 py-1 bg-slate-800 hover:bg-slate-700 rounded border border-slate-600 transition"
            >
              ✕
            </button>
          </div>

          <div className="mt-3 text-xs text-slate-300 space-y-1">
            <p><span className="text-slate-500">Node ID:</span> {selectedNode.id}</p>
            {selectedNode.val && (
              <p><span className="text-slate-500">Weight / Size:</span> {selectedNode.val}</p>
            )}
          </div>
        </div>
      )}
    </div>
  );
};