import { useEffect, useState } from 'react';
import axios from 'axios';
import useToken from './token';

export default function Home() {
  const { token, setToken } = useToken();
  const [name, setName] = useState(null);

  useEffect(() => {
    axios({
      method: 'GET',
      url: '/api/user',
      headers: {
        Authorization: 'Bearer ' + token,
      },
    })
      .then((response) => {
        console.log(response);
        const res = response.data;
        res.access_token && setToken(res.access_token);
        setName(res.name);
      })
      .catch((err) => console.log(err));
  }, []);

  return <div>Welcome {name}!</div>;
}
