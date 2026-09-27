"""Generuje timdr-branches-diagram.svg (mapa galezi, mostow i wynikow TIMDR). Stan: 27 wrzesnia 2026.
Uzycie: python docs/rysuj_diagram_galezi.py  (zapisuje plik w katalogu glownym strony)."""
from pathlib import Path
from xml.sax.saxutils import escape

W, H = 1600, 1310
out = []
A = out.append


def box(x, y, w, h, cls, lines, title_cls="sh", rx=20):
    A(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" class="{cls}"/>')
    ty = y + 34
    for i, (txt, c) in enumerate(lines):
        A(f'<text x="{x + w / 2}" y="{ty}" text-anchor="middle" class="{c}">{escape(txt)}</text>')
        ty += 30 if c in ("sh", "h") else 23


def line(x1, y1, x2, y2, cls="line", arrow=True):
    A(f'<path d="M{x1},{y1} L{x2},{y2}" class="{cls}"' + (' marker-end="url(#arrow)"' if arrow else "") + "/>")


A(f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-labelledby="title desc">')
A('<title id="title">TIMDR — gałęzie, mosty i wyniki (27 września 2026)</title>')
A('<desc id="desc">Chronoproces i cztery gałęzie TIMDR; gałęzie użyte same dają wyniki negatywne, mosty między nimi — pozytywne; '
  'parametry przejść i reguła wykonalności; wyniki na łożyskach, turbinie, konstrukcjach i radarze.</desc>')
A('''<defs><style>
.bg{fill:#11131c}.formal{fill:#202a3e;stroke:#8194b7;stroke-width:3}.ms{fill:#123344;stroke:#22b9e8;stroke-width:3}
.g{fill:#2c1d46;stroke:#b175f5;stroke-width:3}.k{fill:#3c2d10;stroke:#e3ad21;stroke-width:3}.meta{fill:#12343a;stroke:#4fb3a8;stroke-width:3}
.support{fill:#143e2d;stroke:#55ca86;stroke-width:3}.partial{fill:#3c2d10;stroke:#e3ad21;stroke-width:3}.reject{fill:#4b2531;stroke:#ec687a;stroke-width:3}
.line{fill:none;stroke:#7184a4;stroke-width:3}.gline{fill:none;stroke:#55ca86;stroke-width:4}
.h{font:700 30px Arial,sans-serif;fill:#fff}.sh{font:700 21px Arial,sans-serif;fill:#fff}.small{font:17px Arial,sans-serif;fill:#c9d3e7}
.note{font:16px Arial,sans-serif;fill:#b5c1d7}.neg{font:16px Arial,sans-serif;fill:#f3a3ae}.pos{font:700 17px Arial,sans-serif;fill:#8be0ad}
.mid{font:700 17px Arial,sans-serif;fill:#f2cf6b}.label{font:700 16px Arial,sans-serif;fill:#dce6f8}
</style>
<marker id="arrow" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L9,3 L0,6 Z" fill="#7184a4"/></marker></defs>''')
A(f'<rect class="bg" width="{W}" height="{H}" rx="28"/>')
A('<text x="800" y="62" text-anchor="middle" class="h">TIMDR — gałęzie, mosty i wyniki</text>')
A('<text x="800" y="96" text-anchor="middle" class="note">Stan GIA-TIMDR: 27 września 2026. Wszystkie wyniki pre-rejestrowane, jedno uruchomienie, także negatywne.</text>')

# Chronoproces
box(480, 125, 640, 125, "formal", [("Chronoproces Ξ = (T, x, Γ, φ)", "sh"), ("pierwszy trybik: wybór zegara — czas • kąt obrotu • zdarzenie", "small"),
                                    ("turbina: zegar kątowy AUC 1,00, zwykły czas 0,85", "note")])
# galezie
BX = [60, 440, 820, 1200]; BY = 320; BW, BH = 340, 145
gal = [("ms", "M/S — sygnał", "anomalia • defekt • rezonans M", "sama: operatory bez przewagi", "(budynek, prądy silnika, radar)"),
       ("g", "G — geometria", "rura z = x + iH[x] • krzywizna", "sama: bez zysku ponad sito", "(łożyska, radar)"),
       ("k", "K — modalność", "częstotliwość • faza • amplituda", "sama: samonaprawa zbędna", "(przy stałej prędkości)"),
       ("meta", "META-DYNAMICS", "Λ • τ • ρ • J,  M = dS/dt", "sama: ρ bez wyniku (wideo)", "teraz: ρ = D = f·τ, τ = wygaszanie")]
for x, (c, t, s, n1, n2) in zip(BX, gal):
    box(x, BY, BW, BH, c, [(t, "sh"), (s, "small"), (n1, "neg"), (n2, "note")])
    line(800, 250, x + BW / 2, BY - 4)

# mosty (pozytywne, miedzy galeziami)
MY = 540; MW, MH = 360, 145
mosty = [(250, "Most: pole + sito", "rezonans ustala oczka sita", "SUPPORTED — łożyska Paderborn", "3 próby, +0,08 vs klasyka (12/15 foldów)"),
         (620, "Most: kotwica K → sito", "+ prostowanie rury (zegar kątowy)", "SUPPORTED — turbina wiatrowa", "AUC 1,00, swoistość 1,00"),
         (990, "Most: reżim D = f·τ", "cząsteczka ↔ pakiet ↔ fala", "SUPPORTED — łożyska do zniszczenia", "PRONOSTIA 9/11 + 7/11; budynek ρ +0,98")]
for (x, t, s, r1, r2), (a, b) in zip(mosty, [(0, 1), (1, 2), (2, 3)]):
    box(x, MY, MW, MH, "support", [(t, "sh"), (s, "small"), (r1, "pos"), (r2, "note")])
    line(BX[a] + BW / 2, BY + BH, x + 70, MY - 4, "gline"); line(BX[b] + BW / 2, BY + BH, x + MW - 70, MY - 4, "gline")

# wyniki dziedzinowe
RY = 760; RW, RH = 355, 140
wyniki = [(60, "partial", "Konstrukcje: kotwica modalna", ("most KW51 ✓ • rama LANL ✓", "pos"), ("śruba ORION-AE ✓ (trend)", "pos"), ("Hell Bridge: sama kotwica ✕", "neg")),
          (437, "partial", "Zwinięcie pola w rurę", ("rura niesie informację", "mid"), ("radar: 0,76 — tyle co sito", "note"), ("bez zysku ponad klasykę", "neg")),
          (814, "reject", "Radar mikro-Doppler", ("NOT SUPPORTED", "neg"), ("brak kotwicy (rytm zgadywany)", "note"), ("okno 30 ms za krótkie na łopaty", "note")),
          (1191, "partial", "K → G → M/S: przerwa ciągłości", ("HBTA pionowe 0,93–0,94 ≥ AR", "pos"), ("średnio remis z AR 0,80 (stężenia)", "mid"), ("Möbius K↔G odrzucony (artefakt)", "neg"))]
for x, c, t, *ls in wyniki:
    box(x, RY, RW, RH, c, [(t, "sh")] + list(ls))

# parametry przejsc
box(60, 945, 1486, 140, "formal", [("Parametry przejść — reguła wykonalności liczona PRZED testem", "sh"),
    ("N_cyk (cykle rytmu w oknie) • kotwica (stała / śledzona / wolna) • D = f·τ (reżim) • L_koh (koherencja → zegar) • środek oczek (lokalizacja)", "small"),
    ("Trafne przewidywania: słabe sito na PRONOSTIA (okno 0,1 s, N_cyk ≈ 15); wolna kotwica = porażka (radar); reżim fali → linie K (budynek)", "note"),
    ("Każdy krok porównywany ze znanym odpowiednikiem: widmo obwiedni, kurtogram, order tracking, OMA/SSI, AR, wskaźnik harmonicznych", "note")])
A('<text x="800" y="1125" text-anchor="middle" class="label">Obserwacja: gałąź użyta sama daje wynik negatywny, most między gałęziami — pozytywny; o powodzeniu łańcucha decyduje pierwszy trybik (zegar).</text>')

# legenda
LY = 1165
for i, (c, t) in enumerate([("support", "potwierdzony (pre-rejestracja)"), ("partial", "częściowy / mieszany"), ("reject", "odrzucony"), ("formal", "komponent formalny")]):
    x = 150 + i * 340
    A(f'<rect x="{x}" y="{LY}" width="34" height="22" rx="5" class="{c}"/>'); A(f'<text x="{x + 46}" y="{LY + 17}" class="small">{t}</text>')
A('<text x="800" y="1240" text-anchor="middle" class="note">Szczegóły i liczby: README GIA-TIMDR (tabela wyników), docs/geometry/RESULT_*.md; narzędzia: TIMDR-Industrial-Predict, TIMDR-Structural-Health.</text>')
A('<text x="800" y="1270" text-anchor="middle" class="note">TIMDR to model do budowania programów analizujących sygnały — rama, drogowskazy i protokół, nie gotowy detektor.</text>')
A("</svg>")
Path(__file__).resolve().parent.parent.joinpath("timdr-branches-diagram.svg").write_text("\n".join(out), encoding="utf-8")
print("zapisano timdr-branches-diagram.svg")
