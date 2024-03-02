import React from 'react';
import './SideBar.css';
import { TfiAgenda, TfiSettings } from "react-icons/tfi";
import OverlayTrigger from 'react-bootstrap/OverlayTrigger';
import Tooltip from 'react-bootstrap/Tooltip';


const SideBar = ({ setActiveComponent }) => {
    return (
        <div className="sidebar">    
            <div className="sidebarWrapper">
                <h6 className="sidebarTitle" >DASH</h6>
                <div className="sidebarIcon" onClick={() => setActiveComponent('notionPage')}>
                    <OverlayTrigger
                        placement="right"
                        delay={{ show: 10, hide: 40 }}
                        overlay={<Tooltip id="agenda-tooltip">Agenda</Tooltip>}
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
                        overlay={<Tooltip id="settings-tooltip">Settings</Tooltip>}
                    >
                        <button style={{ background: "transparent", border: "none" }}>
                            <TfiSettings size="25" color= "#00f224"/>
                        </button>
                    </OverlayTrigger>
                </div>
            </div>
        </div>
    );
}

export default SideBar;
