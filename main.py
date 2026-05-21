
import tkinter as tk
from tkinter import ttk, filedialog, scrolledtext
from rdf_manager import RDFManager


class AppRDF(tk.Tk):
    def __init__(self):
        super().__init__()

        # WINDOW
        self.title("Club Info_Tech :: Base de Connaissances RDF")
        self.geometry("1400x800")
        self.configure(bg="#111827")

        self.rdf = RDFManager()

        self.setup_style()
        self.build_ui()

    def setup_style(self):
        style = ttk.Style()
        style.theme_use("clam")

        # TREEVIEW
        style.configure(
            "Treeview",
            background="#0f172a",
            foreground="#e2e8f0",
            rowheight=32,
            fieldbackground="#0f172a",
            bordercolor="#14b8a6",
            borderwidth=1,
            font=("Segoe UI", 10)
        )

        style.configure(
            "Treeview.Heading",
            background="#14532d",
            foreground="white",
            font=("Segoe UI", 10, "bold")
        )


    def build_ui(self):


        header = tk.Frame(self, bg="#1e1b4b", height=50)
        header.pack(fill=tk.X)

        tk.Label(
            header,
            text="Club Info_Tech :: Base de Connaissances RDF",
            bg="#1e1b4b",
            fg="#cbd5e1",
            font=("Segoe UI", 14, "bold")
        ).pack(side=tk.LEFT, padx=20, pady=10)

        main = tk.Frame(self, bg="#111827")
        main.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)

        LEFT_WIDTH = 420
        CENTER_WIDTH = 500
        RIGHT_WIDTH = 320


        left = tk.Frame(
            main,
            bg="#0b1120",
            highlightbackground="#7c3aed",
            highlightthickness=2,
            width=LEFT_WIDTH
        )
        left.pack(side=tk.LEFT, fill=tk.BOTH, padx=5)
        left.pack_propagate(False)

        tk.Label(
            left,
            text="Requête SPARQL",
            bg="#7c3aed",
            fg="white",
            font=("Segoe UI", 11, "bold"),
            pady=8
        ).pack(fill=tk.X)

        self.text_query = scrolledtext.ScrolledText(
            left,
            wrap=tk.WORD,
            bg="#020617",
            fg="#a5f3fc",
            insertbackground="white",
            font=("Consolas", 11),
            relief=tk.FLAT,
            padx=10,
            pady=10
        )

        self.text_query.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.text_query.insert("1.0", self.default_query())

        btn_frame = tk.Frame(left, bg="#0b1120")
        btn_frame.pack(fill=tk.X, padx=10, pady=10)

        tk.Button(
            btn_frame,
            text="▶ Exécuter",
            command=self.executer,
            bg="#6d28d9",
            fg="white",
            activebackground="#7c3aed",
            relief=tk.FLAT,
            font=("Segoe UI", 10, "bold"),
            padx=10,
            pady=10,
            cursor="hand2"
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        tk.Button(
            btn_frame,
            text="📂 Charger RDF",
            command=self.charger_rdf,
            bg="#1d4ed8",
            fg="white",
            activebackground="#2563eb",
            relief=tk.FLAT,
            font=("Segoe UI", 10, "bold"),
            padx=10,
            pady=10,
            cursor="hand2"
        ).pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)

        center = tk.Frame(
            main,
            bg="#0b1120",
            highlightbackground="#2563eb",
            highlightthickness=2,
            width=CENTER_WIDTH
        )
        center.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5)
        center.pack_propagate(False)

        tk.Label(
            center,
            text="Graphe RDF",
            bg="#1e3a8a",
            fg="white",
            font=("Segoe UI", 11, "bold"),
            pady=8
        ).pack(fill=tk.X)

        self.canvas_graph = tk.Canvas(
            center,
            bg="#020617",
            highlightthickness=0
        )
        self.canvas_graph.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.draw_demo_graph()


        right = tk.Frame(
            main,
            bg="#0b1120",
            highlightbackground="#10b981",
            highlightthickness=2,
            width=RIGHT_WIDTH
        )
        right.pack(side=tk.RIGHT, fill=tk.BOTH, padx=5)
        right.pack_propagate(False)

        tk.Label(
            right,
            text="Résultats",
            bg="#166534",
            fg="white",
            font=("Segoe UI", 11, "bold"),
            pady=8
        ).pack(fill=tk.X)

        self.tree = ttk.Treeview(right)
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)


        footer = tk.Frame(self, bg="#0f172a", height=35)
        footer.pack(fill=tk.X)

        self.status = tk.Label(
            footer,
            text="RDF chargé : 0 triples | SPARQL prêt",
            bg="#0f172a",
            fg="#94a3b8",
            anchor="w",
            font=("Segoe UI", 9)
        )
        self.status.pack(fill=tk.X, padx=15)


    def draw_demo_graph(self):

        c = self.canvas_graph

        c.create_oval(250, 80, 370, 150, fill="#7c3aed", outline="white", width=2)
        c.create_text(310, 115, text="Membre\nAli", fill="white", font=("Segoe UI", 10, "bold"))

        c.create_oval(70, 180, 190, 250, fill="#14532d", outline="white", width=2)
        c.create_text(130, 215, text="Spécialité\nAlgo", fill="white")

        c.create_oval(420, 180, 540, 250, fill="#92400e", outline="white", width=2)
        c.create_text(480, 215, text="Score\n185", fill="white")

        c.create_oval(240, 300, 380, 380, fill="#0e7490", outline="white", width=2)
        c.create_text(310, 340, text="Concours\nAlgo", fill="white")

        # LINES
        c.create_line(250, 120, 190, 200, fill="#cbd5e1", width=2)
        c.create_line(370, 120, 420, 200, fill="#cbd5e1", width=2)
        c.create_line(310, 150, 310, 300, fill="#cbd5e1", width=2)

        # LABELS
        c.create_text(210, 160, text="aSpécialité", fill="#84cc16")
        c.create_text(400, 160, text="aScore", fill="#84cc16")
        c.create_text(360, 230, text="participeA", fill="#84cc16")


    def charger_rdf(self):
        file = filedialog.askopenfilename(
            filetypes=[("RDF Turtle", "*.ttl"), ("RDF XML", "*.rdf")]
        )

        if file:
            n = self.rdf.charger_rdf(file)
            self.rdf.appliquer_inference()

            self.status.config(
                text=f"RDF chargé : {n} triples | Inférence appliquée"
            )

    def executer(self):
        query = self.text_query.get("1.0", "end")
        results = self.rdf.executer_sparql(query)
        self.afficher_resultats(results)


    def afficher_resultats(self, results):

        for item in self.tree.get_children():
            self.tree.delete(item)

        rows = list(results)

        if not rows:
            self.status.config(text="0 résultats")
            return

        cols = results.vars

        self.tree["columns"] = cols
        self.tree["show"] = "headings"

        for col in cols:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=120)

        for row in rows:
            values = [str(row[c]) for c in cols]
            self.tree.insert("", "end", values=values)

        self.status.config(text=f"{len(rows)} résultats trouvés")

    def default_query(self):
        return """
PREFIX club: <http://club-infotech.org/ontologie#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?membre ?score
WHERE {

  ?membre rdf:type club:Membre .
  ?membre club:scoreCalculé ?score .

}
ORDER BY DESC(?score)
"""


# =========================================================
# RUN
# =========================================================
if __name__ == "__main__":
    app = AppRDF()
    app.mainloop()

