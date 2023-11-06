import { InstagramLogin } from '@amraneze/react-instagram-login';

export default function Login() {
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
          redirectUri="https://amyjbaer.pythonanywhere.com/auth"
          useRedirect={true}
          scope="user_profile,user_media,instagram_graph_user_profile"
        />
      </header>
    </div>
  );
}
