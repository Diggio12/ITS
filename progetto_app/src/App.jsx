import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Saluto from './esercizio_1'
import CardUtente from './esercizio_2'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div>
      <Saluto></Saluto>
      <CardUtente 
        nome="Mario Rossi"
        email="mario.rossi@example.com"
        imgUrl="https://placehold.co/150x150/png"
      />
      <CardUtente 
        nome="Anna Bianchi"
        email="anna.bianchi@example.com"
        imgUrl="https://placehold.co/150x150/jpg"
      />
    </div>
  )
}

export default App
