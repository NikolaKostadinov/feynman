import { useState, useEffect } from "react"

import dataService from './services/data'

import SideBarDiv from "./components/SideBarDiv";
import LineChart from "./components/LineChart";

const App = () => {
  const [dataX, setDataX] = useState([])
  const [dataF, setDataF] = useState([])

  useEffect(() => {
    dataService
      .getUpTo100()
      .then(initialData => {
        setDataX(initialData.x)
        setDataF(initialData.f)
      })
  }, [])

  return (
    <>
      <header>
        <h1>FEYNMANN</h1>
      </header>
      <div className="App">
        <div className="split">
          <SideBarDiv
            id='leftBar'
            srcPath='img2.jpg'
            alt='boys in jackets'
            text={ <> SEXY DILFS ONE KILLOMETER AWAY FROM YOU GETTING TOO LONELY </> }
          />
          
          <LineChart 
          dataX={dataX}
          dataF={dataF}
          labelText='chart'
        />

          <SideBarDiv
            id='rightBar'
            srcPath='img3.jpg'
            alt='minion-vegeta'
            text={ <> HOT DILF NEXT TO YOU IS CRAVING YOUR JUICY ASS </> }
          />
        </div>
      </div>
    </>
  );
}

export default App;
