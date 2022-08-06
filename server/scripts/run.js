import { spawn } from 'child_process';

export default async function run (sctipt) {

    var result;

    const runpy = spawn('python', [`./scripts/${sctipt}`]);
    runpy.stdout.on('data', async (data) => {
        result = await data
        console.log(result.toString())
    });
    //runpy.stderr.on('data', (data) => console.log(data.toString()));
    //runpy.on('close', (code) => console.log(code.toString()));
    
    return result;

}