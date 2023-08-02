import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Dashboard from "./components/Dashboard";
import KanbanBoard from "./components/KanbanBoard";
import DefectLog from "./components/DefectLog";
import Project from "./components/Project";
function App() {
  return (
    <>
      <BrowserRouter>
      <Routes>
          <Route path="/" element={<KanbanBoard/>}/>
          <Route path="/dashboard" element={<Dashboard />}/>
          <Route path="/kanban" element={<KanbanBoard />}/>
          <Route path="/kanban/:kanbanId" element={<KanbanBoard />}/>
          <Route path="/defect" element={<DefectLog />}/>
          <Route path="/project" element={<Project />} />
        </Routes>
      </BrowserRouter>
    </>
  );
}

export default App;
