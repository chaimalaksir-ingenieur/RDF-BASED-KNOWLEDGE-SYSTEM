from rdflib import Graph, Namespace, RDF
from owlrl import DeductiveClosure, OWLRL_Semantics


class RDFManager:
    def __init__(self):
        self.g = Graph()

        # Namespace du projet
        self.club = Namespace("http://club-infotech.org/ontologie#")

        # Bind prefixes
        self.g.bind("club", self.club)
        self.g.bind("rdf", RDF)


    def charger_rdf(self, fichier):
        self.g.parse(fichier)
        return len(self.g)


    def executer_sparql(self, requete):
        return self.g.query(requete)


    def appliquer_inference(self):
        DeductiveClosure(OWLRL_Semantics).expand(self.g)
        return len(self.g)