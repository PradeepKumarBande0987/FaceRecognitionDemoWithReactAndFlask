import React from 'react';
import { createBrowserRouter } from "react-router-dom";
import Layout from "./components/layout/Layout";
import Home from "./pages/Home";
import Register from "./pages/Register";
import LiveDemo from "./pages/LiveDemo";
import RegisteredPersons from "./pages/RegisteredPersons";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Layout />,
    children: [
      { index: true, element: <Home /> },
      { path: "register", element: <Register /> },
      { path: "live-demo", element: <LiveDemo /> },
      { path: "registered-persons", element: <RegisteredPersons /> },
    ],
  },
]);

export default router;
