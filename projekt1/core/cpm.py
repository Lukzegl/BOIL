from core.models import Czynnosc

def oblicz_cpm(dane: dict[str, Czynnosc]) -> dict[str, Czynnosc]:
    KONCOWY_CZAS = 0
    wszyscy_pop = set()
    gotowe = []

    for c in dane.values():
        if not c.poprzednicy:
            c.ES = 0
            c.EF = c.T
            gotowe.append(c.nazwa)

    while len(gotowe) < len(dane):
        for c in dane.values():
            if c.nazwa in gotowe:
                continue

            if all(p in gotowe for p in c.poprzednicy):
                maxEF = max(dane[p].EF for p in c.poprzednicy)

                c.ES = maxEF
                c.EF = maxEF + c.T

                KONCOWY_CZAS = max(KONCOWY_CZAS, c.EF)

                gotowe.append(c.nazwa)

                wszyscy_pop.update(c.poprzednicy)

    if dane:
        KONCOWY_CZAS = max(c.EF for c in dane.values())

    koncowe = []

    for c in dane.values():
        if c.nazwa not in wszyscy_pop:
            c.LF = KONCOWY_CZAS
            c.LS = KONCOWY_CZAS - c.T
            c.R = c.LF - c.EF
            c.critic = (c.R == 0)

            koncowe.append(c.nazwa)

    while len(koncowe) < len(dane):
        for k in koncowe:
            for p in dane[k].poprzednicy:
                poprzednik = dane[p]

                if poprzednik.LF == 0 or dane[k].LS < poprzednik.LF:
                    poprzednik.LF = dane[k].LS
                    poprzednik.LS = poprzednik.LF - poprzednik.T
                    poprzednik.R = poprzednik.LF - poprzednik.EF
                    poprzednik.critic = (poprzednik.R == 0)

                    if p not in koncowe:
                        koncowe.append(p)

    return dane