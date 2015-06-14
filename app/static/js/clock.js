$(document).ready(function() {
	ko.bindingHandlers.slider = {
	  init: function (element, valueAccessor, allBindingsAccessor) {
	    var options = allBindingsAccessor().sliderOptions || {};
	    $(element).slider(options);
	    ko.utils.registerEventHandler(element, "slidechange", function (event, ui) {
	        var observable = valueAccessor();
	        observable(ui.value);
	    });
	    ko.utils.domNodeDisposal.addDisposeCallback(element, function () {
	        $(element).slider("destroy");
	    });
	    ko.utils.registerEventHandler(element, "slide", function (event, ui) {
	        var observable = valueAccessor();
	        observable(ui.value);
	    });
	  },
	  update: function (element, valueAccessor) {
	    var value = ko.utils.unwrapObservable(valueAccessor());
	    if (isNaN(value)) value = 0;
	    $(element).slider("value", value);
	  }
	};

	function r(el, deg) {
    el.setAttribute('transform', 'rotate('+ deg +' 50 50)')
  }

	var ViewModel = function() {
		  //range of hours is 6PM - 7AM = 13hours = 13*60 = 780 minutes

	    var self = this;
	    self.sliderPosition = ko.observable(1);
	    self.clockPosition = ko.computed(function() {
	    	return Math.round((self.sliderPosition() * 780 / 100)+(18*60));
	    });
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
