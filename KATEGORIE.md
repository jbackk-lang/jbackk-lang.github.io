# Katalog publicznych repozytoriów

**Stan: 3 listopada 2026 · 69 publicznych repozytoriów.** Lista porównana z GitHub API; podkatalogi archiwów nie są liczone jako osobne repozytoria.

[Katalog z wyszukiwarką](https://jbackk-lang.github.io/kategorie.html) · [Dane katalogu](data/repo-catalog.json)

## TSI — system i aplikacje (3)

| Repozytorium | Przeznaczenie |
|---|---|
| [AI-SI-TSI](https://github.com/jbackk-lang/AI-SI-TSI) | Dokumentacja lokalnego systemu TSI: własna sieć językowa, pamięć, słowniki i narzędzia. Swobodna rozmowa w rozwoju; aktualny kod i wagi pozostają lokalne. |
| [TSI-math-validator-5](https://github.com/jbackk-lang/TSI-math-validator-5) | Walidator matematyczny: równania, wykresy, całki, geometria, zadania tekstowe i audyt kroków. Panel ucznia i nauczyciela, pomocnik TSI; publiczna dokumentacja i demo. |
| [TSI-MUZ](https://github.com/jbackk-lang/TSI-MUZ) | Lokalny zarządca budżetu i dokumentów: rachunki, koszty stałe, plany oszczędzania, terminy, przypomnienia i raporty. Publiczna dokumentacja projektu. |

## Narzędzia i zastosowania (48)

| Repozytorium | Przeznaczenie |
|---|---|
| [analizator-gieldowy](https://github.com/jbackk-lang/analizator-gieldowy) | Analiza rynku — realne dane giełdowe, SMA/VWAP/OBV |
| [analizator-gieldowy-2.0](https://github.com/jbackk-lang/analizator-gieldowy-2.0) | Druga generacja analizatora giełdowego (FastAPI + Streamlit) |
| [Analizator_Gieldowy_v3.0](https://github.com/jbackk-lang/Analizator_Gieldowy_v3.0) | Trzecia generacja — sygnały TIMDR na realnych danych z yfinance oraz lokalny runtime meta-dynamiki. To NIE jest doradztwo inwestycyjne |
| [deliverable_timdr_finanse](https://github.com/jbackk-lang/deliverable_timdr_finanse) | Rdzeń TIMDR dla danych finansowych + ringdown_resonance() — narzędzie badawczo-edukacyjne, nie doradztwo inwestycyjne |
| [EasySound](https://github.com/jbackk-lang/EasySound) | Filtrowanie i czyszczenie dźwięku (filtr Butterwortha) |
| [FLIGHT-TRACKING-TIMDR](https://github.com/jbackk-lang/FLIGHT-TRACKING-TIMDR) | Śledzenie trajektorii 3D dla modeli latających (drony, RC) — filtr Kalmana, detekcja manewrów, fuzja radar+IMU; walidowane na danych syntetycznych, nie na realnych lotach |
| [Helix-Astro](https://github.com/jbackk-lang/Helix-Astro) | Analiza widm astronomicznych — normalizacja, filtracja, korelacja |
| [Helix-Lock](https://github.com/jbackk-lang/Helix-Lock) | Szyfrator plików z HMAC i licznikiem odczytów |
| [KHIPU-NEURAL](https://github.com/jbackk-lang/KHIPU-NEURAL) | Test, czy koncepcja State9/GIPU z KHIPU przekłada się na moduł sieci neuronowej — wynik mieszany, jawnie opisany (pomaga przy zadaniach dyskretnych, szkodzi przy ciągłych) |
| [MAGE-IN-IMAGE-DECODER](https://github.com/jbackk-lang/MAGE-IN-IMAGE-DECODER) | Modularna analiza obrazu — FFT, HSV, detekcja ruchu |
| [math-validator-3.0](https://github.com/jbackk-lang/math-validator-3.0) | Trzecia generacja — SymPy, algebra liniowa, logika zdaniowa |
| [math-validator-v2.0](https://github.com/jbackk-lang/math-validator-v2.0) | Druga generacja walidatora, wykrywanie problemów mylnych |
| [phi-fiber-dsp](https://github.com/jbackk-lang/phi-fiber-dsp) | Filtr DSP dla sygnałów światłowodowych |
| [phi-topology-filter](https://github.com/jbackk-lang/phi-topology-filter) | Filtr obrazu oparty na operatorach Laplace/Sobel/curl |
| [RADAR-TRACKING](https://github.com/jbackk-lang/RADAR-TRACKING) | Wcześniejsza, bazowa wersja toru radarowego (TRM/GIA/TIMDR, klastrowanie przez KD-tree, asocjacja węgierska) — zobacz też RADAR-TRACKING-TIMDR (rozszerzona wersja) |
| [RADAR-TRACKING-TIMDR](https://github.com/jbackk-lang/RADAR-TRACKING-TIMDR) | Tor radarowy 1D (filtr Kalmana / cząsteczkowy) z adaptacyjną regulacją szumu (JRegulator), walidowany na realnych trasach GPS |
| [Senscore](https://github.com/jbackk-lang/Senscore) | Pipeline filtracji sygnałów z detektorów (5-etapowy, PCA, clustering) |
| [SYNOPTYK-ARCTIC](https://github.com/jbackk-lang/SYNOPTYK-ARCTIC) | Wariant Synoptyka dla stacji arktycznej (Longyearbyen) — realny, zmierzony bias/MAE prognozy vs archiwum Open-Meteo (backtest 90 dni), dashboard www |
| [synoptyk-v2.0](https://github.com/jbackk-lang/synoptyk-v2.0) | Prognoza pogody — realne dane Open-Meteo, filtr falkowy DWT db4 |
| [Synoptyk-v3](https://github.com/jbackk-lang/Synoptyk-v3) | Trzecie podejście do prognozy pogody w tym ekosystemie — pogoda jako pole na siatce geograficznej ("membrana", nie niezależne szeregi czasowe per stacja), analiza widmowa/geometria różniczkowa (fronty, wiry, rezonans międzypolowy), realne dane Open-Meteo (live + archiwum, 10-dniowy backtest trafności) |
| [TIMDR-AI-Core](https://github.com/jbackk-lang/TIMDR-AI-Core) | Rdzeń protokołu TIMDR i silnik audytu twierdzeń claim_audit.py — karty dowodowe przeliczają liczby z README z surowych danych, sprawdzają kotwice pre-rejestracji i sformułowania; użyty do audytu MAST, Modal-Formalism, Aviation, Bio-Signals i MAGE (znalezione i poprawione realne błędy). Linie eksperymentów aktywacji zamknięte bez przyrostu nad baseline'em |
| [TIMDR-Aviation-Diagnostics](https://github.com/jbackk-lang/TIMDR-Aviation-Diagnostics) | Transfer TIMDR-Core (1:1 z TIMDR-Earthquake-Core) do diagnostyki silników lotniczych — test na realnych danych degradacji silnika turbowentylatorowego, z jawnym opisem ograniczeń środowiska testowego |
| [TIMDR-Battery-Predict](https://github.com/jbackk-lang/TIMDR-Battery-Predict) | Predykcyjne utrzymanie ogniwa/pakietu baterii — fuzja 4 czujników, model degradacji, czas do awarii (TTF), wynik zdrowia |
| [TIMDR-Bio-Signals](https://github.com/jbackk-lang/TIMDR-Bio-Signals) | TIMDR dla sygnałów fizjologicznych (EKG/EEG/puls/oddech) — arytmie, anomalie impulsów, zaniki oscylacji (bezdech). To NIE jest wyrób medyczny |
| [TIMDR-Cosmology-Filters](https://github.com/jbackk-lang/TIMDR-Cosmology-Filters) | 3 filtry anomalii dla danych kosmologicznych zbudowane od zera (odstępy pików akustycznych CMB, precesja peryhelium Merkurego, napięcie Hubble'a) — realne, cytowane dane (Planck 2018, MESSENGER, SH0ES) z propagacją niepewności |
| [TIMDR-Crypto-Graph](https://github.com/jbackk-lang/TIMDR-Crypto-Graph) | Graf transakcji (węzły=portfele, krawędzie=transfery) z rdzeniem helisa/rezonans/defekt do detekcji anomalii AML — zweryfikowany ślepy punkt self-eq, poprawka (kalibrowany eq + żywe dane) i peer-group eq po kohortach niezależnych od grafu |
| [TIMDR-Cyclone-RI](https://github.com/jbackk-lang/TIMDR-Cyclone-RI) | Cztery cechy burzy poprzedzające wyrównanie pionowe i gwałtowną intensyfikację cyklonu tropikalnego (Alvey i in. 2026, JGR-Atmospheres) — etykietowanie intensyfikacji zwalidowane na realnych danych, operatory przechylenia i środowiska tylko na kontrolach syntetycznych (brak dostępu do TC-RADAR), opisane wprost w repo |
| [TIMDR-DNA](https://github.com/jbackk-lang/TIMDR-DNA) | Detekcja anomalii głębokości pokrycia sekwencjonowania (styl CNV) — narzędzie badawcze, silne zastrzeżenie w repo: to NIE jest diagnostyka medyczna |
| [TIMDR-Earthquake-Core](https://github.com/jbackk-lang/TIMDR-Earthquake-Core) | Rdzeń analizy sejsmicznej — detekcja mikro-wstrząsów, picker STA/LTA zweryfikowany 1:1 z ObsPy, tryb katalogowy na żywych danych USGS; test trybu prekursorowego dał wynik negatywny (brak sygnału), udokumentowane wprost w repo |
| [TIMDR-Echosonda-3D](https://github.com/jbackk-lang/TIMDR-Echosonda-3D) | Analiza chmury punktów dna (batymetria) + detekcja celów w toni wodnej (ryby, ławice, obiekty sztuczne) — silnik sonarowy |
| [TIMDR-EV-Predict](https://github.com/jbackk-lang/TIMDR-EV-Predict) | Fuzja 3 podsystemów pojazdu elektrycznego (bateria + silnik elektryczny + ładowanie/sieć) w jeden wynik zdrowia i TTF pojazdu, zasada najsłabszego ogniwa — realne dane starzenia baterii NASA PCoE, most do CAN/OBD-II |
| [TIMDR-fusion-tools](https://github.com/jbackk-lang/TIMDR-fusion-tools) | Narzędzia do danych z diagnostyki plazmy (W7-X, JET, DIII-D, EAST) — detekcja punktów skrętu, redukcja szumu |
| [TIMDR-Grid-Monitor](https://github.com/jbackk-lang/TIMDR-Grid-Monitor) | Monitoring starzenia kabli energetycznych (model Arrhenius) + alerty przekroczenia reżimu; lokalnie dołączony runtime meta/sejsmiczny, więc repo działa bez repozytoriów-sąsiadów |
| [TIMDR-Industrial-Predict](https://github.com/jbackk-lang/TIMDR-Industrial-Predict) | Predictive maintenance dla maszyn przemysłowych — fuzja czujników w sygnał energii stanu E(t), predykcja czasu do awarii i health-score; demo API obsługuje także lokalne próbki CWRU łożysk |
| [TIMDR-lightcurve-fewshot](https://github.com/jbackk-lang/TIMDR-lightcurve-fewshot) | Eksperymentalna klasyfikacja rzeczywistych krzywych blasku OGLE, badania fotometrii i kontroli jakości. |
| [TIMDR-Materials-Design](https://github.com/jbackk-lang/TIMDR-Materials-Design) | 8-krokowa procedura projektowania materiału od zera metodą TIMDR (anomalia/defekt/skręt/rezonans) — każdy krok to osobny, przetestowany moduł kodu |
| [TIMDR-META-DYNAMICS](https://github.com/jbackk-lang/TIMDR-META-DYNAMICS) | Symulacja i wizualizacja meta-przepływu (krzywizna/skręt pola, MetaPredict z tłumieniem) |
| [TIMDR-Mold-Risk](https://github.com/jbackk-lang/TIMDR-Mold-Risk) | Wczesne ostrzeganie przed ryzykiem pleśni — model VTT (Hukka & Viitanen) na temperaturze/wilgotności, indeks pleśni M(t) 0-6. Walidowane na danych syntetycznych fizycznie ugruntowanych, nie na realnych danych DALTON (Git LFS niedostępne w środowisku budowy) |
| [TIMDR-orbital-tracker](https://github.com/jbackk-lang/TIMDR-orbital-tracker) | Śledzenie katalogowych obiektów orbitalnych: propagacja orbit, kojarzenie pomiarów i lokalne narzędzia analizy. |
| [TIMDR-Radar-Module](https://github.com/jbackk-lang/TIMDR-Radar-Module) | Moduł RCS (rezonans w reżimie Mie) dla sygnałów radarowych |
| [TIMDR-Robot](https://github.com/jbackk-lang/TIMDR-Robot) | Warstwa TIMDR dla robota wieloosiowego i podsystemów (chwytak, podstawa mobilna, kamera, zasilanie) — detekcja anomalii, flota robotów, mosty integracyjne ROS2/MQTT/OPC-UA |
| [TIMDR-Security-Module](https://github.com/jbackk-lang/TIMDR-Security-Module) | Detekcja anomalii w ruchu/zdarzeniach sieciowych na bazie sygnału stanu TIMDR |
| [TIMDR-Solar-PV](https://github.com/jbackk-lang/TIMDR-Solar-PV) | Detekcja degradacji/brudu/zacienienia/awarii PV — model fizyczny PVWatts (pvlib) i Performance Ratio jako sygnał stanu, plus rozszerzenie analizy zespolonej PV+bateria. Walidowane na danych syntetycznych fizycznie ugruntowanych, nie na realnych danych NREL PVDAQ |
| [TIMDR-Structural-Health](https://github.com/jbackk-lang/TIMDR-Structural-Health) | Monitorowanie konstrukcji (mosty, budynki, połączenia śrubowe): kotwica modalna, linie nieliniowości, reżim fala/cząsteczka + lokalny dashboard. Walidacja pre-rejestrowana: most KW51, rama LANL, śruba ORION-AE — potwierdzone; most Hell Bridge — negatywny. Jak widzi TIMDR → |
| [TIMDR-Tornado-NEXRAD](https://github.com/jbackk-lang/TIMDR-Tornado-NEXRAD) | Detekcja tornad z realnych danych radaru Dopplera NEXRAD Level II — azymutalny shear rotacji (ugruntowana metoda NSSL) + niezależna sygnatura szczątków TDS (spadek ρhv); walidacja shear-only na potwierdzonych przez SPC przypadkach EF1+ dała istotną statystycznie różnicę (Mann-Whitney, duży rozmiar efektu) — sama TDS i połączony werdykt jeszcze nie sprawdzone na realnych danych |
| [TIMeDR-MUZ](https://github.com/jbackk-lang/TIMeDR-MUZ) | Wcześniejsza linia zarządcy budżetu TIMDR. Aktualna aplikacja rozwijana jest w TSI-MUZ. |
| [topologic](https://github.com/jbackk-lang/topologic) | Biblioteka operatorów sygnałowych: zero-crossing, z-score, korelacja kierunkowa |
| [universal-state-analyzer](https://github.com/jbackk-lang/universal-state-analyzer) | Źródłowa implementacja ringdown_resonance() oraz lokalny protokół testów Manna–Whitneya; zwalidowana na syntetycznym ground truth |

## Formalizmy i rama TIMDR (6)

| Repozytorium | Przeznaczenie |
|---|---|
| [GIA-TIMDR](https://github.com/jbackk-lang/GIA-TIMDR) | Rama badawcza TIMDR: gałęzie M/S, G, K i META-DYNAMICS, Chronoproces, aksjomaty, implementacje i wyniki badań. |
| [TIMDR-Geometry-Formalism](https://github.com/jbackk-lang/TIMDR-Geometry-Formalism) | Gałąź geometryczna G: operator kształtu, krzywizny, skręt i testy powierzchni o znanej geometrii. |
| [TIMDR-Math-Formalism](https://github.com/jbackk-lang/TIMDR-Math-Formalism) | Implementacja gałęzi sygnałowej M/S: operatory, kontrola matematyczna, testy i protokół oceny. |
| [TIMDR-Modal-Formalism](https://github.com/jbackk-lang/TIMDR-Modal-Formalism) | Implementacja gałęzi modalnej K: interferencja, rezonans i synchronizacja faz. |
| [TIMDR-Sygnalizacja](https://github.com/jbackk-lang/TIMDR-Sygnalizacja) | Formalizm sygnałowy TIMDR (anomalia/defekt/rezonans/skręt) na trzech historycznych metodach sygnalizacji — kod Morse'a dźwiękowy, Morse świetlny (lampa Aldisa), semafor flagowy; dekodery + 4 detektory + kontrole pozytywne/negatywne z testem Manna-Whitneya, panel web z obsługą mikrofonu/kamery. Zwalidowane na sygnałach syntetycznych; funkcje na żywym sprzęcie niezweryfikowane w izolowanym środowisku budowy |
| [TIMDR-Time-Formalism](https://github.com/jbackk-lang/TIMDR-Time-Formalism) | Chronoproces i wspólny opis czasowy gałęzi TIMDR; implementacje oraz testy. |

## Modele koncepcyjne (10)

| Repozytorium | Przeznaczenie |
|---|---|
| [Architektura-Mapowania-Zmyslowego-TIMDR](https://github.com/jbackk-lang/Architektura-Mapowania-Zmyslowego-TIMDR) | Sensoryczna brama do modelu pola |
| [Boundary-Matter](https://github.com/jbackk-lang/Boundary-Matter) | Silnik decyzyjny generujący sprzeczne tezy rynkowe |
| [FIELDCORE](https://github.com/jbackk-lang/FIELDCORE) | Kosmos jako układ dwóch skrętów pola |
| [genertor-fotonow](https://github.com/jbackk-lang/genertor-fotonow) | Koncepcyjny generator fotonów oparty na skręcie pola |
| [GSF](https://github.com/jbackk-lang/GSF) | Globalny system finansowy jako pole informacji |
| [KHIPU](https://github.com/jbackk-lang/KHIPU) | Koncepcyjna architektura czteroprocesorowa (TETRAGON-4CPU) |
| [PC_TIMDR](https://github.com/jbackk-lang/PC_TIMDR) | Koncepcyjny procesor geometryczny F4-RED |
| [probabilistic-timdr](https://github.com/jbackk-lang/probabilistic-timdr) | Prawdopodobieństwo i warunki brzegowe w TIMDR |
| [THE_TIMDR_Hyperflow_Engine](https://github.com/jbackk-lang/THE_TIMDR_Hyperflow_Engine) | TIMDR Hyperflow Engine — koncepcyjna pętla percepcyjna (strumień/topologia/przepływ/stabilność); zawiera też zwalidowany numerycznie moduł geometrii trajektorii (krzywizna/skręt na helisie analitycznej) |
| [TIMDR-Multisensory-Meditation-Engine](https://github.com/jbackk-lang/TIMDR-Multisensory-Meditation-Engine) | Multisensoryczna medytacja geometryczna |

## Dokumentacja i archiwa (2)

| Repozytorium | Przeznaczenie |
|---|---|
| [jbackk-lang.github.io](https://github.com/jbackk-lang/jbackk-lang.github.io) | Strona projektów, wizualizacje TIMDR i TSI oraz katalog publicznych repozytoriów. |
| [TIMDR-Concept-Archive](https://github.com/jbackk-lang/TIMDR-Concept-Archive) | Archiwum dawnych projektów koncepcyjnych i ich historii. Podkatalogi nie są liczone jako osobne aktywne repozytoria. |

## Historia

[Poprzedni podział i powiązania kodu](docs/archiwum/2026-11-03-przed-katalogiem-KATEGORIE.md).
