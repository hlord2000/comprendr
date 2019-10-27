$(document).ready(function($) {
  var videoEl = $('#myVideo').get(),
    player = plyr.setup(videoEl);
  console.log("  >player:", player[0]);

  player[0].on('ready', function(event) {
    var instance = event.detail.plyr;
    console.log("  >ready - player type: " + instance.getType());
    console.log("  >duration: " + instance.getDuration());
    trace("ready - duration: " + instance.getDuration());
  });

  player[0].on('playing', function(event) {
    var instance = event.detail.plyr;
    console.log("  >playing");
    console.log("  >duration: " + instance.getDuration());
    trace("playing"); 
  });

  player[0].on('seeking', function(event) {
    var instance = event.detail.plyr;
    console.log("  >seeking");
    console.log("  >position: " + instance.getCurrentTime() + "/" + instance.getDuration());
  });

	player[0].on('seeked', function(event) {
    var instance = event.detail.plyr;
    console.log("  >seeked");
    console.log("  >position: " + instance.getCurrentTime() + "/" + instance.getDuration());
    trace("seek - position: " + instance.getCurrentTime() + "/" + instance.getDuration());
  });
  
  player[0].on('ended', function(event) {
    var instance = event.detail.plyr;
    console.log("  >ended");
    console.log("  >duration: " + instance.getDuration());
    trace("ended");
  });

});
/*
function setspeed(){
	loadJSON(function(response){
		var timeJSON = JSON.parse(response);
	});
	setInterval(function(){ var time = instance.getCurrentTime(); }, 1000);
	setInterval(function(){ instance.speed = timeJSON }, 3000);


}
*/
function trace(txt) {
	var t = $("#info").html() + "<br>" + txt;
  $("#info").html(t);
}
/*
function loadJSON(callback) {   
  var xobj = new XMLHttpRequest();
  xobj.overrideMimeType("application/json");
  xobj.open('GET', 'test.json', true);
  xobj.onreadystatechange = function () {
    if (xobj.readyState == 4 && xobj.status == "200") {
      callback(JSON.parse(xobj.responseText));
    }
  };
  xobj.send(null);  
}
*/