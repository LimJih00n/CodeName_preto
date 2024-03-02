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
                                <h5>Mission: 기사를 움직여 골드를 획득하세요!</h5>
                            </div>
                            <div>
                                <h6>기사: (x: {userX},y: {userY})</h6>
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
                <div className='CompletionLogo' style={{textAlign: 'center', marginTop: '50px'}}>
                    <a href="YOUR_DESIRED_URL_HERE">
                        <img src={logo_img} alt="Completion Logo" style={{maxWidth: '100%', height: 'auto'}}/>
                    </a>
                </div>
            )}
        </div>
    );
};

export default PyscriptView;
