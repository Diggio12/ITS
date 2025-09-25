create domain CodiceFiscale as char(16);

create domain RealGEZ as real
    check(value >= 0);

create domain IntGEZ as integer
    check(value >= 0);

create domain IntGZ as integer
    check(value > 0);

create domain Telefono as char(20)
 check(value '[0-9]*10');

create domain Email as char(100)
    check(value ~ '%^[A-Za-z0-9._%\-+!#$&/=?^|~]+@[A-Za-z0-9.-]+[.][A-Za-z]+$%');

create domain Partita_iva as char(11)
    check(value ~ '^[0-9]{11}');

create type StatoOrdine as 
    enum('in preparazione', 'inviato', 'da saldare', 'saldato');