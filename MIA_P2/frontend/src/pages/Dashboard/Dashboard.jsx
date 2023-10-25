import { useState } from 'react';
import { Button } from '@mui/material';
import TextField from '@mui/material/TextField';
import { Link } from 'react-router-dom';

export default function Dashboard() {
  const [text, setText] = useState("");
  const [exit, setExit] = useState("");

  const handleChange = (e) => {
    e.preventDefault();
    setText(e.target.value);
  }

  const handleFileChange = (e) => {
    e.preventDefault();
    const file = e.target.files[0];
    if (file) {
      const reader = new FileReader();
      reader.onload = (event) => {
        const fileContent = event.target.result;
        setText(fileContent);
      };
      reader.readAsText(file);
    }
  }

  const handleClick = (e) => {
    e.preventDefault();

    setExit("Ejecutando...");
    const data = { entry: text }
    fetch(`http://3.88.65.124:8000//api-execute`, {
      method: "POST",
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data)
    })
      .then((res) => res.json())
      .then((data) => { console.log(data); setExit(data.salida); })
      .catch((error) => { console.log(error); setExit(error); });
  }

  const handleClear = (e) => {
    e.preventDefault();
    setText("");
    setExit("");
  } 

  return (
    <div style={{ width: "80%", border: "2px solid red", padding: 10, margin: "auto", marginTop: 50 }}>
      <p>Componentes - Dashboard</p>

      <TextField
        onChange={handleFileChange}
        helperText="Archivo a ejecutar"
        type='file'
        inputProps={{
          accept: '*/*'
        }}
        fullWidth
      />

      <br /> <br />

      <p>Consola</p>
      <TextField
        label="Comandos a Ejecutar"
        multiline
        minRows={10}
        maxRows={10}
        fullWidth
        onChange={handleChange}
        value={text}
      />

      <br /> <br /> <br />
      <div style={{ display: "flex", gap: 10 }}>
        <Button variant="contained" onClick={handleClick}>Ejecutar</Button>
        <Button variant="contained" onClick={handleClear}>Limpiar</Button>
      </div>

      <br /> 

      <p>Salida</p>
      <TextField
        label="Salida comandos"
        multiline
        minRows={10}
        maxRows={10}
        fullWidth
        value={exit}
        disabled={true}
      />

      <br /> <br /> <br />

      <Link to="/login">
        <Button variant="outlined" color="error">Ir a Login</Button>
      </Link>
    </div>
  )
}
