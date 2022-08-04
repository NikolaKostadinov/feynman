import express from 'express';
import bodyParser from 'body-parser';
import cors from 'cors';
import helmet from 'helmet';
import dotenv from 'dotenv';
import chalk from 'chalk';

import serverRouter from './routes/server.routes.js';
import devRouter from './routes/dev.routes.js';

import { none } from './controllers/server.controllers.js';

dotenv.config();
const { PORT, DATA_LIMIT } = process.env;

const app = express();
app.use(express.json());

const bodyParserSettings = { 
	limit: DATA_LIMIT,
	extended: true
};
app.use(bodyParser.json(bodyParserSettings));
app.use(bodyParser.urlencoded(bodyParserSettings));

app.use(cors());

app.use(helmet());

app.use('/', serverRouter);
app.use('/dev', devRouter);
app.use('*', none);

app.listen(PORT, () => {
    console.log(chalk.green(`🟢 WEB SERVER RUNNING ON PORT:${PORT}`));
});