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
      <Container className="d-flex justify-content-between">
        {/* Logo on the left side */}
        <Navbar.Brand href="#home" className="me-auto">
          <img
            src={logo_img}
            width="225"
            height="35"
            className="d-inline-block align-top"
            alt="CODE NAME"
          />
        </Navbar.Brand>
        
        {/* Centered button, but with manual adjustment for visual centering */}
        <div className="d-flex justify-content-center flex-grow-1">
          <Button 
            variant="light"
            className="custom-button"
            onClick={onRunClick}
            style={{
              color: "#00f224",
              backgroundColor: "black",
              fontWeight: "bold",
              borderColor: "#00f224",
              borderWidth: "2px",
              borderStyle: "solid",
            }}
          >
            <TfiControlPlay size="25" style={{ fontWeight: "bold" }} /> RUN
          </Button>
        </div>
        
        {/* Invisible spacer or additional content on the right for balance */}
        <div className="me-auto" style={{ width: '225px', height: '35px' }}></div>
      </Container>
    </Navbar>
  );
}


export default Navbar_;
