import logo from './icone.png';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <p>HEADER</p>
      </header>
      <a>TutorIA - Um Tutor Virtual</a>
      <img src={logo} className="TutorIA-logo" alt="logo" />
      <p></p>
      <button>Registrar</button>
      <p></p>
      <button>Logar</button>
    </div>
  );
}

export default App;
