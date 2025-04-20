from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from loader import NetworkLoader
from graph_builder import GraphBuilder
from graph_analyzer import GraphAnalyzer
from risk_evaluator import RiskEvaluator
from attacker_models import AttackerModel, AttackerType
from attack_simulator import AttackSimulator
import tempfile
import shutil
import uuid
import os

app = FastAPI()

# Настройка CORS для доступа с фронта
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/analyze/")
async def analyze(file: UploadFile = File(...)):
    # Сохраняем временный файл
    tmp_dir = tempfile.mkdtemp()
    tmp_path = os.path.join(tmp_dir, f"{uuid.uuid4()}.json")
    with open(tmp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Загружаем топологию
    loader = NetworkLoader(tmp_path)
    loader.load()

    # Построение графа
    graph = GraphBuilder(loader.get_devices(), loader.get_connections()).build_graph()

    # Анализ уязвимостей и рисков
    analyzer = GraphAnalyzer(graph)
    evaluator = RiskEvaluator(loader.get_devices())
    vuln_nodes = analyzer.find_vulnerable_nodes()
    critical_paths = analyzer.get_critical_paths()
    risk_report = evaluator.evaluate()

    return {
        "nodes": list(graph.nodes(data=True)),
        "edges": list(graph.edges()),
        "vulnerable_nodes": vuln_nodes,
        "critical_paths": critical_paths,
        "risk_report": risk_report
    }


@app.post("/simulate-attack/")
async def simulate_attack(file: UploadFile = File(...), attacker_type: str = "internal"):
    tmp_dir = tempfile.mkdtemp()
    tmp_path = os.path.join(tmp_dir, f"{uuid.uuid4()}.json")
    with open(tmp_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    loader = NetworkLoader(tmp_path)
    loader.load()
    graph = GraphBuilder(loader.get_devices(), loader.get_connections()).build_graph()
    start_node = loader.get_devices()[0]["id"]  # простая точка входа
    attacker = AttackerModel(AttackerType(attacker_type), [start_node])
    simulator = AttackSimulator(graph, attacker)
    compromised = simulator.simulate()

    return {
        "attacker_type": attacker_type,
        "compromised_nodes": list(compromised)
    }
