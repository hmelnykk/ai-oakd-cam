import express from 'express';
import cors from 'cors';

const app = express();
const port = 3001;

app.use(cors());
app.use(express.json());

app.get('/', (req, res) => {
    const { query } = req;
    res.json({
        a: 'hello world'
    });
});

app.post('/', (req, res) => {
    
})

app.listen(port, () => {
    console.log('Server was started successfully!');
});
