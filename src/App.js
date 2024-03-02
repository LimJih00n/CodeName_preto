import logo from './logo.svg';
import './App.css';
import Container from 'react-bootstrap/Container';
import Navbar_ from './Componets/Navbar_';
import SideBar from './Componets/SideBar';
import CodeEditor from './Componets/CodeEditor';
import PyscriptView from './Componets/PyscriptView';
import Iframe from 'react-iframe'
import React, { useState, useEffect } from 'react';
import Axios from 'axios';

function App() {
  const [activeComponent, setActiveComponent] = useState('codeEditor');
  const [initCode, setInitCode] = useState('#RUN 시 한번만 실행됩니다!');
  const [loopCode, setLoopCode] = useState('#진행하는 동안 계속 실행됩니다!');
  const [pyUrl , setPyurl] = useState('');
  const [loading, setLoading] = useState(false);

  const ENDPOINT = "https://codename-preto-heroku-c7a4c4a3942d.herokuapp.com";

  function onRunClick(){
    setLoading(true);
    Axios.post(
      `${ENDPOINT}/compile`
      , {
      initcode: initCode,
      loopcode: loopCode
  }).then(res=>{
    console.log(res.data);
    setPyurl(`${process.env.PUBLIC_URL}/pyscript_test.html`);
    console.log(`${process.env.PUBLIC_URL}/pyscript_test.html`);
  }).then(()=>{
    setLoading(false);
  })
  }

  // 중앙 컨테이너에 렌더링할 컴포넌트를 결정하는 함수
  const renderCenterComponent = () => {
    switch (activeComponent) {
      case 'codeEditor':
        return <CodeEditor initCode={initCode} setInitCode={setInitCode} loopCode={loopCode} setLoopCode={setLoopCode} />;
      case 'notionPage':
        // 노션 페이지를 렌더링하는 경우, 노션 페이지의 URL을 iframe src 속성에 설정해야 합니다.
        return <Iframe 
        url= {`${process.env.PUBLIC_URL}/notion_test.html`}
        width= '100%'
        height= '100%'
        />
        
      default:
        return <div>선택된 컴포넌트가 없습니다.</div>;
    }
  };

  return (
    <Container>
      
    <div className="App">
      <div className="Nav">
        <Navbar_ onRunClick={onRunClick}/>

      </div>
      <div className="body">
        <div className="left-container">
            <SideBar setActiveComponent={setActiveComponent}/>
        </div>
        <div className="center-container">
          {renderCenterComponent()}
        </div>
        <div className="right-container">
        {loading ? ( //loading주어야 새로고침함!!!
                        <div className="spinner-box">
                            
                        </div>
                    ) : ( 
                      <PyscriptView runchRrl={pyUrl}/>
                    )}
          
        </div>
      </div>
    </div>
    </Container>
  );
}

export default App;
