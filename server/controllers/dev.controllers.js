import { linear } from '../math/array.js';
import { waveNormed } from '../math/wave.js';
import { gaussian } from '../math/gaussian.js';

export const testData = (request, response) => {

    try {

        const { set, dx, start, end, dev } = request.query;
        
        const length = end - start;

        switch (set) {

            case '1dsine':

                const X = linear(dx, parseFloat(start), end);
                const Y = X.map(waveNormed(length, start));

                response.status(200).json({ x: X, f: Y });
                break;
            
            case '1dgauss':

                const X = linear(dx, parseFloat(start), end);
                const Y = X.map(gaussian(start + .5 * length, dev));
    
                response.status(200).json({ x: X, f: Y });
                break;
            
            case '2d':
                response.status(200).json({ x: [], y: [], f: [[]], message: 'soon...' });
                break;

            default:
                response.status(404).json({ error: 'unknown set' });
                break;
        
        }

    } catch (error) {
        response.status(500).json({ error: error.message });
    }

}