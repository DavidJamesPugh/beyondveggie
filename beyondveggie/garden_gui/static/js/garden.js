const canvas = document.getElementById("myCanvas");
let ctx = canvas.getContext("2d");

ctx.beginPath();
ctx.arc(10,50,5,0,2*Math.PI);
ctx.stroke();
ctx.beginPath();
ctx.arc(50,70,5,0,6.3);
ctx.stroke();
ctx.beginPath();
ctx.arc(30,20,5,0,2*Math.PI);
ctx.stroke();
