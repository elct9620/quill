import { SidebarProvider } from "@/components/ui/sidebar";
import { Outlet } from "react-router-dom";

import AppSidebar from "@/components/AppSidebar.tsx";

function App() {
  return (
    <>
      <SidebarProvider>
        <AppSidebar />
        <main>
          <Outlet />
        </main>
      </SidebarProvider>
    </>
  );
}

export default App;
