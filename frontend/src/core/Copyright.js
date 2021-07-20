import React from 'react';

import Grid from '@material-ui/core/Grid';
import { Avatar, Typography } from '@material-ui/core';

export default function Gallery() {

    return (
        <div className="copyright" style={{ margin: "10pt 0 0 0" }}>
            {/* <Typography
                variant="caption" color="textPrimary"
                style={{ margin: "1em 0 0 0" }}
            >
                <em>Powered by moriaty.</em>
            </Typography> */}
            <Grid container justifyContent="center" alignItems="center">
                <Grid item>
                    <Avatar src={process.env.PUBLIC_URL + "/Copyright.png"} style={{ margin: "0 0 0 0" }} />
                </Grid>

                <Grid item>
                    <Typography
                        variant="body2" color="textPrimary"
                        style={{ margin: "0 0 0 5pt" }}
                    >
                        Copyright © {new Date().getFullYear()} CS-UIT AI Club. All rights reserved.
                    </Typography>
                </Grid>
            </Grid>
        </div>
    );
}