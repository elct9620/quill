import { RouteObject } from "react-router-dom";

import Dashboard from "./Dashboard.tsx";

export const routes: RouteObject[] = [
  {
    path: "/",
    element: <Dashboard />,
  },
];
