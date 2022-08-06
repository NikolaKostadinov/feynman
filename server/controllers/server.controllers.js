export const main = (request, response) => {

    try {

        const serverResponse = {
            message: 'Welcome to the Feynman Web Server.',
            from: 'Feynman',
            serverStatus: 'working',
            git: 'https://github.com/NikolaKostadinov/feynman'
        };

        response.status(200).json(serverResponse);

    } catch (error) {
        response.status(500).json({ error: error.message });
    }

}

export const none = (request, response) => {

    try {

        response.status(404).json({ error: 'route does not exist' });
        
    } catch (error) {
        response.status(500).json({ error: error.message });
    }

}