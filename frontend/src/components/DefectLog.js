import React from 'react';
import { Box } from '@mui/material';
import Sidebar from './Sidebar';
const DefectLog = () => {
  return (
    <>
      <Box sx={{display: "flex"}}>
      <Sidebar/>
      <Box component="main" sx={{flexGrow: 1, pt: 8, pl: 5}}>
        <h1>Defect Log here</h1>
      </Box>
     </Box>
    </>
  )
}

export default DefectLog