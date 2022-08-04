import express from 'express';

import * as controllers from '../controllers/dev.controllers.js';

const router = express.Router();

router.get('/testdata', controllers.testData);

export default router;