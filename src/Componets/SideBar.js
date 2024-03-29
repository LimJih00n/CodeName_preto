import React from 'react';
import './SideBar.css';
import { TfiAgenda, TfiSettings } from "react-icons/tfi";
import OverlayTrigger from 'react-bootstrap/OverlayTrigger';
import Tooltip from 'react-bootstrap/Tooltip';
import { FaPython } from "react-icons/fa";

const SideBar = ({ setActiveComponent }) => {
    return (
        <div className="sidebar">    
            <div className="sidebarWrapper">
                <h6 className="sidebarTitle" >DASH</h6>
                <div className="sidebarIcon" onClick={() => setActiveComponent('notionPage')}>
                    <OverlayTrigger
                        placement="right"
                        delay={{ show: 10, hide: 40 }}
                        overlay={<Tooltip id="agenda-tooltip">Class</Tooltip>}
                    >
                        <button style={{ background: "transparent", border: "none" }}>
                            <TfiAgenda size="25" color= "#00f224"/>
                        </button>
                    </OverlayTrigger>
                </div>
                <div className="sidebarIcon" onClick={() => setActiveComponent('codeEditor')}>
                    <OverlayTrigger
                        placement="right"
                        delay={{ show: 10, hide: 40 }}
                        overlay={<Tooltip id="settings-tooltip">Coding</Tooltip>}
                    >
                        <button style={{ background: "transparent", border: "none" }}>
                            <FaPython size="25" color= "#00f224"/>
                        </button>
                    </OverlayTrigger>
                </div>
            </div>
        </div>
    );
}

export default SideBar;
