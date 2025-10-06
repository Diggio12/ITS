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