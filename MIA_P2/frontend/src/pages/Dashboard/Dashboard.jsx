import { useState } from 'react';
import { Button } from '@mui/material';
import TextField from '@mui/material/TextField';
import { Link } from 'react-router-dom';

export default function Dashboard() {
  const [text, setText] = useState("");
  const [getText, setGetText] = useState("");

  const handleChange = (e) => {
    e.preventDefault();
    setText(e.target.value);
  }


  const handleClick = (e) => {
    e.preventDefault();
    console.log("Data enviada", text);
    fetch(`http://127.0.0.1:8000/api/data`, {
      method: "GET",
    })
      .then((res) => res.json())
      .then((data) => console.log(data)) 
      .catch((er) => console.log(er));
  }


  return (
    <div style={{ width: "80%", border: "2px solid red", padding: 10, margin: "auto", marginTop: 50 }}>
      <p>Componentes - Dashboard</p>
      

      <TextField
        label="Comandos a Ejecutar"
        multiline
        maxRows={10}
        fullWidth
        onChange={handleChange}

      />

      <br /> <br /> <br />

      <Button variant="contained" onClick={handleClick}>Enviar</Button>

      <br /> <br /> <br />

      <p>Respuesta del Servidor</p>
      {getText}

      <br /> <br /> <br />

      <Link to="/login">
        <Button variant="outlined" color="error">Ir Login</Button>
      </Link>

    </div>
  )
}
