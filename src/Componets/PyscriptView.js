import React, { useEffect, useState } from 'react';
import Iframe from 'react-iframe';
import './PyscriptView.css';
// Import the logo image
import logo_img from '../img_set/logo/CODENAME_green_logo.png';

const PyscriptView = ({ runchRrl }) => {
    const [userX , setUserX] = useState(0);
    const [userY , setUserY] = useState(0);
    // State to track if the game has been completed
    const [gameCompleted, setGameCompleted] = useState(false);

    useEffect(() => {
        const handleMessage = (event) => {
            // Check origin here for security
            // if (event.origin !== "http://trusted-origin.com") return;

            if (event.data.type === "gameCompleted") {
                // Set game completion state
                alert("mission!! 성공!");
                setGameCompleted(true);
            } else if (event.data.type === "XY_state") {
                setUserX(event.data.message.x);
                setUserY(event.data.message.y);
            }
        };

        window.addEventListener("message", handleMessage);

        return () => {
            window.removeEventListener("message", handleMessage);
        };
    }, []);

    return (
        <div className='PyscriptView'>
            {!gameCompleted ? (
                <>
                    <div className='PysciptInfo'>
                        <div className='inner-info-box'>
                            <div>
                                <h6>
                                <span style={{fontFamily: "Noto Sans Mono", color: "#00f224"}}>Mission:</span> 
                                <span style={{fontFamily: "EliceDigitalBaeum-Bd",color: "#00f224"}}>기사를 움직여 골드를 획득하세요!</span>
                                </h6>
                            </div>
                            <div>
                                <h6>
                                <span style={{fontFamily: "EliceDigitalBaeum-Bd",color: "#00f224"}}>기사</span>
                                <span style={{fontFamily: "Noto Sans Mono", color: "#00f224"}}>: (x: {userX},y: {userY})</span> 
                                </h6>
                            </div>
                        </div>
                    </div>
                    <div className='IframeWrapper'>
                        <Iframe url={runchRrl}
                            width="500px"
                            height="500px"
                            id="pyscript-iframe"
                            display="block"
                            position="relative"/>
                    </div>
                </>
            ) : (
                // Display the completion logo when the game is completed
                <>
                <div className='PysciptInfo_'>
                        <div className='inner-info-box'>
                        </div>
                    </div>
                    <div className='IframeWrapper'>
                        <div className='CompletionLogo' style={{textAlign: 'center'}}>
                        <a style={{ borderBottom: "none",  color: '#00f224'}} href="https://walla.my/survey/Cdd7bTtIQ8PwHPn2Eit5">
                            <div>
                                <h4 style={{ fontFamily: 'Noto Sans Mono' }}>Mission-clear</h4>
                            </div>
                            <div>
                                <h5 style={{ fontFamily: 'Noto Sans Mono' }}>Go! Next Stage!</h5>
                            </div>
                        </a>
                    </div>
                </div>
                </>
            )}
        </div>
    );
};

export default PyscriptView;
