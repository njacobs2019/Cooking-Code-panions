// Default imports from the React tutorial
import logo from './logo.svg';
import './App.css';

// Import list
import List from './List/List';



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
          href="https://www.youtube.com/watch?v=Pfdyuz30oQU"
          target="_blank"
          rel="noopener noreferrer"
        >
          Recipes
        </a>
        <p className="App-padding"></p>
        <a
          className="App-link"
          href="https://www.youtube.com/watch?v=CGoI2-kIkkc"
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
      <body className="App-body">
        <p className="App-column">
          Ingredients
          <List/>
        </p>
        <p className="App-padding"></p>
        <p className="App-column">
          Instructions
          <List/>
        </p>
        
      </body>
    </div>
  );
}


export default App;
