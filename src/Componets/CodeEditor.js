import './CodeEditor.css'
import React, { useEffect, useRef, useState } from 'react';
import Editor from "@monaco-editor/react";
import Axios from 'axios'
import Tab from 'react-bootstrap/Tab';
import Tabs from 'react-bootstrap/Tabs';
import OverlayTrigger from 'react-bootstrap/OverlayTrigger';
import Tooltip from 'react-bootstrap/Tooltip';

function CodeEditor({ initCode, setInitCode, loopCode, setLoopCode }) {
  // 각 탭별 코드를 저장할 상태
  const [currentTab, setCurrentTab] = useState('init'); // 현재 선택된 탭 상태
  const [userTheme, setUserTheme] = useState('light');
  const [fontSize, setFontSize] = useState(20);
  const [loading, setLoading] = useState(false);
  const editorRef = useRef(null); // 에디터 컨테이너의 ref
  const [editorHeight, setEditorHeight] = useState('500px'); // 초기 에디터 높이
  const [editorWidth, setEditorWidth] = useState('100%'); // 초기 에디터 너비
  useEffect(() => {
    const observer = new ResizeObserver(entries => {
      for (let entry of entries) {
        setEditorWidth(`${entry.contentRect.width}px`);
        setEditorHeight(`${entry.contentRect.height}px`);
      }
    });

    if (editorRef.current) {
      observer.observe(editorRef.current);
    }

    return () => observer.disconnect();
  }, []);

  const options = {
    fontSize: fontSize
  }
  const renderTooltip = (props, text) => (
    <Tooltip id="button-tooltip" {...props}>
      {text}
    </Tooltip>
  );
  const TabTitle = ({ title, tooltipText }) => (
    <OverlayTrigger
      placement="top"
      overlay={(props) => renderTooltip(props, tooltipText)}
    >
      <span>{title}</span>
    </OverlayTrigger>
  );

  // 현재 탭에 따른 코드를 변경하는 함수
  const handleTabSelect = (key) => {
    setCurrentTab(key);
  }

  // 에디터의 내용이 변경될 때 호출되는 함수
  const handleEditorChange = (value) => {
    if(currentTab === 'init') {
      setInitCode(value);
    } else {
      setLoopCode(value);
    }
  }

  return (
    <div className="Editor_container">
    <div className='EditorInfo'>
    <Tabs
      defaultActiveKey="init"
      id="uncontrolled-tab-example"
      className="mb-3"
      onSelect={handleTabSelect} // 탭이 선택될 때 호출될 함수 설정
      style={{
            width:'100%',
            backgroundColor: 'aquamarine',
          }}
    >
      <Tab eventKey="init" title={<TabTitle title="Init" tooltipText="Initialize your code here"/>}></Tab>
          <Tab eventKey="loop" title={<TabTitle title="Loop" tooltipText="Loop your code here"/>}></Tab>
      
      </Tabs>
    </div>
      <div className='CodeEditorWrapper'>
        <div ref={editorRef} style={{ width: '100%', height: '100%' }}>
            <Editor
            options={options}
              height={editorHeight}
              width={editorWidth}
              theme={userTheme}
              defaultLanguage="python"
              defaultValue="# Enter your code here"
              
              onChange={handleEditorChange}
              value={currentTab === 'init' ? initCode : loopCode} // 현재 탭에 따른 코드를 에디터에 표시
            />
        </div>
        </div>
    </div>
  );
}

export default CodeEditor;
