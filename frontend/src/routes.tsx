import { RouteObject } from "react-router";

import Dashboard from "./Dashboard.tsx";

export const routes: RouteObject[] = [
  {
    path: "/",
    element: <Dashboard />,
  },
];
