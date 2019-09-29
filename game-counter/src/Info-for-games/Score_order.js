import React, {Component}from 'react';
//import logo from './logo.svg';
import './Score_order.css';
import GameData from './counter';


class tableScore extends Component { render(){
  return (
    <div className="App">
      <h1>Score Keeper</h1>


    test{GameData.map((PlayerID, index)=>{
      return <h1> Player name: {PlayerID.name} </h1>

    })}
    <div className="Gamecount">

    {GameData.map((GameScores, index)=>{
      return <p> 	game count: {GameScores.score}</p> 
    })}
    </div>
    
    </div>


  );
};
}

export default tableScore;
