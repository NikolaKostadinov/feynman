import express from 'express';

import * as controllers from '../controllers/server.controllers.js';

const router = express.Router();

router.get('/', controllers.main);

export default router;