import React from 'react';
import Container from 'react-bootstrap/Container';
import Navbar from 'react-bootstrap/Navbar';
import Button from 'react-bootstrap/Button'; // Button 컴포넌트 추가
import logo_img from '../img_set/logo/CODENAME_green_logo_blank.png'; // 로고 이미지 import
import { TfiControlPlay } from "react-icons/tfi"; // button run icon
import './Navbar.css';

const Navbar_ = ({ onRunClick }) => {
  return (
    <Navbar expand="lg" className="navbar-custom">
      <Container>
        {/* 로고 이미지 추가 */}
        <Navbar.Brand href="#home">
          <img
            src={logo_img}
            width="225" // 로고의 너비 설정, 적절한 크기로 조정해야 할 수 있음
            height="35" // 로고의 높이 설정, 적절한 크기로 조정해야 할 수 있음
            className="d-inline-block align-top" // 로고 이미지 정렬을 위한 클래스
            alt="CODE NAME" // 대체 텍스트 설정
          />
        </Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav" className="justify-content-center">
            <Button 
                variant="light"
                className="mx-3 custom-button"
                onClick={() => onRunClick()}
                style={{
                  color: "#00f224", // 글씨 색상 설정
                  backgroundColor: "black", // 배경색 설정
                  fontWeight: "bold", // 글씨 굵기 설정
                  borderColor: "#00f224", // 테두리 색상 설정
                  borderWidth: "2px", // 테두리 두께 설정
                  borderStyle: "solid", // 테두리 스타일 설정
                }}
              >
      <TfiControlPlay size="25" style={{ fontWeight: "bold" }} /> RUN
    </Button>

        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
}

export default Navbar_;
