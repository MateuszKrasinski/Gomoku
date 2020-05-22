# Gomoku
# Opis zadania
Projekt podobny do Cztery w rzędzie z listy projektów.
https://pl.wikipedia.org/wiki/Gomoku
1. Okno wyświetlające siatkę 15 kolumn x 15 wierszy,
informację o turze gracza, przycisk do resetowania, menu 
do wyboru reguł gry(kto zaczyna, vs AI lub vs Player, Standardowe zasady lub swap2 zasady)
2. Początkowo pola siatki są puste.
3. Gracze na zmianę stawiają po jednym swoim kamieniu na wybrane przez siebie pole.
4. Pola w których jest kamien gracza 1 są białe, pola z kamieniami gracza 2
są czarne.
5. Gracze wybierają pole klikając na jego obszar.
6. Wygrywa gracz który pierwszy ustawi pięć kamieni w linii (poziomo, pionowo
lub po skosie).
7. Gdy gra się kończy, wyświetlane jest okienko z napisem “Wygrał gracz 1” lub
“Wygrał gracz 2”, zależnie kto wygrał grę. Możliwe jest zresetowanie planszy
bez zamykania głównego okna.
8. Reprezentacja reguł gry ma być realizowana poprzez hierarchię klas. Klasa
bazowa  Game() definiuje między innymi funkcję wirtualną playGame() nadpisywaną w
klasach pochodnych. Realizowane powinny być przynajmniej dwa zestawy reguł,
jako dwie klasy pochodne.
# Testy
1. Ułożenie pionowej linii i przez jednego gracza - oczekiwana informacja o
jego wygranej.
2. Ułożenie poziomej linii  przez drugiego gracza - oczekiwana informacja o
jego wygranej.
3. Ułożenie skośnej linii przez dowolnego gracza - oczekiwana informacja o
jego wygranej.
4. Zapełnienie pola gry tak, że żaden gracz nie ułożył linii - oczekiwana informacja
o remisie.
# Link
https://github.com/MateuszKrasinski/Gomoku
