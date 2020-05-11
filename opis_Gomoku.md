# Gomoku
# Opis zadania
1. Okno wyświetlające siatkę 15 kolumn x 15 wierszy,
informację “Tura gracza 1” lub “Tura gracza 2”, przycisk do resetowania gry
oraz rozwijalną listę wyboru reguł gry.
2. Początkowo pola siatki są puste.
3. Gracze na zmianę stawiają po jednym swoim kamieniuu na wybrane przez siebie pole.
4. Pola w których jest kamien gracza 1 są białe, pola z kamieniami gracza 2
są czarne.
5. Gracze wybierają pole klikając na jego obszar.
○ Wygrywa gracz który pierwszy ustawi pięć(nie więcej) kamieni w linii (poziomo, pionowo
lub po skosie).
6. Gdy gra się kończy, wyświetlane jest okienko z napisem “Wygrał gracz 1” lub
“Wygrał gracz 2”, zależnie kto wygrał grę. Możliwe jest zresetowanie planszy
bez zamykania głównego okna.
7. Reprezentacja reguł gry ma być realizowana poprzez hierarchię klas. Klasa
bazowa definiuje między innymi funkcję wirtualną ktoWygral() nadpisywaną w
klasach pochodnych. Realizowane powinny być przynajmniej dwa zestawy reguł,
jako dwie klasy pochodne.
# Testy
1. Wykonanie po dwa ruchy przez każdego z graczy - monety spadają na dół pola
gry lub zatrzymują się na już wrzuconym żetonie.
2. Ułożenie pionowej linii monet przez jednego gracza - oczekiwana informacja o
jego wygranej.
3. Ułożenie poziomej linii monet przez drugiego gracza - oczekiwana informacja o
jego wygranej.
4. Ułożenie skośnej linii przez dowolnego gracza - oczekiwana informacja o
jego wygranej.
5. Zapełnienie pola gry tak, że żaden gracz nie ułożył linii - oczekiwana informacja
o remisie.
6. Ułożenie linii dłuższej niż 5 przez jednego z graczy - brak informacji o wygranej.
7. Próba ustawienia kamienia na wcześniej ustawiony kamień- brak możliwości wykonania takiego działania.
# Link
https://github.com/MateuszKrasinski/Gomoku
