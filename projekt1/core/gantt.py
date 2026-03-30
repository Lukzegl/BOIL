from __future__ import annotations

import matplotlib.pyplot as plt

from core.models import Czynnosc

def rysuj_jeden_gantt(ax, dane: dict[str, Czynnosc], start_atrybut: str, tytul: str) -> None:
    czynnosci = list(dane.values())
    czynnosci.sort(key=lambda x: getattr(x, start_atrybut))

    y = list(range(len(czynnosci)))

    for i, c in enumerate(czynnosci):
        start = getattr(c, start_atrybut)
        ax.barh(i, c.T, left=start, height=0.5)

    ax.set_yticks(y)
    ax.set_yticklabels([c.nazwa for c in czynnosci])
    ax.set_xlabel("Czas")
    ax.set_title(tytul)
    ax.grid(axis="x", linestyle="--", alpha=0.5)
    ax.invert_yaxis()

def rysuj_gantt_asap(dane: dict[str, Czynnosc]) -> None:
    fig, ax = plt.subplots(figsize=(8, max(3, len(dane))))
    rysuj_jeden_gantt(ax, dane, "ES", "Gantt chart ASAP")
    plt.tight_layout()
    plt.show()

def rysuj_gantt_alap(dane: dict[str, Czynnosc]) -> None:
    fig, ax = plt.subplots(figsize=(8, max(3, len(dane))))
    rysuj_jeden_gantt(ax, dane, "LS", "Gantt chart ALAP")
    plt.tight_layout()
    plt.show()

def rysuj_gantty(dane: dict[str, Czynnosc]) -> None:
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, max(6, len(dane))), sharex=True)

    fig.canvas.manager.set_window_title("CPM")

    rysuj_jeden_gantt(ax1, dane, "ES", "Gantt chart ASAP")
    rysuj_jeden_gantt(ax2, dane, "LS", "Gantt chart ALAP")

    plt.tight_layout()
    plt.show()