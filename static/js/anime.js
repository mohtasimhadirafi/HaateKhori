
if(!window.JSFX) JSFX=new Object();

if(!JSFX.createLayer)
{/*** Include Library Code ***/

var ns4 = document.layers;
var ie4 = document.all;
JSFX.objNo=0;

JSFX.getObjId = function(){return "JSFX_obj" + JSFX.objNo++;};

JSFX.createLayer = function(theHtml)
{
	var layerId = JSFX.getObjId();

	document.write(ns4 ? "<LAYER  NAME='"+layerId+"'>"+theHtml+"</LAYER>" :
				   "<DIV id='"+layerId+"' style='position:absolute'>"+theHtml+"</DIV>" );

	var el = 	document.getElementById	? document.getElementById(layerId) :
			document.all 		? document.all[layerId] :
							  document.layers[layerId];

	if(ns4)
		el.style=el;

	return el;
}
JSFX.fxLayer = function(theHtml)
{
	if(theHtml == null) return;
	this.el = JSFX.createLayer(theHtml);
}
var proto = JSFX.fxLayer.prototype

proto.moveTo     = function(x,y){this.el.style.left = x;this.el.style.top=y;}
proto.setBgColor = function(color) { this.el.style.backgroundColor = color; }
proto.clip       = function(x1,y1, x2,y2){ this.el.style.clip="rect("+y1+" "+x2+" "+y2+" "+x1+")"; }
if(ns4){
	proto.clip = function(x1,y1, x2,y2){
		this.el.style.clip.top	 =y1;this.el.style.clip.left	=x1;
		this.el.style.clip.bottom=y2;this.el.style.clip.right	=x2;
	}
	proto.setBgColor=function(color) { this.el.bgColor = color; }
}
if(window.opera)
	proto.setBgColor = function(color) { this.el.style.color = color==null?'transparent':color; }

if(window.innerWidth)
{
	gX=function(){return innerWidth;};
	gY=function(){return innerHeight;};
}
else
{
	gX=function(){return document.body.clientWidth;};
	gY=function(){return document.body.clientHeight;};
}

/*** Example extend class ***/
JSFX.fxLayer2 = function(theHtml)
{
	this.superC = JSFX.fxLayer;
	this.superC(theHtml + "C");
}
JSFX.fxLayer2.prototype = new JSFX.fxLayer;
}/*** End Library Code ***/

/*************************************************/
/*** Firework Spark - extends fxLayer ***/
JSFX.FireworkSpark = function(x, y)
{
	this.superC = JSFX.fxLayer;
	this.superC("*");

	this.dx 	= Math.random() * 4 - 2;
	this.dy	= Math.random() * 4 - 2;
	this.ay	= .09;
	this.x	= x;
	this.y	= y;
	this.type = 0;
}
JSFX.FireworkSpark.prototype = new JSFX.fxLayer;
/*** END Class FireworkSpark Constructor - start methods ***/

JSFX.FireworkSpark.prototype.fire0 = function()
{
	var a = Math.random() * 6.294;
	var s = Math.random() * 2;
	if(Math.random() >.6) s = 2;
	this.dx = s*Math.sin(a);
	this.dy = s*Math.cos(a) - 2;
}
JSFX.FireworkSpark.prototype.fire1 = function()
{
	var a = Math.random() * 6.294;
	var s = Math.random() * 2;
	this.dx = s*Math.sin(a);
	this.dy = s*Math.cos(a) - 2;
}
JSFX.FireworkSpark.prototype.fire2 = function()
{
	var a = Math.random() * 6.294;
	var s = 2;
	this.dx = s*Math.sin(a);
	this.dy = s*Math.cos(a) - 2;
}
JSFX.FireworkSpark.prototype.fire3 = function()
{
	var a = Math.random() * 6.294;
	var s = a - Math.random();
	this.dx = s*Math.sin(a);
	this.dy = s*Math.cos(a) - 2;
}
JSFX.FireworkSpark.prototype.fire4 = function()
{
	var a = Math.random() * 6.294;
	var s = (Math.random() > 0.5) ? 2 : 1;
	if(s==1)this.setBgColor("#FFFFFF");
	s -= Math.random()/4;
	this.dx = s*Math.sin(a);
	this.dy = s*Math.cos(a) - 2;
}
JSFX.FireworkSpark.prototype.fire = function(sx, sy, fw, cl)
{
	this.setBgColor(cl);

	if(fw == 1)
		this.fire1();
	else if(fw == 2)
		this.fire2();
	else if(fw == 3)
		this.fire3();
	else if(fw == 4)
		this.fire4();
	else
		this.fire0();

	this.x	= sx;
	this.y	= sy;
	this.moveTo(sx, sy);
}
JSFX.FireworkSpark.prototype.animate = function(step)
{
	this.dy += this.ay;
	this.x += this.dx;
	this.y += this.dy;
	this.moveTo(this.x, this.y);
}
/*** END Class FireworkSpark Methods***/

/*** Class FireworkDisplay extends Object ***/
JSFX.FireworkDisplay = function(numStars)
{
	window[ this.id = JSFX.getObjId() ] = this;

	this.sparks = new Array();
	for(i=0 ; i<numStars; i++)
	{
		this.sparks[i]=new JSFX.FireworkSpark(-10, -10);
		this.sparks[i].clip(0,0,3,3);
		this.sparks[i].setBgColor("#00FF00");
	}
	this.step = 0;
	this.timerId = -1;
}
JSFX.FireworkDisplay.prototype.explode = function()
{
	var colors = new Array("#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#FFFFFF");
	var cl = colors[Math.floor(Math.random()*colors.length)];

	var x = (50 + (Math.random() * (gX()-150)));
	var y = (50 + (Math.random() * (gY()-150)));
	var fw = Math.floor(Math.random() * 35);

	for(i=0 ; i<this.sparks.length ; i++)
		this.sparks[i].fire(x, y, fw, cl);
}
JSFX.FireworkDisplay.prototype.animate = function()
{

	if(this.step > 40)this.step = 0;
	if(this.step == 0)this.explode();

	this.step++;

	for(i=0 ; i<this.sparks.length ; i++)
		this.sparks[i].animate(this.step);

}
JSFX.FireworkDisplay.prototype.start = function()
{
	if(this.timerId == -1)
		this.timerId = setInterval("window."+this.id+".animate()", 20);

}
JSFX.FireworkDisplay.prototype.stop = function()
{
	if(this.timerId != -1)
	{
		clearInterval(this.timerId);
		for(i=0 ; i<this.sparks.length ; i++)
			this.sparks[i].moveTo(-30,-30);
		this.timerId = -1;
		this.step = 0;
	}
}
/*** END Class FireworkDisplay***/

JSFX.FWStart = function()
{
	if(JSFX.FWLoad)JSFX.FWLoad();
	myFW1.start();
	setTimeout("myFW2.start()", 1000);
}
myFW1 = new JSFX.FireworkDisplay(140);
myFW2 = new JSFX.FireworkDisplay(140);
JSFX.FWLoad=window.onload;
window.onload=JSFX.FWStart;
