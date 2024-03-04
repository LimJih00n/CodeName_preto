import logo from './logo.svg';
import './App.css';
import Container from 'react-bootstrap/Container';
import Navbar_ from './Componets/Navbar_';
import SideBar from './Componets/SideBar';
import CodeEditor from './Componets/CodeEditor';
import PyscriptView from './Componets/PyscriptView';
import pre_game_img from './img_set/pre_game_img.png';
import Iframe from 'react-iframe'
import React, { useState, useEffect } from 'react';
import Axios from 'axios';

function App() {
  const [activeComponent, setActiveComponent] = useState('codeEditor');
  const [initCode, setInitCode] = useState('#Run을 눌러 시작하세요!!\n\n#init code: RUN 클릭시 한번만 실행됩니다!\n#기사를 움직일 수 있는 코드를 활용하세요!\n#warrior.set_direction("R") #오른쪽으로 이동\nwarrior.set_direction("R")\n\n#warrior.set_velocity(5,5) #이동속도 지정\nwarrior.set_velocity(5,5)\n#loop 창에서, 언제 아래로 내려가야하는지 알아봅시다.\n');
  const [loopCode, setLoopCode] = useState('#loop code: 진행하는 동안 계속 실행됩니다!\n#x 좌표가 40일때 아래로 이동하세요!\n\n#if warrior.get_x() == 400:#금화 x좌표값이랑 같을때\n#   warrior.set_direction("D")#아래로 방향변경\n\nif warrior.get_x() == 400:\n   warrior.set_direction("D")\n');
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
    setPyurl(`${ENDPOINT}/pyscript_test.html`);
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
        url= {`https://www.notioniframe.com/notion/udhq6shqizb`}
        width= '100%'
        height= '100%'
        />
        
      default:
        return <div>선택된 컴포넌트가 없습니다.</div>;
    }
  };

  return (
    <div className="App">
    <Container>
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
            {loading ? (
              <div className="spinner-box"></div>
            ) : pyUrl === '' ? (
              <div style={{ width: '100%', height: '100%', display: 'flex', justifyContent: 'center', alignItems: 'center', backgroundColor: 'black', borderRadius: "10px"}}>
                <img src={pre_game_img} alt="Placeholder" style={{ maxWidth: '85%', height: 'auto' }} />
              </div>
            ) : (
              <PyscriptView runchRrl={pyUrl}/>
            )}
        </div>
      </div>
    </Container>
    </div>
  );
}

export default App;
