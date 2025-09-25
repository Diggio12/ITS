create table statoordine (
    id serial primary key,
    nome stringa not null,
    unique(nome)
);

create table nazione (
    nome stringa primary key
);

create table regione (
    nome stringa not null,
    nazione stringa not null,
    primary key (nome, nazione),

    foreign key(nazione)
        refences nazione(nome)
);

create table citta (
    id serial primary key,
    nome stringa not null,
    regione stringa not null,
    nazione stringa not null,
    unique(nome, regione, nazione)
);

create table Direttore(
    nome Stringa not null,
    cognome Stringa not null,
    cf CodiceFiscale not null,
    anni_servizio PosInteger not null,
    data_nascita date not null,
    dipartimento Stringa not null,
    città integer not null,

    primary key(cf),
    unique(cf),
    foreign key(dipartimento) references Dipartimento(nome),
    foreign key(città) references citta(id)
);

create table Dipartimento (
	nome Stringa primary key,
	indirizzo Indirizzo not null
	citta integer not null,
    direttore CodiceFiscale not null,
    ordine integer not null,
    
	foreign key (citta) references citta(id),
    foreign key (direttore) references Direttore(cf),
    foreign key (ordine) references Ordine(id)
);

create table Ordine(
    data_stipula date not null,
    imponibile RealGEZ not null,
    aliquota RealBZO not null,
    descrizione StringaM not null,
    id integer not null,
    dipartimento stringa not null,
    statoordine integer not null,
    fornitore Partita_iva not null,

    primary key(id),
    foreign key(dipartimento) references Dipartimento(nome),
    foreign key(statoordine) references StatoOrdine(id),
    foreign key(fornitore) references Fornitore(partita_iva)
);

create table StatoOrdine(
    nome Stringa not null,
    id integer not null,
    ordine integer not null,

    primary key(id),
    foreign key(ordine) references Ordine(id)
);

create table Fornitore(
    ragione_sociale Stringa not null,
    partita_iva Partita_iva not null,
    indirizzo Indirizzo not null,
    telefono Telefono not null,
    email Email not null,
    città integer not null,
    ordine integer not null,

    primary key(partita_iva),
    unique(partita_iva),
    foreign key(città) references citta(id),
    foreign key(ordine) references Ordine(id)
);