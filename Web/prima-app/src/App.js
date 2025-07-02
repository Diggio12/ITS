import { useState } from 'react';
import './App.css';
import { anagrafica } from "./dati"

function App() {

  let nome = "Mattia";

  const [nome1, setNome1] = useState(nome);

  const [persone, setPersone] =  useState(anagrafica);

  const cambiaNome = () => {
    console.log(nome);
    nome = "Mario";
    setNome1(nome);
    console.log(nome)
  }

  const elimina = (id) => {
    const newAnag = persone.filter(p => p.id !== id);
    setPersone(newAnag)
  }
  const cliccami = (nome, cognome) => {
    alert("Ciao" + nome + " " + cognome);
  }

  return(
    <div className='App'>
      <h1>{nome1}</h1>
      <button onClick={cambiaNome} className='btn btn-primary'>
        Cambia nome
      </button>
      
      {
        persone.map((p) => {
          return (<div><span>{p.nome} {p.cognome}</span><button>ELimina</button></div>)
        })
      }
    </div>
  );
}

export default App;
