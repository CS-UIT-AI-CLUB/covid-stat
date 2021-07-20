import React from 'react';
import '@fontsource/roboto';
import './App.css';

import { makeStyles } from '@material-ui/core/styles';
import { ThemeProvider, createTheme, responsiveFontSizes } from '@material-ui/core/styles';

import { Box, Grid } from '@material-ui/core';

import GlobalStat from './core/GlobalStat';
import ProvinceStat from './core/ProvinceStat';
import Copyright from './core/Copyright';

const theme = responsiveFontSizes(createTheme({
    palette: {
        primary: {
            main: '#ED6A5A',
        },
        secondary: {
            main: '#000000',
        },
    }
}));

const useStyles = makeStyles(theme => ({
    root: {
        height: '100vh',
        width: '100vw',
        // padding: '1vh',
        display: "flex",
        flexDirection: "column",
        boxSizing: 'border-box',
    },
    content: {
        flex: "1 1 auto",
        padding: theme.spacing(1),
    },
    stats: {
    }
}));

const homepage = document.location.href;
// const homepage = "https://aiclub.uit.edu.vn/covidstat"; // development server

export default function App() {

    const classes = useStyles();

    return (
        <div className="App">
            <ThemeProvider theme={theme}>
                <Box
                    className={classes.root}
                >
                    <Grid container className={classes.content}>
                        <Grid item xs={12} md={7}>
                            <Grid container className={classes.stats}>
                                <Grid item xs={12} sm={6}>
                                    <GlobalStat
                                        title="VIỆT NAM"
                                        url={homepage + "/api/vietnam"}
                                        media="https://i.ytimg.com/vi/N5Be56e6f7Q/maxresdefault.jpg"
                                    />
                                </Grid>
                                <Grid item xs={12} sm={6}>
                                    <GlobalStat
                                        title="THẾ GIỚI"
                                        url={homepage + "/api/global"}
                                        media="https://wallpaper.dog/large/5492398.jpg"
                                    />
                                </Grid>
                            </Grid>
                            <ProvinceStat url={homepage + "/api/provinces"} />
                        </Grid>
                    </Grid>
                    <Copyright/>
                </Box>
            </ThemeProvider>
        </div>
    );
}