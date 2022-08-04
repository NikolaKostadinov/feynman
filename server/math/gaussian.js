export function gaussian (mean, deviation) {

    return (x) => Math.exp( - 0.5 * ( ( x - mean ) / deviation )^2 ) / ( Math.sqrt(2 * Math.PI) * deviation );

}