import run from '../scripts/run.js';

export const main = (request, response) => {

    try {

        const diracResponse = {
            message: 'Welcome to the Dirac Engine. I have provided you with some help.',
            help: {},
            from: 'Feynman'
        };

        response.status(200).json(diracResponse);

    } catch (error) {
        response.status(500).json({ error: error.message });
    }

}

export const potentialWell = (request, response) => {

    try {

        const data = run('__test.py').toString();
        console.log(data);

        response.status(200).json({ x: [], f: [], message: 'Ready to solve Schroedinger\' equation for the potential well ?', data });

    } catch (error) {
        response.status(500).json({ error: error.message });
    }

}