import React, { useState, useEffect } from 'react';
import ReactDOM from 'react-dom/client';
import { InstagramLogin } from '@amraneze/react-instagram-login';

function App() {
  const responseInstagram = (response) => {
    console.log(response);
  };

  return (
    <div className="App">
      <header className="App-header">
        <InstagramLogin
          clientId="283690477978497"
          onSuccess={responseInstagram}
          onFailure={responseInstagram}
          redirectUri="https://willowy-biscuit-0a7ec9.netlify.app/api/auth"
          useRedirect={true}
        />
      </header>
    </div>
  );
}

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(<App />);

// useEffect(() => {
//     fetch('/time').then(res => res.json()).then(data => {
//       setCurrentTime(data.time);
//     });
//   }, []);

//   return (
//     <div className="App">
//       <header className="App-header">

//         ... no changes in this part ...

//         <p>The current time is {currentTime}.</p>
//       </header>
//     </div>
//   );
