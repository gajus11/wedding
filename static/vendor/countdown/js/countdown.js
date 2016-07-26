function initializeClock(id, endtime){
	var ts = endtime;

	$('#countdown-id').countdown({
		timestamp	: ts,
		callback	: function(days, hours, minutes, seconds){}
	});

};