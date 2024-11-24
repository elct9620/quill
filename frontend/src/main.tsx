import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { createBrowserRouter } from "react-router";
import { RouterProvider } from "react-router/dom";

import "./index.css";
import { routes } from "./routes.tsx";
import ErrorPage from "./ErrorPage.tsx";
import App from "./App.tsx";

const router = createBrowserRouter([
  {
    path: "/",
    element: <App />,
    errorElement: <ErrorPage />,
    children: routes,
  },
], {
  future: {
    v7_relativeSplatPath: true,
  }
});

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <RouterProvider router={router} />
  </StrictMode>,
);
