import { useEffect, useState } from 'react';
import axios from 'axios';
import useToken from './token';
import { Navigate } from 'react-router-dom';
import ErrorPage from './error';

export default function Auth() {
  const current_url = window.location.href;
  const index = current_url.indexOf('/auth');
  const start_new_url = '/api';
  const new_url = start_new_url.concat(current_url.slice(index));

  const { setToken } = useToken();
  const [err, setErr] = useState(null);
  const [isBusy, setIsBusy] = useState(true);

  useEffect(() => {
    axios
      .get(new_url)
      .then((response) => {
        if (response.data.access_token) {
          setToken(response.data.access_token);
          localStorage.setItem('insta_token', response.data.insta_access_token);
        } else {
          let error = response.data.error;
          if (!error) {
            error = 'some error occured';
          }
          console.log(error);
          setErr(error);
        }
        setIsBusy(false);
      })
      .catch((error) => {
        console.log(error);
        setErr(error);
        setIsBusy(false);
      });
  }, []);

  if (isBusy) {
    return <div>Loading...</div>;
  } else if (err) {
    return <ErrorPage inputError={err} />;
  } else {
    return <Navigate to="/home" />;
  }
}
