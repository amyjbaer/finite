import { useRouteError } from 'react-router-dom';

export default function ErrorPage(props) {
  const { inputError } = props;
  const error = useRouteError();
  error && console.error(error);

  return (
    <div id="error-page">
      <h1>Oops!</h1>
      <p>Sorry, an unexpected error has occurred.</p>
      <p>
        <i>{inputError || error.statusText || error.message}</i>
      </p>
    </div>
  );
}
