import { useState } from 'react';
import Container from 'react-bootstrap/Container';
import Navbar from 'react-bootstrap/Navbar';
import { FaMoon, FaSun } from 'react-icons/fa';
import  '../styling/navbar.css';

function NavBar() {
  const [darkMode, setDarkMode] = useState(false);

  const toggleTheme = () => {
    setDarkMode(!darkMode);

    if (!darkMode) {
      document.body.style.backgroundColor = "#121212";
      document.body.style.color = "white";
       document.body.style.transition = "all 0.3s ease"
    } else {
      document.body.style.backgroundColor = "white";
      document.body.style.color = "black";
      document.body.style.transition = "all 0.3s ease"
    }
  };

  return (
    <Navbar bg={darkMode ? "dark" : "light"} variant={darkMode ? "dark" : "light"}>
      <Container className="d-flex justify-content-between align-items-center">
        
        <Navbar.Brand className='fs-2'>BetrayalAI</Navbar.Brand>    
        <div
          onClick={toggleTheme}
          style={{
            width: "40px",
            height: "40px",
            borderRadius: "50%",
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            cursor: "pointer",
            backgroundColor: darkMode ? "#fff" : "#121212",
            color: darkMode ? "#000" : "#fff",
            transition: "all 0.3s ease"
          }}
        >
          {darkMode ? <FaSun /> : <FaMoon />}
        </div>
        
      <span className='dev-text'>Developed By Pranjal</span>

      </Container>
    </Navbar>
  );
}

export default NavBar;