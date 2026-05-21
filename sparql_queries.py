from rdflib import Graph, Namespace, RDF

g = Graph()
club = Namespace("http://club-infotech.org/ontologie#")

g.bind("club", club)
g.bind("rdf", RDF)

# Load RDF file
g.parse("club_infotech.ttl", format="turtle")


# =========================
# Query 1: Members + Specialty
# =========================
q1 = """
SELECT ?membre ?spec
WHERE {
    ?membre rdf:type club:Membre .
    ?membre club:aSpécialité ?spec .
}
"""

print("=== Members & Specialties ===")
for row in g.query(q1):
    print(row.membre, row.spec)


# =========================
# Query 2: Ranking in a competition
# =========================
concours_uri = club["Concours1"]

q2 = f"""
SELECT ?membre ?score
WHERE {{
    ?membre club:participeA <{concours_uri}> .
    ?membre club:scoreCalculé ?score .
}}
ORDER BY DESC(?score)
"""

print("\n=== Ranking Concours1 ===")
for r in g.query(q2):
    print(r.membre, r.score)


# =========================
# Query 3: Filter by specialty
# =========================
specialite = "Algorithmique"

q3 = f"""
SELECT ?m
WHERE {{
    ?m club:aSpécialité club:{specialite} .
}}
"""

print("\n=== Algorithmique Members ===")
for r in g.query(q3):
    print(r.m)


# =========================
# Query 4: Winners (if inferred)
# =========================
q4 = """
SELECT ?m
WHERE {
    ?m club:estVainqueur ?concours .
    ?concours rdf:type club:Concours .
}
"""

print("\n=== Winners ===")
for r in g.query(q4):
    print(r.m)


# =========================
# Query 5: High scores
# =========================
q5 = """
SELECT ?m ?sf
WHERE {
    ?m club:scoreCalculé ?sf .
    FILTER(?sf > 100)
}
"""

print("\n=== High Scores (>100) ===")
for r in g.query(q5):
    print(r.m, r.sf)