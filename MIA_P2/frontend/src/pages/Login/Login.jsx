import { Button } from "@mui/material";
import { Link } from "react-router-dom";

export default function Login() {
   return (
     <>
       <p>Componentes</p>
       <p>Login</p>

       <Link to="/">
         <Button  variant="contained" color="success">Ir Dashboard</Button>
      </Link>

     </>
   )
 }
