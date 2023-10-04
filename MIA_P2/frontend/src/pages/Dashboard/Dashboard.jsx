import { useState } from 'react';
import { Button } from '@mui/material';
import TextField from '@mui/material/TextField';
import { Link } from 'react-router-dom';

export default function Dashboard() {
   const [text, setText] = useState("");
   const [file, setFile] = useState("");

   const handleChange = (e) => {
      e.preventDefault();
      setText(e.target.value);
   }

   const handleChangeFile = (e) => {
      e.preventDefault();
      console.log("handleChangeFile=======",e.target.files[0]);
      setFile(e.target.files[0]);
   }

   const handleClick = (e) => {
      e.preventDefault();
      // axios request
      // fecth request
      
      console.log("Data enviada", text);

   }


   return (
     <div style={{width:"80%", border:"2px solid red", padding:10, margin: "auto", marginTop:50}}>
       <p>Componentes</p>
       <p>Dashboard</p>

       <TextField
          label="Comandos a Ejecutar"
          multiline
          maxRows={10}
          fullWidth
          onChange={handleChange}

        />
      <br/> <br/> <br/>
      <p> {text} </p>

      <TextField
         type='file'
         inputProps={{ accept: 'image/*' }}
         name="photo"
         onChange={handleChangeFile}
      />

      <br/> <br/> <br/>
      <p>Imgen seleccionada:</p>
      {
         file && (
            <p> {file.name} </p>
         )
      }

      <Button variant="contained" onClick={handleClick}>Enviar</Button>

      <br/> <br/> <br/>

      <Link to="/login">
         <Button variant="outlined" color="error">Ir Login</Button>
      </Link>

     </div>
   )
 }
