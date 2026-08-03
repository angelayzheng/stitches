from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import GraphData, GraphNode, GraphLink
import networkx as nx

app = FastAPI(title="Graph Visualization API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/graph", response_model=GraphData)
def get_graph():
    # Example graph generation with NetworkX
    G = nx.erdos_renyi_graph(n=100, p=0.03)

    nodes = [
        GraphNode(id=str(i), name=f"Node {i}", val=float((i % 5) + 1))
        for i in G.nodes()
    ]
    links = [GraphLink(source=str(u), target=str(v)) for u, v in G.edges()]

    return GraphData(nodes=nodes, links=links)
