from rdflib import URIRef

class Chaining:
    def __init__(self, rdf_manager):
        self.g = rdf_manager.g

    def trouver_vainqueur(self, uri_concours: str) -> str:
        """
        Backward chaining:
        Goal → Find the winner of a competition
        Strategy → Retrieve highest score
        """
        requete = f"""
        PREFIX club: <http://club-infotech.org/ontologie#>
        SELECT ?membre ?score WHERE {{
            ?membre club:participeA <{uri_concours}> .
            ?membre club:scoreCalculé ?score .
        }}
        ORDER BY DESC(?score)
        LIMIT 1
        """

        res = list(self.g.query(requete))
        return str(res[0][0]) if res else "Aucun résultat"

    def qualifier_membres(self, seuil: float = 100.0):
        """
        Forward chaining:
        Rule → If score > threshold → member is qualified
        """
        CLUB = "http://club-infotech.org/ontologie#"

        req = f"""
        PREFIX club: <{CLUB}>
        SELECT ?m ?s WHERE {{
            ?m club:scoreCalculé ?s .
            FILTER(?s > {seuil})
        }}
        """

        for (m, s) in self.g.query(req):
            self.g.add((
                m,
                URIRef(CLUB + "estQualifié"),
                URIRef(CLUB + "Vrai")
            ))