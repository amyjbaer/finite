import React from 'react';
import ReactDOM from 'react-dom/client';
import Login from './login';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import ErrorPage from './error';
import Auth from './auth';
import Home from './home';

const router = createBrowserRouter([
  {
    path: '/',
    element: <Login />,
    errorElement: <ErrorPage />,
  },
  {
    path: '/auth',
    element: <Auth />,
    errorElement: <ErrorPage />,
  },
  {
    path: '/home',
    element: <Home />,
    errorElement: <ErrorPage />,
  },
]);

ReactDOM.createRoot(document.getElementById('root')).render(
  <RouterProvider router={router} />
);
