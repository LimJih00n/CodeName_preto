import React, { useState, useEffect } from 'react';
import Axios from 'axios';
import 'react-notion/src/styles.css';
import 'prismjs/themes/prism-tomorrow.css'; 

//36953a931f2d485c85800d980d5c5e16
export default function NotionPage() {
    const [response, setResponse] = useState({});
  
    useEffect(() => {
      const NOTION_PAGE_ID = '36953a931f2d485c85800d980d5c5e16';
      Axios
        .get(`https://notion-api.splitbee.io/v1/page/${NOTION_PAGE_ID}`)
        .then(({ data }) => {
          setResponse(data);
        });
    }, []);
  
    return (
      Object.keys(response).length && (
        <NotionRenderer blockMap={response} fullPage={true} />
      )
    );
  }