import graphviz
from core.models import Czynnosc

def create_cpm_graph(dane: dict[str, Czynnosc]) -> graphviz.Digraph:
    graph = graphviz.Digraph(format='png')

    for c in dane.values():
        label = f"{c.nazwa}\nT={c.T}\nES={c.ES}, EF={c.EF}\nLS={c.LS}, LF={c.LF}\nR={c.R}"

        graph.node(c.nazwa, label=label, shape='circle', style='filled', fillcolor='red' if c.critic else 'white')

    for c in dane.values():
        for p in c.poprzednicy:
            graph.edge(p, c.nazwa)

    return graph
    
def rysuj_cpm(dane: dict[str, Czynnosc]) -> None:
    graph = create_cpm_graph(dane)
    graph.render('cpm_graph', view=True)
