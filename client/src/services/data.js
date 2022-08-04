import axios from 'axios'
const baseUrl = 'https://quantum-server-app.herokuapp.com/dev/testdata'

const getUpTo100 = () => {
    const request = axios.get(`https://quantum-server-app.herokuapp.com/dev/testdata/?set=1dsine&start=0&end=10&dx=1`)

    return request.then(response => response.data)
}

const getWanted = (set, start, end, dx) => {
    const request = axios.get(baseUrl, { params: { set, start, end, dx } })

    return request.then(response => response.data)
}

const dataService = {
    getUpTo100,
    getWanted
}

export default dataService
