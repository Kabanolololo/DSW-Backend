## Wymagania na poszczególne oceny

### 3.0
* GOTOWE
  
### 3.5
* GOTOWE

### 4.0
* GOTOWE

### 4.5
* wszystkie wymagania na ocenę 4.0
* dodanie prostego uwierzytelnienia:
  * rozszerzenie API o endpointy `POST /register` oraz `POST /login`, które pozwalają na rejestrację oraz logowanie nowego użytkownika:
    * endpoint `POST /register` powinien przyjmować w body następujące parametry: `username`, `password`, `repeated_password`
    * endpoint `POST /login` powinien przyjmować w body następujące parametry: `username`, `password`
  * obsługa błędów rejestracji i logowania:
    * w endpoincie `POST /register` wszystkie pola muszą być niepuste, a hasła muszą się zgadzać
    * w endpoincie `POST /login` powinien być zwrócony błąd, jeżeli użytkownik o podanej nazwie i haśle nie istnieje

### 5.0
* wszystkie wymagania na ocenę 4.5
* dodanie zwracania tokenu autoryzacyjnego w formacie JWT do endpointu `POST /login`, który zawiera ID użytkownika
* dodanie autoryzacji do endpointów za pomocą tokena JWT:
  * każdy request powinien być walidowany pod kątem obecności nagłówka `Authorization: Bearer <token>` i w przypadku jego braku powinien być zgłaszany odpowiedni błąd
  * jeżeli token jest niepoprawny (nie zawiera wymaganych danych lub ID użytkownika nie istnieje w bazie), to powinien zostać zwrócony błąd