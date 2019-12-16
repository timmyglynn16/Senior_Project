const path = require('path');
//const expressEdge = require('express-edge'); // outdated?
const { config, engine } = require('express-edge');
const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const fileUpload = require("express-fileupload");
const Post = require('./backend/database/db-models/Post');

const app = new express();

// THIS NEEDS TO BE CHANGED IF CSS FILES MOVE IN APP.JS
app.use(express.static(__dirname + '/frontend/public'));
//app.use(express.static(path.join(__dirname, 'public')));

mongoose.connect('mongodb+srv://timmyglynnv3:westmoreland@mep0-jfvcw.mongodb.net/mepDB?retryWrites=true&w=majority', 
{ useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => 'You are now connected to Mongo!')
    .catch(err => console.error('Something went wrong', err))

app.use(fileUpload());
app.use(express.static('/frontend/public'));
app.use(engine);
app.set('views', __dirname + '/frontend/views');
//app.set('views', '${__dirname}/views'); // fix, doesn't work - outdated?

app.use(bodyParser.json())
app.use(bodyParser.urlencoded({
    extended: true
}));

 
app.get('/', async (req, res) => {
    const posts = await Post.find({})
    res.render('index', {
        posts
    })
});

app.get('/post/:id', async (req, res) => {
    const post = await Post.findById(req.params.id)
    res.render('post', {
        post
    })
});

app.get('/posts/new', (req, res) => {
    res.render('create')
});
 
app.post("/posts/store", (req, res) => {
    const {
        image
    } = req.files
 
    image.mv(path.resolve(__dirname, 'public/posts', image.name), (error) => {
        Post.create({
            ...req.body,
            image: `/posts/${image.name}`
        }, (error, post) => {
            res.redirect('/');
        });
    })
});
 
/**
 * OLD STATIC IMPLEMENTATION
 *
app.get('/', (req, res) => {
    res.sendFile(path.resolve(__dirname, 'pages/index.html'));
});

app.get('/', (req, res) => {
    res.render('index');
});

app.get('/about', (req, res) => {
    res.sendFile(path.resolve(__dirname, 'pages/about.html'));
});
 
app.get('/contact', (req, res) => {
    res.sendFile(path.resolve(__dirname, 'pages/contact.html'));
});
 
app.get('/post', (req, res) => {
    res.sendFile(path.resolve(__dirname, 'pages/post.html'));
});
*
*/


// for cloud 
app.listen(8080, () => {
    console.log('App listening on port 8080')
});

// for local testing 
/*app.listen(4000, () => {
    console.log('App listening on port 4000')
});*/

