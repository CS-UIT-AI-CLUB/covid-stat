import React from 'react';

import { makeStyles } from '@material-ui/core/styles';

import { Box, Grid, Card, CardMedia, Typography } from '@material-ui/core';

const useStyles = makeStyles(theme => ({
    root: {
        position: 'relative',
        backgroundColor: "#fff",
        margin: theme.spacing(1),
    },
    globalHeader: {
        position: 'absolute',
        top: '0',
        color: '#fff',
        textShadow: "-1px 0 3pt black, 0 1px 3pt black, 1px 0 3pt black, 0 -1px 3pt black",
        margin: theme.spacing(2, 2, 1, 2),
    },
    globalContent: {
        margin: theme.spacing(1.5, 0, 1.5, 0),
        padding: theme.spacing(0, 2),
    },
    globalStats: {
        margin: theme.spacing(1, 0),
    },
}));

export default function GlobalStat(props) {

    const classes = useStyles();

    const [stats, setStats] = React.useState([
        {
            name: 'Tổng ca nhiễm',
            stat: '...',
        },
        {
            name: 'Đang điều trị',
            stat: '...',
        },
        {
            name: 'Đã chữa khỏi',
            stat: '...',
        },
        {
            name: 'Tử vong',
            stat: '...',
        },
    ]);

    const fetchGlobalStat = url => {
        const reqData = {
            method: 'GET',
        }

        fetch(url, reqData)
            .then(res => res.json())
            .then(res => setStats([
                {
                    name: 'Tổng ca nhiễm',
                    stat: res.value.toLocaleString(),
                },
                {
                    name: 'Đang điều trị',
                    stat: res.socadangdieutri.toLocaleString(),
                },
                {
                    name: 'Đã chữa khỏi',
                    stat: res.socakhoi.toLocaleString(),
                },
                {
                    name: 'Tử vong',
                    stat: res.socatuvong.toLocaleString(),
                },
            ]))
            .catch(err => console.log(err));
    }

    React.useEffect(() => fetchGlobalStat(props.url), [props.url]);

    return (
        <Card className={classes.root}>
            <CardMedia
                component="img"
                alt="COVID-19 Stat"
                height="60"
                image={props.media}
            />
            <Box textAlign="left" className={classes.globalHeader}>
                <Typography variant="h5">{props.title}</Typography>
            </Box>
            {stats.map(stat => (
                <Grid container className={classes.globalContent} alignItems="center">
                    <Grid item xs={6}>
                        <Box textAlign="left">
                            <Typography variant="body2">{stat.name}</Typography>
                        </Box>
                    </Grid>
                    <Grid item xs={6}>
                        <Box textAlign="right">
                            <Typography variant="body2">{stat.stat}</Typography>
                        </Box>
                    </Grid>
                </Grid>
            ))}
        </Card >
    )
}