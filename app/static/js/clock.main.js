require.config({
	shim : {
		"jqueryui" : { "deps" :['jquery'] },
		"koclock" : { "deps" : ['knockout', 'jqueryui']}
	},
	paths: {
		jquery: '/libraries/jquery.min',
		jqueryui: '/libraries/jquery-ui.min',
		knockout: '/libraries/knockout',
		koclock: '/libraries/ko-binding-clock'
	}
});

require(["jquery", "knockout", "koclock"], function($,ko,koclock) {
	var r = function(el, deg) {
	  el.setAttribute('transform', 'rotate('+ deg +' 50 50)')
	}

	var ViewModel = function() {
		//range of hours is 6PM - 7AM = 13hours = 13*60 = 780 minutes

	    var self = this;
	    self.selectedDate = ko.observable("");
	    self.sliderPosition = ko.observable(1);
	    self.closestImg = ko.observable("");
	    self.clockPosition = ko.computed(function() {
	    	if(self.sliderPosition() && self.selectedDate()) {
	    	  var thisClockPosition = Math.round((self.sliderPosition() * 780 / 100)+(18*60));
		    	$.getJSON('/api/getImgBasedOnTime/' + self.selectedDate() + "/" + thisClockPosition, {}, function(data) {
		    		self.closestImg("/static/img/"+self.selectedDate()+"/"+data.imgSrc);
		    	});
		    	return thisClockPosition;	
	    	} else {
	    		return "";
	    	}
	    }).extend({rateLimit: 50});

	    self.clockHours = ko.computed(function() {
	    	var thisHour = (Math.floor(self.clockPosition() / 60)) % 24;
	    	r(hour, 30*thisHour);
	    	return thisHour;
	    });
	    self.clockMinutes = ko.computed(function() {
	    	r(min, 6*Math.round(self.clockPosition() % 60));
	    	return Math.round(self.clockPosition() % 60);
	    });
	}

	ko.applyBindings(new ViewModel());
});