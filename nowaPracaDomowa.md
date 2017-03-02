### Zadanie

Napisz obiektowo program, który będzie obsługiwał zapisywanie się studentów na zajęcia.

Stwórz klasę 'Student'. Klasa ta ma posiadać podane atrybuty:
  * `id` - liczba całkowita. Powinna być unikalna w całym systemie.
  * `index` - liczba całkowita. Jest to numer indeksu studenta.
  * `name` - string.
  * `surname` - string.
  * `grade` - liczba całkowita. Jest to ocena z zajęć. 

Klasa powinna mieć też nastepujące metody:
  * konstruktor - powinien przyjmować indeks, imię i nazwisko. Id powinno być nadawane automatycznie. Ocena początkowo powinna być ustawiona na None.
  * atrybut id powiniem mieć możliwość wyłącznie odczytu.

Stwórz klasę 'Teacher'. Klasa ta ma posiadać podane atrybuty:
  * `id` - liczba całkowita. Powinna być unikalna w całym systemie.
  * `name` - string
  * `surname` - string.
 
Klasa powinna mieć też nastepujące metody:
  * konstruktor - powinien przyjmować imię i nazwisko
  * atrybut id powiniem mieć możliwość wyłącznie odczytu.
  
####Generowanie unikalnego id dla produktu:
W dalszej części programu będziemy chcieli identyfikować naszych studentów i wykładowców po ich id. Dlatego musimy zagwarantować że każdy z stworzonych obiektów będzie miał unikalny numer identyfikacyjny. W tym celu w obu klasach powinniśmy zdefiniować statyczną zmienną ```next_id```, którą będziemy nadawać obiektom w konstruktorze i tam będzie ona zwiększana.



Napisz klasę `Course`. Jest to klasa opisująca kurs. Klasa ta ma posiadać podane atrybuty:
  * `name` - Nazwa przedmiotu
  * `description` - Opis przedmiotu
  * `teacher` - obiekt klasy `Teacher`. Jest to prowadzący zajęcia.
  * `students` - lista z obiektami klasy `Student`. Są to studenci zapisani na zajęcia.
 
Klasa powinna mieć też nastepujące metody:
  * konstruktor - przyjmujący w parametrach nazwę przedmiotu, opis oraz prowadzącego typy Teacher
  * `add_student(new_student)` - metoda ta powinna dodawać nowego studenta do tablicy ze studentami. 
  * `remove_student(student_id)` - metoda ta powinna usuwać studenta z przedmiotu. Jeśli student o takim id nie jest zapisany na kurs powinien wypisać się stosowny komunikat.
  * `change_student_grade(student_id, grade)` - metoda ta powinna zmianiać ocenę u studenta o podanym id. Jeśli ocena nie jest liczbą całkowitą z zakresu od 2 do 5 powiniem wypisać się stosowny komunikat. Jeśli student o takim id nie jest zapisany na kurs powinien wypisać się stosowny komunikat.
  * `print()` - metoda drukująca informację o przedmiocie. Powinny się znaleźć tu informacje: nazwa i opis przedmiotu, kto go prowadzi, oraz lista studenów zawierająca ich imiona, nazwiska, indeksy i oceny.

