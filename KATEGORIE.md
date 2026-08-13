## 🗂️ Struktura projektów: dwie kategorie
Repozytoria w tym profilu dzielą się na dwie wyraźnie różne kategorie. Rozróżnienie jest celowe i konsekwentne:
- **Narzędzia inżynierskie** — kod zweryfikowany, działający na realnych danych, testowalny.
- **Modele koncepcyjne** — język metaforyczny (Λ–τ–ρ / TIMDR / TRM / GIA) używany jako narzędzie do myślenia, bez klasycznej warstwy obliczeniowej pod spodem. Nie są to teorie naukowe ani modele empiryczne.
---
### 🔧 Narzędzia inżynierskie
*Zweryfikowany kod, realne dane, testy.*
| Repo | Co robi |
|---|---|
| [math-validator](https://github.com/jbackk-lang/math-validator) | Walidator wyrażeń matematycznych — detekcja osobliwości i defektów |
| [math-validator-v2.0](https://github.com/jbackk-lang/math-validator-v2.0) | Druga generacja walidatora, wykrywanie problemów mylnych |
| [math-validator-3.0](https://github.com/jbackk-lang/math-validator-3.0) | Trzecia generacja — SymPy, algebra liniowa, logika zdaniowa |
| [synoptyk-v2.0](https://github.com/jbackk-lang/synoptyk-v2.0) | Prognoza pogody — realne dane Open-Meteo, filtr falkowy DWT db4 |
| [RADAR-TRACKING-TIMDR](https://github.com/jbackk-lang/RADAR-TRACKING-TIMDR) | Tor radarowy 1D (filtr Kalmana / cząsteczkowy) z adaptacyjną regulacją szumu (JRegulator) i niezależnym detektorem krzywizny trajektorii — walidowane na 4 realnych trasach GPS + symulacji wstrzykniętych usterek sensora, 34 testy |
| [Radar-TIMDR](https://github.com/jbackk-lang/Radar-TIMDR) | Generyczna analiza trajektorii 2D: gradient przepływu (TIMDR-flow), detekcja nagłych zmian kierunku (twist, z poprawką na zawijanie kąta), redukcja szumu, predykcja — 10 testów |
| [FLIGHT-TRACKING-TIMDR](https://github.com/jbackk-lang/FLIGHT-TRACKING-TIMDR) | Śledzenie toru lotu (lat/lon/alt/t) z korekcją geodezyjną kursu (cos(lat)) i detektorem krzywizny/torsji 3D, zwalidowanym na helisie analitycznej |
| [TIMDR-Security-Module](https://github.com/jbackk-lang/TIMDR-Security-Module) | Detekcja anomalii w ruchu sieciowym i metrykach serwera produkcyjnego — nagłe skoki (twist, robust z-score) i osobno powolny dryf (np. wyciek pamięci), 22 testy |
| [THE](https://github.com/jbackk-lang/THE) | Moduł krzywizny/torsji trajektorii (THE-GEO PRO 4D), zwalidowany na helisie analitycznej (błąd <0.01% przy gęstym próbkowaniu), 8 testów. Repo zawiera też osobną warstwę pseudokodu koncepcyjnego (sekcje 1-7), jawnie oznaczoną w README jako niezwalidowaną |
| [analizator-gieldowy](https://github.com/jbackk-lang/analizator-gieldowy) | Analiza rynku — realne dane giełdowe, SMA/VWAP/OBV |
| [analizator-gieldowy-2.0](https://github.com/jbackk-lang/analizator-gieldowy-2.0) | Druga generacja analizatora giełdowego (FastAPI + Streamlit) |
| [EasySound](https://github.com/jbackk-lang/EasySound) | Filtrowanie i czyszczenie dźwięku (filtr Butterwortha) |
| [Helix-Lock](https://github.com/jbackk-lang/Helix-Lock) | Szyfrator plików z HMAC i licznikiem odczytów |
| [topologic](https://github.com/jbackk-lang/topologic) | Biblioteka operatorów sygnałowych: zero-crossing, z-score, korelacja kierunkowa |
| [Senscore](https://github.com/jbackk-lang/Senscore) | Pipeline filtracji sygnałów z detektorów (5-etapowy, PCA, clustering) |
| [fusion-tools](https://github.com/jbackk-lang/fusion-tools) | Narzędzia do danych z diagnostyki plazmy (W7-X, JET, DIII-D) |
| [phi-fiber-dsp](https://github.com/jbackk-lang/phi-fiber-dsp) | Filtr DSP dla sygnałów światłowodowych |
| [phi-topology-filter](https://github.com/jbackk-lang/phi-topology-filter) | Filtr obrazu oparty na operatorach Laplace/Sobel/curl |
| [MAGE-IN-IMAGE-DECODER](https://github.com/jbackk-lang/MAGE-IN-IMAGE-DECODER) | Modularna analiza obrazu — FFT, HSV, detekcja ruchu |
| [Helix-Astro](https://github.com/jbackk-lang/Helix-Astro) | Analiza widm astronomicznych — normalizacja, filtracja, korelacja |
---
### 🌀 Modele koncepcyjne
*Warstwa metaforyczna, narzędzie do myślenia — nie teoria naukowa.*
| Repo | Temat |
|---|---|
| [Architektura-Mapowania-Zmyslowego-TIMDR-Transduction-](https://github.com/jbackk-lang/Architektura-Mapowania-Zmyslowego-TIMDR-Transduction-) | Sensoryczna brama do modelu pola |
| [AstroCycles-TIMDR](https://github.com/jbackk-lang/AstroCycles-TIMDR) | Cykle astrologiczne w języku TIMDR |
| [astro-map](https://github.com/jbackk-lang/astro-map) | Symboliczna mapa danych astronomicznych |
| [Boundary-Matter](https://github.com/jbackk-lang/Boundary-Matter) | Silnik decyzyjny generujący sprzeczne tezy rynkowe |
| [FAI](https://github.com/jbackk-lang/FAI) | Minimalny model AI oparty na stanach λ/τ/ρ |
| [FIELDCORE](https://github.com/jbackk-lang/FIELDCORE) | Kosmos jako układ dwóch skrętów pola |
| [FUNDAMENTAL-AI-MODEL-WERSJA-PRO-main](https://github.com/jbackk-lang/FUNDAMENTAL-AI-MODEL-WERSJA-PRO-main) | Architektura AI oparta na Λ–τ–ρ |
| [genertor-fotonow](https://github.com/jbackk-lang/genertor-fotonow) | Koncepcyjny generator fotonów oparty na skręcie pola |
| [GIA-TIMDR](https://github.com/jbackk-lang/GIA-TIMDR) | Fundament matematyczny/logiczny całego systemu TIMDR |
| [GSF](https://github.com/jbackk-lang/GSF) | Globalny system finansowy jako pole informacji |
| [J-Photon-Drive](https://github.com/jbackk-lang/J-Photon-Drive) | Operator J w geometrii helisy |
| [KHIPU](https://github.com/jbackk-lang/KHIPU) | Koncepcyjna architektura czteroprocesorowa (TETRAGON-4CPU) |
| [MAGE-EGYPT-OPERATORS](https://github.com/jbackk-lang/MAGE-EGYPT-OPERATORS) | Interpretacja egipskich znaków operacyjnych |
| [MAPA-PO-HELU-STRUKTURA](https://github.com/jbackk-lang/MAPA-PO-HELU-STRUKTURA) | Układ pierwiastków jako struktura topologiczna |
| [MOD-DWOISTOSCI-ELEKTRONU](https://github.com/jbackk-lang/MOD-DWOISTOSCI-ELEKTRONU) | Model elektronu jako dwuwarstwowego stanu pola |
| [PC_TIMDR](https://github.com/jbackk-lang/PC_TIMDR) | Koncepcyjny procesor geometryczny F4-RED |
| [Photo-Hel](https://github.com/jbackk-lang/Photo-Hel) | Interakcja foton–hel jako model koncepcyjny |
| [probabilistic-timdr](https://github.com/jbackk-lang/probabilistic-timdr) | Prawdopodobieństwo i warunki brzegowe w TIMDR |
| [RADAR-TRACKING](https://github.com/jbackk-lang/RADAR-TRACKING) | Szkic geometrycznego trackera radarowego (TRM/GIA/TIMDR) — pseudokod, bez testów i bez implementacji funkcji, na których się opiera |
| [REGULA-GIATIMA](https://github.com/jbackk-lang/REGULA-GIATIMA) | Notacja operatorowa GIATIMA |
| [Spoleczny-Protokol-Informacyjny](https://github.com/jbackk-lang/Spoleczny-Protokol-Informacyjny) | Protokół kodowania komunikatów (TIMDERA) |
| [TIMDER-Multisensory-Meditation-Engine](https://github.com/jbackk-lang/TIMDER-Multisensory-Meditation-Engine) | Multisensoryczna medytacja geometryczna |
| [TIV](https://github.com/jbackk-lang/TIV) | Koncepcyjna "waluta informacyjna" TIMDR |
| [Topological-Reduction-Model-TRM-Structure-Twist-and-Information-Flow](https://github.com/jbackk-lang/Topological-Reduction-Model-TRM-Structure-Twist-and-Information-Flow) | Fale topologiczne w biosferze, geologii, kosmosie |
| [topologia-informacji](https://github.com/jbackk-lang/topologia-informacji) | Centralny framework pojęciowy Λ–τ–ρ |
| [TRM-Geometry-Core](https://github.com/jbackk-lang/TRM-Geometry-Core) | Geometria bazowa modeli TRM/TIMDR |
| [trm-dna-stabilizer](https://github.com/jbackk-lang/trm-dna-stabilizer) | DNA jako topologiczny stabilizator szumu |
| [trm-particle-geometry](https://github.com/jbackk-lang/trm-particle-geometry) | Cząstki jako węzły geometryczne |
| [WHITE-LASER-MAP](https://github.com/jbackk-lang/WHITE-LASER-MAP) | Model białego lasera bez fosforu |
---
*Podział sporządzony na podstawie przeglądu kodu (nie tylko README). Odświeżono w sierpniu 2026 — dodano Radar-TIMDR, FLIGHT-TRACKING-TIMDR, TIMDR-Security-Module, THE i RADAR-TRACKING; zaktualizowano opis RADAR-TRACKING-TIMDR o JRegulator i CurvatureDetector. Ze względu na limit API GitHuba odświeżenie objęło ~15 ostatnio zmienianych repozytoriów, nie pełny, ponowny audyt wszystkich ~50 — starsze pozycje przyjęto bez zmian. Kategoria „narzędzia inżynierskie" oznacza, że w repozytorium znajduje się działający kod przetwarzający realne dane wejściowe — nie jest to gwarancja bezbłędności, tylko potwierdzenie, że narzędzie robi to, co deklaruje.*
