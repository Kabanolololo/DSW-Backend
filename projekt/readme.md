## Wymagania na poszczególne oceny

### 3.0
* GOTOWE
  
### 3.5
* GOTOWE

### 4.0
* GOTOWE

### 4.5
* GOTOWE

### 5.0
* dodanie zwracania tokenu autoryzacyjnego w formacie JWT do endpointu `POST /login`, który zawiera ID użytkownika
* dodanie autoryzacji do endpointów za pomocą tokena JWT:
  * każdy request powinien być walidowany pod kątem obecności nagłówka `Authorization: Bearer <token>` i w przypadku jego braku powinien być zgłaszany odpowiedni błąd
  * jeżeli token jest niepoprawny (nie zawiera wymaganych danych lub ID użytkownika nie istnieje w bazie), to powinien zostać zwrócony błąd