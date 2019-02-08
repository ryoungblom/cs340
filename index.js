var express = require('express');
var app = express();
var path = require('path');

//add handlebars view engine
var handlebars = require('express-handlebars')
	.create({defaultLayout: 'main'});  //default handlebars layout page

app.engine('handlebars', handlebars.engine);
app.set('view engine', 'handlebars'); //sets express view engine to handlebars

app.set('port', process.env.PORT || 3000);

app.get('/', function(req,res){
	res.render('home');
});

app.get('/characters', function(req,res){
	res.render('characters');
});

app.get('/skills', function(req,res){
	res.render('skills');
});

app.get('/houses', function(req,res){
	res.render('houses');
});

app.get('/religions', function(req,res){
	res.render('religions');
});

app.use(express.static(path.join(__dirname, 'public')));

app.use(function(req,res){
	res.status(404);
	res.render('404');
});


app.listen(app.get('port'), function(){
	console.log( 'Express Server Started on http://localhost:3000');
});
