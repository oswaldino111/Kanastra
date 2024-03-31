import * as React from 'react';
import { DataGrid } from '@mui/x-data-grid';

const columns = [
  { field: 'id', headerName: 'ID', width: 70 },
  { field: 'name', headerName: 'Nome do Arquivo', width: 130 },
  { field: 'lastModifiedDate', headerName: 'Data', width: 500 },
];

export default function DataTable(props) {
  return (
      <DataGrid
        sx ={{borderRadius: "35px"}}
        rows={props.rows}
        columns={columns}
        initialState={{
          pagination: {
            paginationModel: { page: 0, pageSize: 5 },
          },
        }}
        pageSizeOptions={[5, 10]}
        checkboxSelection
      />
  );
}