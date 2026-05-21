# 🧠 RDF-Based Knowledge System

This project is a semantic knowledge system built using RDF (Resource Description Framework) and SPARQL. It provides an interactive graphical interface to load RDF data, execute queries, and visualize relationships between entities.

The system also integrates semantic reasoning to infer new knowledge from existing data.

---

## 🚀 Features

✅ Load RDF files (Turtle / RDF XML)  
✅ Execute SPARQL queries through a user-friendly interface  
✅ Display query results in a dynamic table  
✅ Apply semantic inference (OWL RL reasoning)  
✅ Visualize RDF graph structure (nodes & relationships)  
✅ Interactive desktop application (Tkinter GUI)

---

## 🖥️ User Interface

The application is divided into three main sections:

- **Left Panel** → SPARQL query editor  
- **Center Panel** → RDF graph visualization  
- **Right Panel** → Query results (table view)

---

## 🛠️ Technologies Used

- Python  
- Tkinter (GUI)  
- rdflib (RDF management)  
- owlrl (semantic reasoning)  
- SPARQL  

---

## ⚙️ How It Works

1. Load an RDF file (.ttl or .rdf)
2. The system parses the data into RDF triples
3. Inference rules are applied to enrich the knowledge base
4. Users can run SPARQL queries
5. Results are displayed dynamically in the interface

---

## ▶️ Installation & Execution

### 1. Clone the repository

git clone https://github.com/your-username/rdf-based-knowledge-system.git

### 2. Install dependencies

pip install rdflib owlrl

### 3. Run the application

python main.py

---

## 📊 Example Query

```sparql
PREFIX club: <http://club-infotech.org/ontologie#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?membre ?score
WHERE {
  ?membre rdf:type club:Membre .
  ?membre club:scoreCalculé ?score .
}
ORDER BY DESC(?score)
