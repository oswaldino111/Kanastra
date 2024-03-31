import * as React from 'react';
import Box from '@mui/material/Box';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';


export default function OutlinedCard(promps) {

    const card = (
        <React.Fragment>
          <CardContent >
            <Typography sx={{ fontSize: 16 }} color="text.secondary" gutterBottom>
                {promps.texto}
            </Typography>
            <Typography align="center" variant="h5" component="div">
                {promps.quantidade}
            </Typography>
          </CardContent>
        </React.Fragment>
      );

    return (
        <Box sx={{ maxWidth: "40%", maxHeight: "40%"}}>
            <Card variant="outlined" sx={{backgroundColor: 'transparent', border: 1, borderRadius: "20px"}}>
              {card}
            </Card>
        </Box>
    );
}
