import React, { useEffect, useState } from 'react';
import Iframe from 'react-iframe';
import './PyscriptView.css';

const PyscriptView = ({ runchRrl }) => {
    const [userX , setUserX] = useState(0);
    const [userY , setUserY] = useState(0);
    useEffect(() => {
        const handleMessage = (event) => {
            // 출처 확인 (보안상 중요)
            // if (event.origin !== "http://trusted-origin.com") return;

            // 메시지 타입이 gameCompleted일 때 처리
            if (event.data.type === "gameCompleted") {
                alert("성공! 골드와 보석을 모두 획득하셨습니다!");
            }
            if(event.data.type ==="XY_state"){
                setUserX(event.data.message.x);
                setUserY(event.data.message.y);
                
            }
        };

        // 메시지 이벤트 리스너 추가
        window.addEventListener("message", handleMessage);

        // 컴포넌트 언마운트 시 이벤트 리스너 제거
        return () => {
            window.removeEventListener("message", handleMessage);
        };
    }, []); // 빈 배열을 전달하여 컴포넌트 마운트 시 한 번만 실행되도록 함

    return (
        <div className='PyscriptView'>
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
        </div>
    );
};

export default PyscriptView;
