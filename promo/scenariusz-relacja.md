# Relacja FB/IG — Historia animacji (10 plansz)

Plansze pionowe **1080×1920** (9:16), renderowane @2x, gotowe jako kolejne
klatki Relacji na Facebooku i Instagramie.

Estetyka 1:1 z portalem: ciepła czerń `#0f0e13`, bursztyn `#ffb320`, perforacja
taśmy filmowej, outline'owe numery klatek (Archivo Black / Space Grotesk / IBM
Plex Mono). Generator: `build_stories.py` → `story-1..10.png`.

**Link (naklejka „Link"):** `https://futureshow.pl/historia-animacji/` (działa też dłuższa ścieżka `…/futureshow/projects/historia-animacji/`)

## Łuk narracyjny

| # | Plansza | Rola |
|---|---------|------|
| 1 | „Historia animacji" + 430/231/30 | **identyfikacja** — okładka, motyw taśmy |
| 2 | „Animacja jest starsza niż kino" (1833) | **hak** — zaskakujący, prawdziwy fakt zatrzymuje scroll |
| 3 | 430 filmów · 231 twórców · 30 rozdziałów | **skala** |
| 4 | „Ułożone według kanonu" (Bendazzi, Furniss, Sitkiewicz, Giżycki) | **wiarygodność** — to nie przypadkowa playlista |
| 5 | Pionierzy (Fenakistiskop → Steamboat Willie) | **głębia 1** — początki |
| 6 | Mistrzowie świata (McLaren → Miyazaki) | **głębia 2** — kanon |
| 7 | Polska szkoła (Starewicz → Bagiński, Oscary) | **duma lokalna** — hak dla polskiego odbiorcy |
| 8 | „Cała oś czasu" — 1833 → 2005 | **struktura** — sweep 30 rozdziałów |
| 9 | „Klikasz kartę — oglądasz film" | **mechanika** — jak działa portal |
| 10 | „Oglądaj." + link | **CTA** |

Hak z planszy 2 („animacja starsza niż kino") to najmocniejszy pojedynczy
element — fenakistiskop 1833 wyprzedza Lumière'ów (1895) o 62 lata. Plansza 7
(Polska szkoła + dwa Oscary: Tango 1983, nominacja Katedra 2003) jest lokalnym
punktem dumy — mocna jako samodzielny post.

## Wskazówki publikacji

- **Naklejka „Link":** plansza 10 (i opcjonalnie 1).
- **Tempo:** plansze-katalogi (5–8) zostaw na ~6 s — są do przeczytania tytułów.
- **Tekst od siebie (1. klatka):** „Ułożyłem całą historię animacji — 430 filmów
  w 30 rozdziałach wg kanonu Bendazziego. Od 1833 do dziś. Wątek 👇".
- **Highlight:** zapisz jako wyróżnioną Relację „Historia animacji".
- **Samodzielne posty:** plansze 2 (hak), 7 (Polska szkoła) i 8 (oś czasu).
- **Publiczność EN:** portal jest dwujęzyczny — plansza 2 („Animation is older
  than cinema") świetnie działa jako pojedynczy post na Reddit r/animation /
  r/InternetIsBeautiful.

## Uwaga o danych

Liczby (430 filmów, 231 twórców, 30 rozdziałów) i przypisania (reżyser, rok)
pochodzą z `data.js` portalu. Odznaki „Oscar/nominacja" na planszy 7: Tango —
Oscar 1983; Katedra — nominacja do Oscara 2003.

## Edycja

Treść i kolejność: lista `SLIDES` + funkcje `s_*` na końcu `build_stories.py`.
Po zmianie: `python3 build_stories.py`.
