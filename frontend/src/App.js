// Default imports from lab
import logo from './logo.svg';
import './App.css';
// Import list
import List from './list/list';

function App() {

  return (
    <div className="App">
      <header className="App-header">
        <h1>
          Cooking Companion
        </h1>
        <p className="App-padding"></p>
        <a
          className="App-link"
          href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
          target="_blank"
          rel="noopener noreferrer"
        >
          Recipes
        </a>
        <p className="App-padding"></p>
        <a
          className="App-link"
          href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
          target="_blank"
          rel="noopener noreferrer"
        >
          Cooks
        </a>
        <p className="App-padding"></p>
        <a
          className="App-link"
          href="https://www.youtube.com/watch?v=dQw4w9WgXcQ"
          target="_blank"
          rel="noopener noreferrer"
        >
          Sign-in
        </a>
        <p className="App-padding"></p>
        <img src={logo} width={125} height={125} className="App-logo" alt="logo" />
      </header>
      <header className="App-body">
        <p>
          Plain text
        </p>
        <List/>
      </header>
    </div>
  );
}


export default App;
