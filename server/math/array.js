export function linear (width, start, end) {

    const array = [];
    var index = 0;

    const x = (index) => start + index * width;

    while (x(index) <= end) {

        array.push(x(index));
        index++;
    
    }

    return array;

}

export function linearBound (width, start, end) {

    const array = [];
    var index = 0;

    const x = (index) => start + index * width;

    while (x(index) < end) {

        array.push(x(index));
        index++;
    
    }
    
    return array;

}