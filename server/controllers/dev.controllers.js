import { linear } from '../math/array.js';
import { waveNormed } from '../math/wave.js';

export const testData = (request, response) => {

    try {

        const { set, dx, start, end } = request.query;
        
        const length = end - start;

        switch (set) {

            case '1d':

                const X = linear(dx, parseFloat(start), end);
                const Y = X.map(waveNormed(length, start));

                response.status(200).json({ x: X, f: Y });
                break;
        
            default:
                response.status(404).json({ error: 'unknown set' });
                break;
        
        }

    } catch (error) {
        response.status(500).json({ error: error.message });
    }

}