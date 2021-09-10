<!DOCTYPE html>
<html>
<head>
	<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=2.0, minimum-scale=1.0, user-scalable=yes">
	<style>
		body{background-color:#000;margin:0;padding:0;}
	</style>
	<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
</head>
<body>
	<div id="player"></div>
	
	<script>
		vidId='aZ_rw6FDOAM';
		
		var tag = document.createElement('script');
		tag.src = "https://www.youtube.com/iframe_api";
		var firstScriptTag = document.getElementsByTagName('script')[0];
		firstScriptTag.parentNode.insertBefore(tag, firstScriptTag);
		
		var player;
		function onYouTubeIframeAPIReady() {
			player = new YT.Player('player', {
				width: '100%',
				height: window.innerHeight,
				videoId: vidId,
				playerVars: { 'autoplay': 1, 'playsinline': 1 },
				events: {
					'onReady': onPlayerReady,
					'onStateChange': onPlayerStateChange
				}
			});
		}
		
		function onPlayerReady(event) {
			event.target.mute();
			event.target.playVideo();
		}
		
		function onPlayerStateChange(event) {
			if (event.data == YT.PlayerState.ENDED) {
				player.seekTo(0);
				player.playVideo();
			}
		}
		
		function stopVideo() {
			player.stopVideo();
		}
		
		
		function updateVideo(){
			$.get( "videoId.txt", function( data ) {
				if(data!=vidId){
					vidId=data;
					player.loadVideoById(vidId);
				}
			});
		}
		
		$(function(){
			setInterval(updateVideo, 10000);
		});
	</script>
</body>
</html>