select wp.nome, wp.inizio, wp.fine
from progetto prog, wp
where wp.progetto = prog.id
    and prog.nome = 'Pegasus';



--2

select distinct pers.id, pers.nome, pers.cognome, pers.posizione
from persona pers, progetto prog, attivitaprogetto ap 
where ap.persona = pers.id
    and ap.progetto = prog.id
    and prog.nome = 'Pegasus'
order by pers.cognome desc;


--3 

select *
from persona pers, progetto prog, attivitaprogetto ap1, attivitaprogetto ap2
where prog.nome = 'Pegasus'
    and ap1.persona = pers.id
    and ap2.persona = pers.id
    and ap1.progetto = prog.id
    and ap2.progetto = prog.id
    and ap1.id <> ap2.id;



--8

select *
from persona p, attivitaprogetto ap, attivitanonprogettuale anp
where  ap.giorno = anp.giorno
    and ap.persona = p.id
    and anp.persona = p.id;