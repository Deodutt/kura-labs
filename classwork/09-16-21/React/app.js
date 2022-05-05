
function Header (props) {
    return (
      <header>
        <h1>{ props.title }</h1>
        <span className="stats">Players: { props.totalPlayer }</span>
      </header>
    );
  }
  
function Player (props) {
      return (
          <div className='player'>
              <span className='player-name'>
                  <button className="remove-player" onClick={() => props.removePlayer(props.id)}>X</button>
                  {props.name}
              </span>

              <Counter />
          </div>
    );
}

class Counter extends React.Component {

    constructor() {
        super()
        this.state = {
            score: 0
        };
    }

    incrementScore = () => {
        this.setState( prevState => {
            return { 
            score: prevState.score + 1
            } 
        });
    }

    decrementScore = () => {
        this.setState( prevState => {
            return { 
            score: prevState.score - 1
            } 
        });
    }

    render () {
        return (
            <div className="counter">
                <button className="counter-action decrement" onClick={this.decrementScore.bind(this)}>-</button>
                <span className="counter-score">{this.state.score}</span>
                <button className="counter-action increment" onClick={this.incrementScore.bind(this)}>+</button>
            </div>
        );
    }
}

class App extends React.Component {


    state = {
        players: [
            {
                name: "Tyrone",
                id: 1
            },
            {
                name: "Tasha",
                id: 2
            },
            {
                name: "Nikki",
                id: 3
            }

        ]
    };

    handleRemovePlayer = (id) => {
        this.setState( prevState => {
            return {
                players: this.state.players.filter( p => p.id !== id )
                };
        });

    }
    


    render() {
        return (
            <div className="scoreboard">
                <Header title='scoreboard' totalPlayer={this.state.players.length} />
                
                {this.state.players.map( player => 
                    <Player
                    name={player.name}
                    id={player.id}
                    score={player.score}
                    key={player.id.toString()}
                    removePlayer={this.handleRemovePlayer}
                    />
                    
    
                )}
            </div>
        );
    }
}


  ReactDOM.render(
    <App />,
    document.getElementById('root')
  );