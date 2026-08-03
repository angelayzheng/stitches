from pydantic import BaseModel
from typing import List, Optional


class GraphNode(BaseModel):
    id: str
    name: str
    val: Optional[float] = 1.0
    color: Optional[str] = "#3b82f6"
    x: Optional[float] = None
    y: Optional[float] = None
    z: Optional[float] = None


class GraphLink(BaseModel):
    source: str
    target: str
    value: Optional[float] = 1.0


class GraphData(BaseModel):
    nodes: List[GraphNode]
    links: List[GraphLink]
