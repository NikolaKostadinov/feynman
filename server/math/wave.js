export function waveNormed (width, offset) {

    return (x) => .5 * Math.PI / width * Math.sin(Math.PI / width * (x - offset));

}