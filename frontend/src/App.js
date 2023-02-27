import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>
          Cooking Companion
        </h1>
        <a
          className="App-link"
          href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
          target="_blank"
          rel="noopener noreferrer"
        >
          Add a Recipe
        </a>
        <img src={logo} width={25} height={25} className="App-logo" alt="logo" />
      </header>
      <header className="App-body">
          <a>Hello Worlda</a>
      </header>
    </div>
  );
}

export default App;
