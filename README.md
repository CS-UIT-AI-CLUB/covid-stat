# CovidStat: Real-time statistic update for COVID-19

[Live demo](https://aiclub.uit.edu.vn/hcm-covidsafe)

Get all the latest news and statistics such as COVID-19 cases, deaths for over 60 Vietnam provinces, and more!

## Features

- Fetch real-time statistics from Bo Y Te Viet Nam (https://ncov.moh.gov.vn/).
- Data will be automatically fetched every 10 minutes and stored in redis database.
- REST API for fast and easy access to fetched data. 

## Table of contents

- [Quick start](#quick-start)
- [Customize](#customize)
- [API](#api)
- [Authors](#authors)

## Quick start

[Live demo](https://aiclub.uit.edu.vn/hcm-covidsafe)

To start customizing as your own system, you need to clone the repo:

```
git clone https://github.com/CS-UIT-AI-CLUB/covid-stat
```

Thanks to Docker, the system can be easily deployed using the following command:

```
docker-compose --env-file=config/.env up -d --build --no-deps
```

## Customize

Currently there is nothing much you can customize.

## API

The system also provides REST API for easy access to lastest statistics.

### Global data

Global/worldwide statistics on COVID-19 can be retrieved using
```
GET /api/global
```
which will return a json in the following format:
```jsonc
{
    "value": 987, // total number of COVID-19 cases, worldwide, since the beginning of pandemic
    "socadangdieutri": 654, // number of ongoing cases
    "socakhoi": 321, // number of cured cases
    "socatuvong": 0, // number of deaths caused by COVID-19
}
```

### Vietnam's data

National statistics in Vietnam on COVID-19 can be retrieved using
```
GET /api/vietnam
```
which will return a json in the following format:
```jsonc
{
    "value": 987, // total number of COVID-19 cases happened in Vietnam since the beginning of pandemic
    "socadangdieutri": 654, // number of ongoing cases in Vietnam
    "socakhoi": 321, // number of cured cases in Vietnam
    "socatuvong": 0, // number of deaths caused by COVID-19 in Vietnam
}
```

### Provincial data

COVID-19 statistics of every Vietnamese provinces can be retrieved using
```
GET /api/provinces
```
which will return a json in the following format:
```jsonc
{
    "23": {
        "hc-key": "23", // primary key of province
        "name": "Hồ Chí Minh", // name of province
        "value": 987, // total number of COVID-19 cases happened in HCM since the beginning of pandemic
        "socadangdieutri": 654, // number of ongoing cases in HCM
        "socakhoi": 321, // number of cured cases in HCM
        "socatuvong": 0, // number of deaths caused by COVID-19 in HCM
    },
    "42": {
        "hc-key": "42", // primary key of province
        "name": "Bắc Giang", // name of province
        // ...
    },
    // ...
}
```

## Acknowledgements

This repository would not be possible without the use of real-time data from Vietnam Ministry of Health (https://ncov.moh.gov.vn/).

## License

This codebase is protected under MIT License. People are free to contribute, copy, modify or publishing without any restriction.