import React from 'react';

function CardUtente(props) {
  return (
    <div style={{ border: '1px solid #ccc', padding: '10px', margin: '10px', width: '250px' }}>
      <h2>{props.nome}</h2>
      <p>{props.email}</p>
      <img src={props.imgUrl} alt="Avatar utente" style={{ width: '100%', height: 'auto' }} />
    </div>
  );
}

export default CardUtente;

