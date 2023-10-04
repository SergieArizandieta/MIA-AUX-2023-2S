import {BrowserRouter,Route,Routes} from 'react-router-dom';
import Dashboard from './pages/Dashboard/Dashboard';
import Login from './pages/Login/Login';

export default function App() {

  return (
    <BrowserRouter>
        <Routes>

          <Route path="/" element={<Dashboard/>} />
          <Route path="/login" element={<Login/>} />

        </Routes>
    </BrowserRouter>
  )
}
