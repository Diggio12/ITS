begin transaction;
set constraints all deferred;


create domain posinteger as integer
    check (value >= 0);

create domain stringam as varchar(100);

create domain codIATA as char(3);

create table compagnia(
    nome stringam primary key,
    annofondaz posinteger
);

create table volo(
    codice posinteger not null,
    comp stringam not null,
    primary key (codice, comp),
    durataMinuti posinteger not null,
    foreign key (comp)
        references compagnia(nome)...........
);

create table aereoporto(
    codice codIATA primary key,
    nome stringam not null
);

create table luogoaereoporto (
    aereoporto codIATA primary key,
    citta stringam not null,
    nazione stringam not null,
    foreign key (aereoporto)
        references aereoporto(codice) deferrable
);

alter table aereoporto
    add constraint aereoporto_luogoaereoporto_fk
        foreign key (codice)
        references luogoaereoporto(aereoporto) deferrable;


create table arrpart (
    codice posinteger not null,
    comp stringam not null,
    primary key (codice, stringam),
    foreign key (codice, comp)
        references volo(codice, comp) deferrable,
    partenza codIATA not null,
    arrivo codIATA not null,
    foreign key (partenza)
        references aereoporto(codice)
    foreign key (arrivo)
        references aereoporto(codice)
    
);


alter table volo
    add constraint volo_arrpart_fk
    foreign key (codice, comp)
        references arrpart(codice, comp) deferrable;


commit;