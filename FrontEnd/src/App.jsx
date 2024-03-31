import React, { useState } from "react";
import Stack from '@mui/material/Stack';
import Button from '@mui/material/Button';
import CloudUploadIcon from '@mui/icons-material/CloudUpload';
import Paper from '@mui/material/Paper';
import DataTable from "./ui/table";
import { http } from "./utils/api";
import { styled } from '@mui/material/styles';
import OutlinedCard from "./ui/cards";
import { useFileContext } from "./context/filecontext";


const VisuallyHiddenInput = styled('input')({
  clip: 'rect(0 0 0 0)',
  clipPath: 'inset(50%)',
  height: 1,
  overflow: 'hidden',
  position: 'absolute',
  bottom: 0,
  left: 0,
  whiteSpace: 'nowrap',
  width: 1,
});

const styles = {
  paperContainer: {
      height: "100%",
      width: "100%",
      backgroundImage: `url(${"./background.png"})`
  }
};


function App() {

    const [file, setFile] = useState();
    
    const { dispatch, lineNumber, uploadedCount, statusEnvio, files} = useFileContext();

    const fileReader = new FileReader();
  
    const handleOnChange = (e) => {

      let dados = e.target.files[0];
      dados["id"] = uploadedCount + 1;

      setFile(e.target.files[0]);
      dispatch({ type: 'new', dados });
    };

    const handleOnSubmit = (e) => {
      e.preventDefault();
  
      if (file) {
        dispatch({ type: 'start' });
        fileReader.onload = function (event) {

          const csvOutput = event.target.result.split('\n');
          
          var i ; //csvOutput.length
          for(i=1; i < 5; i++){
              const dados =  csvOutput[i].split(',')

              let json_dados = {
                "name": dados[0],
                "governmentId": dados[1],
                "email": dados[2],
                "debtAmount": dados[3],
                "debtDueDate": dados[4],
                "debtID": dados[5],
              };

              dispatch({ type: 'next' });

              http(json_dados);

          };
          dispatch({ type: 'done' });
        };
  
        fileReader.readAsText(file);
      };
      
    };


  return (
    <div style={styles.paperContainer} >
      <div>
        <br></br>
        <Stack spacing={5} direction="row" justifyContent="center">
          <OutlinedCard texto={`Arquivos obtidos`} quantidade={uploadedCount}/>
          <OutlinedCard texto={`Emails Enviados`} quantidade={lineNumber}/>
          <OutlinedCard texto={`Status de Envio`} quantidade={statusEnvio}/>
        </Stack>

        <br></br>
        <Stack spacing={2} direction="row" justifyContent="center">
          <Button
              component="label"
              role={undefined}
              variant="contained"
              tabIndex={-1}
              id="file" 
              type="file" 
              onChange={handleOnChange} 
              accept="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet,application/vnd.ms-excel,text/csv"
              startIcon={<CloudUploadIcon />}
              color="success" 
          >
            Inserir Csv
            <VisuallyHiddenInput type="file" />
          </Button>
          <Button onClick={ handleOnSubmit } color="success" variant="contained">Enviar emails</Button>
        </Stack>
        <br></br>
        <div style={{ height: 520, width: '70%', marginLeft: "15%"}}>
          <DataTable rows={files}/>
        </div>
      </div>
    </ div>
  );
}

export default App;
