import React from 'react';
import Container from 'react-bootstrap/Container';
import Navbar from 'react-bootstrap/Navbar';
import Button from 'react-bootstrap/Button'; // Button 컴포넌트 추가
import './Navbar.css'
const Navbar_ = ({ onRunClick }) => {
  return (
    <Navbar expand="lg" className="navbar-custom">
      <Container>
        <Navbar.Brand href="#home">CODE NAME</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav" className="justify-content-center">
          <Button 
            variant="light" // 버튼의 배경색을 흰색으로 설정
            className="mx-3" // 버튼 주변의 여백을 추가
            onClick={() => onRunClick()}
            style={{ color: 'aquamarine' }} // 인라인 스타일을 사용하여 버튼 내의 글씨 색상을 aquamarine으로 설정
          >
            RUN
          </Button>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default Navbar_;
