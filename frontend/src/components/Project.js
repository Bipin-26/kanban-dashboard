import React from 'react';
import { Box } from '@mui/material';
import Sidebar from './Sidebar';
const Project = () => {
  return (
    <>
       <Box sx={{display: "flex"}}>
      <Sidebar/>
      <Box component="main" sx={{flexGrow: 1, pt: 8, pl: 5}}>
          {/* Add Your code here */}
        <h1>Projects</h1>
      </Box>
     </Box>
    </>
  )
}

export default Project