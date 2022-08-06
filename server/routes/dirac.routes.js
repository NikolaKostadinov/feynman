import express from 'express';

import * as controllers from '../controllers/dirac.controllers.js';

const router = express.Router();

router.get('/', controllers.main);
router.get('/potentialwell', controllers.potentialWell);

export default router;