(function($){

	// Number of seconds in every time division
	var days	= 24*60*60,
		hours	= 60*60,
		minutes	= 60;

	// Creating the plugin
	$.fn.countdown = function(prop){

		var options = $.extend({
			callback	: function(){},
			timestamp	: 0
		},prop);

		var left, d, h, m, s, positions;

		positions = this.find('.position');

		(function tick(){

			// Time left
			left = Math.floor(Date.parse(options.timestamp) - Date.parse(new Date())) / 1000;

			if(left < 0){
				left = 0;
			}

			// Number of days left
			d = Math.floor(left / days);
			updateTrio(0, 1, 2, d);
			left -= d*days;

			// Number of hours left
			h = Math.floor(left / hours);
			updateDuo(3, 4, h);
			left -= h*hours;

			// Number of minutes left
			m = Math.floor(left / minutes);
			updateDuo(5, 6, m);
			left -= m*minutes;

			// Number of seconds left
			s = left;
			updateDuo(7, 8, s);

			// Calling an optional user supplied callback
			options.callback(d, h, m, s);

			// Scheduling another call of this function in 1s
			setTimeout(tick, 1000);
		})();

		// This function updates two digit positions at once
		function updateDuo(minor,major,value){
			switchDigit(positions.eq(minor),Math.floor(value/10)%10);
			switchDigit(positions.eq(major),value%10);
		}

		function updateTrio(first, second, third, value){
		    switchDigit(positions.eq(first),Math.floor(value/100)%10);
		    switchDigit(positions.eq(second),Math.floor(value/10)%10);
			switchDigit(positions.eq(third),value%10);
		}

		return this;
	};

    // Creates an animated transition between the two numbers
    function switchDigit(position,number){

        var digit = position.find('.digit')

        if(digit.is(':animated')){
            return false;
        }

        if(position.data('digit') == number){
            // We are already showing this number
            return false;
        }

        position.data('digit', number);

        var replacement = $('<div>',{
            'class':'digit',
            css:{
                top:'-2.1em',
                opacity:0
            },
            html:number
        });

        // The .static class is added when the animation
        // completes. This makes it run smoother.

        digit
            .before(replacement)
            .removeClass('static')
            .animate({top:'2.5em',opacity:0},'fast',function(){
                digit.remove();
            })

        replacement
            .delay(100)
            .animate({top:0,opacity:1},'fast',function(){
                replacement.addClass('static');
            });
    }

})(jQuery);