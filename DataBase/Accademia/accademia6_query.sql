--Quanti sono gli strutturati di ogni fascia?

select posizione, count(posizione)
from Persona
group by posizione;

--Quanti sono gli strutturati con stipendio ≥ 40000?
select count(posizione)
from Persona
where stipendio >= 40000;

--Quanti sono i progetti già finiti che superano il budget di 50000?
select count(*)
from Progetto
where budget > 50000 and fine < current_date


---Qual è la media, il massimo e il minimo delle ore delle attività relative al progetto "Pegasus" ?
select avg(oreDurata), min(oreDurata), max(oreDurata)
from Progetto as pr, AttivitaProgetto as ap
where pr.id = ap.progetto and pr.nome = 'Pegasus';


---Quali sono le medie, i massimi e i minimi delle ore giornaliere dedicate al progetto ‘Pegasus’ da ogni singolo docente?
select avg(oreDurata), min(oreDurata), max(oreDurata)
from Progetto as pr, AttivitaProgetto as ap, Persona as pers 
where pr.id = ap.progetto and pr.nome = 'Pegasus' and pers.id = ap.persona;